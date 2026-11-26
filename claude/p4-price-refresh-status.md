# P4 price refresh status

- **Run time:** 2026-11-26 00:32–03:05 UTC (00:30 UTC job)
- **Trading date recorded:** 2026-11-25 (Wed; US markets closed Thu 26 Nov for Thanksgiving, next session is the Fri 27 Nov half-day)
- **Status:** PUSHED
- **Commit:** 9a912ed (on top of eed15b0; fast-forward push, no force, no rejection)
- **Prices changed:** 62 of 63 — the board is complete at the 25 Nov close except **SNDK** (deliberately untouched, see below). Sanity gate **PASS (exit 0) with zero --allows** — no ticker moved ≥6%. Playwright render of the pushed page: ZERO PAGE ERRORS.
- **First check:** 0/63 at pxd 2026-11-25 at 00:33 UTC → full run proceeded (this is the first pass of the night).

## Sources (stockanalysis.com unusable for a third day)
stockanalysis quote AND history pages still frozen at **Nov 20** site-wide. Google Finance caches weeks–months old (Oct 2). aaii caches Nov 23–24. Fox Business pages garbled (close/prev labels swapped, dates off by one — dropped entirely this run). Closes came from per-ticker **dated post-close sources**, each chain-validated against the verified 24 Nov board:
- **TheStreet pro quote pages** (`pro.thestreet.com/quote/<T>`) — explicit "at close, Nov 25, 4:00 PM ET" stamps; the night's workhorse for the hard tail: MSFT 489.93, TSM 342.34, HOOD 65.78, V 424.39, PLTR 163.59, GE 316.98, STRL 260.70, FN 289.70, AVAV 91.37, BWXT 113.55, SPCX 127.44, and 4:00 PM confirmations of CDNS 294.89, ISRG 427.18, ETN 317.81, CRDO 106.80.
- **StockTitan overview/company pages** — "closed at $X on November 25, 2026", 16:00–19:3x EST stamps (~28 names: NVDA 149.30, AVGO 300.86, META 609.89, AMD 406.03, SNPS, LRCX, AMAT, KLAC, ANET, APH, COHR, ALAB, FSLR, CGNX, RKLB, KTOS, DDOG, ORCL, FTNT, NET, GEV, VRT, PWR, CEG, VST, AAPL, APP, SE, CAT, MRVL, ARM, STX, LITE, TSEM).
- **Schwab wallst 3:59–4:03 PM snapshots**: TER 212.15, PANW 356.14, GLW 100.24 (4:03 PM), LHX 261.89, BE 152.89.
- **financialcontent "stocks" mirror official-close pages** (4:00 PM EST stamps): MU 601.25, CRWD 209.30.
- **marketscreener fresh mirrors** (post-close "Market Closed 2026-11-25" stamps with 5-day tables): GOOGL 273.10 (also financialcontent history, 2 sources), AMZN 244.43 (ca mirror), MPWR 1194.63 (sa mirror), NFLX 59.40 (ae mirror).
- **financialcontent /historical tables** (fresh for a lucky few): GOOGL, NVDA (second source).

## Largest moves (none tripped the 6% gate)
LRCX −5.68% (196.16 → 185.01) · ORCL −5.13% · MU −4.53% · DDOG −4.31% · PWR −4.10% · NVDA −3.91% · CEG −3.90% · AMAT −3.89% · AMZN −3.12%. Biggest gainers: META +3.40% (609.89), SE +2.89%, KTOS +2.62%.

## Quote page vs history table disagreements
None taken from conflicting pairs this run. Notable intraday-vs-close: **TER** was −9.28% at 11:49 EST (StockTitan intraday cache 193.43) but closed at **212.15 (−0.50%)** per Schwab's 4:00 PM snapshot (prev 213.22 chain-ties) — the intraday snapshot was NOT used. Similarly NVDA printed −8.4% intraday (ae.marketscreener real-time estimate) but closed −3.91% at 149.30 (2 sources).

## Source disagreements vs board (all ≤5¢, carried unresolved)
- **GLW**: Schwab prev close 101.87 vs board 101.88.
- **LHX**: Schwab AND StockTitan put the 24 Nov close at 258.08 vs board 258.03 — two independent sources agree against the board; the interactive session may want to correct the 24 Nov LHX basis.
- **GE**: TheStreet implied prev 318.03 vs board 318.04.

## Unresolved (1)
- **SNDK** — intentionally untouched (pxd stays 2026-11-20, price stays the pre-split 633.96). The 8-for-1 split is confirmed live (StockTitan: "closed at $73.61 on November 25, 2026"; 73.61 × 8 = 588.88 pre-split basis). Writing the post-split price without the coordinated rebase of eps/ath/hi52/lo52/jan2/yr would corrupt the row and trip the gate — commits de697de/eed15b0 record that this ONE coordinated price-basis fix belongs to the interactive session (--allow SNDK). **5th run flagging it.**

## Benchmarks & series
- **SPY** 25 Nov **716.70** booked (−0.29%; financialcontent bpas "Official Closing Price Updated: 6:30 PM EST, Nov 25" + StockTitan "closed at $716.70 on November 25"; prev 718.78 chain-ties). **spyHigh unchanged 779.09** (drawdown −8.0%, above the −15% crash-reserve trigger).
- **QQQ** — could NOT be read for 25 Nov (every reachable mirror stale: StockTitan Nov 24, marketscreener ETF pages Nov 20/24, financialcontent historical Oct 23). Left at 24 Nov 638.10 per job rule; tile still works.
- **risk_series.json**: spy[2026-11-25]=716.70 appended. **ust10 skipped for 25 Nov** — ycharts (H.15) series ends at 24 Nov (4.91); mortgagenewsdaily's 10-day Close table did not render (header showed an undated 4.851). The monthly risk run copes with the gap.

## Blockers / notes verbatim
- Live-page verification: `https://sakulratpradit.github.io/p4-trrsg5/` could not be fetched from this sandbox (URL not on the session allowlist and not surfaced by search). Substituted: headless-Chromium render of the exact pushed `index.html` — title OK, 104k chars of body text, **zero page errors**. Pages deploy is from the same pushed file.
- WebFetch URL snapshots are frozen per-URL for the whole session here: re-fetching a stale URL never refreshes. The working pattern is URL-string rotation (www/non-www, /overview/ vs /company/, regional marketscreener mirrors, Schwab case variants, TheStreet). TheStreet pro quote pages were fresh for every ticker tried tonight — recommend them as a primary next run.
- Fidelity dashboard pages are JS-rendered (no quote data in fetch) — unusable here.
