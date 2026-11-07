# P4 price-refresh status

- **Run (UTC):** 2026-11-07 ~09:55–10:10 (Sat pass; the 00:30/03:30 firings did not run — this is a catch-up firing)
- **Trading date recorded:** 2026-11-06 (Friday close) — already on the board before this run
- **Result:** **NOT PUSHED for prices — none needed.** First-check passed in substance:
  **all 63 of 63 tickers already carried `pxd = 2026-11-06`**, booked by the concurrent
  interactive session from Salee's POEMS positions screen (commit `5623365`,
  "6 Nov close booked from POEMS … SPY 735.36/QQQ 656.29"). BENCH spyLast/qqqLast
  (735.36 / 656.29, both dated 2026-11-06), the HISTORY row for 2026-11-06
  (mv 717,837.17, unreal −10,320.68 / −1.42%), spyHigh (779.09 unchanged, SPY −5.6%
  off the high — crash-reserve trigger 662.23 not near) and ASOF were all current.
  Overwriting POEMS broker marks with web-scraped closes would add risk, not accuracy,
  so prices, mcapB, pxd, hi52/lo52 and ratios were left untouched.
- **Prices changed by this job:** 0. **Largest move:** n/a (no price written).
- **Quote-vs-history disagreements:** none examined — no web price resolution was run,
  per the first-check stop rule.
- **Unresolved tickers:** none (63/63 current at 2026-11-06).
- **Sanity gate:** run anyway on the rebuilt page — **PASS**, and the rebuilt
  dashboard is byte-identical to the committed `index.html`.

## What this run did push — commit `c6a452c`
`src/risk_series.json` `ust10` had gone stale at 2026-10-27 (this job owns it and had
not run). Backfilled seven rows from the series' canonical source
(ycharts 10-Year Treasury Rate, Fed H.15 — the stored series matches it exactly
through 10-27):
10-28 5.05, 10-29 4.98, 10-30 4.94, 11-02 4.91, 11-03 4.95, 11-04 4.90, 11-05 4.84.
Cross-checked direction/level against mortgagenewsdaily's 10-day Close table (its
values are the intraday market close, 1–5 bp different by convention; it also still
shows a mislabeled "Nov 01" row — the known quirk).
**`ust10` for 2026-11-06 was NOT written:** neither ycharts (last value Nov 05,
"next release Nov 6 18:00 EST" not yet served) nor mortgagenewsdaily carried a dated
Nov 6 close at run time. Skipped per the gap rule — the next run should pick it up.
`spy` 2026-11-06 = 735.36 was already present (written by the concurrent session).

## Source notes
- ycharts 10_year_treasury_rate: current through Nov 05 only at run time.
- mortgagenewsdaily /treasury/10yr: current through Nov 05; "Nov 01" row mislabeling persists.
- Live page at sakulratpradit.github.io not fetchable from this sandbox (URL
  allowlist/provenance); nothing on the page changed in this run, so the live render
  is whatever commit `5623365` produced.
- Blockers: none. Push accepted first try, no force, no conflict.
