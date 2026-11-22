# P4 weekly price lines + USD/THB — every Monday (Bangkok)

Adopted by Salee on 22 Nov 2026. One method for every stock on the board (held and watch):

    line = LOWER of (a) fair value (fvAvg) x 0.70
                    (b) forward EPS x 100 / (10-year yield + 0.5)      forward EPS = price / fpe
    rounded down: $1 under $100, $5 for $100-$999, $10 for $1,000+.  No forward earnings = no line.

The script `src/jobs/weekly_lines.py` does all the arithmetic and edits: PLINES, TOTALS.fx, the standing
line rows on the Schedule (they follow the method; the suspended NVDA row keeps its suspension), and ASOF.

## Inputs you must find (WebSearch / WebFetch only; follow price_refresh.md source rules)
1. **10-year Treasury CLOSING yield** for the last US trading day (normally Friday). Good sources: ycharts.com/indicators/10_year_treasury_rate,
   a dated market close recap (cappnotes.substack.com "Closing Look", stocktitan "Stock Market Today"), CNBC US10Y.
   Need TWO sources agreeing within 0.02. If they disagree, use the one with an explicit date/close stamp and say so.
   Also add the value to src/risk_series.json -> "ust10" {"YYYY-MM-DD": value} if that date is missing.
2. **USD/THB** for the same date or later: tradingeconomics.com/thailand/currency (use the dated sentence
   "fell/rose to X on <date>"), or a Bank of Thailand reference rate. Never a page dated in an earlier month.
If either input cannot be confirmed: DO NOT run the script with a guess. Leave last week's lines in place, and report it.

## Steps
1. Follow deploy/src/README.md steps 0-2 (clone/pull, extract_data).
2. `cd deploy/src && python3 jobs/weekly_lines.py --ust10 <y> --ust10d <YYYY-MM-DD> --fx <r> --fxd <YYYY-MM-DD> --set <Monday YYYY-MM-DD> --asof "<Mon DD, YYYY HH:MM> Bangkok" --src "<sources>"`
3. `python3 gen_dashboard.py ../index.html ../../us-portfolio-dashboard.html`
4. `python3 sanity_check.py --new ../../us-portfolio-dashboard.html` (prices are not touched, so this should pass with no --allow)
5. Publish per README step 6-7 (cp, extract_data, also `python3 gen_notes_page.py; python3 build_workbook_v2.py`, commit, push without force; on rejection fetch, reset to origin, redo from step 1).
6. `PYTHONPATH=. python3 jobs/price_alert.py` and include its output in the report.

## Report (plain English, for Salee)
- 10-year used and date, bond-beating P/E, USD/THB old -> new.
- Standing lines that moved (e.g. AVGO $320 -> $315) and any stock now at or below its line, split into
  (i) standing row with money (an order for that evening: Day LIMIT at the close, one raise to +1%, after 22:00 Bangkok, never in the first 30 minutes; check Market = NASD/NYSE and USD), (ii) held with budget room (waits for February under the funding gate unless Salee decides), (iii) information only.
- Anything that could not be done. Never place trades. Never invent a number.
- Write the project doc `claude/p4-weekly-lines-status.md` (overwrite) with run time, inputs, PUSHED/NOT PUSHED, commit hash.
