# Pillar-4 pipeline sources (bootstrap kit)

These scripts let ANY fresh Claude session rebuild the working environment
from this repo alone — no dependency on a surviving cloud container.

Bootstrap (run in an empty session):

```bash
mkdir -p /home/claude/pillar4 && cd /home/claude/pillar4
git clone https://github.com/sakulratpradit/p4-trrsg5.git deploy
cp deploy/src/*.py deploy/src/*.js .
python3 extract_data.py            # rebuilds portfolio_data.py from deploy/index.html
```

Then the normal cycle:

1. Edit values in `portfolio_data.py` (prices, fundamentals, METRICS3/M3).
   Never touch ticker/name/ex/g, POS (positions), or jan2 during refreshes.
2. `python3 gen_dashboard.py` → writes `us-portfolio-dashboard.html`
   (uses `deploy/index.html` as layout template; with unchanged data the
   output is byte-identical — that is the roundtrip self-test).
3. `python3 build_workbook_v2.py` → `Pillar4_US_Portfolio_Workbook.xlsx`
   (v3 static rebuild; original live-formula workbook was lost 2026-07-28).
4. Verify: `node check_dashboard.js` (Playwright at /opt/pw-browsers/chromium,
   --no-sandbox) must print ZERO PAGE ERRORS.
5. Deploy: `cp us-portfolio-dashboard.html deploy/index.html`, commit in
   `deploy/`, push to main.

IMPORTANT: whenever `index.html` data changes, re-run `extract_data.py`
before editing, so `portfolio_data.py` is always in sync with what is live.
