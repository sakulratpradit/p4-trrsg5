#!/usr/bin/env python3
"""P4 weekly price lines + USD/THB (adopted by Salee 22 Nov 2026). Run from deploy/src.

ONE METHOD for every stock on the board (held and watch):
    line = LOWER of  (a) fair value (analysts' average, fvAvg) x 0.70
                     (b) forward EPS x bond-beating P/E,  bond-beating P/E = 100 / (10-year yield + 0.5)
    forward EPS = price / forward P/E (the board's fpe moves with price, so this is stable between results)
    rounded DOWN: below $100 to $1, $100-$999 to $5, $1,000+ to $10.
    No forward earnings (fpe missing or <= 0) -> no line (loss-makers stay out under the rate rule).

Usage:
    python3 jobs/weekly_lines.py --ust10 4.92 --ust10d 2026-11-20 --fx 33.94 --fxd 2026-11-20 --set 2026-11-23 [--src "..."]
Edits portfolio_data.py: PLINES (all lines), TOTALS.fx, the standing line rows in SCHEDULE
(AVGO/APP/PLTR/... and the suspended NVDA row) and ASOF. Prints a summary. Never places trades.
Then: gen_dashboard -> sanity_check -> publish, exactly as README.md.
"""
import argparse, importlib.util, math, os, pprint, re

LEVEL_RE = re.compile(r"below \$(\d[\d,]*(?:\.\d+)?)", re.I)

def rdown(x):
    step = 1 if x < 100 else (5 if x < 1000 else 10)
    return math.floor(x / step) * step

def rep(name, val, src):
    m = re.search(r'^' + name + r' = .*?(?=^[A-Z][A-Z0-9_]* = )', src, re.S | re.M)
    if not m:
        raise SystemExit(f"constant {name} not found in portfolio_data.py")
    return src[:m.start()] + name + ' = ' + pprint.pformat(val, width=120, sort_dicts=False) + '\n\n' + src[m.end():]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ust10", type=float, required=True); ap.add_argument("--ust10d", required=True)
    ap.add_argument("--fx", type=float, required=True); ap.add_argument("--fxd", required=True)
    ap.add_argument("--set", required=True, help="date the lines are set (the Monday)")
    ap.add_argument("--src", default="", help="where the yield and FX were read")
    ap.add_argument("--asof", default="", help="ASOF timestamp text, e.g. 'Nov 23, 2026 10:40 Bangkok'")
    a = ap.parse_args()
    if not (3.0 <= a.ust10 <= 7.0): raise SystemExit("10-year outside 3-7% - check the input")
    if not (28.0 <= a.fx <= 40.0): raise SystemExit("USD/THB outside 28-40 - check the input")

    src = open("portfolio_data.py", encoding="utf-8").read()
    spec = importlib.util.spec_from_file_location("pd", "portfolio_data.py"); p = importlib.util.module_from_spec(spec); spec.loader.exec_module(p)
    bpe = round(100 / (a.ust10 + 0.5), 2)
    old = getattr(p, "PLINES", {}) or {}
    lines = {}
    for s in p.STOCKS:
        t, px, fpe, fv = s["t"], s.get("price"), s.get("fpe"), s.get("fvAvg")
        eps = round(px / fpe, 2) if (px and fpe and fpe > 0) else None
        A = round(fv * 0.70, 2) if fv else None
        B = round(eps * bpe, 2) if eps else None
        if B is None:
            lines[t] = {"line": None, "a": A, "b": None, "eps": None, "fv": fv, "by": None,
                        "why": "no forward earnings - no line"}
            continue
        raw, by = (min(A, B), "a" if A < B else "b") if A is not None else (B, "b")
        lines[t] = {"line": rdown(raw), "a": A, "b": B, "eps": eps, "fv": fv, "by": by, "pxset": px}
    hist = list(old.get("history", []))
    if old.get("set"):
        hist.append({k: old.get(k) for k in ("set", "ust10", "ust10d", "bpe", "fx", "fxd")})
    P = {"set": a.set, "ust10": a.ust10, "ust10d": a.ust10d, "bpe": bpe, "fx": a.fx, "fxd": a.fxd, "src": a.src,
         "method": "Line = lower of (a) fair value x 0.70 and (b) forward EPS x 100/(10-year + 0.5); rounded down "
                   "($1 under $100, $5 to $999, $10 above). Adopted by Salee 22 Nov 2026; reset every Monday with the "
                   "latest 10-year close and USD/THB. A hit buys only where a standing line row has money; otherwise it is information.",
         "lines": lines, "history": hist[-26:]}

    # standing line rows on the Schedule follow the method
    changed = []
    for i in p.SCHEDULE["items"]:
        t = i.get("t")
        if i.get("d") or i.get("c") != "standing" or t not in lines or lines[t]["line"] is None:
            continue
        susp = i.get("a") == "HOLD" and str(i.get("w", "")).startswith("SUSPENDED")
        if i.get("a") not in ("LIMIT", "TRIGGER") and not susp:
            continue
        m = LEVEL_RE.search(i.get("w", ""))
        if not m:
            continue
        was, L = m.group(1), lines[t]["line"]
        if susp:
            i["w"] = f"SUSPENDED - no buying until Salee lifts it. Line under the one method: any close at or below ${L:,}"
        else:
            i["w"] = f"Any close at or below ${L:,} (one method, set {a.set})"
        if was.replace(",", "") != f"{L}":
            i["cond"] = f"LINE RESET {a.set}: ${was} -> ${L:,} (10-year {a.ust10}% on {a.ust10d}; P/E {bpe}x). || " + i.get("cond", "")
        changed.append((t, was, L))

    oldfx = p.TOTALS.get("fx"); p.TOTALS["fx"] = a.fx
    hit = [(t, s["price"], lines[t]["line"]) for s in p.STOCKS for t in [s["t"]]
           if lines[t]["line"] and s.get("price") and s["price"] <= lines[t]["line"]]
    asof = (a.asof or a.set) + (f" - WEEKLY PRICE LINES + FX: one method for all {len(lines)} stocks; 10-year {a.ust10}% ({a.ust10d}) -> "
            f"bond-beating P/E {bpe}x; USD/THB {oldfx} -> {a.fx} ({a.fxd}). Standing rows reset: "
            + (", ".join(f"{t} ${w} -> ${L:,}" for t, w, L in changed) or "none")
            + f". Closes at or below their line: {', '.join(t for t, _, _ in hit) or 'none'}. {a.src}") + " || PREVIOUS ENTRY: " + p.ASOF
    src = rep("PLINES", P, src); src = rep("SCHEDULE", p.SCHEDULE, src); src = rep("TOTALS", p.TOTALS, src); src = rep("ASOF", asof, src)
    open("portfolio_data.py", "w", encoding="utf-8").write(src)
    print(f"bond-beating P/E {bpe}x (10-year {a.ust10}%), USD/THB {a.fx}")
    held = {t for t, v in p.POS.items() if v.get("shares")}
    for s in p.STOCKS:
        L = lines[s["t"]]
        print(f"{s['t']:6} {'HELD ' if s['t'] in held else 'watch'} px {s.get('price')!s:>9}  line {L['line']!s:>7}  by {L['by']}  "
              f"(a) {L['a']!s:>9} (b) {L['b']!s:>9}" + ("   <= LINE" if L['line'] and s.get('price') and s['price'] <= L['line'] else ""))
    print("standing rows reset:", changed)

if __name__ == "__main__":
    main()
