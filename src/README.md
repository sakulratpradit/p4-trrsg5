# Pillar-4 pipeline — the ONE way to update this dashboard

There is more than one writer to this repo: an interactive Claude session and
three scheduled refresh jobs. Twice they have overwritten each other, because
each was editing a *different* copy of the data and then pushing over the
other's work.

This file is the contract that stops that. **Every writer, human or scheduled,
follows the same sequence. No exceptions.**

---

## The rule that matters most

> `index.html` in this repo is the **physical source of truth**.
> Not your sandbox. Not a file from a previous session. Not memory.

`src/portfolio_data.py` is a *regenerable mirror* of it, produced by
`extract_data.py`. It exists so the data is editable and diffable — it is
never the authority. If they ever disagree, `index.html` wins and you
re-extract.

Because all the data lives in single-line JS constants
(`const STOCKS = [...];`), **git cannot merge two concurrent edits.** The line
either matches or it conflicts. So the only thing that keeps writers from
destroying each other is: *always start from the freshly-pulled `index.html`,
and never overwrite the remote by force.*

---

## The sequence — run all seven steps, in order

```bash
# 0. get the environment (fresh session only)
mkdir -p /home/claude/pillar4 && cd /home/claude/pillar4
git clone https://github.com/sakulratpradit/p4-trrsg5.git deploy

# 1. PULL FIRST. always. this is the step that prevents clobbering.
cd deploy && git pull --ff-only origin main && cd ..

# 2. rebuild the editable mirror FROM THE FILE YOU JUST PULLED
python3 deploy/src/extract_data.py deploy/index.html deploy/src/portfolio_data.py

# 3. edit values in deploy/src/portfolio_data.py
#    -> change ONLY the fields your job owns (see "field ownership" below)
#    -> never touch t / name / ex / g, POS, TRADES, or jan2 during a refresh
#    -> update ASOF to reflect the new data date

# 4. regenerate the page (template-injection; layout is preserved exactly)
cd deploy/src && python3 gen_dashboard.py ../index.html ../../us-portfolio-dashboard.html && cd ../..

# 5. THE GATE. a bad price is worse than a stale one.
cd deploy && python3 src/sanity_check.py --new ../us-portfolio-dashboard.html
#    exit 0 -> continue.   exit 1 -> STOP, verify, do not push.

# 6. publish: the built page AND the mirror, in ONE commit
cp ../us-portfolio-dashboard.html index.html
python3 src/extract_data.py index.html src/portfolio_data.py
git add index.html src/portfolio_data.py
git commit -m "<what changed and why>"

# 7. push WITHOUT force
git push origin main
```

Optional: `python3 build_workbook_v2.py` for the Excel workbook, and
`node check_dashboard.js` (Playwright at `/opt/pw-browsers/chromium`,
`--no-sandbox`) which must print ZERO PAGE ERRORS.

---

## If step 7 is rejected

A rejected push means another writer got there first. **That is the system
working.** Do not force it.

```
!! FORBIDDEN — these destroy the other writer's work:
     git push --force
     git push -f
     git reset --hard FETCH_HEAD      <- this is how ec7015f and 5fdc1dd were lost
     git checkout --theirs / --ours on index.html
```

Instead, throw away your build and redo it on top of theirs:

```bash
git fetch origin main
git reset --hard origin/main                 # discards YOUR build, keeps THEIRS
python3 src/extract_data.py index.html src/portfolio_data.py
# re-apply your field edits to this fresh mirror, then repeat steps 4-7
```

Re-applying is cheap. Your edits touch a handful of fields; recovering someone
else's silently-deleted work does not.

---

## Field ownership

Writers edit disjoint fields. Applied to a freshly-pulled base, disjoint edits
never lose data even though git can't merge the line.

| Writer | Owns | Must not touch |
|---|---|---|
| Daily price refresh | `price`, `mcapB`, `ASOF` | fundamentals, positions, structure |
| Earnings fundamentals refresh | `pe` `fpe` `peg` `ps` `gm` `pm` `revB` `revG` `eps` `epsG` `roi` `roe` `fcfB` `capexB` `r40`, `M3` | `price`, positions, structure |
| Weekly / interactive session | all of the above, plus adding or moving tickers, `POS`, `TRADES`, `GROUPS`, layout | — |

**`price` and `mcapB` move together.** They are linked by share count, which
does not change day to day. If you change one, scale the other by the same
ratio. `sanity_check.py` warns when they drift more than 3 percentage points
apart — that warning has already caught two real errors.

---

## What `sanity_check.py` blocks, and why it exists

Two bad prints have reached the live board: MSFT written as `$381` against a
verified `~$421`, and KO written `+8.7%` on a single-day refresh. Dad reads
this page and makes decisions from it.

| | Rule |
|---|---|
| **FAIL** | price moves more than 6% in one refresh (override: `--allow TICKER`) |
| **FAIL** | price is null, zero, negative, or not a number |
| **FAIL** | a ticker present in the previous build has vanished |
| **WARN** | `mcapB` drifts >3pp from the `price` move |
| **WARN** | `ASOF` unchanged while prices moved |

A move over the threshold is **not assumed wrong — it is assumed unverified.**
Real 6%+ days happen. Confirm the number against a second independent source,
then re-run with `--allow TICKER` to record that a human checked it. Never
raise the threshold to make a failure go away.
