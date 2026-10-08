# P4 price refresh status

- Run time (UTC): 2026-10-08 ~00:40-01:05 (first run of the day, 00:30 slot)
- Trading date recorded: 2026-10-07 (Wed)
- Result: **PUSHED**
- Commit: 6580073 (`Daily price refresh 2026-10-07: 63 prices`), confirmed at origin/main via ls-remote
- Prices changed: 63 of 63 (all pxd set to 2026-10-07); SPY 777.22 written to BENCH (spyLastD 2026-10-07); HISTORY row appended for 2026-10-07 (mv 818,819.74, n=37, cash 170,247.90); previous HISTORY row's sha set to b881415
- Largest move: CGNX -7.75% (66.35 → 61.21)
- Sanity gate: first run EXIT 1 on CGNX (>6%); verified against ycharts (61.24, stamped "Oct 07, 16:00", -7.70%) and a 7 Oct StockStory article (12:50 PM EDT, $61.86, -7.5% intraday, sector-wide selling) → re-ran with `--allow CGNX`, PASS
- Quote vs history disagreements (quote page taken per the resolution rule in both cases):
  - NET: quote 342.97 ("At close: Oct 7, 4:00 PM EDT", prev close 355.01 matched) vs a history row of 345.66 captured intraday at 10:10 AM
  - CGNX: history table stale (latest row Oct 5); quote page prev close 66.35 matched our validated 6 Oct close. Google Finance (both forms, Sep 25 / Oct 2 caches) and marketscreener (Aug 11) were stale for CGNX; ycharts + StockStory used instead
- Unresolved tickers: none
- Hi/lo updates: ANET hi52 → 215.83; LHX lo52 → 233.63; KTOS lo52 → 41.94
- Live page: could not fetch https://sakulratpradit.github.io/p4-trrsg5/ from this sandbox (WebFetch provenance block on that URL). Verified instead by rendering the pushed index.html locally with check_dashboard.js: 799 table rows, ZERO PAGE ERRORS; remote head matches the pushed commit.
- Stale/broken sources this run: stockanalysis CGNX /history/ (2 days stale); Google Finance quote + beta caches stale for CGNX and NET; marketscreener CGNX stale (Aug 11); ycharts NET stale (Oct 6). WebFetch needed a seeding WebSearch per ticker for most quote/history pages (PROVENANCE_REQUIRED otherwise).
- Blockers: none
