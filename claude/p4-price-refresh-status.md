# P4 price refresh status

- Run time (UTC): 2026-10-14 00:30 slot (job ran ~00:41-01:15 UTC)
- Trading date recorded: 2026-10-13 (Tue)
- Result: **PUSHED**
- Commit: 6170d8f (Daily price refresh 2026-10-13: 63 prices) — remote main confirmed at 6170d8f
- Prices changed: 63 of 63 (incl. SPCX, stale since 2026-10-08, now current)
- Unresolved tickers: none
- Sanity gate: first run BLOCKED on AMAT -6.69% and FN -6.26% (the >6% rule working as intended). Both confirmed real against second sources — AMAT via the fool.com quote box (exact Oct 13 range 452.81-485.63, prev close 497.53), FN via ycharts (Oct 13 16:00 stamp, 427.62 vs official 427.82, its usual few-cent lag). Re-run with `--allow AMAT --allow FN`: PASS.
- Quote-vs-history disagreements: BWXT — history-table Oct 13 row internally impossible (close 137.39 below its own low 137.87, volume 27,245); row discarded, quote page used (138.86, both resolution tests passed). FN, LHX, STRL — history tables had no Oct 13 row yet ~40 min after the close; quote pages passed both tests (stamp + prev-close match) and were used.
- SPY: 778.01 (2026-10-13) → BENCH.spyLast; spyHigh unchanged at 779.09 (6 Oct). Crash-reserve trigger not tripped (SPY 0.14% below the high; trigger is -15%).
- Risk series: spy[2026-10-13]=778.01, ust10[2026-10-13]=5.21 (ycharts, 10Y CMT) appended. No 2026-10-12 ust10 row exists — bond market was closed (Columbus Day), expected gap.
- HISTORY: row appended for 2026-10-13 (n=37, mv 828,015.40, cost 680,966.29, unreal +147,049.11 / +21.59%, cash 55,050.83 free after the SGOV park). Previous row's sha set to 4fdab14.
- Stale/broken sources this run: Google Finance FN served a Sep 25 cache; fool.com /quote/ page for FN was one day stale (Oct 12 data) while its AMAT page was current — per-ticker staleness, as documented. GitHub Pages build-status API is blocked by the sandbox proxy and the live URL could not be web-fetched from this sandbox (provenance gate), so live-render verification was done on the exact pushed file with Playwright: 860 table rows, ZERO PAGE ERRORS.
- Blockers: none.
