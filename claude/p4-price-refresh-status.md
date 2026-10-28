# P4 price refresh status

- **Run time (UTC):** 2026-10-28 00:32 - 02:50 (00:30 scheduled pass)
- **Trading date recorded:** NONE - target was Tue 2026-10-27; no ticker could be resolved to that close
- **Pushed:** PUSHED - commit `88f1a23` ("Daily price refresh 2026-10-28 00:30 UTC: 0 prices ... ust10 2026-10-26=5.00 back-filled")
- **Prices changed:** 0 of 63. All prices, mcaps, pxd, SPY/QQQ BENCH values left at the Mon 2026-10-26 close (CGNX still 2026-10-23). No HISTORY row added (one row per trading day; 2026-10-26 already present).
- **What did land:** `risk_series.json` ust10["2026-10-26"] = 5.00 (ycharts 10-Year Treasury Rate page, stamped "Last Value 5.00% for Oct 26 2026, Last Updated: Oct 26 2026, 18:04 EDT") - this fills the gap both 2026-10-27 runs reported skipping. ASOF rewritten to describe this run. Local Playwright render check of the pushed page: 870 table rows, ZERO PAGE ERRORS.
- **Unresolved tickers:** all 63 (GOOGL MSFT AMZN META NVDA AVGO AMD ARM MRVL CDNS SNPS MPWR TSM ASML LRCX AMAT KLAC TER MU SNDK STX ANET APH GLW LITE COHR ALAB CRDO FN FSLR CGNX SPCX RKLB PLTR LHX KTOS AVAV DDOG ISRG ORCL V HOOD PANW CRWD FTNT NET BWXT GEV ETN VRT PWR BE CEG VST AAPL NFLX APP SE CAT GE STRL TSEM CIEN), plus SPY and QQQ.

## Blocker (verbatim finding)

Every stockanalysis.com quote AND history page served to this sandbox tonight was a cached snapshot taken BEFORE the Oct 27 4:00 PM EDT close. Across ~80 fetches of 63 tickers + SPY/QQQ between 00:35 and 02:35 UTC, the freshest snapshot seen was stamped "Oct 27, 2026, 1:04 PM EDT - Market open"; most were 9:36 AM-11:26 AM EDT; retries of the same URL returned randomly older shards (MSFT "At close: Sep 2, 2025", NVDA "At close: May 22, 2025", ANET flipping between "At close: Oct 26, 2026" and "At close: Jul 7, 2025", marketscreener GOOGL "May 08, 2024"). Google Finance (GOOGL cached "Chiusura: 25 set"), fool.com live coverage (May 2026 cache) and marketscreener were equally stale, so the >6%-move second-sourcing would also have been impossible. Resolution rule test (a) (stamp = "Oct 27, 4:00 PM EDT") failed for every name; the history tables' own Oct 27 rows were intraday partial captures (e.g. GOOGL 7.5M shares vs 18-29M normal) and were NOT used. Per the rules, a missing value over an invented one: nothing was written.

Waited through five 10-minute probe cycles (01:40-02:35 UTC) for a cache rollover; none came. The 03:30 UTC second pass should retry - yesterday's runs got post-close pages in this same window, so this looks like upstream-cache timing, not a permanent outage.

Also: the live page https://sakulratpradit.github.io/p4-trrsg5/ could not be verified from this sandbox (WebFetch provenance refusal; browser gets ERR_TUNNEL_CONNECTION_FAILED on github.io). The pushed index.html itself renders clean locally.

ust10/spy rows for 2026-10-27 skipped: SPY close unresolved; ycharts prints the 10-27 Treasury value ~16:15 EDT Oct 28. MND /treasury/10yr was unreachable (provenance refusal).
