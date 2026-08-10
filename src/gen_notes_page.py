#!/usr/bin/env python3
"""Build notes.html - the iPad-friendly Stock Notes page for Dad.

Reads src/weekly_summaries.json (curated, sentiment-tagged weekly summaries),
src/portfolio_data.py (groups / prices / positions) and the follow-up list in
gen_stock_notes.py, and writes a single self-contained page published on the
same GitHub Pages site as the dashboard.

Usage: python3 src/gen_notes_page.py [output.html]
"""
import json, os, sys, datetime, html

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import portfolio_data as P
from gen_stock_notes import FOLLOW_UPS, week_label

def build(out_path):
    weekly = json.load(open(os.path.join(HERE, 'weekly_summaries.json')))
    ovpath = os.path.join(HERE, 'company_overviews.json')
    overviews = json.load(open(ovpath)) if os.path.exists(ovpath) else {}
    stocks = []
    for s in sorted(P.STOCKS, key=lambda x: x['t']):
        t = s['t']
        pos = P.POS.get(t, {})
        weeks = sorted(weekly.get(t, []), key=lambda w: w['week'], reverse=True)
        stocks.append({
            't': t, 'name': s['name'], 'g': P.GROUPS[s['g']],
            'desc': overviews.get(t, ''),
            'held': bool(pos.get('shares')),
            'sh': pos.get('shares'), 'cost': pos.get('cost'), 'bud': pos.get('budget'),
            'px': s.get('price'), 'pxd': s.get('pxd'),
            'weeks': [{'w': w['week'], 'label': week_label(w['week']),
                       'pts': w['points']} for w in weeks],
        })
    fups = [{'t': f[0], 'type': f[1], 'text': f[2], 'raised': f[3]} for f in FOLLOW_UPS]
    today = datetime.date.today().strftime('%b %d, %Y')
    data = json.dumps({'stocks': stocks, 'fups': fups, 'gen': today},
                      ensure_ascii=False).replace('</', '<\\/')

    page = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex,nofollow,noarchive">
