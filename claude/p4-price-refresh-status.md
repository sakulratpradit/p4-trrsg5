# P4 price refresh status

- Run time (UTC): 2026-10-02 00:30 run, finished ~01:05 UTC
- Trading date recorded: 2026-10-01 (Thu)
- Result: **PUSHED**
- Commit: 792381e (Daily price refresh 2026-10-01: 90 prices)
- Prices changed: 90 of 94
- Sanity gate: PASS. Ten moves at/over the 6% threshold, every one confirmed against a dated second source before `--allow`: SNPS +12.78% (gurufocus 1 Oct 4:58 PM, "closing at $490.54", investor day), COHR +10.90% (stockstory/yahoo published 1 Oct 5:57 PM EDT, day change +10.90%), AAOI +8.12% (ycharts Oct 01 16:00 = 107.29), CRDO +7.90% (gurufocus 210.17 +7.9% post-close, implied prev 194.79 = stored), CIEN +7.77% (gurufocus Key Metrics Oct 1 = 379.14), LITE +7.67% (ycharts Oct 01 16:00 = 1045.72), TEM −6.59% (gurufocus 76.50 −6.59% post-close, implied prev 81.90 = stored), FN +6.40% (ycharts Oct 01 16:00 = 451.47), CDNS +6.22% (ycharts Oct 01 16:00 = 350.72), TSEM +6.10% (ycharts 241.34; stockanalysis history-table 242.43 REJECTED, quote 241.30 written).
- Unresolved tickers (left at prior close, pxd unchanged at 2026-09-30):
  - CGNX — quote prev close 60.65 ≠ history Sep 30 close 60.72 (board's verified Sep 30 close is 60.66, so the history table itself looks wrong); no Oct 1 history row; Google Finance/ycharts/fool/marketscreener all stale (Sep 21–25).
  - XE — quote stamped intraday 2:29 PM EDT (same on refetch); history ends Sep 30; Google Finance stale Sep 25.
  - FPS — quote stamped intraday 10:08 AM EDT; history ends Sep 30; no dated second source found.
  - AEP — quote had the 4:00 PM stamp and prev close 118.64 = stored, but its history table ends Sep 29 so the prev-close cross-check was impossible; marketscreener's latest dated close is still Sep 30 (118.64).
- Other source anomalies this run: PWR quote prev close read 642.40 vs stored 642.51 — Oct 1 history row used (both sources read 662.60 for the close). ZETA history Oct 1 row corrupt (close 32.54 > high 32.30, vol 488K) — discarded, quote 32.40 used. No Oct 1 history row for MPWR, AAOI, FSLR, LHX, AMBA — quotes passed both freshness tests and were used. Google Finance was stale (Sep 25 cache) on essentially every name tried tonight; ycharts and gurufocus did the second-source work instead.
- HISTORY row appended for 2026-10-01: n 38, mv 808,917.58, cost 659,798.18 (reflects the MU fill booked 1 Oct), unreal 149,119.40 (+22.6%), cash 153,862.15. The 2026-09-30 row sha set to a8f009a.
- hi52 extended: CRWD 266.09. lo52 extended: FSLR 172.11, APP 281.31.
- Verification: local Playwright render of the pushed page — ZERO PAGE ERRORS, 494 table rows. The live GitHub Pages URL could not be fetched from this sandbox (provenance gate, no one present to approve), but the push to main is confirmed (4f8f4c0 → 792381e).
- Blockers: none.
