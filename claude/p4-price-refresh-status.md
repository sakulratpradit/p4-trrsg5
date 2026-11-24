# P4 price refresh status

- **Run time (UTC):** 2026-11-24 00:33–02:00 (00:30 UTC pass)
- **Trading date recorded:** 2026-11-23 (Mon) — the Huang-reinstatement rally session
- **Result:** PUSHED (pending — see commit line below, updated after push)
- **Prices changed:** 29 of 63 (27 of 36 held positions, ~91% of stock MV now at the 23 Nov close)
- **Largest move:** NVDA +31.48% to 165.05 (Jensen Huang reinstated as CEO; +$954B market cap day). Sector sweep: ALAB +23.2%, CRDO +22.6%, MU +19.0%, MRVL +18.4%, LITE +18.2%, KLAC +15.0%, TSM +14.1%, VRT +12.1%, APH +11.0%. Indexes: S&P 500 7,237.17 +4.73%, Nasdaq 24,089.56 +6.51%, QQQ 651.03 +7.00%, VIX 26.62 -25.8%.
- **Sanity gate:** PASS (exit 0) with --allow on the 22 names that moved >6%; every one verified as described below. No internal-impossibility rows used; no thresholds raised.

## Source situation tonight (00:33–02:00 UTC)
stockanalysis.com (primary) served a stale Fri 20 Nov snapshot SITE-WIDE (crawl stamp Nov 21) — quote AND history pages, for every ticker sampled, including ?-param variants. Google Finance caches ran Sep 18–Oct 26. statmuse/financialcontent/fool quote pages also pre-close or garbled. Same failure mode as the 27–28 Oct incident recorded in ASOF. Usable post-close sources found this run:
1. fool.com same-day articles, quote widgets stamped "As of 4:00 PM ET 11/23/26" — proven exact vs independent sources on NVDA/AMD/MU (writes: NVDA 165.05, AMD 453.46, MU 707.70, ASML 1383.78, MRVL 144.74, TSM trajectory; fool post-close ticker bar at 4:40–5:16 PM EST = closing values, cross-proven on NVDA+AMZN: AAPL 349.08, META 597.60, MSFT 492.50, SPCX 133.35)
2. financefeeds.com post-close wrap ("Updated 23 Nov, after the 4:00 pm ET close") — close table corroborated all of the above and supplied TSM 363.60, ORCL 113.68
3. StockTitan /overview and /company pages with explicit "closed at $X on November 23, 2026" + consistent same-evening after-hours quotes (the same source the 20 Nov run used): ANET 178.31, GEV 756.71, ISRG 416.23, VRT 186.35, CAT 547.04, CRDO 122.46, ETN 336.34, APH 77.41, KLAC 145.85, FSLR 146.53, RKLB 49.63, LITE 544.38, ALAB 222.12, VST 123.87
4. foxbusiness/massive.com at-close captures: AMZN 255.39, GOOGL 282.10, CEG 251.72
5. marketscreener fresh mirrors (NVDA 165.05, confirmed) — most regional mirrors stale

## Quote page vs other sources — disagreements and which was taken
- **MSFT:** marketscreener ae mirror showed 495.43 as the 23 Nov row — rejected as a ~3:51–4:08 PM print (MSFT faded into the close; its own header showed +1.86%≠table). Took 492.50 (fool post-close bar ×3 pages + financefeeds); ycharts showed 492.61 ("Nov 23 16:00") — 11c above the booked value, unresolved to the cent but immaterial (0.02%).
- **NVDA:** 247 Wall St's 4:10 PM movers strip said 164.50 — rejected (strip proven ~0.3% off); official 165.05 from fool widget + marketscreener + financefeeds.
- **VST:** three captures within 5c (fox 3:59 PM 123.82, massive series 123.85, StockTitan "closed at 123.87"); took StockTitan's dated close print.
- **CRWD (watch):** financefeeds 208.97 vs 247wallst 207.68 — CONFLICT, left unresolved at the stale 19 Nov 243.46.

## >6% verification notes (per the gate rule)
Multi-source exact: NVDA, GOOGL, META, TSM, AMD, MU, MRVL(fool widget; move corroborated by connectivity-peer prints), ASML(fool widget + gurufocus 9:55am 1387.63 same level), LITE(fool wrap +18.20% + StockTitan print 544.38), ALAB(StockTitan 222.12 + 247wallst 222.20 + marketbeat +23.2%), CEG(massive at-close + tipranks intraday +5.8%), VST(three captures), GEV(StockTitan + tipranks intraday +9.1%).
StockTitan dated close + sector-tape corroboration only (flagging honestly): ANET +6.4%, CAT +7.2%, CRDO +22.6%, ETN +8.0%, APH +11.0%, KLAC +15.0%, FSLR +6.5%, RKLB +9.3%. Each page carried a consistent same-evening after-hours quote vs its stated close; magnitudes consistent with SOXX +13.63% / sector wraps. Salee's morning POEMS reconciliation remains the authoritative true-up.

## Unresolved (left at prior close, pxd untouched)
- Held: AMAT, LRCX, PANW, V, PLTR, CDNS, TER, CGNX, AVAV (~$59k MV, 9% of stock MV) — no post-close print found from a permitted dated source.
- Watch: ARM (+16.1% per financefeeds but no level), APP, HOOD, NFLX, SE, GE, STRL, TSEM, CIEN, SNDK, STX, SNPS, MPWR, GLW, COHR, FN, DDOG, NET, FTNT, BWXT, PWR, KTOS, LHX, BE (fool wrap +18.09%, no print), CRWD (conflict).
- **SPY 23 Nov close NOT found** — BENCH spyLast/spyHighD stay at 20 Nov (689.81); risk_series spy 2026-11-23 skipped. QQQ WAS booked (651.03). risk_series spy 2026-11-20 = 689.81 back-filled (was missing; value from massive.com SPY page prev-close this session, ties BENCH).
- **ust10 2026-11-23** not yet published on mortgagenewsdaily (page still showed the 20 Nov close 4.940) — skipped, gaps OK.

## Also done
- HISTORY row appended for 2026-11-23: n=36, mv=731,037.68, cost=763,111.29 (incl. yesterday's AVGO fill), unreal -32,073.61 (-4.20%), cash 1,267.41. NOTE: mv still carries 9 held names at 20 Nov marks — true mv is somewhat higher; the morning POEMS true-up should correct it.
- pe/ps/fpe/peg/M3-pfcf rescaled for the 29 names per the 26 Oct rule. hi52 extended where applicable.
- Live-page verification: sakulratpradit.github.io is refused by the sandbox proxy (known since the 20 Nov run) — remote main == pushed commit verified via ls-remote instead.

## For the 03:30 UTC pass
9 held + 25 watch names still need the 23 Nov close; stockanalysis snapshots may have refreshed by then (first check: 29 tickers already have pxd 2026-11-23 — threshold of 80 NOT met, so the pass will run). SPY and ust10 also still needed. StockTitan /company/<T> and /overview/<T> variants were the most productive fallback tonight.
