# P4 price refresh — status

**Run:** 2026-11-28 00:33–02:55 UTC (00:30 UTC scheduled pass)
**Trading date recorded:** 2026-11-27 (post-Thanksgiving half-day, 1:00 PM ET close)
**Result:** PUSHED — commit `16948ce` (3f340e6 → 16948ce, fast-forward, no force)
**Prices changed:** 61 of 63
**Sanity gate:** PASS (13 movers >6%, every one confirmed by a second independent source and passed with `--allow`: ARM +6.22, MRVL +7.34, MU +7.60, STX +7.90, ANET +6.55, LITE +7.98, COHR +14.07, ALAB +8.67, CRDO +8.21, RKLB +8.21, FN +6.18, BE +6.63, TSEM +6.69). Threshold never raised.
**Render check:** `node check_dashboard.js` → 921 rows, ZERO PAGE ERRORS (live-page WebFetch blocked by the sandbox allowlist this session; the pushed index.html is what Pages serves).

## Unresolved / excluded
- **AMAT — unresolved, price stays at the 25 Nov close (311.18, pxd 2026-11-25).** No dated 27 Nov close found: StockTitan/Schwab/Fox/financialcontent/fool all served Nov 25 or intraday caches. fool.com's quote field implied 322.04 (+3.49%) but that field proved wrong on KLAC, so it was not booked. The 03:30 pass should retry (stockanalysis usually rolls over overnight).
- **SNDK — deliberately untouched (5th run flagging it).** Closed **85.36 post-split (+15.96%)** on 27 Nov (two sources). Board row still carries the pre-split price 633.96; the coordinated price/pe/hi52/jan2/yr rebase (--allow SNDK) remains with the interactive session per commits de697de/eed15b0.

## Session character
Broad AI/semi rebound on the half-day: SPY **728.32 +1.62%** (2 sources, prev 716.70 chain-ties; drawdown vs spyHigh 779.09 now −6.5%, above the −15% crash-reserve trigger), QQQ **650.99 +2.69%** (2 sources; bridges the missing 25 Nov QQQ close via source prev 633.93), Nasdaq Composite +2.31%. Largest board mover COHR +14.07% (optical-stock rebound; GuruFocus +14.1% confirms). SPY/QQQ/BENCH, HISTORY row (mv 717,787.53, n=36, unreal −45,323.76 / −5.94%), risk_series spy[2026-11-27]=728.32 and ust10[2026-11-27]=4.94 all written.

## Sources & staleness (for the next run)
- **stockanalysis.com stale site-wide AGAIN** — quote + history frozen at Nov 25 throughout the run (checked twice, 00:40 and 02:00 UTC).
- Google Finance both cache forms weeks stale (Oct 19 / Oct 26). Benzinga months stale (May). statmuse one day behind. marketscreener mixed (fresh for NVDA only). CBOE quote pages JS-only (no data).
- What worked, all chain-validated against the 25 Nov board: **StockTitan overview** "closed at $X on November 27, 2026" lines (~28 names); **financialcontent mirrors** with "Official Closing Price Updated … Nov 27" (NVDA, GE-wedbush, V-wral, GLW-chroniclejournal) and main-site last-trade pages (ALAB 206.84, CRDO 115.57); **Schwab wallst** 12:58–1:00 pm ET prints (~15 names — same basis as the 25 Nov run's 3:59–4:03 pm snapshots); **TheStreet** "At close: Nov 27, 1:00 PM ET" (NVDA, ARM, TSEM); **Fox Business** 1:00 PM prints with prev-close tie (KTOS, CDNS, STRL, QQQ); **fool.com** "Last close 2026-11-27" (STX, FN); **AAII** post-close (TER 222.96); three Nov-27 market-wrap articles for cross-ties (currentlogic dispersion brief, BigGo, finexus).
- Quote/secondary **disagreements, resolved or carried**: AMD — wrap printed 424.58, StockTitan + BigGo both 424.54 → 424.54 booked. NFLX — source prev 59.41 vs board 59.40 (1¢, carried). Statmuse claimed MU 25-Nov close 600.56 vs board/3-source 601.25 (ignored, statmuse cached). One Schwab fetch for KLAC returned AMAT's table verbatim — discarded as cross-contaminated; KLAC booked 140.86 from a 1:00 PM chroniclejournal print instead. A garbled stockanalysis KTOS page (prev close 39.33, impossible vs board 28.95) was discarded whole; KTOS booked 30.39 from Fox with exact chain tie.

## Blockers
None fatal. Live-page fetch blocked by the session allowlist (render verified locally via Playwright instead).
