# P4 price refresh status

- **Run time:** 2026-10-22 00:33–01:05 UTC (scheduled 00:30 run).
- **Trading date recorded:** 2026-10-21 (Wed).
- **Result:** PUSHED.
- **Commit:** 78bd44f "Daily price refresh 2026-10-22 run (closes of 2026-10-21): 63 prices" (fast-forward 8498b7a → 78bd44f, no force, no conflict with other writers).
- **Prices changed:** 63 of 63, all to the official Wed 2026-10-21 close; pxd = 2026-10-21 on every ticker; ASOF updated.
- **Unresolved tickers:** none.
- **Blockers:** none.

## Detail

- **Source discipline:** every price from a stockanalysis.com quote page stamped "At close: Oct 21, 2026, 4:00 PM EDT" with the stated previous close validated against the history table's prior-day close (and against the board's stored 10-20 closes). Every number came from a tool call in this session.
- **Four moves past the 6% gate, all confirmed via a second independent source and pushed with --allow:**
  - SPCX +7.79% → 159.31 (fool.com quote page, last-close table dated 2026-10-21, close 159.31, range 156.93–166.18 — EXACT; 220.8M shares, heaviest volume on the board)
  - BE +7.13% → 238.53 (247wallst.com, published Oct 21 11:57 am ET: "up 7% in morning trading" at 237.27 ahead of the Q3 report; page widget later 239.64 +7.63% — direction and size confirmed)
  - DDOG +6.50% → 273.09 (gurufocus dated 10/21/2026 16:17: "rose 6.5% to a current price of $273.09" — EXACT)
  - CRDO +6.28% → 182.28 (digrin 182.28 — EXACT)
- **Stale quote pages, history-table fallback per resolution rule step 4 (both second-sourced):** MPWR (quote stamped "Oct 21, 3:20 PM EDT - Market open") → history close 1283.32, confirmed by ycharts "Oct 21, 16:00" 1283.30 (ycharts' known 2-3c lag); ETN (quote stamped "Oct 21, 10:13 AM EDT - Market open") → history close 393.94, confirmed EXACTLY by financialcontent.com "Last Trade: Oct 21st, 8:41 PM EDT" 393.94 +3.13%.
- **Quote/history disagreement, quote kept per the partial-capture rule:** KTOS — quote closing print 38.73 vs history row 38.74.
- **History pages lagged (no Oct 21 row) but quote pages passed both tests:** CDNS, LHX, CGNX.
- **Range extensions:** KTOS lo52 38.96 → 38.73; AVAV lo52 117.63 → 117.51; NFLX lo52 65.08 → 65.04; AAPL hi52/ath 343.67 → 343.99 (new all-time high); V hi52/ath 406.57 → 407.85 (new all-time high).
- **SPY/BENCH:** SPY 773.09 (2026-10-21, +0.53%) written to spyLast/spyLastD; spyHigh stays 779.09 of 2026-10-06 — SPY 0.77% below the high, the -15% crash-reserve trigger NOT tripped.
- **Risk series:** spy[2026-10-21] = 773.09 appended; ust10 gap 2026-10-20 = 5.12 backfilled (ycharts, period Oct 20 2026, released 18:00 EDT). **UST10 for 2026-10-21 not yet published** at run time (ycharts next release Oct 21 18:00 EDT not served; mortgagenewsdaily's 10-day table ends Oct 19) — skipped per the gap rule.
- **HISTORY:** row appended for 2026-10-21 (n=36, mv 804,378.50, cost 702,026.18, unreal +102,352.32 / +14.58%, real 5,895.47, net 108,247.79, cash 36,615.38); the 2026-10-20 row's sha set to 5e42bd5 (its push commit).
- **Sanity gate:** PASS (exit 0) with --allow SPCX --allow BE --allow DDOG --allow CRDO. Playwright render check on the built page: 865 table rows, ZERO PAGE ERRORS.
- **Live-page verification caveat:** the sandbox could not fetch https://sakulratpradit.github.io/p4-trrsg5/ directly this run (WebFetch provenance/permission block in an unattended session — not a site failure). The push itself fast-forwarded cleanly and the committed index.html passed the local render check, so Pages should be serving the new build.
- **Stale/broken sources this run:** Google Finance caches badly stale per-ticker (CRDO Sep 30/Oct 8, MPWR Sep 25, DDOG Sep 15); ycharts stale for DDOG (Sep 08) and BE (Oct 09) though current for MPWR and the UST10 indicator; tipranks historical-prices ends Oct 08; benzinga SPCX quote internally inconsistent; marketscreener SPCX ends Oct 16; digrin now shows only a monthly table (its current-month figure still matched CRDO's close exactly, but did NOT match DDOG/BE — treat digrin as hit-or-miss going forward).
- Prices, mcapB (scaled by the same ratio), pxd, hi52/lo52/ath extensions, ASOF, HISTORY, BENCH spy fields and risk_series only; fundamentals, POS, TRADES, GROUPS, jan2 untouched.
