# P4 price refresh — status

- Run time (UTC): 2026-09-25 03:30 run (started ~03:40)
- Result: NO-OP — FIRST CHECK passed. All 94 of 94 tickers already have pxd = 2026-09-24, the most recent completed US trading day, so the 00:30 run succeeded and this run made no data changes.
- Trading date recorded: 2026-09-24 (Thu), by the earlier run
- PUSHED or NOT PUSHED: nothing to push from this run (status doc only)
- Commit carrying the prices: fe0bfc1 ("Daily price refresh 2026-09-24: 94 prices")
- Prices changed this run: 0
- Unresolved tickers: none
- Blockers: none

## Earlier run's report (00:30 UTC, preserved — this is the run that did the work)

- Run time (UTC): 2026-09-25 00:30 run, finished ~01:05
- Trading date recorded: 2026-09-24 (Thu)
- Result: PUSHED
- Commit: fe0bfc1 ("Daily price refresh 2026-09-24: 94 prices"), remote main confirmed at fe0bfc1
- Prices changed: 94 of 94 (all pxd set to 2026-09-24; mcapB scaled with price; HISTORY row for 2026-09-24 appended: n=37, mv=749,958.38, cost=609,758.47, unreal=+140,199.91 / +22.99%, real=-540.47, cash=203,906.85)
- Sanity gate: PASS with --allow ARM --allow FSLR --allow TEM --allow NBIS
  - ARM -7.88% → confirmed vs Google Finance AND MarketScreener (306.34)
  - FSLR -10.32% → confirmed vs GuruFocus article same day (172.16)
  - TEM +7.38% → confirmed vs Google Finance (82.24)
  - NBIS +7.44% → confirmed vs Google Finance (243.48)
- Largest moves: FSLR -10.32%, ARM -7.88%, NBIS +7.44%, TEM +7.38%, TSEM -5.74% (217.28, Google-Finance-confirmed), IONQ +5.74%
- Unresolved tickers: none (94/94 resolved)
- Quote-vs-history disagreements (quote page taken in every case, per the resolution rule):
  - AXTI: quote 75.90 vs history-row 77.61 → Google Finance independently confirmed 75.90; history row looks erroneous
  - DDOG: history 09-24 row internally impossible (close 251.93 outside its own 247.27–250.58 range, volume 189K vs ~2.7M normal) → discarded, quote 256.92 used
  - SE: quote 100.73 vs history 101.39 → Google Finance confirmed 100.73
  - STRL: quote 513.72 vs history 516.63 → quote used (internally consistent); NOT externally verified — Google Finance and MarketScreener both served stale caches (Sep 11/23). Watch this one.
  - Minor cent-level gaps, quote used: SNPS (424.91 vs 425.00), KTOS (47.02 vs 47.04), FPS (38.92 vs 38.95), NFLX (71.72 vs 71.70), CIEN (358.43 vs 358.48)
