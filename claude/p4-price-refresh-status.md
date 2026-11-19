# P4 daily price refresh — status

- **Run time (UTC):** 2026-11-19 00:33 – 02:05 (00:30 pass)
- **Trading date recorded:** 2026-11-18 (Wed)
- **Result:** **PUSHED** — commit `f620edc` (`ef6dd85..f620edc main`)
- **Prices changed:** **61 of 63** + SPY 730.20 / QQQ 659.51 (both 2026-11-18); HISTORY row appended (mv 744,727.13, unreal −13,754.19, −1.81%); risk_series `spy[2026-11-18]=730.20`.
- **Sanity gate:** PASS with `--allow PANW --allow CRWD` (both ≥6% moves verified against two independent sources). Local render check: ZERO PAGE ERRORS, 901 rows.

## Unresolved — left at the 17 Nov close (pxd 2026-11-17)
- **GEV** (held, 13 sh, 1.36% of stocks MV): every source served stale caches (fool quote-page variants crawled 4/16 Nov, stockanalysis 6 Nov, marketscreener 12 Nov); only an intraday 12:16 PM ET capture (778.04, −0.24%) exists. The 11-18 HISTORY row therefore carries GEV at 779.91 (17 Nov) — error bounded well under 0.1% of mv.
- **COHR** (not held): sources conflict — fool NYSE page main/AH-base 210.87 vs fool delisted-NASDAQ page "Last close USD 212.84 dated 2026-11-18" vs a junk +7.44 change line. Left unchanged rather than guess.
- **ust10[2026-11-18]:** skipped — MND's 10-day table and ycharts end at 17 Nov (5.084). Dated news recaps print ~5.07 (cappnotes 5.07, investrade 5.065 at 21:09 UTC) but those are 4 PM marks, not the named sources' close. **Also note:** 17 Nov in risk_series is 5.10; MND's table now prints the 17 Nov close as 5.084 — the main session may want to true that up.
- 03:30 pass should mop up GEV, COHR and ust10 (the ≥80-ticker first-check can never trigger with 63 tickers, so it will run).

## Largest moves
PANW +9.90% → 339.92 (FQ1-2027 results day; fool box stamped "As of 4:00 PM ET 11/18/26", +30.63 ties exactly to the 17 Nov base; cappnotes recap +9.90% — second source). CRWD +7.95% → 237.03 (fool quote page printed "Last close 2026-11-18"; cappnotes +7.95% — second source). Then FTNT +5.87%, NET +5.66%, AMD +5.31%, ANET +4.03%, AMZN +3.82%, AVGO +3.64%. **NVDA −2.89% → 150.96, a new 52-week low (lo52 extended from 155.46), the day after its Q3 print.** Index context: S&P −0.23%, Nasdaq +0.42%, Dow −1.11%.

## Sources, staleness and method (deviations flagged)
- **stockanalysis.com (primary) was stale for 62 of 63 names all night** — quote pages served crawl-archive copies dated Nov 6–17 (MRVL even Sep 2025); history tables ended Nov 13, so the resolution rule's test (b) could not use them. Only NVDA's quote page was fresh ("At close: Nov 18, 2026, 4:00 PM EST"). ETF pages (SPY/QQQ) stale at Nov 13 all night.
- **Google Finance (second source) was worse:** Oct 26 / Oct 23 / Oct 5 / Sep 24 caches on both URL forms. marketscreener Nov 12–13. 247wallst's "movers at the close (4:10 PM)" are delayed snapshots (printed PANW 338.12 against the true 339.92) — rejected. financhle = live after-hours — rejected. marketlog/chartrow garbage or frozen.
- **What worked: fool.com pages crawled fresh after tonight's close.** Deviation from the letter of the job (quote page + history table): with both primaries stale, 61 closes were taken from fool.com post-close pages under this validation, applied per ticker: (1) an after-hours quote on the page proves a post-close crawl; (2) the printed "Last close" line either shows **2026-11-18 with the close itself** (dated print — strongest) or shows 2026-11-17 **equal to the board's POEMS-reconciled 17 Nov close** (proving lineage), with the "Previous Close" field rolled to the new value; (3) the page's day-change arithmetic reproduces the 17 Nov base exactly; (4) the value sits inside the page's printed day range. Field semantics calibrated on NVDA (field = 150.96 = the stockanalysis-stamped official close) and cross-checked on TSM/V/CAT/CRWD dated prints. Six megacaps came from the fool market-wrap article's post-close ticker bar (published 22:40 UTC), anchored by NVDA 150.96 exact and AMZN 267.74 = 257.89 × (1+3.82% cappnotes) exact; GOOGL 282.44 from a 21:26 UTC post-close recap, +0.80% ties to the cent.
- fool quote-page slug variants have independent caches — a stale variant does not mean the ticker is stale; trying 2–3 variants resolved LRCX, STX, ASML, BWXT, VRT, LITE (and exposed GEV/COHR as genuinely unresolvable tonight).
- **Could not verify the live GitHub Pages URL from this sandbox** (fetch allowlist); verified instead that the pushed page renders locally via src/check_dashboard.js (ZERO PAGE ERRORS). Pages deploys from main, and the push was clean.

## Watch-outs for the next runs
- LITE's two fool crawls disagreed on after-hours (594.71 vs 562.80); the accepted close 551.07 comes from the self-consistent crawl (−1.65% ties exactly to 559.97). LITE AH +2.2–6% on evening news — expect a gap tomorrow.
- PANW reported FQ1 AMC tonight and was +8% after hours — expect a big 19 Nov move (likely >6%, plan second sources).
- Anthropic (ANT) IPO expected to start trading Thu 19 Nov — market-wide volatility risk for the AI names.
