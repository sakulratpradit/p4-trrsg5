# P4 price refresh status

- **Run time:** 2026-11-25 03:33–05:25 UTC (03:30 UTC job)
- **Trading date recorded:** 2026-11-24 (Tue)
- **Status:** PUSHED
- **Commit:** 9c83df2 (on top of 8b571a4; fast-forward push, no force, no rejection)
- **Prices changed:** 42 of 63 — the board is now complete at the 24 Nov close (62/63) except **SNDK**. Sanity gate PASS (exit 0) with 16 `--allow`s. Playwright: ZERO PAGE ERRORS, 921 rows.
- **First check:** 20/63 at pxd 2026-11-24 at 03:33 UTC (below the stop threshold) → run proceeded as the completing pass after the 00:30 partial (49b3efc, 21 prices).

## Sources (stockanalysis.com unusable again)
stockanalysis quote pages still served a stale **Nov 20** snapshot; even /history/ tables ended Nov 20–23 — no Nov 24 row anywhere. Google Finance caches were months old (Sep 25/30). Closes came from per-ticker **dated post-close sources**, each chain-validated against the verified 23 Nov board:
- **StockTitan overview/company pages** — explicit "closed at $X on November 24, 2026" with 16:08–19:59 EST update stamps (the workhorse: ~24 names).
- **aaii.com "Stock Price as of Market Close"** 4:00 PM prints (auto-updating; per-URL cache lottery — a second article URL for the same ticker often had the fresh copy): NET, HOOD, ISRG, ETN, FN, BWXT, STRL, LITE, CIEN, AMAT.
- **financialcontent partner pages** with "Official Closing Price Updated" / 4:00 PM stamps: ORCL (concordmonitor), MPWR (chroniclejournal), STX (prnews), ASML (bpas), MRVL (wedbush), CDNS.
- **Fox Business 4:00 PM "Closed Market" pages**: TER, NFLX, SPCX, CIEN (+ intraday corroboration on several).
- **Schwab wallst 3:59–4:00 PM snapshots**: TER, MPWR (+ intraday corroboration RKLB).

## Largest move
ALAB −13.88% (222.12 → 191.30). The whole AI-hardware complex sold off: CRDO −13.07%, FN −11.92%, MPWR −10.77%, LITE −10.52%.

## >6% movers, all verified and --allowed (16)
MRVL 131.57 (−9.10%, FC wedbush + StockTitan) · MPWR 1190.16 (−10.77%, chroniclejournal official close + Schwab 3:59) · LRCX 196.16 (−6.48%, StockTitan close + Fox intraday corroboration) · AMAT 323.76 (−6.66%, aaii 4PM + StockTitan intraday corroboration) · TER 213.22 (−8.69%, Fox 4PM Closed + Schwab 4PM) · STX 482.48 (−7.23%, StockTitan + FC prnews 4PM) · LITE 487.12 (−10.52%, StockTitan + aaii) · COHR 196.24 (−9.07%, StockTitan ×2 + FC wss intraday corroboration) · ALAB 191.30 (−13.88%, StockTitan + the 00:30 run's fool print at the same 191.30) · CRDO 106.46 (−13.07%, StockTitan + Fox 106.87 near-close corroboration) · FN 290.12 (−11.92%, aaii 4PM + Fox 3:59 PM 290.01) · RKLB 45.98 (−7.35%, StockTitan + Schwab intraday corroboration) · VRT 173.82 (−6.72%, StockTitan + FC ricentral intraday corroboration) · BE 156.41 (−6.98%, StockTitan + the 00:30 run's Fox 156.38 print) · STRL 256.15 (−8.11%, aaii + StockTitan FAQ) · CIEN 239.27 (−9.57%, aaii + Fox 239.28). Corroboration on LRCX/CRDO/RKLB/VRT/COHR/AMAT is a dated close print plus an independent intraday/near-close confirmation of the move (the KLAC precedent), not two close prints — flagged for transparency.

## Source disagreements (which value was taken)
- **TSM**: StockTitan 349.20 vs Fox ~349.66 (page internally garbled; labels swapped) → took **349.20**.
- **BE**: StockTitan 156.41 vs Fox (00:30 run) 156.38 → took **156.41** (later, post-close stamp).
- **CIEN**: aaii 239.27 vs Fox 239.28 → took **239.27**; note aaii/StockTitan put the 23 Nov CIEN close at 264.73 vs the board's 264.60.
- **FN**: prev close shown 329.22 (aaii) / 329.32 (Fox) vs board 329.40 — closes chain-consistent, mismatches ≤5 bp, noted.

## Unresolved (1)
- **SNDK**: left at 633.96 / pxd 2026-11-20. The 8-for-1 split is still unbooked — a price-only booking would corrupt P/E against the pre-split eps 15.70. Needs the interactive/earnings job (standing warning, third run in a row).

## Benchmarks / series
- **SPY 718.78 (24 Nov)** booked — FC bpas "Official Closing Price Updated: 8:00 PM EST, Nov 24", chain-valid vs 722.29 (−0.49%). The 00:30 run could not find this; now filled. spyHigh unchanged 779.09 (drawdown −7.7%, above the −15% crash-reserve trigger). QQQ was already at 24 Nov (638.10).
- **risk_series**: spy[2026-11-24] = 718.78; ust10[2026-11-24] = **4.91** (ycharts, dated "for Nov 24 2026"). ycharts shows 23 Nov at 4.92 vs the backfilled 4.91 — left unchanged (1 bp, not confirmed by a second source).
- **HISTORY 2026-11-24 row trued up** (was computed with 15 names at 23 Nov marks): n 36, mv 708,944.58, cost 763,111.29, unreal −54,166.71 (−7.10%), real 6,263.88, net −47,902.83, cash 1,267.41.

## Blockers verbatim
- "URL_NOT_ON_ALLOWLIST" — the live page https://sakulratpradit.github.io/p4-trrsg5/ is still not fetchable from this sandbox, so rendering was verified locally instead: `node src/check_dashboard.js` → "ZERO PAGE ERRORS", 921 rows.
