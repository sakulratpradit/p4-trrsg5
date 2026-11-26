# P4 price refresh status

- **Run time:** 2026-11-26 03:33 UTC (03:30 UTC second pass)
- **Trading date recorded:** 2026-11-25 (Wed) — already complete before this run. US markets closed Thu 26 Nov (Thanksgiving); next session is the Fri 27 Nov half-day (1:00 PM ET close), booked by the Sat 28 Nov runs.
- **Status:** NOT PUSHED (no data changes) — first-check stop: the 00:30 UTC pass succeeded. This commit carries only this status doc.
- **Commit (data):** 9a912ed — the 00:30 pass, 62 of 63 prices at the 25 Nov close, sanity gate PASS with zero --allows, Playwright ZERO PAGE ERRORS. Full source detail in that run's status doc (commit 4cd2f90) and the 9a912ed commit message.
- **Prices changed this pass:** 0. Verified on the freshly-pulled base: 62/63 tickers at pxd 2026-11-25; HISTORY row for 2026-11-25 present (no duplicate appended); BENCH spyLast 716.70 / spyLastD 2026-11-25; spyHigh unchanged 779.09.
- **Unresolved / carried:**
  - **SNDK** — pxd still 2026-11-20, deliberately untouched by this job. The 8-for-1 split price-basis rebase (price/pe/hi52/jan2/yr, --allow SNDK) still needs the INTERACTIVE session per commits de697de/eed15b0. Fifth run flagging it.
  - **QQQ** — qqqLast still 2026-11-24; the 00:30 pass found no dated 25 Nov close on any reachable mirror. Benchmark tile works with the older value.
  - **risk_series ust10** — 25 Nov value skipped at 00:30 (ycharts H.15 only through 24 Nov = 4.91); the monthly risk run copes with gaps.
  - stockanalysis.com quote + history pages frozen at Nov 20 site-wide for a third day (the 00:30 pass worked around it with per-ticker dated sources).
- **Blockers this pass:** none.
