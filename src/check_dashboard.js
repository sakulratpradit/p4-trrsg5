const { chromium } = require('playwright');
(async () => {
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium', args: ['--no-sandbox'] });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('PAGEERROR: ' + e.message));
  page.on('console', m => { if (m.type() === 'error' && !m.text().includes('tradingview') && !m.text().includes('net::')) errors.push('CONSOLE: ' + m.text()); });
  await page.goto('file:///home/claude/pillar4/us-portfolio-dashboard.html', { waitUntil: 'load' });
  await page.waitForTimeout(2500);
  const rows = await page.locator('table tr').count();
  console.log('table rows rendered:', rows);
  console.log(errors.length ? 'ERRORS:\n' + errors.join('\n') : 'ZERO PAGE ERRORS');
  await browser.close();
  process.exit(errors.length ? 1 : 0);
})();
