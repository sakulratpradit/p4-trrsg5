# P4 price refresh status

- **Run time (UTC):** 2026-09-26 00:41–01:05 (Saturday 00:30 scheduled run)
- **Trading date recorded:** 2026-09-25 (Friday close)
- **Result:** PUSHED
- **Commit:** 92f22c9 (`Daily price refresh 2026-09-25: 94 prices`, on top of 5427aab)
- **Prices changed:** 94 of 94 tickers updated to the Fri 2026-09-25 close; sanity_check's rounded diff showed 93 moves. mcapB scaled with each price (SKHY has no mcapB, left null). pxd set to 2026-09-25 on all 94. ASOF updated.
- **HISTORY row appended:** {d: 2026-09-25, n: 37, mv: 753,448.87, cost: 609,758.47, unreal: +143,690.40 (+23.57%), real: -540.47, net: +143,149.93, cash: 203,906.85}. Previous row's sha set to fe0bfc1.
- **Largest move:** BE +8.27% (266.65 → 288.70).
- **Sanity gate:** first run BLOCKED on BE +8.27%, CRDO +7.65%, TSEM +6.07% (expected >6% trips). All three confirmed against Google Finance (each stamped "Closed: Sep 25, 4:00 PM GMT-4" with matching price and % move: BE 288.70 +8.27%, CRDO 210.97 +7.65%, TSEM 230.47 +6.07%). Re-ran with `--allow BE --allow CRDO --allow TSEM` → PASS. Threshold not touched.
- **Quote vs history disagreements (quote taken per resolution rule; prev-close test passed on every one):** ONDS 7.64 vs history 7.82 (2.4% gap — Google Finance confirmed 7.64 at the Sep 25 close, history row rejected); MCHP 78.69 vs 78.63; LRCX 315.21 vs 315.17; FSLR 177.71 vs 177.59; HUBB 466.62 vs 466.00; AMBA 72.68 vs 72.64; SE 99.55 vs 99.49; KTOS 45.62 vs 45.47; IBM 225.51 vs 225.75; CRWV 87.59 vs 87.61; SPCX 148.68 vs 148.67.
- **History tables missing the Sep-25 row (quote page used, prev-close verified):** AXTI, CGNX, LHX, BWXT.
- **Unresolved tickers:** none — 94/94 resolved.
- **52-week range extensions (close outside stored range):** AMD hi52 → 630.63; LHX lo52 → 237.69; BWXT lo52 → 138.47.
- **Source notes:** stockanalysis.com quote pages all stamped "Sep 25, 2026, 4:00 PM EDT" — no stale or intraday snapshots this run. WebFetch provenance enforcement was intermittent; per-ticker searches restored access. Google Finance /quote and /beta/quote both worked for second-sourcing.
- **Blockers:** live-page render check could NOT be performed: WebFetch refused https://sakulratpradit.github.io/p4-trrsg5/ with PROVENANCE_REQUIRED (URL never appeared in a search result), and the PAT lacks Pages/Actions API scope (403). The push itself succeeded (5427aab..92f22c9), so Pages should redeploy as on every prior run, but rendering is unverified this session.
