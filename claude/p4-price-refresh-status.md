# P4 price refresh status

- Run time (UTC): 2026-09-24 00:41 (00:30 scheduled run)
- Trading date recorded: 2026-09-23 (Wed)
- Result: PUSHED
- Commit: 3e8941e (39a00b4..3e8941e main -> main, no force)
- Prices changed: 94 of 94 (pxd 2026-09-23 on all 94; ASOF updated)
- Sanity gate: PASS, exit 0, with --allow AXTI --allow LUNR (both >6% movers confirmed against Google Finance closed-market Sep 23 stamps: AXTI 72.98 -6.18%, LUNR 15.24 -6.16%)
- Largest move: AXTI -6.18%; biggest gainers PANW +5.00%, CRWD +4.97%, IONQ +4.42%
- Unresolved tickers: none
- Quote/history disagreements (quote page taken unless noted): CDNS, SNPS, TER, MCHP, FN, FSLR, ONDS, DDOG, TEM, TSEM (history rows were partial captures / anomalously low volume; material ones second-source confirmed), AXTI (history row internally impossible — close below its own low). LRCX: quote page had a stale previous close, history row 307.28 taken (same price both pages).
- Source problems: XE stockanalysis quote page intraday-stamped (10:32 AM) with corrupt history — resolved via Google Finance beta (16.38, Closed Sep 23 4:00 PM). AMBA history table frozen at Jul 21 — quote page 67.62 taken, YCharts ballpark 67.69. AEP/HUBB history tables had no Sep 23 row yet — quote pages taken, second-source confirmed. Google Finance non-beta cache wildly stale on several names (April data); marketscreener stale for ONDS/XE.
- SKHY has mcapB = None in the data — price updated, mcapB left as None (pre-existing).
- Live page: could not be fetched from this sandbox (WebFetch provenance block on the github.io URL — not a site failure). Push confirmed on origin/main; local Playwright render check of the built page: 472 table rows, ZERO PAGE ERRORS.
- Blockers: none.
