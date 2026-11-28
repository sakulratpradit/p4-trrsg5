# P4 price refresh — status

**Run:** 2026-11-28 03:35–03:55 UTC (03:30 UTC scheduled pass)
**Trading date recorded:** 2026-11-27 (post-Thanksgiving half-day, 1:00 PM ET close) — recorded by the earlier 00:30 pass
**Result:** NOT PUSHED (no price edits this pass) — board already current; status-doc-only commit pushed
**Prices changed:** 0 (first check: 61 of 63 tickers already carry pxd = 2026-11-27, so the 00:30 pass succeeded — stopped per the job's first-check rule)
**Commit of record for the 27 Nov closes:** `16948ce` (00:30 pass)

## AMAT retry (the one task this pass owned)
The 00:30 doc asked this pass to retry AMAT. Retried — **still unresolved; price stays at the 25 Nov close (311.18, pxd 2026-11-25).** What was found:
- **Triangulation points to 322.04 (+10.86, +3.49% on prev 311.18)**: GuruFocus article title "After 3.5% Gain — GF Value $285.35 vs Price $322.04" (article 9228911, fetch fails with client_error, so its date stamp could not be read), Fox Business search-result title "(+10.86)", and the 00:30 pass's fool.com implied field (322.04) agree. A MarketBeat instant alert URL-dated 2026-11-27 ("Up 2.7%", midday) is consistent in direction.
- **But no fetchable page carried a dated 27 Nov close.** Fox Business served a 10:02 AM EDT Nov-27 intraday capture (310.37) twice; Schwab wallst summary stamped "4:00pm ET 11/25/2026" (311.18); StockTitan overview still pre-market ("closed at $311.18 on November 25", snapshot 05:15 EST Nov 27); stockanalysis.com history still frozen at Nov 25 site-wide; Google Finance both cache forms absurdly stale (Oct 9 / Sep 25); GuruFocus and MarketBeat article fetches fail at the site.
- Per the absolute rule (a number must come from a fetched, dated print — a search-result title is not one), AMAT was left unchanged. The Tue 1 Dec run books the Mon 30 Nov close and supersedes this; no back-fill duty applies (not a year-end boundary).

## Still excluded
- **SNDK — untouched (6th run flagging it).** 8-for-1 split rebase (closed 85.36 post-split on 27 Nov; board row still pre-split 633.96) remains with the interactive session.

## Blockers
None. No edits to index.html or portfolio_data.py this pass; nothing for the sanity gate to check.
