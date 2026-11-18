# P4 price refresh status

- **Run:** 2026-11-18 00:32–03:05 UTC (00:30 pass)
- **Trading date recorded:** 2026-11-17
- **Result:** PUSHED — commit `ae1bcaf` (36a1aae..ae1bcaf, no force)
- **Prices changed:** 63 of 63 (every ticker moved; pxd set to 2026-11-17 on all)
- **Benchmarks:** SPY 732.44, QQQ 656.95 (both 2026-11-17); spyHigh unchanged at 779.09
- **HISTORY row appended:** 2026-11-17 — mv 739,880.57, cost 758,481.32, unreal −18,600.75 (−2.45%), cash 5,880.06
- **risk_series.json:** spy[2026-11-17]=732.44 appended; **ust10 SKIPPED** — the 17 Nov 10-year close was not yet published anywhere dated (mortgagenewsdaily table and ycharts both ended at 16 Nov = 5.132 / 5.12; CNBC 403). Needs backfill by a later session.
- **Sanity gate:** PASS, no --allow needed (largest move FSLR −5.84%)
- **Unresolved tickers:** none
- **Sources & deviations (verbatim blockers):**
  - stockanalysis.com (the primary) served stale caches for the entire run: quote pages stamped "At close: Nov 13" (GOOGL's "Nov 17, 9:15 AM EST - Market open"), history tables ending Nov 13–16. Zero tickers resolvable from the primary; same failure mode as the 11-12 Nov run.
  - 61 closes taken from Google Finance pages carrying an explicit "Closed: Nov 17, 4:00 PM GMT-5" stamp. GF serves randomly stale per-URL caches (some months old); fresh pages were found by rotating rare URL variants (hl=th/ja/fi/..., ucbcb=1, ved-param URLs) surfaced via extended search. Every accepted price was validated by implied previous close (price − day change) against the board's POEMS-verified 16 Nov close.
  - MU from a fool.com article quote box labeled "As of 4:00 PM ET 11/17/26" (close 712.42 inside day range 666.88–726.99); SPCX from the fool.com quote page with "Last close 2026-11-16" printed (141.69).
  - Prev-close tie was exact (≤1¢) on 59 of 63. Four small mismatches vs the board's stored 16 Nov closes, close itself Nov-17-stamped in each case: GLW (implied 106.21 vs stored 106.17), LHX (261.58 vs 261.75), V (426.53 vs 426.46), APH (75.46 vs 75.43). Worth a glance at the next POEMS reconciliation.
  - Live-page verification NOT possible from this sandbox (github.io firewalled; WebFetch provenance blocked it). Verified instead with Playwright on the built file: 901 table rows, ZERO PAGE ERRORS. Repo HEAD confirmed at ae1bcaf.
- **Note for the 03:30 pass:** all 63 pxd = 2026-11-17 → first-check stop applies; only ust10 remains open.
