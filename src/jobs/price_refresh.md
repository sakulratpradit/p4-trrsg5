# P4 daily price refresh - job instructions

GIT ACCESS (updated 21 Sep 2026 - the old token-in-URL method is rejected by the sandbox proxy):
  TOKEN is given in the scheduled-task prompt. TOKEN does not persist between shell calls; re-declare it in every command block, then:
  AUTH=$(printf 'x-access-token:%s' "$TOKEN" | base64 -w0)
  git -c http.extraheader="Authorization: Basic $AUTH" <pull|fetch|push> https://github.com/sakulratpradit/p4-trrsg5.git main
  Wherever this file says `git pull/fetch/push origin main`, use that form instead.
  After ANY fetch, run: git update-ref refs/remotes/origin/main FETCH_HEAD   (so origin/main is current)
  Pipe all git output through: sed -E 's/github_pat_[A-Za-z0-9_]+/[REDACTED]/g'

RUNS TWICE (00:30 and 03:30 UTC, Tue-Sat) so that one failed start does not leave the board stale.
FIRST CHECK: if 80 or more tickers already have `pxd` equal to the most recent completed US trading day, the earlier run succeeded - STOP and do nothing else except the status step at the end.

Refresh closing prices on Salee's Pillar-4 US portfolio dashboard.

You are one of several writers to this repo. Another session may have pushed since your last run. FOLLOW deploy/src/README.md EXACTLY — it is the contract that stops writers from overwriting each other. Read it before you touch anything.


=========================================================================
WHERE PRICES COME FROM — READ THIS SECTION IN FULL BEFORE FETCHING ANYTHING
=========================================================================

The FMP MCP server is DOWN and its tools are gone. Do not wait for them.
All raw HTTP to data providers is firewalled from this sandbox (curl/python
to financialmodelingprep, eodhd, tiingo, polygon, alphavantage, twelvedata,
sec.gov, query1.finance.yahoo.com all return nothing). Use WebSearch and
WebFetch only.

PRIMARY SOURCE: the stockanalysis.com QUOTE page.
    https://stockanalysis.com/stocks/<lowercase-ticker>/

*** DO NOT TAKE THE CLOSE FROM THE /history/ TABLE. ***
This is the single most important instruction in this prompt. On roughly one
name in six, the /history/ table's row for the MOST RECENT trading day is a
PARTIAL-SESSION capture, not the official close — it shows anomalously low
volume, and on some names the quote page's price is higher than the history
row's own stated high for that day, which is arithmetically impossible. On
2026-07-31 this defect put wrong prices on this board (COIN written 143.31
against a true 146.26; HOOD written 87.92 against a true 86.56). The QUOTE
page carries the official closing-auction print. The history table is for
VALIDATION ONLY.

THE RESOLUTION RULE — apply per ticker, every time:
  1. WebFetch the quote page. Ask for, verbatim: the last price, the previous
     close, the date/time stamp next to the price, the day change and percent
     change, and the market cap.
  2. WebFetch the /history/ page. Ask for the most recent 6 rows verbatim:
     date, open, high, low, close, volume.
  3. USE THE QUOTE PAGE PRICE if and only if BOTH hold:
       (a) its stamp reads "<target date>, 4:00 PM EDT" (or EST in winter), and
       (b) its stated previous close EQUALS the history table's prior-day close.
     That second test is what proves the quote page is on the right day.
  4. If the quote page is stale (it sometimes serves a snapshot weeks old —
     ASTS once served a Jul 13 page in August) or is stamped at an intraday
     time such as 3:49 PM (NET did exactly this), fall back to the history
     table and SAY SO in your report.
  5. If neither page is trustworthy, leave that ticker's price UNCHANGED and
     list it as unresolved. A stale price is recoverable; a wrong one is not.

SANITY CHECK EVERY TABLE YOU RECEIVE: a close cannot be below that row's low
or above its high. EOSE once printed a close of 3.17 on a row whose stated low
was 3.22. If a row is internally impossible, discard the whole table for that
ticker and resolve it externally.

SECOND SOURCES — required for any move of 6% or more, and for anything odd:
  - Google Finance: https://www.google.com/finance/quote/<T>:<EXCHANGE>
    Carries an explicit "Closed: <date>, 4:00 PM GMT-4" line, so you can tell
    whether it is current. IMPORTANT QUIRKS: staleness is per-ticker (it has
    served caches days or weeks old for individual names — AMPX, ENPH, EOSE);
    the /finance/quote/ and /finance/beta/quote/ forms have INDEPENDENT caches,
    so try both; and what the page labels "Previous Close" is actually the
    after-hours price, so derive the real previous close by subtracting the day
    change from the price.
  - fool.com ARTICLE-embedded quote widgets. An article published AFTER 4:00 PM
    ET on the target date carries that day's official close in a box reading
    "Current Price / Today's Change / Day's Range / Volume". These are reliable.
    The fool.com /quote/<exchange>/<ticker>/ pages are a separate thing and are
    often stale — check for a printed date before trusting one.
  - ycharts.com/companies/<TICKER> — clean "<Month> <day>, 16:00" stamp, but it
    runs 2-3 cents BELOW the official closing-auction print. Good for confirming
    a value is in the right place; do not quote it as the close.
  - marketscreener.com — carries an explicit "(Market Closed)" stamp on some
    names. Good when stockanalysis fails outright.

