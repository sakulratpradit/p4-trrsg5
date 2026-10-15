# P4 price refresh status

- Run time (UTC): 2026-10-15 00:30 slot (job ran ~00:41–01:40 UTC)
- Trading date recorded: 2026-10-14 (Wed)
- Result: **PUSHED** — commit `374a1f6` "Daily price refresh 2026-10-15 run (closes of 2026-10-14): 63 prices" (63e682b..374a1f6, clean fast-forward, no rejection)
- Prices changed this run: **63 of 63** (every close from a stockanalysis.com quote page validated against its history table; every number from a tool call this session)
- Largest move: **CIEN −10.19% to 359.60**. Broad risk-off day: 60 of 63 names red; only gainers LHX +1.18, AAPL +0.50, NFLX +0.16. SPY −1.08% to 769.60; UST10 5.19 (−2bp).
- Unresolved tickers: **none**

## Sanity gate
- First pass BLOCKED 17 tickers >6% (by far the most this board has seen in one day). Every one was verified against a second independent dated source BEFORE the gate ran, then passed with `--allow` per ticker (threshold untouched):
  - Google Finance (Closed Oct 14, 4:00 PM GMT-4, exact): MRVL −8.73% → 245.28, ALAB −7.72% → 300.28
  - Benzinga quote pages (Last update Oct 14, 7:56–7:59 PM EDT): ARM 238.01 (exact), CRDO 179.23 (BZ 179.22), RKLB 59.18 (exact), COHR 263.32 (BZ 263.23), GEV 941.78 (BZ 941.60), NET 324.33 (exact), HOOD 101.08 (exact), LITE 896.33 (exact), FN 392.95 (BZ 392.93), VRT 222.83 (BZ 222.85), VST 151.79 (exact), BE 239.34 (BZ 239.54), STRL 453.07 (exact), CIEN 359.60 (BZ 359.46)
  - ORCL −8.83% → 130.55: corroborated only by Benzinga's **intraday** Oct 14 2:15 PM print (130.26, −9.03%); no second *closing* print found. The stockanalysis quote page passed both validation tests, so the close was taken with this caveat.

## Quote page vs history table disagreements (quote taken per the resolution rule)
- **LHX**: history Oct 14 row showed close 239.26 but the page itself flagged the row as intraday; quote 237.50 (+1.18%) passed both tests — taken.
- **STRL**: history Oct 14 row was a partial-session capture (close 488.00 on volume 24,346 vs normal ~500K) — discarded; quote 453.07 confirmed exactly by Benzinga.
- **KTOS**: history close 39.39 vs quote 39.33 — quote passed both tests, taken.
- **MU**: quote's prev-close read 953.04 vs history 953.19 (15¢ apart), but quote price and history Oct 14 close agree at 914.13 — taken.
- **MPWR, FN**: history pages lagged (no Oct 14 row yet); quote pages passed both tests — taken.
- **BWXT** 134.44 (−3.18%): its history URL never surfaced in search this run (fetch provenance rule), so validated as: stamp 4:00 PM EDT + prev close equal to the board's own validated Oct 13 close.

## Source health
- Google Finance: stale per-ticker caches for most names tonight (Sep 25–Oct 13 snapshots); only 2 of 17 verifications usable.
- ycharts: stale (LITE Sep 21, ORCL Oct 12). marketscreener: very stale (FN Aug 18). Benzinga quote pages were the reliable dated second source tonight.
- One WebFetch was rate-limited by the sandbox proxy (Google Finance NET URL) — worked around via Benzinga.

## Also written
- BENCH: spyLast 769.60, spyLastD 2026-10-14; spyHigh stays 779.09 (2026-10-06). SPY is 1.22% below the high — **crash-reserve trigger (−15%) NOT tripped**.
- risk_series.json: spy[2026-10-14]=769.60, ust10[2026-10-14]=5.19 (ycharts, dated).
- HISTORY row 2026-10-14: mv 797,341.88, cost 680,966.29, unreal +116,375.59 (+17.09%), net +119,654.63, cash 55,050.83. Prior row's sha set to 6170d8f (its push commit, per the status log). Portfolio mv −30,673.52 on the day (−3.70%).
- New 52-week lows marked: KTOS 39.33, AVAV 120.60, APP 262.19. CIEN hi52/lo52 are None on the board — left untouched.

## Verification of the build
- Playwright check on the pushed file: 860 table rows, **ZERO PAGE ERRORS**.
- Live page at https://sakulratpradit.github.io/p4-trrsg5/ could NOT be fetched from this sandbox (the fetch tool's provenance gate blocks that URL in an unattended run — no one present to approve). The push itself was clean, so Pages will serve 374a1f6; worth an eyeball from the main session.

- Blockers: none
