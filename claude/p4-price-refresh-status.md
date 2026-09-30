# P4 price refresh — status

- **Run time:** 2026-09-30 00:41–00:57 UTC (00:30 scheduled run)
- **Trading date recorded:** 2026-09-29 (Tue)
- **Result:** PUSHED
- **Commit:** 7880328 ("Daily price refresh 2026-09-29: 93 prices"), on top of 1312605; remote main confirmed at 7880328 after push
- **Prices changed:** 93 of 94 (all to the Tue 2026-09-29 close; OKLO closed flat at 37.11, still re-dated)
- **Sanity gate:** PASS with `--allow BE --allow AXTI`
  - BE +10.80% → 291.25 — confirmed via MarketBeat 29 Sep alert (prev close 262.87, day high 302.35, volume 23.6M)
  - AXTI +6.12% → 78.18 — confirmed via MarketBeat 29 Sep gap-up alert (prev close 73.67)
- **Unresolved (1):** **XE** — left at the Sep 28 close 14.43. stockanalysis history table had no Sep 29 row and its Sep 28 row (14.46) contradicts the board's validated 14.43, so the quote page (14.29) failed the prev-close cross-check. Second sources all stale: Google Finance Sep 25 on both cache forms, fool.com quote widget dated Sep 28 and self-inconsistent, marketscreener Aug 5. A stale price is recoverable; nothing was written.
- **Quote/history disagreements (quote taken unless noted):** MCHP quote page stale, stamped Sep 28 → history row 78.78 used. AMKR quote stamped intraday 1:53 PM → history row 54.14 used. FSLR (hist 174.50 is a partial-session row: quote close 176.93 exceeds the row's own stated high 175.18, volume 1.3M vs 2–6M on neighboring days) → quote 176.93. LHX (hist 236.04, volume 476K vs 1.3–2.0M) → quote 236.47. BWXT (hist 139.75, volume 171K vs 0.8–1.3M) → quote 138.01. HUBB history table stuck at Sep 25 → quote 459.09, confirmed via ycharts "Sep 29, 16:00" (459.16). TSEM history had no Sep 29 row and a suspect Sep 28 row → quote 234.43, confirmed via GuruFocus 29 Sep article (234.43, +3.7%). Cent-level quote-vs-history gaps (quote taken per rule): NVDA .09, QCOM .11, SNPS .07, TER .25, SKHY .01, RKLB .02, ASTS .07, ONDS .01, NBIS .09, LEU .48. NET history had no Sep 29 row but quote passed both checks.
- **Source health:** stockanalysis.com quote pages healthy (91/94 passed both checks). Google Finance stale per-ticker (BE, AXTI, XE, HUBB all served Sep 24–25 caches on both cache forms). marketscreener stale on AXTI (weeks) and XE (Aug 5). MarketBeat instant alerts and GuruFocus dated articles were the working second sources tonight.
- **Largest move:** BE +10.80% (291.25). Next: AXTI +6.12%, LITE +5.66%, AMAT +5.19%.
- **Extremes extended:** hi52 CRWD 262.74; lo52 LHX 236.47, KTOS 43.05, LEU 138.18.
- **HISTORY row appended** for 2026-09-29: n 38, mv 788,413.23, cost 645,117.62, unreal +143,295.61 (+22.21%), net 142,755.14, cash 168,542.71. Sep-28 row's sha set to e2a1c8f.
- **Live page:** push to main confirmed (Pages deploys from main). Direct fetch of https://sakulratpradit.github.io/p4-trrsg5/ was blocked by the sandbox proxy's provenance rule this run, so the rendered page itself was not eyeballed — flagged per the report-failures-plainly rule.
