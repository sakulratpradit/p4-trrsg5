#!/usr/bin/env python3
"""Risk-sensitivity table for the Pillar 4 board (approved by Salee 11 Oct 2026).

For every held stock it estimates, from daily closes:
  beta      - simple regression on SPY: % move per 1% S&P 500 move
  downBeta  - same regression using only days the S&P 500 fell (bad-day risk)
  rate      - multiple regression on SPY AND the 10-year yield: % move of the
              stock per +0.10 percentage-point rise in the 10-year, holding the
              market constant
  vol       - annualised volatility of daily returns
  r2        - share of the stock's daily moves explained by the S&P 500

Data:
  * stock closes are rebuilt from the board's own git history (every commit of
    src/portfolio_data.py; each STOCKS row carries its own price date 'pxd'),
  * SPY and the 10-year come from src/risk_series.json (appended nightly).
Only consecutive trading days are used; moves over 35% in a day are treated as
split artefacts and dropped.

Writes the RISK constant into src/portfolio_data.py (run from src/:
    PYTHONPATH=. python3 jobs/risk_sensitivity.py
then run the normal dashboard pipeline).
"""
import json, os, re, subprocess, sys, datetime as dt

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)


def stock_closes():
    shas = subprocess.run(["git", "-C", REPO, "log", "--format=%h", "--", "src/portfolio_data.py"],
                          capture_output=True, text=True).stdout.split()
    closes = {}
    for sha in shas:
        src = subprocess.run(["git", "-C", REPO, "show", f"{sha}:src/portfolio_data.py"],
                             capture_output=True, text=True).stdout
        m = re.search(r"^STOCKS = (.*?)(?=^[A-Z][A-Z0-9_]* = )", src, re.S | re.M)
        if not m:
            continue
        try:
            rows = eval(m.group(1), {"__builtins__": {}}, {"None": None, "True": True, "False": False})
        except Exception:
            continue
        for r in rows:
            t, px, d = r.get("t"), r.get("price"), r.get("pxd")
            if t and px and d and re.match(r"\d{4}-\d{2}-\d{2}$", str(d)):
                closes.setdefault(t, {}).setdefault(d, float(px))   # newest commit wins
    return closes


def ols(y, X):
    """Least squares with intercept. X: list of columns. Returns (coefs, r2)."""
    n, k = len(y), len(X) + 1
    rows = [[1.0] + [c[i] for c in X] for i in range(n)]
    XtX = [[sum(r[a] * r[b] for r in rows) for b in range(k)] for a in range(k)]
    Xty = [sum(r[a] * y[i] for i, r in enumerate(rows)) for a in range(k)]
    # Gauss-Jordan
    M = [XtX[a] + [Xty[a]] for a in range(k)]
    for c in range(k):
        p = max(range(c, k), key=lambda r: abs(M[r][c]))
        if abs(M[p][c]) < 1e-15:
            return None, None
        M[c], M[p] = M[p], M[c]
        for r in range(k):
            if r != c:
                f = M[r][c] / M[c][c]
                M[r] = [M[r][j] - f * M[c][j] for j in range(k + 1)]
    b = [M[a][k] / M[a][a] for a in range(k)]
    fit = [sum(b[j] * rows[i][j] for j in range(k)) for i in range(n)]
    my = sum(y) / n
    sst = sum((v - my) ** 2 for v in y)
    sse = sum((y[i] - fit[i]) ** 2 for i in range(n))
    return b, (1 - sse / sst) if sst else None


