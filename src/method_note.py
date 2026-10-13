"""Allocation-method note for the Stock Notes page (Notes tab).

Saved on 13 Oct 2026 at Salee's request so the Quality scoring, the priority
ranking and the worked examples stay on record for his understanding.
The worked examples are fixed to the 12 Oct 2026 closes; the ranking table at
the end is rebuilt from live board data every time notes.html is generated.
"""
import html

THRESHOLDS = [
    ('Net profit margin', 'Profit after everything, as % of sales', '15% or more = 2 points · 5% to 15% = 1 point · under 5% = 0'),
    ('Gross margin', 'What is left after the direct cost of making the product', '50% or more = 1 point · under 50% = 0'),
    ('Return on equity', 'Profit earned on the shareholders’ money', '20% or more = 2 points · 10% to 20% = 1 point · under 10% = 0'),
    ('Free cash flow', 'Real cash left after running and investing in the business', 'positive = 2 points · zero or negative = 0'),
    ('Rule of 40', 'Sales growth % plus profit margin % added together', '40 or more = 2 points · 25 to 40 = 1 point · under 25 = 0'),
    ('Debt to equity', 'Borrowings compared with shareholders’ money', 'debt smaller than equity (below 1.0) = 1 point · otherwise 0'),
]

# Worked examples, 12 Oct 2026 closes (figures from the board data on that day).
EXAMPLES = [
    ('AVGO', 'Broadcom', 10, ['42.9% → 2', '68.8% → 1', '38.4% → 2', '+$39.4bn → 2', '92.9 → 2', '0.60 → 1'],
     'Full marks. Fat margins, strong returns, big cash, growing fast, modest debt.'),
    ('VRT', 'Vertiv', 8, ['14.4% → 1', '37.2% → 0', '45.1% → 2', '+$2.3bn → 2', '50.0 → 2', '0.77 → 1'],
     'Loses a point on net margin (just under 15%) and one on gross margin (hardware, under 50%).'),
    ('CAT', 'Caterpillar', 6, ['14.5% → 1', '29.7% → 0', '57.0% → 2', '+$9.0bn → 2', '30.4 → 1', '2.33 → 0'],
     'Good returns and cash, but a heavy-industry gross margin, slower growth, and borrowings over twice its equity.'),
    ('VST', 'Vistra', 5, ['11.5% → 1', '38.6% → 0', '42.9% → 2', '+$1.8bn → 2', '16.7 → 0', '3.29 → 0'],
     'A utility: steady cash, but thin growth-plus-margin and a lot of debt.'),
    ('AMZN', 'Amazon', 4, ['12.1% → 1', '50.8% → 1', '17.0% → 1', '−$7.6bn → 0', '18.6 → 0', '0.40 → 1'],
     'Scores low on purpose: free cash flow is negative because it is spending record sums on data centres. The score measures today’s numbers, not the story.'),
]


def _tbl(head, rows):
    h = '<table><thead><tr>' + ''.join('<th>' + html.escape(c) + '</th>' for c in head) + '</tr></thead><tbody>'
    for r in rows:
        h += '<tr>' + ''.join('<td>' + c + '</td>' for c in r) + '</tr>'
    return h + '</tbody></table>'


