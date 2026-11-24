# P4 Price Refresh — Status

**Run:** 2026-11-24 03:40 UTC (03:30 UTC Tue–Sat job)
**Trading date recorded:** 2026-11-23 (Mon)
**Result:** PUSHED
**Commit:** e420207 (70be41f..e420207, main)
**Prices changed:** 23 watch-list tickers + SPY benchmark + risk_series spy row
**Sanity gate:** PASS (exit 0), with --allow ARM STX COHR HOOD BE TSEM
**Live render:** build passed gen_dashboard + sanity gate; local Playwright check_dashboard.js = ZERO PAGE ERRORS, 921 rows. Live github.io page not fetchable from sandbox (network-firewalled) — serves the byte-identical pushed index.html.

## What happened
All 36 held positions were already at the 23 Nov close (POEMS true-up, prior commit 70be41f). This run cleared the remaining stale **watch-list** names (not held → no MV/HISTORY impact). The existing 2026-11-23 HISTORY row was left unchanged (no held price moved); no duplicate row added.

## 23 resolved (prior → 23 Nov close)
ARM 152.20→176.67 · SNPS 430.91→426.99 · MPWR 1295.86→1333.88 · STX 457.01→520.10 · GLW 105.97→108.31 · COHR 187.21→215.81 · FN 311.71→329.40 · LHX 256.54→254.82 · KTOS 29.65→28.50 · DDOG 166.46→169.02 · HOOD 62.20→67.37 · FTNT 131.46→131.10 · NET 303.68→291.13 · BWXT 117.06→115.83 · PWR 587.43→609.00 · BE 142.39→168.15 · NFLX 58.46→58.10 · APP 379.02→373.92 · SE 65.94→65.53 · GE 318.88→321.26 · STRL 273.25→278.77 · TSEM 127.77→136.81 · CIEN 262.63→264.60
(mcapB, pe, ps, fpe, peg, M3 pfcf rescaled with price for each.)

## Six >6% moves — verified vs 2nd source, --allow'd
- ARM +16.1%: Fox dated 4PM 176.67 (prev 152.20 chains) + ycharts 176.84 (+16.19%)
- STX +13.8%: Fool dated 520.10 (11-23) + ycharts 519.28 (+13.63%)
- COHR +15.3%: StockTitan 215.81 (11-23) + ycharts 215.82 (+15.28%)
- HOOD +8.3%: StockTitan 67.37 + Fool 67.37 (both dated 11-23)
- BE +18.1%: StockTitan 168.15 + Fox 168.11 (+18.05%)
- TSEM +7.1%: Fox dated 4PM 136.81 + Fool 136.81 (both 11-23)

## Quote vs history / source disagreements
- stockanalysis.com (primary) was serving a STALE 20 Nov snapshot site-wide all run; its /history/ tables ended weeks back (FN Oct 26, STRL Nov 6). Fell back to Fox Business dated-4PM quote pages (prev-close chain-validated), StockTitan dated closes, and Motley Fool dated last-close lines; ycharts used only as 2nd-source confirmation (runs a few cents light, never quoted as the close).
- **FN & STRL cross-contaminated** across Fox/Fool (their day-change *bases* were swapped). Untangled by each page's day-change base price: the name trading ~285 on 20 Nov (=FN) went +44.5 → **FN 329.40**; the name at 247.92 on 20 Nov (=STRL) went +30.85 → **STRL 278.77**. FN additionally chain-validated on Fox (prev close 284.99 = FN's own 20 Nov).

## UNRESOLVED (left at prior close)
- **CRWD** — left at 243.46 (11-19). No clean dated 23 Nov 4:00PM close: ycharts 204.60 was 14:54 *intraday*, Fool price undated, Google Finance cache stale (Oct). Prior overnight run also flagged CRWD source-conflicted. A stale price is recoverable; a wrong one is not.
- **SNDK** — left at 633.96. 8-for-1 split completed ~20 Nov (post-split 23 Nov close ≈ 87.71 per StockTitan). Booking a price-only split against the stored pre-split eps 15.70 would ship a wrong P/E to the board. **Per the standing split warning, eps, hi52/lo52, ath, jan2 and the post-split price must be adjusted together in one commit by the interactive/earnings job.** Flagged for that session.

## Benchmarks / series
- SPY 23 Nov **722.29** (+4.71% vs 689.81) — stockanalysis ETF quote (prev close 689.81 chains), finimize and Fox all agree. spyHigh unchanged (722.29 < 779.09). QQQ already at 23 Nov (651.03).
- risk_series: spy[2026-11-23]=722.29 added. **ust10 23 Nov skipped** — ycharts published only through 19 Nov (5.04%); news wraps said "~4.95%" but gave no precise dated close. Per README, gap tolerated.
