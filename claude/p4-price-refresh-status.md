# P4 price refresh status

- Run time: 2026-10-20 00:33–00:55 UTC (scheduled 00:30 run)
- Trading date recorded: 2026-10-19 (Mon)
- Result: PUSHED
- Commit: 8aaacf3 (`Daily price refresh 2026-10-20 run (closes of 2026-10-19): 63 prices`)
- Prices changed: 63 of 63 (all pxd -> 2026-10-19); SPY 766.48 written to BENCH and the daily risk series
- Sanity gate: PASS, no `--allow` needed (no move reached 6%; largest SE -5.65%, SNDK +5.53%, DDOG +5.36%, AMZN +4.98%)
- Unresolved tickers: none
- UST10: SKIPPED for 2026-10-19 — mortgagenewsdaily's 10-day table ends at an Oct-18-dated close (5.064) and ycharts at Oct 16 (5.09); undated live tickers (5.077, 5.144) failed the provenance bar. Gap left in risk_series.json per the job's rule.
- History-fallbacks (quote page stale, per resolution rule step 4): ETN 391.50 (quote stamped "Oct 19, 10:10 AM EDT - Market open"; confirmed exactly by Google Finance "Closed: Oct 19, 4:00:07 PM GMT-4") and TSEM 200.30 (quote stamped Oct 16; confirmed exactly by ycharts "Oct 19, 16:00").
- Quote/history disagreements, quote kept per the partial-capture rule: NET (history row a 9:41 AM partial capture, vol 215k, close 300.68 discarded; quote 297.58) and BWXT (history 135.77 vs quote 135.83). CGNX and LHX history pages lagged (no Oct 19 row); their quote pages passed both stamp and prev-close tests.
- Range extensions: FSLR lo52 -> 171.80, KTOS lo52 -> 39.17, AVAV lo52 -> 117.90 (all new 52-week lows); V hi52/ath -> 402.92 (new all-time high).
- HISTORY row appended for 2026-10-19: n=36 (post-CRWD exit), mv 796,904.83, unreal +94,878.65 (+13.51%), real 5,895.47, cash 36,615.38. The 2026-10-16 row's sha set to 6deb64b.
- spyHigh unchanged at 779.09 (2026-10-06); SPY is 1.62% below it — the -15% crash-reserve trigger NOT tripped.
- Verification: remote main matches the local build byte-for-byte after push; `check_dashboard.js` (Playwright) rendered 865 table rows with ZERO PAGE ERRORS. Direct fetch of the live github.io URL was not possible from this sandbox (the fetch tool's permission prompt cannot be answered in an unattended run) — rendering was verified on the identical pushed HTML instead.
- Blockers: none.