<title>P4 Stock Notes</title>
<style>
:root{--green:#1e7b34;--red:#c00000;--ink:#1a1a2e;--mut:#667;--bg:#f4f6fa;--card:#fff;--line:#dde3ee;--blue:#1f3864}
*{box-sizing:border-box;-webkit-tap-highlight-color:transparent}
body{margin:0;background:var(--bg);color:var(--ink);font:17px/1.55 -apple-system,"Segoe UI",Roboto,Arial,sans-serif}
header{background:var(--blue);color:#fff;padding:14px 16px;position:sticky;top:0;z-index:5}
header h1{margin:0;font-size:22px}
header .sub{font-size:13px;opacity:.85;margin-top:2px}
header a{color:#cfe0ff}
.wrap{max-width:860px;margin:0 auto;padding:14px}
#search{width:100%;font-size:22px;padding:14px 16px;border:2px solid var(--line);border-radius:14px;background:var(--card);margin:4px 0 12px}
#search:focus{outline:none;border-color:var(--blue)}
.chips{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:10px}
.chip{border:1.5px solid var(--line);background:var(--card);border-radius:20px;padding:8px 14px;font-size:15px;cursor:pointer;user-select:none}
.chip.on{background:var(--blue);color:#fff;border-color:var(--blue)}
.chip.warn.on{background:var(--red);border-color:var(--red)}
.groupname{font-size:13px;font-weight:700;color:var(--mut);text-transform:uppercase;letter-spacing:.4px;margin:14px 2px 6px}
.tk{display:flex;flex-wrap:wrap;gap:8px}
.tkbtn{border:1.5px solid var(--line);background:var(--card);border-radius:12px;padding:10px 14px;font-size:17px;font-weight:700;cursor:pointer;min-width:76px;text-align:center}
.tkbtn small{display:block;font-weight:400;font-size:11px;color:var(--mut)}
.tkbtn.held{border-color:var(--green);box-shadow:inset 0 0 0 1px var(--green)}
.card{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:16px;margin:12px 0}
.card h2{margin:0 0 2px;font-size:24px}
.card .meta{color:var(--mut);font-size:14px;margin-bottom:8px}
.desc{background:#eaf1fb;border-left:5px solid var(--blue);border-radius:0 12px 12px 0;padding:12px 14px;margin:4px 0 10px;font-size:17px;line-height:1.5;color:#1c2b45}
.desc b{display:block;font-size:12px;letter-spacing:.5px;text-transform:uppercase;color:var(--blue);margin-bottom:3px;font-weight:700}
.badge{display:inline-block;background:#e7f3ea;color:var(--green);font-size:13px;font-weight:700;border-radius:8px;padding:2px 8px;margin-left:6px}
.wk{border-top:1px solid var(--line);padding:10px 0 2px;margin-top:8px}
.wk h3{margin:0 0 6px;font-size:15px;color:var(--blue)}
.pt{margin:6px 0;padding-left:26px;position:relative;font-size:16px}
.pt:before{position:absolute;left:0;top:0;font-weight:700}
.pt.p{color:var(--green)}.pt.p:before{content:"▲"}
.pt.n{color:var(--red)}.pt.n:before{content:"▼"}
.pt.w{color:var(--red);font-weight:700}.pt.w:before{content:"⚠"}
.pt.z{color:var(--ink)}.pt.z:before{content:"•";color:var(--mut)}
#back{display:none;margin:8px 0;font-size:18px;background:var(--card);border:1.5px solid var(--line);border-radius:12px;padding:10px 18px;cursor:pointer}
.empty{color:var(--mut);font-style:italic}
.fup{border-left:4px solid var(--red);padding:8px 12px;margin:8px 0;background:var(--card);border-radius:0 10px 10px 0;font-size:15px}
.fup b{color:var(--blue)}
footer{color:var(--mut);font-size:12px;text-align:center;padding:20px}
@media(max-width:480px){body{font-size:16px}.card h2{font-size:21px}}
</style>
</head>
<body>
<header>
  <h1>Stock Notes</h1>
  <div class="sub">Claude's comments on every stock, week by week · updated __GEN__ · <a href="index.html">back to dashboard</a></div>
</header>
<div class="wrap">
  <input id="search" type="search" placeholder="Type a stock symbol or name..." autocomplete="off">
  <div class="chips">
    <div class="chip on" data-f="all">All stocks</div>
    <div class="chip" data-f="held">Only stocks we own</div>
    <div class="chip warn" data-f="warn">⚠ Red flags</div>
    <div class="chip" data-f="fup">Open follow-ups</div>
  </div>
  <button id="back">‹ Back to all stocks</button>
  <div id="out"></div>
</div>
<footer>Analytical commentary, not licensed investment advice. Salee places every order himself.<br>
Each note is a snapshot of its week - always check the date before acting on it.</footer>
<script>
const DATA = __DATA__;
const out = document.getElementById('out'), q = document.getElementById('search'),
      back = document.getElementById('back');
let filter = 'all';
const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const cls = {'+':'p','-':'n','!':'w','0':'z'};
const money = v => v == null ? '' : '$' + Math.round(v).toLocaleString();

function ptHtml(p){ return '<div class="pt '+(cls[p.s]||'z')+'">'+esc(p.text)+'</div>'; }

function cardHtml(s, weeksToShow){
  let h = '<div class="card"><h2>'+s.t+(s.held?'<span class="badge">WE OWN '+(s.sh||'')+' sh</span>':'')+'</h2>';
  h += '<div class="meta">'+esc(s.name)+' · '+esc(s.g);
  if(s.px!=null) h += ' · last close $'+s.px.toLocaleString()+(s.pxd?' ('+s.pxd+')':'');
  if(s.held) h += ' · cost '+money(s.cost)+(s.bud?' · budget '+money(s.bud):'');
  h += '</div>';
  if(s.desc) h += '<div class="desc"><b>What this company does</b>'+esc(s.desc)+'</div>';
  const wk = weeksToShow || s.weeks;
  if(!wk.length) h += '<div class="empty">No comments on record yet for this stock.</div>';
  for(const w of wk){
    h += '<div class="wk"><h3>Week of '+w.label+'</h3>'+w.pts.map(ptHtml).join('')+'</div>';
  }
  return h+'</div>';
}

function groupsView(list){
  const by = {};
  for(const s of list){ (by[s.g] = by[s.g] || []).push(s); }
  let h='';
  for(const g of Object.keys(by).sort()){
    h += '<div class="groupname">'+esc(g)+'</div><div class="tk">';
    for(const s of by[g]) h += '<button class="tkbtn'+(s.held?' held':'')+'" data-t="'+s.t+'">'+s.t+'<small>'+esc(s.name.slice(0,14))+'</small></button>';
    h += '</div>';
  }
  return h || '<div class="empty">Nothing matches.</div>';
}

function render(){
  const term = q.value.trim().toUpperCase();
  back.style.display='none';
  if(filter==='fup'){
    out.innerHTML = DATA.fups.map(f => '<div class="fup"><b>'+esc(f.t)+'</b> · '+esc(f.type)+' · raised '+esc(f.raised)+'<br>'+esc(f.text)+'</div>').join('');
    return;
  }
  if(filter==='warn'){
    let h='';
    for(const s of DATA.stocks){
      const wk = s.weeks.map(w => ({label:w.label, pts:w.pts.filter(p=>p.s==='!'||p.s==='-')})).filter(w=>w.pts.length);
      if(wk.length && (!term || s.t.includes(term) || s.name.toUpperCase().includes(term))) h += cardHtml(s, wk);
    }
    out.innerHTML = h || '<div class="empty">No red flags match.</div>';
    return;
  }
  let list = DATA.stocks;
  if(filter==='held') list = list.filter(s=>s.held);
  if(term){
    const hit = list.filter(s => s.t.includes(term) || s.name.toUpperCase().includes(term));
    if(hit.length===1 || (hit.length && hit[0].t===term)){ out.innerHTML = hit.map(s=>cardHtml(s)).join(''); return; }
    out.innerHTML = groupsView(hit);
    return;
  }
  out.innerHTML = groupsView(list);
}

out.addEventListener('click', e=>{
  const b = e.target.closest('.tkbtn'); if(!b) return;
  const s = DATA.stocks.find(x=>x.t===b.dataset.t);
  out.innerHTML = cardHtml(s);
  back.style.display='inline-block';
  window.scrollTo({top:0});
});
back.addEventListener('click', ()=>{ q.value=''; render(); });
q.addEventListener('input', render);
document.querySelectorAll('.chip').forEach(c=>c.addEventListener('click', ()=>{
  document.querySelectorAll('.chip').forEach(x=>x.classList.remove('on'));
  c.classList.add('on'); filter=c.dataset.f; render();
}));
render();
</script>
</body>
</html>"""
    page = page.replace('__GEN__', today).replace('__DATA__', data)
    open(out_path, 'w').write(page)
    return len(stocks), sum(len(s['weeks']) for s in stocks)

if __name__ == '__main__':
    out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(REPO, 'notes.html')
    n, w = build(os.path.abspath(out))
    print(f'{out} written: {n} stocks, {w} ticker-weeks')
