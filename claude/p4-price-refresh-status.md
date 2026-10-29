# P4 price refresh — status

- Run time: 2026-10-29 00:33–02:20 UTC (00:30 scheduled pass)
- Trading date recorded: **2026-10-28** (Wed)
- Result: **PUSHED** — commit `eb2990a` ("Daily price refresh 2026-10-28: 48 prices"), fast-forward on main from 4e71c89, no force.
- Prices changed: **48 of 63** (all 48 get pxd 2026-10-28). Largest move: **VRT +16.48% → 242.94**.
- Sanity gate: PASS with `--allow SNPS FN ORCL BE STRL VRT STX SNDK` (each >6% vs stored; verification below). MU +5.86% under threshold.
- HISTORY row 2026-10-28 appended: mv 819,022.76, cost 718,974.66, unreal +100,048.10 (+13.92%), net 105,943.57, cash 29,714.36.
- BENCH: qqqLast 725.61 / 2026-10-28 (post-close fool.com article quote box). **spyLast/spyHigh unchanged** — SPY close not cleanly readable (two fool alias captures disagreed 771.62 vs 772.31; stockanalysis frozen). risk_series: **spy and ust10 both skipped** (10-27 and 10-28 are gaps; mortgagenewsdaily unreachable via proxy provenance, ycharts cache frozen pre-close).

## Sources this run (third night of frozen caches)
stockanalysis.com, Google Finance and ycharts proxy captures were all frozen at Oct-27 morning or older (NVDA quote May-2025, MSFT Sep-2025) — primary source unusable again. Prices came from **fool.com quote pages carrying a dated "last close | USD x | 2026-10-28" line**, cross-checked per ticker: back-out of the day change had to equal the board's POEMS-exact Oct-27 close (held on every one of the 36 holdings tested), close within the day's range. For pages mid-cache-rollover, the refreshed previous-close field was used as the close; this reading was validated by 8 clean pages where field == dated close, and independently by 247wallst.com sidebars matching **MU 983.23, SNDK 1404.77, STX 697.97, VRT 242.94, ORCL 144.54 to the cent**.

## 6% movers — verification detail
- ORCL 144.54 (+10.73% d/d, investor-day guidance): fool market-wrap stated close + 247wallst winners list — strong.
- VRT 242.94 (+16.49% d/d, Q3 beat/raised guidance): 247wallst sidebar exact + gurufocus "surge 16%" — strong.
- SNDK 1404.77 / STX 697.97 / (MU 983.23): 247wallst sidebar exact — strong.
- BE 228.08 (+4.31% d/d; +11.85% vs stored Oct-26): dated fool close; marketbeat Oct-28 headline "+4.3%" matches d/d move — good.
- FN 367.30 (+7.55% d/d): dated fool close, internally consistent OHLC; marketbeat Oct-28 "up 4.7%" (intraday) confirms direction only — weaker.
- STRL 388.87 (+5.52% d/d): dated fool close; marketbeat Oct-28 "shares gap up" headline; open 391.80 consistent with gap — weaker.
- SNPS 481.89 (+1.57% d/d; +6.07% vs stored Oct-26): clean dated fool close; the unverified leg is Oct-27 (+4.4%), consistent with the EDA rally (CDNS +6.5% Oct-27 POEMS-verified) — weakest of the allowed set; price itself is from a dated close line.

## Unresolved (left at prior close, pxd untouched)
- Holdings at 10-27 (POEMS): **CDNS, CRDO, AVAV, GEV, ETN, CEG** — every fool quote alias and fool.com.au page served a pre-close or 1-2-day-old capture; no dated Oct-28 close found.
- Watch at 10-26: **ARM, MPWR, COHR, SPCX, LHX, PWR, GE, TSEM, CIEN** (COHR's fool page resolves to the delisted "Coherent Inc"; SPCX only has a /quote/crypto/ page).
- marketscreener blocked by sandbox provenance permission (unattended run, no one to approve).

## Live page
Playwright check on the pushed index.html: 871 rows, **ZERO PAGE ERRORS**. Direct fetch of https://sakulratpradit.github.io/p4-trrsg5/ was blocked by the sandbox's URL-provenance rule, and the Pages build-status API is blocked by the proxy — could not confirm the deploy itself; the pushed content renders clean locally.

## Notes for the next pass / interactive session
- fool.com quote pages + fool.com.au ticker pages (Close Price stamped 07:00 AEDT = 4 PM ET) are currently the only sources that roll past the close; 247wallst "Companies Mentioned" sidebars give exact closes on same-day articles and make a good second source.
- CGNX: fool's dated Oct-28 page implies an Oct-27 close of 58.32 vs POEMS 58.22 (10 c) — written 58.43 for 10-28 regardless (dated close, in range); flagging the 10 c discrepancy.
- FTNT closed −6.02% d/d at 174.08 and was −26% after hours (earnings); LITE +8.6% AH; MU/TER/KLAC/STX also moved AH. Thursday's refresh will see large d/d gaps on these — they are real.
