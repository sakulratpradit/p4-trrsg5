# P4 price refresh — last run status

- **Run time (UTC):** 2026-10-27 00:30 run (started 00:32, finished ~01:1x UTC)
- **Trading date recorded:** 2026-10-26 (Monday close)
- **Status:** PUSHED
- **Commit:** 277c77c (`Daily price refresh 2026-10-26: 61 prices`)
- **Prices changed:** 61 of 63 (SPY 765.37 and QQQ 712.20 also written to BENCH; SPY appended to the risk series)
- **Unresolved tickers (prices left at 2026-10-23):**
  - **FSLR** — quote/stat header intraday ("10:34 AM EDT - Market open"); history's Oct 26 row internally impossible (close 169.11 below its own low 169.38 on 87k volume) and discarded per the sanity rule; Google Finance cached Sep 29, benzinga cached Nov 2024, gurufocus undated, digrin monthly only. everhint's after-hours wrap shows a new 52-week low 168.41 touched, 168.09 after hours — the stale board price 171.99 likely overstates Monday's close by ~2%.
  - **CGNX** — history table ends Oct 23; every header (stockanalysis stats/market-cap/overview, stocktitan, Google Finance, benzinga, marketscreener) stale or intraday. No dated Oct 26 close anywhere.
- **Sanity gate:** blocked ARM +6.19%, LITE +8.19%, TSEM +6.68%; each verified against a dated second source (ARM: gurufocus 10/26 16:05 "$223.35" EXACT; LITE: gurufocus 10/26 16:13 "$818.10" EXACT + thecerbatgem prev close 756.17 identical; TSEM: aaii dated Oct 26 intraday +9.13% from prior close 167.560 identical — direction and size) and pushed with `--allow ARM --allow LITE --allow TSEM`. Re-run: PASS.
- **History-table fallbacks (headers intraday/stale):** KTOS 40.43, BE 203.92, STRL 360.72, CIEN 335.93 — all history rows internally consistent on normal volume. BWXT quote close 131.20 kept (history page never surfaced; stated prev close 127.19 = Friday's verified close).
- **UST10:** skipped for 2026-10-26 — ycharts latest period is Oct 23 (5.00, next release Oct 27 16:15 EDT); mortgagenewsdaily's dated table ends at an Oct-25 row and its live 4.964 is undated.
- **ath note:** CRWD (261.83), FTNT (183.33), NET (331.86) closed above their stored `ath` but below `hi52`; board precedent extends ath only together with hi52, so ath was left untouched — flagging for the interactive session to reconcile.
- **Live page:** push confirmed on origin/main (277c77c); the built page renders locally with ZERO PAGE ERRORS (Playwright). The GitHub Pages URL could not be re-fetched from this sandbox (WebFetch provenance approval has no one to answer in a scheduled run) — not verified end-to-end this run.
- **Blockers:** none.
