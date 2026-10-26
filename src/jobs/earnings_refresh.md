# P4 earnings-day fundamentals refresh - job instructions

GIT ACCESS (updated 21 Sep 2026 - the old token-in-URL method is rejected by the sandbox proxy):
  TOKEN is given in the scheduled-task prompt. TOKEN does not persist between shell calls; re-declare it in every command block, then:
  AUTH=$(printf 'x-access-token:%s' "$TOKEN" | base64 -w0)
  git -c http.extraheader="Authorization: Basic $AUTH" <pull|fetch|push> https://github.com/sakulratpradit/p4-trrsg5.git main
  Wherever this file says `git pull/fetch/push origin main`, use that form instead.
  After ANY fetch, run: git update-ref refs/remotes/origin/main FETCH_HEAD   (so origin/main is current)
  Pipe all git output through: sed -E 's/github_pat_[A-Za-z0-9_]+/[REDACTED]/g'

RUNS TWICE (03:00 and 05:00 UTC, Tue-Sat). FIRST CHECK: if `git log --since="20 hours ago"` already shows an "Earnings refresh" commit, STOP except for the status step.

Refresh fundamentals for any Pillar-4 ticker that reported earnings since the last run, PLUS the staleness sweep (3b) and, on Saturdays, the fair-value sweep (3c).

You are one of several writers to this repo. Another session may have pushed since your last run. FOLLOW deploy/src/README.md EXACTLY — it is the contract that stops writers from overwriting each other. Read it before you touch anything.


THEN, in order:
1. cd deploy && git pull --ff-only origin main && cd ..
2. python3 deploy/src/extract_data.py deploy/index.html deploy/src/portfolio_data.py
3. Identify which of the 107 tickers reported since the last run. If none reported, STOP — do not push an empty commit.
4. Edit deploy/src/portfolio_data.py for those tickers ONLY. You own: pe, fpe, peg, ps, gm, pm, revB, revG, eps, epsG, roi, roe, fcfB, capexB, r40, and the M3 entries (pfcf, ev = EV/EBITDA ratio, de = debt/equity).
   YOU DO NOT OWN `price` OR `mcapB`. A separate daily job owns those and runs 30 minutes before you. Leave them exactly as you found them, even if the stock moved on the print. Touching them is what caused the V/KO/PYPL conflict.
   Also never touch POS, TRADES, GROUPS, jan2, or any ticker/name/ex/g field.
   Conventions: null out pe/fpe/peg/ev/pfcf for negative-earnings names; null r40 for lenders and garbage-margin names; store capexB positive; null EV/EBITDA when the ratio exceeds ~500x.
   WATCH FOR ONE-OFF GAINS. If net income exceeds operating profit, something non-operational is inflating it (asset sales, stake disposals, tax items). Record the underlying operating figure and note the one-off in your report — do not let a disposal gain masquerade as earnings power.
   ALSO write `fqd` = the TTM period-end date of the figures you stored ('YYYY-MM-DD', e.g. '2026-09-30'),
   and re-read the analyst targets for the same tickers from https://stockanalysis.com/stocks/<t>/forecast/
   (fields an, fvAvg, fvMin, fvMax) with `fvd` = today's date - targets move after a print. (Both fields added 26 Oct 2026.)
   Then apply the consistency rule to the refreshed tickers: pe = round(price/eps, 2) if eps > 0 else None; ps = round(mcapB/revB, 2).
   Update ASOF only if you are the last writer of the day and the data date genuinely moved.
3b. STALENESS SWEEP (added 26 Oct 2026 - a dozen names missed their Jul-Aug refresh and nobody noticed for
   three months): for every board ticker, compare `fqd` with the company's most recent reported quarter
   (the statistics page's "last earnings date", or an earnings-calendar search). Any ticker whose fundamentals
   predate its latest report is refreshed in this run too, not just the names that reported since the last run.
   Tickers with no `fqd` yet count as unknown - fill it when you touch them.
3c. FAIR-VALUE SWEEP: once a week (the Saturday run), re-read an/fvAvg/fvMin/fvMax for EVERY board ticker
   and set fvd. Priority rank (matrix rows 28-30) runs on fvAvg, so stale targets mis-rank the buy list.
5. cd deploy/src && python3 gen_dashboard.py ../index.html ../../us-portfolio-dashboard.html && cd ../..
6. cd deploy && python3 src/sanity_check.py --new ../us-portfolio-dashboard.html
   HARD GATE. Exit 1 means DO NOT PUSH. If it reports price moves, you edited something you do not own — revert those.
7. cp ../us-portfolio-dashboard.html index.html
   python3 src/extract_data.py index.html src/portfolio_data.py
   git add index.html src/portfolio_data.py
   git commit -m "Earnings refresh <date>: <tickers>"
8. git push origin main   — WITHOUT force.

IF THE PUSH IS REJECTED, someone else pushed first. That is the system working. NEVER use git push --force, git push -f, or git reset --hard FETCH_HEAD to win — that is exactly how commits ec7015f and 5fdc1dd were destroyed. Instead: git fetch origin main; git reset --hard origin/main (discards YOUR build, keeps THEIRS); re-run extract_data.py; re-apply your fundamentals edits to that fresh base; repeat steps 5-8. Retry at most 3 times, then stop and report.

Report which tickers you updated, any figure that surprised you versus consensus, any one-off item inflating a headline number, and anything the sanity gate blocked. Every figure must come from a real source — if you cannot find a number, leave the old value and say so. Do not estimate.

FINAL STEP - ALWAYS: write the project doc `claude/p4-earnings-refresh-status.md` (overwrite) with run time, PUSHED/NOT PUSHED/NOTHING TO DO, tickers updated, and any blocker verbatim.
