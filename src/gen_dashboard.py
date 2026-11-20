#!/usr/bin/env python3
"""Regenerate us-portfolio-dashboard.html from portfolio_data.py.

Uses deploy/index.html as the layout template and injects the current data
constants from portfolio_data.py, so data edits flow to the page while the
UI stays exactly as deployed. Roundtrip invariant: with unchanged data the
output is byte-identical to the template.

Usage:  python3 gen_dashboard.py [template] [output]
"""
import json, re, sys
import portfolio_data as P

CONSTS = ["ASOF", "GROUPS", "STOCKS", "POS", "TRADES", "SELLPLAN", "CASH",
          "REALIZED", "TOTALS", "SOLD", "MONTHLY", "THBFX", "M3", "SCHEDULE", "SELLBOOK", "HISTORY", "BENCH", "APPROVALS", "RISK", "BUYPLAN"]

def roll_years(stocks):
    """Year start / end prices for the Overview matrix (added 20 Nov 2026).

    yr[YYYY] = {'c': last close seen with a date in that year, 'cd': that date,
                'o': official OPEN on the first trading day of that year}.
    'c'/'cd' follow price/pxd on every build, so a year's close freezes by itself
    once prices move into the next year. 'o' for 2026 mirrors jan2; later years
    are written by the price job (see jobs/price_refresh.md, YEAR PRICES).
    Idempotent: unchanged data gives byte-identical output."""
    for s in stocks:
        yr = dict(s.get("yr") or {})
        if s.get("jan2") is not None:
            yr.setdefault("2026", {})
            yr["2026"] = dict(yr["2026"], o=s["jan2"])
        px, d = s.get("price"), s.get("pxd")
        if isinstance(px, (int, float)) and px > 0 and isinstance(d, str) and len(d) == 10:
            e = dict(yr.get(d[:4]) or {})
            if not e.get("cd") or d >= e["cd"]:
                e["c"], e["cd"] = px, d
            yr[d[:4]] = e
        s["yr"] = {y: {k: yr[y].get(k) for k in ("c", "cd", "o")} for y in sorted(yr)}

def main():
    roll_years(P.STOCKS)
    template = sys.argv[1] if len(sys.argv) > 1 else "deploy/index.html"
    output = sys.argv[2] if len(sys.argv) > 2 else "us-portfolio-dashboard.html"
    html = open(template, encoding="utf-8").read()
    for name in CONSTS:
        blob = json.dumps(getattr(P, name), separators=(",", ":"), ensure_ascii=False)
        new_line = f"const {name} = {blob};"
        html, n = re.subn(r"^const %s = .*;$" % name, new_line.replace("\\", "\\\\"), html, count=1, flags=re.M)
        if n != 1:
            raise SystemExit(f"ERROR: const {name} not found in template {template}")
    with open(output, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{output} written ({len(html):,} bytes, {len(P.STOCKS)} stocks, as of {P.ASOF!r})")

if __name__ == "__main__":
    main()
