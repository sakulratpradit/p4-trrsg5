# P4 price refresh — run status

- Run time: 2026-09-29 00:40–01:10 UTC (00:30 scheduled run)
- Trading date recorded: 2026-09-28 (Mon)
- Result: **PUSHED**
- Commit: e2a1c8f "Daily price refresh 2026-09-28: 94 prices" (remote main confirmed at e2a1c8f after push)
- Prices changed: 94 of 94 (sanity_check counted 93 moved; LHX closed 237.70 vs 237.69, effectively flat)
- Unresolved tickers: none
- HISTORY row appended for 2026-09-28: n=38, mv=782,478.53, cost=645,117.62, unreal=+137,360.91 (+21.29%), net=+136,820.44, cash=168,542.71. Previous row's sha set to 92f22c9.
- ASOF: prepended "Sep 28, 2026 (2) - DAILY PRICE REFRESH" entry; interactive session's six-buys entry preserved below it.
- lo52 extended: BWXT 134.35, LEU 140.37.

## Six moves over the 6% gate, all confirmed against second sources, pushed with --allow
- BE -8.95% → 262.87 (fool.com; Oracle Project Jupiter force-majeure news)
- ARM -8.70% → 283.33 (fool.com article 21:17 ET)
- CRDO -8.67% → 192.67 (gurufocus + marketbeat, both dated Sep 28)
- QCOM -7.17% → 187.48 (fool.com article 7:15 PM ET)
- AXTI -6.68% → 73.67 (gurufocus + marketbeat)
- FPS -6.11% → 36.59 (stockanalysis quote AND history rows agree exactly with normal volume; Robinhood day-range match. marketscreener printed 37.75/-4.28%, internally inconsistent — implies a previous close of 39.44 that never existed — discarded)

## Quote/history disagreements and fallbacks
- AEP: quote page stamped intraday 1:56 PM EDT — took the HISTORY row close 118.20 (sanity-checked, volume normal)
- CRCL: history Sep 28 row internally impossible (close 85.58 below its own low 86.00) — quote 85.80 used
- MCHP, ZETA, TSEM: history Sep 28 rows looked like partial-session captures (anomalously low volume) — quote closes used (77.97 / 28.99 / 226.04)
- TEM, CIEN, XE: minor cent-level quote-vs-history disagreements — quote used per rule
- AXTI, FSLR, CGNX, LHX, HUBB, AMBA: history table had no Sep 28 row yet — quote used (passed both stamp and prev-close checks)

## Source health
- stockanalysis.com quote pages: all 94 stamped Sep 28 4:00 PM EDT (except AEP, intraday) and every previous-close check matched the stored Fri 2026-09-25 close exactly
- Google Finance: cache stale (Sep 25) on every >6% name checked — useless tonight
- marketscreener FPS: internally inconsistent, discarded

## Verification
- sanity_check.py: PASS (exit 0) with --allow ARM QCOM CRDO AXTI BE FPS
- Playwright render check (check_dashboard.js): 490 table rows, ZERO PAGE ERRORS
- Live page: could not be fetched from this sandbox (WebFetch provenance block, not a page failure); remote main verified at e2a1c8f, which is exactly the file that passed the render check

No blockers.
