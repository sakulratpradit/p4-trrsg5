# P4 price refresh — status

- Run time (UTC): 2026-10-06 00:42–01:15
- Trading date recorded: 2026-10-05 (Mon)
- Result: PUSHED
- Commit hash: 078c5a6 ("Daily price refresh 2026-10-05: 63 prices"), pushed 1fcd7ca..078c5a6 on main, first attempt, no rejection.
- Prices changed this run: 63 of 63. All from stockanalysis.com QUOTE pages stamped "Oct 5, 2026, 4:00 PM EDT", each validated against its history table's Oct-2 prior close per the resolution rule.
- Largest move: SPCX +7.63% (158.96 → 171.09). Over the 6% gate; confirmed against a second source (fool.com article published 5 Oct with embedded quote box: $171.09, +7.63%). Google Finance was unusable for SPCX (both quote and beta caches stale at Sep 25). Gate re-run with --allow SPCX → RESULT: PASS.
- Next largest: APP +5.13%, STX +4.49%, CEG +3.93%, ISRG +3.71% — all under threshold.
- Quote page vs history table disagreements (quote taken per rule 4 in every case, quote passed both tests): SNPS (488.47 vs 488.49), LRCX (345.80 vs 345.84), LITE (1,091.67 vs 1,092.45), ALAB (362.34 vs 362.50), CGNX (64.37 vs 64.36), LHX (236.88 vs a partial-session history row: close 236.50 on volume 29,016 vs ~1.5M normal — the known defect, discarded).
- History tables missing the Oct 5 row entirely (quote page used, passed both tests): MPWR, FN.
- GE note: quote page "previous close" 309.09 is the dividend-adjusted Oct-2 close (raw 309.56 matches the board) — ex-dividend adjustment, not staleness.
- Unresolved tickers: none. 63/63 resolved, no values invented, none carried from memory.
- HISTORY row appended for 2026-10-05: n=38, mv=828,367.91, cost=659,849.81, unreal=+168,518.10 (+25.54%), net=+167,977.63, cash=153,810.52. Previous row's sha set from 'live' to 3b87f15. NOTE: mv still includes ORCL 75 sh and CRWD 20+20 sh at full count — the Monday-night sell orders (ORCL 75, CRWD 20) are not yet reflected in POS; that reconciliation belongs to the interactive session.
- Live-page verification: NOT DONE. This unattended cloud run could not fetch https://sakulratpradit.github.io/p4-trrsg5/ (WebFetch provenance/permission requires a live user approval) and the GitHub Pages build-status API path is blocked by the sandbox proxy. The pushed index.html is the exact sanity-checked build; please eyeball the live page.
- First-check outcome at 00:42 UTC: 0/63 tickers had pxd = 2026-10-05, so this (00:30) run did the refresh. The 03:30 run should stop at the first check. The literal "80 or more" threshold remains unreachable on a 63-name board — previous run already suggested updating it in price_refresh.md.
- Blockers: none.