def main():
    import portfolio_data as P
    ser = json.load(open(os.path.join(HERE, "risk_series.json")))
    spy, ust = ser["spy"], ser["ust10"]
    days = sorted(spy)
    mret = {days[i]: spy[days[i]] / spy[days[i - 1]] - 1 for i in range(1, len(days))}
    dy = {days[i]: (ust[days[i]] - ust[days[i - 1]]) / 0.10
          for i in range(1, len(days)) if days[i] in ust and days[i - 1] in ust}
    closes = stock_closes()
    S = {s["t"]: s for s in P.STOCKS}
    held = {t: v for t, v in P.POS.items() if v.get("shares")}
    mv = {t: v["shares"] * (S.get(t, {}).get("price") or 0) for t, v in held.items()}
    tot = sum(mv.values())
    out = []
    for t in sorted(held, key=lambda x: -mv[x]):
        c = closes.get(t, {})
        y, xm, xy = [], [], []
        for i in range(1, len(days)):
            d0, d1 = days[i - 1], days[i]
            if d0 in c and d1 in c and d1 in dy:
                r = c[d1] / c[d0] - 1
                if abs(r) > 0.35:
                    continue
                y.append(r); xm.append(mret[d1]); xy.append(dy[d1])
        row = {"t": t, "w": round(mv[t] / tot * 100, 2), "n": len(y)}
        if len(y) >= 20:
            b1, r2 = ols(y, [xm])
            b2, _ = ols(y, [xm, xy])
            down = [(y[i], xm[i]) for i in range(len(y)) if xm[i] < 0]
            bd = ols([a for a, _ in down], [[b for _, b in down]])[0] if len(down) >= 10 else None
            mean = sum(y) / len(y)
            vol = (sum((v - mean) ** 2 for v in y) / (len(y) - 1)) ** 0.5 * (252 ** 0.5) * 100
            row.update(beta=round(b1[1], 2), r2=round(r2 * 100), downBeta=round(bd[1], 2) if bd else None,
                       rate=round(b2[2] * 100, 2), vol=round(vol))
        out.append(row)
    ok = [r for r in out if "beta" in r]
    wsum = sum(r["w"] for r in ok)
    pb = sum(r["w"] * r["beta"] for r in ok) / wsum
    pd_ = sum(r["w"] * (r["downBeta"] if r["downBeta"] is not None else r["beta"]) for r in ok) / wsum
    pr = sum(r["w"] * r["rate"] for r in ok) / wsum
    # multiple-regression market coefficient for the scenario
    scen = []
    for spx, rise in ((-10, 0.0), (-10, 0.5), (0, 0.5), (-20, 1.0)):
        chg = pb * spx + pr * (rise / 0.10)
        scen.append({"spx": spx, "ust": rise, "pct": round(chg, 1), "usd": round(tot * chg / 100)})
    first = min(d for d in mret if d in dy)
    RISK = {"asof": dt.date.today().isoformat(), "from": first, "to": days[-1],
            "days": len([d for d in mret if d in dy]),
            "holdUSD": round(tot), "beta": round(pb, 2), "downBeta": round(pd_, 2), "rate": round(pr, 2),
            "ust10": ust[sorted(ust)[-1]], "spyLast": spy[days[-1]],
            "scen": scen, "rows": out,
            "note": "Estimated from about %d trading days (%s to %s) only - treat as a first reading; it firms up as the nightly refresh adds one day at a time. Regression shows association, not cause, and says nothing about future returns." % (len(mret), first, days[-1])}
    path = os.path.join(HERE, "portfolio_data.py")
    src = open(path).read()
    line = "RISK = " + repr(RISK) + "\n\n"
    m = re.search(r"^RISK = .*?(?=^[A-Z][A-Z0-9_]* = )", src, re.S | re.M)
    if m:
        src = src[:m.start()] + line + src[m.end():]
    else:
        m = re.search(r"^METRICS3 = ", src, re.M)
        src = src[:m.start()] + line + src[m.start():]
    open(path, "w").write(src)
    print(f"RISK written: {len(ok)}/{len(out)} holdings, beta {pb:.2f}, downBeta {pd_:.2f}, rate {pr:.2f}%/+0.1pt, {RISK['days']} days")


if __name__ == "__main__":
    main()
