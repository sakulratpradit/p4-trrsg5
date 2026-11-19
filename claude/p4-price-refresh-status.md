# P4 price-refresh status — 2026-11-19 03:30 UTC pass

- **Run time:** 2026-11-19 ~03:33–04:00 UTC (second scheduled pass)
- **Trading date recorded:** 2026-11-18
- **Result:** PUSHED — commit `c1ae515` ("Daily price refresh 2026-11-18 (03:30 pass): GEV 772.22 resolved; COHR still unresolved")
- **Prices changed this pass:** 1 (GEV). The 00:30 pass (commit f620edc) had already booked 61/63 at the 18 Nov close plus SPY/QQQ and the HISTORY row, so this pass only chased the leftovers.

## GEV — resolved
- Booked **772.22**, pxd 2026-11-18 (−0.99% vs the POEMS-reconciled 17 Nov close 779.91).
- Source: fool.com /quote/nyse/gev/ dated "Last close USD 772.22, 2026-11-18" row; the page's day change (−7.73 / −0.99%) back-computes exactly to 779.91, and intraday prints (fool article 778.04 @ 12:16 PM ET, day range 770.00–800.53) are consistent. After-hours quoted separately (782.00), confirming 772.22 is the regular-session close.
- Note: the same page's undated "current price" field read 772.18 (4¢ below the dated row); the dated last-close row was taken.
- mcapB scaled to 205.66; pe 20.22, ps 4.67, fpe 36.76, peg 0.93, M3 pfcf 13.66 rescaled per the price-linked-ratio rule. hi52/lo52 unchanged (within range). HISTORY 2026-11-18 row corrected in place (mv 744,627.16; unreal −13,854.16 / −1.83%).

## COHR — STILL UNRESOLVED (second run in a row), left at 17 Nov close 210.86
- No source anywhere shows a dated 18 Nov close. stockanalysis quote stamped Nov 6, history ends Nov 13; Google Finance both cache forms stamped Oct 26 / Oct 6; marketscreener Nov 16; fool quote page internally inconsistent (mixes Nov 17 close 210.86 with a Nov 17 day-change block and an unexplained +6.68% after-hours print).
- Best intraday evidence: ycharts 210.88 at Nov 18 14:41 (+0.01%) — suggests roughly flat, but intraday is not a close. Per the rules, left unchanged rather than guessed.

## Other
- **ust10 (risk_series):** 18 Nov 10-year close not yet published — MND 10-day table and ycharts both end at 17 Nov. Skipped again (spy 18 Nov row was already written by the 00:30 pass). The monthly risk run copes with gaps, but if MND/ycharts have rolled by the next run, backfilling 2026-11-18 would be worthwhile.
- **Sanity gate:** exit 0, nothing blocked, no --allow needed (GEV −0.99%).
- **Live page:** sakulratpradit.github.io is unreachable from this sandbox (proxy + fetch-provenance limits), so the exact pushed index.html was rendered locally with Playwright instead: ZERO page errors, GEV 772.22 present. Pages deploys from main; the push landed cleanly (99385e6..c1ae515, no force, no rejection).
- **Stale/broken sources tonight:** stockanalysis (quote + history, both tickers), Google Finance (all cache forms), marketscreener (GEV Nov 13 / Oct 16, COHR Nov 16), benzinga (client error), futunn (JS-only), finance.biggo (Nov 17 session only).
