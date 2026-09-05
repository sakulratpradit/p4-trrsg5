#!/usr/bin/env python3
"""Pillar-4 price-sanity guard.

Compares the dashboard you are ABOUT to deploy against the one currently in
git, and refuses to let an implausible price through.

Motivation: two separate refresh runs have shipped bad prints to the live
board (MSFT written as $381 against a verified ~$421; KO written +8.7% on a
single-day refresh). A bad price on dad's dashboard is worse than a stale
one, so every writer must pass this gate before pushing.

Usage
-----
    python3 sanity_check.py                      # HEAD:index.html vs ../us-portfolio-dashboard.html
    python3 sanity_check.py --new deploy/index.html
    python3 sanity_check.py --threshold 8
    python3 sanity_check.py --allow NVDA --allow SKHY   # confirmed big movers

Exit codes
----------
    0  clean (or only warnings)
    1  at least one blocking failure -- DO NOT PUSH

Rules
-----
    FAIL  price move  > threshold%  (default 6) and ticker not in --allow
    FAIL  price is null / zero / negative / non-numeric
    FAIL  a ticker present in the base build has vanished
    WARN  mcapB moves more than 3 percentage points differently from price
          (market cap and price must scale together for a given share count --
          this is the check that would have caught the SKHY mcap error)
    WARN  ASOF unchanged while prices moved
    INFO  brand-new tickers (never blocking)

A move larger than the threshold is not assumed wrong. It is assumed
UNVERIFIED. Confirm it against a second independent source, then re-run with
--allow TICKER to record that you checked it.
A ticker deliberately REMOVED from the board also needs --allow TICKER;
without it, a vanishing ticker is always a hard failure.
"""
import argparse
import json
import re
import subprocess
import sys

CONST_RE = r"^const %s = (.*);$"
THRESHOLD_DEFAULT = 6.0
MCAP_DIVERGENCE_PP = 3.0


def consts_from_html(html, names=("STOCKS", "ASOF")):
    out = {}
    for name in names:
        m = re.search(CONST_RE % name, html, re.M)
        if not m:
            raise SystemExit("ERROR: const %s not found in build" % name)
        out[name] = json.loads(m.group(1))
    return out


def read_git(ref, path, repo):
    try:
        return subprocess.check_output(
            ["git", "-C", repo, "show", "%s:%s" % (ref, path)],
            stderr=subprocess.PIPE,
        ).decode("utf-8")
    except subprocess.CalledProcessError as e:
        raise SystemExit(
            "ERROR: cannot read %s:%s from repo %s\n%s"
            % (ref, path, repo, e.stderr.decode("utf-8", "replace").strip())
        )


def index_by_ticker(stocks):
    return {s["t"]: s for s in stocks}


def pct(new, old):
    if old in (None, 0):
        return None
    return (new - old) / abs(old) * 100.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--new", default="../us-portfolio-dashboard.html",
                    help="the build about to be deployed")
    ap.add_argument("--repo", default=".", help="path to the deploy git repo")
    ap.add_argument("--base", default="HEAD", help="git ref to compare against")
    ap.add_argument("--threshold", type=float, default=THRESHOLD_DEFAULT,
                    help="max unverified single-refresh price move, in %%")
    ap.add_argument("--allow", action="append", default=[],
                    help="ticker whose large move you have independently verified")
    a = ap.parse_args()

    allow = {t.upper() for t in a.allow}

    base = consts_from_html(read_git(a.base, "index.html", a.repo))
    new = consts_from_html(open(a.new, encoding="utf-8").read())

    b, n = index_by_ticker(base["STOCKS"]), index_by_ticker(new["STOCKS"])

    fails, warns, moves, fresh = [], [], [], []

    for t in sorted(set(b) - set(n)):
        if t in allow:
            warns.append("%-6s REMOVED from the board deliberately (--allow %s)" % (t, t))
        else:
            fails.append("%-6s VANISHED -- was in %s build, absent from new build" % (t, a.base))

    for t in sorted(set(n) - set(b)):
        fresh.append("%-6s NEW  price %s" % (t, n[t].get("price")))

    for t in sorted(set(b) & set(n)):
        po, pn = b[t].get("price"), n[t].get("price")

        if not isinstance(pn, (int, float)) or pn <= 0:
            fails.append("%-6s BAD PRICE %r -- must be a positive number" % (t, pn))
            continue
        if not isinstance(po, (int, float)) or po <= 0:
            warns.append("%-6s base price was %r; cannot compare" % (t, po))
            continue

        d = pct(pn, po)
        if abs(d) < 0.005:
            continue
        moves.append((abs(d), t, po, pn, d))

        if abs(d) > a.threshold and t not in allow:
            fails.append(
                "%-6s %+7.2f%%  %s -> %s  EXCEEDS %.1f%% -- verify against a second "
                "source, then re-run with --allow %s" % (t, d, po, pn, a.threshold, t)
            )

        mo, mn = b[t].get("mcapB"), n[t].get("mcapB")
        if all(isinstance(x, (int, float)) and x > 0 for x in (mo, mn)):
            dm = pct(mn, mo)
            if abs(dm - d) > MCAP_DIVERGENCE_PP:
                warns.append(
                    "%-6s price %+.2f%% but mcapB %+.2f%% (%.1f pp apart) -- "
                    "market cap and price should scale together" % (t, d, dm, abs(dm - d))
                )

    if moves and base["ASOF"] == new["ASOF"]:
        warns.append("ASOF unchanged (%r) while %d prices moved -- update ASOF"
                     % (new["ASOF"], len(moves)))

    print("=" * 72)
    print("PILLAR-4 SANITY CHECK   base=%s  threshold=%.1f%%  allow=%s"
          % (a.base, a.threshold, ", ".join(sorted(allow)) or "-"))
    print("  base build : %3d tickers  ASOF %s" % (len(b), base["ASOF"]))
    print("  new  build : %3d tickers  ASOF %s" % (len(n), new["ASOF"]))
    print("=" * 72)

    if fresh:
        print("\nNEW TICKERS (%d)" % len(fresh))
        for line in fresh:
            print("  " + line)

    if moves:
        moves.sort(reverse=True)
        print("\nLARGEST PRICE MOVES (%d changed)" % len(moves))
        for _, t, po, pn, d in moves[:15]:
            mark = "!!" if abs(d) > a.threshold else "  "
            print("  %s %-6s %10.2f -> %10.2f  %+7.2f%%" % (mark, t, po, pn, d))
        if len(moves) > 15:
            print("     ... and %d more within tolerance" % (len(moves) - 15))

    if warns:
        print("\nWARNINGS (%d) -- not blocking" % len(warns))
        for line in warns:
            print("  ~ " + line)

    if fails:
        print("\nFAILURES (%d) -- DO NOT PUSH" % len(fails))
        for line in fails:
            print("  X " + line)
        print("\nRESULT: BLOCKED")
        return 1

    print("\nRESULT: PASS -- safe to commit and push")
    return 0


if __name__ == "__main__":
    sys.exit(main())
