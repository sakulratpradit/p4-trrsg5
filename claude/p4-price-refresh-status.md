# P4 price refresh — status

- **Run time:** 2026-10-01 ~00:40–01:10 UTC (00:30 scheduled run)
- **Trading date recorded:** 2026-09-30 (Wed)
- **Result:** PUSHED
- **Commit:** a8f009a "Daily price refresh 2026-09-30: 94 prices" (on top of 91167e5; remote main confirmed at a8f009a via ls-remote after push)
- **Prices changed:** 94 of 94 (93 moved; MU changed by 3 cents). Largest move: **ZETA +9.01%**.
- **Sanity gate:** PASS (exit 0) with `--allow ZETA`. ZETA +9.01% confirmed real against two independent sources: marketbeat 30 Sep instant alert (prev close 28.96, intraday +6% to 30.69) and cryptonomist 30 Sep (+9.43% intraday); stockanalysis history row agrees exactly (31.57).
- **Unresolved tickers:** none. **XE recovered** from its Sep 28 staleness: quote page stamped Sep 30, 4:00 PM EDT, stated prev close 14.29 matched the history table's Sep 29 row; close **14.18** written, pxd jumps 2026-09-28 → 2026-09-30.
- **MPWR special case:** quote page (stamped Sep 30, 4:00 PM EDT) stated prev close 1,353.99 vs the validated Sep 29 close 1,355.99 — exactly the $2.00 quarterly dividend going ex (payable Oct 15 per marketscreener). Quote close **1,347.22** taken (−0.65% vs the unadjusted stored close, within gate). Every second source was stale (Google Finance quote cache Sep 25, ycharts Sep 21, fool.com Sep 4, marketscreener showing the Sep 22 close).
- **Quote vs history disagreements (quote taken per the resolution rule in all cases — quote passed both freshness tests):**
  - Partial-session history rows on anomalously low volume: PWR (row 647.07 on 30.6K shares; quote 642.51 is below the row's stated low), HUBB (row 459.96 on 33.6K shares; quote 453.60), CGNX (row 60.72 on 355K shares; quote 60.66).
  - Cent-level disagreements: SNDK (9c), LITE (~$1), CRDO (6c), ISRG (4c), DDOG (16c), FTNT (1c), SHOP (1c), AMBA (22c), TSEM (10c), HOOD (6c).
  - History tables had **no Sep 30 row** for FN, FSLR, AEP, STRL, CIEN, FPS, XE — quote pages passed both tests (4:00 PM EDT Sep 30 stamp + prev close matched the validated prior close) and were used.
- **Source gaps:** TER, STX, BWXT history pages never surfaced through WebSearch, so WebFetch's provenance gate blocked them; their quote pages passed the stamp test and the prev-close test against the stored (validated) Sep 29 closes. SKHY history page confirmed the quote exactly.
- **hi52 extended:** PANW 397.31, CRWD 264.75, FTNT 178.76. **lo52 extended:** KTOS 42.69, APP 290.43.
- **HISTORY:** row appended for 2026-09-30 (n=38, mv=787,941.44, cost=645,117.62, unreal=142,823.82 / +22.14%, net=142,283.35, cash=168,542.71); the 2026-09-29 row's sha set to 7880328.
- **Live-page render check:** NOT performed. The GitHub Pages URL could not be surfaced in any search result, so WebFetch's provenance gate refused to fetch it, and raw HTTP from the sandbox is not permitted. Push to main is confirmed (ls-remote shows a8f009a), so Pages should rebuild from it as usual.
- **Blockers:** none otherwise. Prices only; fundamentals, POS, TRADES, GROUPS untouched.
