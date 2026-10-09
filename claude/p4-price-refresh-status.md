# P4 price refresh status

- Run time (UTC): 2026-10-09 00:40 - 01:0x (00:30 slot)
- Trading date recorded: 2026-10-08 (Thu)
- Result: PUSHED
- Commit: c0a55e3 ("Daily price refresh 2026-10-08: 63 prices")
- Prices changed: 63 of 63 (plus SPY 773.93 / 2026-10-08 written to BENCH; HISTORY row appended: mv 799,237.60, unreal +153,573.28, 23.79%)
- Largest move: COHR -9.63% to 302.35
- Moves >6%, all second-sourced and pushed with --allow: COHR -9.63% (Google Finance exact, Closed Oct 8), ALAB -9.21% (marketscreener, Market Closed 08/10/2026, 347.05 exact), TSEM -7.85% (Google Finance exact), ARM -6.48% (ycharts 275.37, Oct 08 16:00), GLW -6.38% (Google Finance labs form exact), VST -6.35% (see below), BE -6.34% (Google Finance hl=es cache exact, Closed Oct 8 16:00:08)
- VST caveat: no fresh USD second source found - Google Finance caches (4 language variants), marketscreener USD page, ycharts, alphaquery, fool/tikr articles were all stale (Oct 2-6 or older). Confirmed instead via marketscreener's Boerse Muenchen EUR cross-listing: -6.40% stamped 2026-10-08, matching the stockanalysis quote page (which passed both resolution-rule tests: stamp "Oct 8, 4:00 PM EDT"; prev close 166.72 == history Oct 7 close == our stored 10-07 price). Judged confirmed; flagging the weaker source per the report rule.
- Quote/history disagreements: CGNX - quote page stamped intraday 12:26 PM EDT, so took the HISTORY row close 60.91 (-0.49%) per rule 4. DDOG - history Oct 8 row was a partial-session capture (754K volume vs ~2M normal, close 277.79); quote page passed both tests, took the quote 273.80 (+0.91%).
- Unresolved tickers: none (63/63). Stored 10-07 prices matched every quote page's previous close exactly - right-day check passed on all 63.
- Sanity gate: PASS (exit 0) with --allow COHR ALAB TSEM ARM GLW VST BE; threshold untouched. check_dashboard.js: ZERO PAGE ERRORS, 799 rows.
- Live page: could NOT verify https://sakulratpradit.github.io/p4-trrsg5/ from this sandbox (WebFetch provenance block on that URL). Remote main confirmed at c0a55e3 via ls-remote and the committed page render-checked locally with Playwright instead.
- Other source notes: Google Finance /quote/ caches were per-ticker stale as usual (ARM Sep 25, BE Sep 25 on default cache, VST Oct 2-6); the hl=xx language variants carry independent caches and twice yielded a fresh page. nasdaq.com/articles, tikr, weissratings, digrin, globeandmail all stale or unusable for Oct 8.