NEVER USE THESE — they return a price with NO DATE ATTACHED, which is far more
dangerous than a source that fails, because a confident wrong number is
indistinguishable from a right one:
    stocktwits.com, cnn.com, kraken.com, simplywall.st, tradingview.com
Also never back-solve a price from tradingkey.com — its dates are right but its
percentage moves are wrong (it printed COIN at -8.03% on a true -10.59% day).
Known dead or useless: cnbc.com (403), financecharts.com (403), barchart.com
(serves raw template placeholders), nasdaq.com ("Data is currently not
available"), morningstar.com (fields absent), msn.com and seekingalpha.com
(robots-disallowed), finviz.com (404), finance.yahoo.com history (404) and its
quote page (undated and wrong), investing.com and macrotrends.net (days to
weeks stale), marketbeat.com (paywall).

WebSearch quirk: passing allowed_domains for any host OTHER than
stockanalysis.com returns PROXY_REJECTED (HTTP 400). Use unrestricted queries
for everything else. WebFetch enforces provenance — a URL must have appeared in
a prior search result before you can fetch it.

ABSOLUTE RULE, above every other instruction here: every number you write must
have come from a tool call in THIS session. Never write a price from your own
knowledge, memory, or estimation, and never "round out" a table to make it look
complete. Prices fabricated from memory have reached this board before and they
were close enough to right that nothing looked wrong. A missing value is
completely acceptable. An invented value is a serious failure.

=========================================================================
THE JOB
=========================================================================
1. cd deploy && git pull --ff-only origin main && cd ..
2. python3 deploy/src/extract_data.py deploy/index.html deploy/src/portfolio_data.py
3. Edit deploy/src/portfolio_data.py. You own EXACTLY FOUR THINGS: `price`,
   `mcapB`, `pxd`, and `ASOF`. Do not touch fundamentals (pe/fpe/peg/ps/gm/pm/
   revB/revG/eps/epsG/roi/roe/fcfB/capexB/r40), M3, POS, TRADES, GROUPS, jan2,
   or any ticker/name/ex/g field. Another job owns those.
   - Use the most recent US regular-session CLOSE. Never after-hours or pre-market.
   - price and mcapB are linked by share count, which does not change day to
     day. If you change price, scale mcapB by the SAME ratio:
     new_mcapB = old_mcapB * (new_price / old_price).
   - `pxd` is the date of the close you just wrote, as "YYYY-MM-DD". SET IT FOR
     EVERY TICKER YOU UPDATE, and leave it alone for tickers you could not
     resolve — that is what drives the staleness badges on the page. Get this
     date from the SOURCE PAGE's own stamp, not from the container clock: this
     job fires at 00:30 UTC, which is the previous evening in New York, so
     "today" in the container is NOT the trading day you are recording.
   - Also extend `hi52` / `lo52` if today's close sits outside the stored range.
   - Update ASOF to the date of the closes you just wrote.
4. cd deploy/src && python3 gen_dashboard.py ../index.html ../../us-portfolio-dashboard.html && cd ../..
5. cd deploy && python3 src/sanity_check.py --new ../us-portfolio-dashboard.html
   THIS IS A HARD GATE. Exit 1 means DO NOT PUSH.
   Note: --allow is action="append" — repeat the flag per ticker
   (--allow COIN --allow HOOD). A comma-separated list does NOT work.
   Two bad prices have already reached this board (MSFT written $381 against a
   verified ~$421; KO written +8.7% in one day). Salee's father reads this page
   and trades from it.
   If a ticker trips the >6% rule: verify that close against a SECOND
   independent source from the list above. If confirmed real, re-run with
   --allow TICKER. If you cannot confirm it, revert that ticker to its previous
   value and note it. NEVER raise --threshold to silence a failure.
6. cp ../us-portfolio-dashboard.html index.html
   python3 src/extract_data.py index.html src/portfolio_data.py
   git add index.html src/portfolio_data.py
   git commit -m "Daily price refresh <date>: <n> prices"
7. git push origin main   — WITHOUT force.

IF THE PUSH IS REJECTED, someone else pushed first. That is the system working.
NEVER use git push --force, git push -f, or git reset --hard FETCH_HEAD to win
— that is exactly how commits ec7015f and 5fdc1dd were destroyed. Instead:
git fetch origin main; git reset --hard origin/main (this discards YOUR build
and keeps THEIRS); re-run extract_data.py; re-apply your price edits to that
fresh base; repeat steps 4-7. Retry at most 3 times, then stop and report.

Finally, verify the live page at https://sakulratpradit.github.io/p4-trrsg5/
renders, and report: how many prices changed, the largest move, every ticker
where the quote page and the history table DISAGREED and which you took, every
ticker you left unresolved and why, anything the sanity gate blocked and what
you did about it, and any source that was stale or broken. Salee has asked
explicitly to be told what could not be done — report failures plainly rather
than quietly shipping around them.

FINAL STEP - ALWAYS, success or failure:
Write the project doc `claude/p4-price-refresh-status.md` (overwrite it) with: run time (UTC), trading date recorded, PUSHED or NOT PUSHED, commit hash, number of prices changed, unresolved tickers, and any blocker verbatim. This is how the main session sees what happened.
