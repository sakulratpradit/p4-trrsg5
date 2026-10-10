# P4 price refresh status

- Run time (UTC): 2026-10-10 (Saturday slot; scheduled-cloud run)
- Trading date recorded: 2026-10-09 (Friday)
- Result: PUSHED
- Commit: 8664868 "Daily price refresh 2026-10-09: 62 prices" (another writer then pushed 16d6303 on top; verified our 62 prices, HISTORY row and BENCH survive on that head)
- Prices changed: 62 of 63 (all from stockanalysis.com quote pages, each validated against its /history/ table; Playwright render check: ZERO PAGE ERRORS)
- Unresolved / skipped: SPCX (SpaceX - private, no public quote; left at its 2026-10-08 mark by design)
- >6% movers: DDOG +7.11% to 293.26 - confirmed via Google Finance BETA page (exact match, "Closed: Oct 9, 4:00:01 PM GMT-4"); the non-beta Google page was badly stale (Nov 1, $123.26) and was discarded. Gate re-run with --allow DDOG: PASS.
- Quote/history disagreements (took history row per resolution rule; quote page's own last price agreed in both cases): MRVL 275.28 (quote prev-close 274.60 vs history Oct 8 274.66), ORCL 141.40 (quote prev-close 135.19 vs history 135.69). FN and LHX history Oct 9 rows looked like partial captures (491.87 vs quote 486.28; 237.04 vs 236.97) - quote page passed both tests and was used.
- 52w ranges extended on closes outside stored range (ANET 216.74, V 385.45, FTNT 194.75, PLTR 209.05, DDOG 293.26).
- HISTORY row appended for 2026-10-09: n=37, mv=828,407.84, cost=667,992.30, unreal=+160,415.54 (+24.01%), real=3,279.04, net=+163,694.58, cash=148,016.38.
- BENCH: spyLast=778.57, spyLastD=2026-10-09 (stockanalysis.com/etf/spy/, at-close stamp, prev close matched history).
- Stale/broken sources: Google Finance non-beta DDOG page served a Nov 1 cache ($123.26) - discarded; STRL and TSEM /history/ tables had no Oct 9 row yet (quote pages passed both tests and were used).
- Blockers: live-page HTTP check from this sandbox was blocked by egress policy (github.io CONNECT denied), so the live URL was not fetched directly; render verified locally (Playwright, zero errors) and remote head verified to carry the data.
