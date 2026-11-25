# P4 price refresh status

- **Run time:** 2026-11-25 00:33–03:05 UTC (00:30 UTC job)
- **Trading date recorded:** 2026-11-24 (Tue) — plus CRWD un-staled to its 2026-11-23 close
- **Status:** PUSHED
- **Commit:** 49b3efc (on top of 96f97df; fast-forward push, no force, no rejection)
- **Prices changed:** 21 of 63 (20 at the 24 Nov close + CRWD at its verified 23 Nov close). Sanity gate PASS (exit 0) with `--allow AMD ARM MU TSEM KLAC CRWD`. Playwright check on the built page: ZERO PAGE ERRORS, 921 rows.

## Sources (stockanalysis.com was unusable)
- stockanalysis.com quote pages served a stale **Nov 20** snapshot; /history/ tables ended **Nov 23** — no Nov 24 row all session. Google Finance caches were weeks old (Sep 21 / Oct 26). marketscreener Nov 12. ycharts a day behind. fool.com quote pages were intraday snapshots (AVGO shown 304.28 vs true close 301.08) — rejected.
- Closes came from per-ticker **dated 4:00 PM sources**, each chain-validated (its stated previous close vs the board's verified 23 Nov close): Fox Business dated-4PM pages, financialcontent.com (V explicitly flagged "Official Closing Price"), Schwab wallst 3:59–4:00 PM snapshots, the StockTitan Nov-24 live-close article, chroniclejournal 4 PM print. Caches on all of these are per-URL lotteries of mixed ages; only dated post-close copies were accepted.

## Changed (close, day move)
GOOGL 279.05 −1.08% · MSFT 496.13 +0.74% · AMZN 252.29 −1.21% · META 589.82 −1.30% · NVDA 155.38 −5.86% (Fox + StockTitan) · AVGO 301.08 −3.98% · AMD 413.27 −8.86% (financialcontent 4PM + StockTitan % match) · ARM 161.56 −8.55% (Fox + thepilotnews 4PM) · MU 629.79 −11.01% (StockTitan + Schwab; **Fox printed 630.07 — discarded**, 2-vs-1) · TSEM 123.47 −9.75% (Fox + Schwab) · KLAC 133.65 −8.36% (chroniclejournal 4PM close; 2nd source was Fox **intraday** corroboration of the move, not a second close print) · GLW 101.88 −5.94% · PLTR 161.18 · PANW 352.99 · LHX 258.03 · SE 65.00 · APP 381.11 · V 416.78 · AAPL 354.07 · GE 318.04 · **CRWD 208.97, pxd 2026-11-23** (−14.17% post-earnings; fox 208.96 vs financialcontent/Schwab 208.97, took the 2-source value; its Nov-24 close looked ≈210.9 on Schwab 3:59 PM but no second close print — left for the next run).

## Source disagreements
- MU: Fox 630.07 vs StockTitan/Schwab 629.79 → took 629.79.
- CRWD 23 Nov: fox 208.96 vs financialcontent + Schwab prev-close 208.97 → took 208.97.
- Small prev-close mismatches vs the board (noted, closes still chain-consistent): GLW prev shown 108.28 vs board 108.31; LHX 254.87 vs 254.82; GE 321.27 vs 321.26; NET 291.01 vs 291.13 (NET not updated).
- GE's Fox page labeling was ambiguous (close vs prev swapped); resolved by arithmetic + the board's prev close; only −1.0%.

## Unresolved (left at prior closes) — 42
- **BE**: Fox had a dated Nov-24 3:59 PM close **156.38 (−7.00%)** but no second source could confirm → reverted per the >6% rule. First candidate for the 03:30 run.
- **SNDK**: 8-for-1 split still unbooked — price-only booking would corrupt P/E vs pre-split eps 15.70; needs the interactive/earnings job (standing warning).
- No dated Nov-24 close reachable (caches stale or intraday-stamped): CDNS SNPS MPWR TSM ASML LRCX AMAT TER STX ANET APH LITE COHR ALAB CRDO FN FSLR CGNX SPCX RKLB KTOS AVAV DDOG ISRG ORCL HOOD FTNT NET BWXT GEV ETN VRT PWR CEG VST NFLX CAT STRL CIEN. Several had intraday Nov-24 candidates (CAT 539.50 @2:08PM, FTNT 134.21 @1:43PM, CRDO 106.87 @3:32PM, ALAB ~191.30 fool undated, SNPS ~415.03 fool undated, STRL 256.74 @10:07AM) — none accepted as closes.

## Benchmarks / series
- QQQ 638.10 (24 Nov) booked, chain-valid vs 651.03. **SPY 24 Nov close not found in any dated source** (StockTitan gave only −0.51%, no price; all quote caches intraday or Nov 23) → spyLast stays 722.29 / 2026-11-23; spyHigh unchanged (779.09). SPY is well above the −15% crash-reserve trigger either way.
- risk_series: spy 24 Nov **skipped** (no close); ust10 24 Nov **skipped** (not published); backfilled the gap **ust10[2026-11-23] = 4.91** from mortgagenewsdaily's page dated 11/23 (4.909; caveat: page headline figure, not the 10-day Close table).
- HISTORY row 2026-11-24 appended: n 36, mv 722,509.17, cost 763,111.29, unreal −40,602.12 (−5.32%), real 6,263.88, net −34,338.24, cash 1,267.41. **15 held names inside mv are still at 23 Nov marks** — the row will true up as the 03:30 run fills the gaps.

## Blockers verbatim
- "URL_NOT_ON_ALLOWLIST" — the live page https://sakulratpradit.github.io/p4-trrsg5/ cannot be fetched from this sandbox (not in any search result), so live rendering was verified locally instead: `node check_dashboard.js` → "ZERO PAGE ERRORS".
- First check at 00:33 UTC: 0 of 63 tickers had pxd 2026-11-24, so this run proceeded as the first attempt; 42 tickers remain for the 03:30 UTC run, whose first check will see 20/63 at Nov 24 and continue.
