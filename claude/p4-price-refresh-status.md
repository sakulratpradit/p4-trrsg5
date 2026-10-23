# P4 price refresh status

- Run time (UTC): 2026-10-23 00:33 - 01:0x (00:30 scheduled run)
- Trading date recorded: 2026-10-22 (Thu)
- Result: PUSHED
- Commit: ec6c645 ("Daily price refresh 2026-10-23 run (closes of 2026-10-22): 63 prices")
- Prices changed: 63 of 63 (plus SPY 763.96 and QQQ 704.47 to BENCH, both 2026-10-22)
- Largest move: COHR -12.51% (237.53 -> 207.82)
- 6% gate: THIRTY-TWO tickers tripped it (Lam Research supply-warning selloff, chips industry-wide; SPY only -1.18%, QQQ -2.86%). Every one verified against a dated second independent source before pushing with --allow: COHR, LRCX, LITE, TSEM, ALAB, FN, CIEN, CRDO, GEV, TER, VST, STRL, KLAC, SPCX, MPWR, MRVL, BE, SNDK, AMAT, AMD, GLW, PWR, STX, VRT, APH, ARM, ANET, META, ASML, SNPS, ETN, MU. Sources and per-ticker figures are in the ASOF entry. Sanity gate: PASS.
- Quote/history disagreements: none among the 60 history rows fetched (all matched the quote closes exactly).
- Stale/lagging sources: MPWR quote page stale again ('Oct 22, 11:07 AM EDT - Market open') -> history-table fallback 1167.93, confirmed EXACT by gurufocus (10/22/2026 17:32, 'fell 9.0% to 1167.93'). TSEM and CDNS history pages lagged (no Oct 22 row); their quote pages passed both the stamp and prev-close tests and were used. Benzinga was stale for COHR/ALAB/APH/FN/TSEM (fell back to digrin, marketchameleon, stockinvest.us, ycharts); Google Finance stale (Sep 25 caches) on every name tried; digrin stale for AMD/KLAC(0.26% off)/MPWR.
- Unresolved tickers: none.
- 52-week ranges extended: FSLR lo52 171.25, KTOS lo52 38.27, BWXT lo52 127.30, SE lo52 75.69; V hi52/ath 414.34 and AAPL hi52/ath 348.22 (new all-time highs).
- HISTORY row appended for 2026-10-22 (n=36, mv 774,693.43, unreal +60,787.43 = +8.51%, cash 24,735.56); the 2026-10-21 row's sha set to 78bd44f. Risk series: spy[2026-10-22]=763.96 appended; ust10 gap 2026-10-21=5.13 backfilled (ycharts, released Oct 22 16:15 EDT); ust10 for 2026-10-22 not yet published - skipped.
- Crash reserve: SPY 1.94% below spyHigh 779.09 - the -15% trigger NOT tripped.
- Live page: push accepted (ddfa383..ec6c645). Could NOT fetch https://sakulratpradit.github.io/p4-trrsg5/ from this sandbox (WebFetch provenance restriction) and the Pages-build API is blocked by the proxy, so live rendering was verified locally instead: node check_dashboard.js on the pushed index.html printed "table rows rendered: 867 / ZERO PAGE ERRORS".
- Blockers: none.
