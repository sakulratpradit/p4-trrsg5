# P4 price refresh status

- **Run time:** 2026-10-21 03:33 UTC (scheduled 03:30 backup run) — **NO-OP: the 00:30 run already succeeded.** FIRST CHECK passed: all 63 of 63 tickers carry pxd = 2026-10-20, the most recent completed US trading day, so this run stopped per the job rules and changed no prices.
- **Trading date recorded:** 2026-10-20 (Tue) — written by the 00:30 run.
- **Result:** NOT PUSHED by this run (nothing to push); board is current via the 00:30 run's push.
- **Commit:** 5e42bd5 (the 00:30 run's price push; repo HEAD at this run's start: ac86149).
- **Prices changed this run:** 0 (63 of 63 changed by the 00:30 run).
- **Unresolved tickers:** none.
- **Blockers:** none. Known open gap carried over, not touched by this run per the stop rule: UST10 2026-10-20 still absent from risk_series.json (ycharts had not served it at 00:30; the monthly risk run copes with gaps).

---

## Retained report of the successful 00:30 UTC run (2026-10-21), which did the work

- **Run time:** 2026-10-21 00:33–01:05 UTC (scheduled 00:30 run)
- **Trading date recorded:** 2026-10-20 (Tue)
- **Result:** PUSHED
- **Commit:** 5e42bd5 (75c7a81 → 5e42bd5, no push conflict)
- **Prices changed:** 63 of 63 (all pxd = 2026-10-20); SPY 769.05 written to BENCH (spyHigh stays 779.09, SPY 1.29% below — crash-reserve trigger NOT tripped); HISTORY row appended (mv 792,824.86, unreal +90,798.68 / +12.93%, net +96,694.15)
- **Unresolved tickers:** none
- **Sanity gate:** PASS with `--allow SE --allow TSEM`
  - SE −9.09% (80.43): confirmed real by stockstory.org (pub. Oct 20 20:05 UTC, "closed the day at $80.17, down 9.4%") and benzinga intraday −8.33%; quote-page closing print 80.43 kept per the rules (history table matches 80.43 exactly on heavy volume). StockStory's 80.17 is a snapshot variance, noted.
  - TSEM −8.25% (183.78): confirmed EXACTLY by gurufocus dated 10/20/2026 16:39, "closing at $183.78".
- **Quote/history disagreements:** none — all 62 fetched history Oct-20 rows matched the quote closes exactly. CGNX history page lagged (no Oct 20 row); its quote page passed both the stamp and prev-close tests (56.77, +2.92%).
- **Stale/broken sources:** Google Finance SE:NYSE served an Oct 19 3:29 PM intraday cache (unusable); yahoo-news SE article was from Oct 2025; ycharts weekly-chart URL 500'd; GitHub Pages build-status API is blocked by the sandbox proxy; the live page URL itself cannot be WebFetched from this sandbox (provenance gate), so live-render verification was done via Playwright on the exact pushed file: **ZERO PAGE ERRORS, 865 table rows rendered**.
- **UST10:** 2026-10-20 close NOT published yet at run time (ycharts latest period Oct 19 = 5.15; next release 18:00 EDT not served; mortgagenewsdaily /treasury/10yr unreachable via provenance). Backfilled the two open gaps from the same ycharts daily table instead: 2026-10-16 = 5.09, 2026-10-19 = 5.15. 2026-10-20 remains the only gap.
- **hi52/lo52:** KTOS lo52 → 38.96, AVAV lo52 → 117.63, BWXT lo52 → 134.24, V hi52 & ath → 406.57 (new all-time high).
- **FYI for Salee (no action taken — this job never trades):** ISRG closed 438.00 (+1.11%) BEFORE its Q3 release, then traded ≈ −7% after hours (407.46 at 7:58 PM EDT) — relevant to tonight's conditional ISRG test (board carries the official close only). NFLX −5.78% after hours post-results. SE's −9.09% day put it near its 52-week low (77.05).
