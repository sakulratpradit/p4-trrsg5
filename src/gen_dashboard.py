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
          "REALIZED", "TOTALS", "SOLD", "MONTHLY", "THBFX", "M3", "SCHEDULE"]

def main():
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
