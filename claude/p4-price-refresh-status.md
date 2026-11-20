# P4 price refresh status

- **Run time (UTC):** 2026-11-20 03:32–04:00 (03:30 UTC pass)
- **Trading date recorded:** 2026-11-19
- **Result:** PUSHED
- **Commit:** b40478e109d8f72e2045e0367c6f60a0168b3c66 (remote main confirmed via ls-remote)
- **Prices changed:** 3 — the three names the 00:30 pass left unresolved; all 63/63 now at 2026-11-19
  - COHR 212.84 → 214.94 (+0.99%) — StockTitan, stamped "November 19, 2026 at 19:59 EST", after-hours 209.24 quoted against "the $214.94 close"; corroborated by Yahoo close widget +1.08% and stockstory intraday 214.44 (12:20 ET). The widely-syndicated "+10.78% buyback" figure was a 10:00 ET spike that faded with the tape.
  - GEV 772.22 → 756.28 (-2.06%) — stockanalysis quote page, "At close: Nov 19, 2026, 4:00 PM EST"; stated previous close 772.22 chains exactly to the stored verified 18 Nov close. Its /history/ table was stale (Nov 13), so the chain test used the board's own 18 Nov value.
  - SNDK 776.22 → 755.16 (-2.71%, PRE-SPLIT) — StockTitan, same 19:59 EST stamp, after-hours 736.80 against "the $755.16 close"; corroborated by marketbeat dated alert headline "Shares Down 2.7%" 2026-11-19. The "+6.29% hours before split" headline was also intraday.
- **Largest move this pass:** SNDK -2.71%. No ticker tripped the 6% gate; sanity_check RESULT: PASS (exit 0), no --allow needed.
- **Unresolved tickers:** none.
- **SNDK SPLIT WARNING STANDS:** 8-for-1 split effective after the 19 Nov close; split-adjusted trading starts Fri 20 Nov. POS/eps/hi52/lo52/fundamentals must be split-adjusted by the interactive/earnings jobs BEFORE the next price refresh books a post-split close (~1/8, about 94; the 6% gate will trip).
- **Also done:** HISTORY 2026-11-19 row recomputed in place (GEV held 13 sh → mv -207.22 to 721,979.62); pe/ps/fpe/peg/M3-pfcf rescaled for the 3 names. SPY/QQQ/BENCH/risk_series were already booked by the 00:30 pass and were not touched.
- **Blockers / source notes:**
  - Live-page verification FAILED: sakulratpradit.github.io is refused by both the sandbox proxy (403 connect_rejected) and WebFetch's allowlist, so the rendered page could not be checked this run. Remote main == pushed commit was confirmed instead.
  - stockanalysis quote pages stale for COHR (Nov 6) and SNDK (Nov 13); /history/ tables stale for COHR, GEV, SNDK (all ending Nov 6–13). Google Finance COHR stale (Oct 26). marketscreener stale (Oct 9 / Oct 15) for COHR/SNDK. gurufocus, qz, benzinga, alphastreet article fetches returned client errors. StockTitan /overview/ pages (dated close + after-hours vs close) were the usable post-close source tonight.