def build(P):
    """Return the HTML fragment for the Notes page. P = portfolio_data module."""
    M3 = getattr(P, 'METRICS3', {})

    def score(s):
        m = M3.get(s['t'], {})
        pm = s.get('pm') or 0; gm = s.get('gm') or 0; roe = s.get('roe') or 0
        f = s.get('fcfB') or 0; r = s.get('r40') or 0; de = m.get('de')
        return ((2 if pm >= 15 else (1 if pm >= 5 else 0)) + (1 if gm >= 50 else 0)
                + (2 if roe >= 20 else (1 if roe >= 10 else 0)) + (2 if f > 0 else 0)
                + (2 if r >= 40 else (1 if r >= 25 else 0)) + (1 if (de is not None and de < 1) else 0))

    rows = []
    for s in P.STOCKS:
        if not s.get('fvAvg') or not s.get('price'):
            continue
        up = (s['fvAvg'] / s['price'] - 1) * 100
        q = score(s)
        held = bool(P.POS.get(s['t'], {}).get('shares'))
        rows.append((up * q / 10, s['t'], s['name'], q, up, held))
    rows.sort(reverse=True)
    asof = max((s.get('pxd') or '') for s in P.STOCKS)

    e = html.escape
    H = []
    H.append('<div class="card method"><h2>How we rank the stocks (method approved 12 Oct 2026)</h2>')
    H.append('<div class="meta">Saved 13 Oct 2026 for the record · the live version is on the dashboard: Method &amp; Budget Tiers tab, and rows 27–29 of the data matrix on the Portfolio tab</div>')

    H.append('<h3>1. The idea in one line</h3>')
    H.append('<p>The old way gave every stock a budget so the board was spread across many kinds of company. The new way asks one question for every dollar: <b>where is it most likely to earn the roughly 15% a year the $2.0M goal needs?</b> Diversification is still a limit (no sector or name too big), but it is no longer the reason to buy.</p>')

    H.append('<h3>2. Quality score, 0 to 10</h3>')
    H.append('<p>Six yes/no checks on the company’s own numbers, taken straight from the board data. Add the points. A missing figure scores zero, so a thin data record drags a score down — I flag that when it affects a decision.</p>')
    H.append(_tbl(['Check', 'What it measures', 'Points'], [[e(a), e(b), e(c)] for a, b, c in THRESHOLDS]))
    H.append('<p><b>How to read it:</b> 9–10 = a money machine (Nvidia, Broadcom, Micron, TSMC). 7–8 = good business with one soft spot. 5–6 = cyclical, capital-heavy or indebted. 4 or less = the numbers do not yet support the story.</p>')

    H.append('<h3>3. Worked examples (12 Oct 2026 closes)</h3>')
    H.append('<p>Columns are the six checks in the same order as the table above: net margin, gross margin, return on equity, free cash flow, Rule of 40, debt to equity.</p>')
    ex = [['<b>' + e(t) + '</b> ' + e(n), '<b>' + str(q) + '</b>'] + [e(x) for x in parts] + [e(why)] for t, n, q, parts, why in EXAMPLES]
    H.append(_tbl(['Stock', 'Score', 'Net margin', 'Gross margin', 'ROE', 'Free cash flow', 'Rule of 40', 'Debt/equity', 'Why'], ex))

    H.append('<h3>4. Priority = upside × quality ÷ 10</h3>')
    H.append('<p><b>Upside</b> is how far the price sits below our fair value: fair value ÷ price − 1. <b>Priority</b> multiplies that upside (in %) by the quality score and divides by 10, so a 10-quality stock keeps its full upside and a 5-quality stock keeps half.</p>')
    H.append('<p>Example: Broadcom at $354.73 against fair value $523.73 is 47.6% below, quality 10 → priority 47.6. Vistra is 41% below but quality 5 → priority 20.5. Amazon is 20% below but quality 4 → priority 8. A stock above fair value gets a negative priority and no new money.</p>')

    H.append('<h3>5. How the number is used</h3>')
    H.append('<ol><li><b>Fund from the top of the list down.</b> When the money runs out, the bottom waits. Budgets on low-priority names are cut and returned to a ranked pool.</li>')
    H.append('<li><b>The gates still apply before any buy:</b> price trigger (never more than 1% over the reference close); results test where one is set; rate rule (no loss-making names while the 10-year is above 5%); no-China rule; sector cap.</li>')
    H.append('<li><b>Position size:</b> every holding is built to at least 1.5% of the portfolio or exited. Target about 28 names.</li>')
    H.append('<li><b>No idle cash:</b> money not needed within 30 days sits in SGOV (T-bill fund), sold the session before each buy. The $50k crash reserve lives there too.</li>')
    H.append('<li><b>Review:</b> the ranking is re-run at every quarterly review (next 10 Dec) and whenever a budget is added or cut.</li></ol>')

    H.append('<h3>6. Two cautions</h3>')
    H.append('<div class="pt w">A high priority on a stock we do not own is not a buy signal. The ranking tells us where to look; the gates and the quarterly review decide. Sterling, BWXT and Oracle rank high on upside with quality 5–6, and we exited Oracle for its debt-funded data centres.</div>')
    H.append('<div class="pt w">A missing figure scores zero. After a data refresh a company with an incomplete record can drop unfairly; check the six component rows in the data matrix before acting on a surprise.</div>')

    H.append('<h3>7. Ranking of the whole board (prices of ' + e(asof) + ')</h3>')
    H.append('<p>Rebuilt automatically each time this page is generated. <b>Bold</b> = we own it.</p>')
    rk = []
    for i, (pr, t, n, q, up, held) in enumerate(rows, 1):
        nm = e(t) + ' ' + e(n)
        if held:
            nm = '<b>' + nm + '</b>'
        pc = 'pos' if pr >= 30 else ('neg' if pr < 0 else '')
        rk.append([str(i), nm, str(q), ('%+.0f%%' % up), '<span class="' + pc + '">%.1f</span>' % pr])
    H.append(_tbl(['#', 'Stock', 'Quality', 'Upside', 'Priority'], rk))
    H.append('<div class="empty">Analytical commentary, not licensed investment advice.</div></div>')
    return ''.join(H)
