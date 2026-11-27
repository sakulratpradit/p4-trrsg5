# P4 price refresh status

- **Run time:** 2026-11-27 03:33 UTC (03:30 UTC pass)
- **Trading date recorded:** 2026-11-25 (Wed) — already complete before this run. Thu 26 Nov was Thanksgiving (US markets closed), so there is no 26 Nov session to book; this run fired at 22:33 EST Thu, before the Fri 27 Nov half-day (1:00 PM ET close). The 27 Nov half-day closes will be booked by the Sat 28 Nov runs.
- **Status:** NOT PUSHED (no data changes) — first-check stop: the board is fully current. 62/63 tickers at pxd 2026-11-25 on the freshly-pulled base (HEAD 901dcda); the only exception is SNDK, deliberately excluded. This commit carries only this status doc.
- **Commit (data):** 9a912ed — the 25 Nov refresh (62 prices, sanity gate PASS, zero --allows). Source detail in that run's status doc (commit 4cd2f90) and the 9a912ed commit message.
- **Prices changed this pass:** 0. Verified on the freshly-pulled base: BENCH spyLast 716.70 / spyLastD 2026-11-25; spyHigh unchanged 779.09.
- **Unresolved / carried:**
  - **SNDK** — pxd still 2026-11-20, deliberately untouched by this job. The 8-for-1 split price-basis rebase (price/pe/hi52/jan2/yr, --allow SNDK) still needs the INTERACTIVE session per commits de697de/eed15b0. Seventh run flagging it.
  - **QQQ** — qqqLast still 2026-11-24 (no dated 25 Nov close was found by the 25 Nov passes). Benchmark tile works with the older value.
  - **risk_series ust10** — 25 Nov value still absent (ycharts H.15 only ran through 24 Nov = 4.91 at the last attempt); the monthly risk run copes with gaps.
- **Blockers this pass:** none. No price fetching attempted (none needed), so no source status to report.
