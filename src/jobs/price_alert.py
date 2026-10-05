#!/usr/bin/env python3
"""P4 daily price-trigger alert (read-only).

Run from the repo's src/ folder after the nightly price refresh. Reads the
board's own trigger rows, so changing a rule on the board changes the alert.

Prints "NO TRIGGERS HIT" when nothing fires; otherwise one line per alert.
Never edits the board and never places trades.
"""
import datetime as dt
import importlib.util
import re
import subprocess
import sys

LEVEL_RE = re.compile(r"(?:at or )?below \$(\d{1,3}(?:,\d{3})*(?:\.\d+)?)", re.I)
LIMIT_RE = re.compile(r"LIMIT (?:ORDER )?AT \$(\d{1,3}(?:,\d{3})*(?:\.\d+)?)", re.I)
DROP_PCT = -8.0      # one-day fall on a held name
MU_CAP = 8.0         # Micron weight cap, % of held market value
STALE_DAYS = 4       # warn if board prices are older than this


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def previous_prices(cur):
    """Prices from the most recent earlier board version with an older price date."""
    shas = subprocess.run(["git", "log", "--format=%H", "-n", "60", "--", "portfolio_data.py"],
                          capture_output=True, text=True).stdout.split()
    ref = cur.get("NVDA", {}).get("pxd")
    for sha in shas[1:]:
        src = subprocess.run(["git", "show", f"{sha}:src/portfolio_data.py"],
                             capture_output=True, text=True).stdout
        if not src:
            continue
        path = f"/tmp/pd_{sha[:8]}.py"
        open(path, "w", encoding="utf-8").write(src)
        try:
            old = load(path, "pd_old")
        except Exception:
            continue
        o = {s["t"]: s for s in old.STOCKS}
        if o.get("NVDA", {}).get("pxd") and o["NVDA"]["pxd"] < (ref or ""):
            return o
    return {}


def main():
    p = load("portfolio_data.py", "pd")
    S = {s["t"]: s for s in p.STOCKS}
    today = dt.date.today().isoformat()
    out = []

    pxd = max((s.get("pxd") or "") for s in p.STOCKS)
    if pxd and (dt.date.today() - dt.date.fromisoformat(pxd)).days > STALE_DAYS:
        out.append(f"STALE: board prices are dated {pxd} - the nightly price refresh may have failed; triggers not reliable.")

    # 1) standing price triggers written on the board
    for i in p.SCHEDULE["items"]:
        if i.get("c") != "standing" or i.get("a") not in ("LIMIT", "TRIGGER"):
            continue
        m = LEVEL_RE.search(i.get("w", ""))
        t = i["t"]
        if not m or t not in S or not S[t].get("price"):
            continue
        level = float(m.group(1).replace(",", ""))
        px = S[t]["price"]
        if px <= level:
            amt = i.get("amt") or 0
            sh = int(amt // px) if px else 0
            out.append(f"BUY TRIGGER: {t} closed {px:,.2f} <= {level:,.2f} ({S[t].get('pxd')}). "
                       f"Rule: {i['w'][:80]}. Money: ${amt:,.2f} = about {sh} shares.")

    # 1b) standing SELL STOP rows (e.g. CrowdStrike: sell the rest below $243)
    for i in p.SCHEDULE["items"]:
        if i.get("c") != "standing" or i.get("a") != "STOP":
            continue
        m = LEVEL_RE.search(i.get("w", ""))
        t = i["t"]
        sh = (p.POS.get(t) or {}).get("shares") or 0
        if not m or not sh or t not in S or not S[t].get("price"):
            continue
        level = float(m.group(1).replace(",", ""))
        px = S[t]["price"]
        if px <= level:
            out.append(f"SELL STOP: {t} closed {px:,.2f} <= {level:,.2f} ({S[t].get('pxd')}). "
                       f"Rule: {i['w'][:80]}. Sell all {sh:g} shares, about ${sh * px:,.0f}.")

    # 2) dated limit buys still open (e.g. Meta $705 until its date)
    for i in p.SCHEDULE["items"]:
        if i.get("a") != "BUY" or i.get("c") == "done" or not i.get("d") or i["d"] < today:
            continue
        m = LIMIT_RE.search(i.get("cond", "") + " " + i.get("w", ""))
        t = i["t"]
        if m and t in S and S[t].get("price") and S[t]["price"] <= float(m.group(1).replace(",", "")):
            out.append(f"LIMIT REACHABLE: {t} closed {S[t]['price']:,.2f}, at or under the {m.group(1)} limit "
                       f"for the {i['d']} order (${i.get('amt', 0):,.2f}).")

    # 3) big one-day falls on held names
    held = {t: v for t, v in p.POS.items() if v.get("shares")}
    prev = previous_prices(S)
    for t, v in held.items():
        a, b = S.get(t, {}).get("price"), prev.get(t, {}).get("price")
        if a and b:
            chg = (a / b - 1) * 100
            if chg <= DROP_PCT:
                out.append(f"BIG DROP: {t} {chg:+.1f}% to {a:,.2f} (from {b:,.2f}). "
                           f"Check the news before any action - price alone is not a reason to sell.")

    # 4) Micron weight cap
    mv = {t: v["shares"] * (S.get(t, {}).get("price") or 0) for t, v in held.items()}
    total = sum(mv.values())
    if total and mv.get("MU", 0) / total * 100 > MU_CAP:
        out.append(f"SIZE: Micron is {mv['MU'] / total * 100:.1f}% of holdings (cap {MU_CAP:.0f}%). "
                   f"Per the 1 Oct rule, trim back toward 6%.")

    print("\n".join(out) if out else f"NO TRIGGERS HIT (prices dated {pxd}).")


if __name__ == "__main__":
    sys.exit(main())
