# P4 price-refresh status

**Run:** 2026-11-20 00:33–01:15 UTC (00:30 pass)
**Trading date recorded:** 2026-11-19 (plus COHR advanced to its 2026-11-18 close)
**Result:** PUSHED — commit `83de621` (sanity gate PASS, exit 0)
**Prices changed:** 61 of 63 (60 tickers at the 19 Nov close; COHR to its verified 18 Nov close 212.84)

## Headline numbers
- Portfolio MV (36 held lines): 722,186.84 | unrealised -36,294.48 (-4.79%) | HISTORY 11-19 row added
- SPY 715.87 (-1.96%), QQQ 645.04 (-2.19%) → BENCH updated; spyHigh unchanged 779.09 (SPY now -8.1% off the high; crash-reserve trigger 662.23 not hit)
- S&P 500 7,175.83 -2.02%, Nasdaq -2.25% (broad AI sell-off)
- risk_series: spy 2026-11-19 = 715.87; ust10 2026-11-18 = 5.07 (ycharts, named source — fills the gap skipped by the last two runs) and 2026-11-19 = 5.04 (dated market-wrap close, −3bp, chain-consistent with the ycharts 18 Nov value; MND/ycharts had not yet published 19 Nov)

## Largest moves (both >6% verified on a second independent source, pushed with --allow)
- **AMD -7.72% → 489.19** (China-exposure short report): fool.com header + JKN dated post-close article (489.19 / -40.95 exactly) + ycharts chain
- **PANW +6.42% → 361.73** (Q1 beat, $4.5bn Applied Compute deal): fool.com stats + Wall Street Republic dated closing wrap, both exactly 361.73
- Next: AVAV -5.14%, VRT -4.88%, MRVL -4.86%, CRDO -4.21%, CEG -4.08%. NVDA -3.30% → 145.98, another 52-week low (Q3 beat landed AFTER the close; after-hours gain not on the board, per the never-after-hours rule)

## ⚠️ SNDK SPLIT — ACTION NEEDED BEFORE THE NEXT REFRESH
SanDisk executed an **8-for-1 split effective after the 19 Nov close; split-adjusted trading begins Fri 20 Nov** (record date 9 Nov; fool.com article 16 Nov, 8-K filed 19 Nov). The 19 Nov session itself traded pre-split, but its close could not be found, so SNDK is left at the 18 Nov pre-split 776.22. **The interactive/earnings jobs must split-adjust POS shares, eps, hi52/lo52 and other per-share fundamentals BEFORE the next price refresh books a 20 Nov close (~1/8 of the old price; the 6% gate will trip by design).** Do not --allow SNDK through the gate until positions and eps are adjusted, or every SNDK-derived number on the board will be wrong.

## Unresolved (left unchanged, pxd shows staleness)
- **SNDK** — left at 18 Nov 776.22. 19 Nov pre-split close not published anywhere usable (intraday swung +7.5% at 10:05 ET to roughly -2.4% later; no dated close found). See split note above.
- **GEV** — left at 18 Nov 772.22, third run in a row. Marketbeat's 19 Nov alert headline says "falls 2.2% on analyst downgrade" (≈755) but the body is unreadable (403), and stockanalysis / Google Finance (4 variants) / ycharts / marketscreener / fool all served stale caches.
- **COHR (partial)** — 19 Nov close unresolved: +10.78% to 235.79 at 10:00 ET (dated article; chain ties), closed somewhere well up on the $2bn buyback, but no dated close print found. Booked instead its **verified 18 Nov close 212.84** (fool dated row on two URLs, chains exactly to the POEMS-reconciled 17 Nov 210.86) — this resolves the 210.87-vs-212.84 conflict noted on 19 Nov in favour of 212.84. Tomorrow's run should catch both days' catch-up (likely >6%; verify and --allow).

## Quote-page vs history-table disagreements / vendor gaps
- The primary (stockanalysis.com) and Google Finance served stale caches all night again (quote pages stamped Nov 13–18, histories ending Nov 13); GF variants were fresh only for GOOGL and NVDA. All other closes came from fool.com post-close pages — the dated "Last close 2026-11-19" row or the post-close stats block — each accepted only when the page's own day-change chained exactly to the board's stored 18 Nov close. ycharts "Nov 19, 16:00" prints used as corroboration only (per standing rule, never quoted as the close; it printed PANW 363.00 vs the verified 361.73 — its 16:00 last-trade vs the auction print).
- Fool's own 18 Nov reference close differed from the board's stored value on three names: **AMAT 351.77 vs 352.30, CGNX 49.04 vs 49.13, BWXT 117.66 vs 117.93** (0.15–0.23%). The day was proven by fool's printed 2026-11-18 date; the 19 Nov closes were booked from the stats block. Gap noted, not resolved — worth a POEMS cross-check at the next reconciliation.
- One wrong-year trap caught and discarded: a "US close… ahead of Nvidia results" article that was from 19 Nov **2025**; also a stale blockchain.news "GEV closed 796.77" figure that failed the chain check. quantisnow compare pages are undated and were discarded on sight.

## Blockers / notes
- Live-page verification not possible from this sandbox: sakulratpradit.github.io is refused by both WebFetch (not on allowlist) and the egress proxy (403), and the GitHub Pages build API is blocked by the proxy. The push landed cleanly on main (2edbf64 → 83de621, no rejection), and the committed index.html is byte-identical to the sanity-gated build.
- Previous HISTORY row (2026-11-18) 'sha' set from 'live' to c1ae515 per the 18 Nov status note.
- Every number written this run came from a tool call in this session; AMD and PANW were the only --allow overrides, both dual-source verified.
