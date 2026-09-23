// Recon helper: open a live admin page with the saved session, screenshot it, and dump every
// interactive element's role+name (from the accessibility tree) so locators can be written from
// the real DOM instead of guessed. Usage: node src/recon.mjs [url]
import { chromium } from 'playwright';
import { mkdirSync } from 'node:fs';
import { config, launchOpts } from './config.mjs';

mkdirSync(config.screenshotsDir, { recursive: true });
const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
const page = ctx.pages()[0] || (await ctx.newPage());
const url = process.argv[2] || config.adminUrl;
await page.goto(url, { waitUntil: 'domcontentloaded' });
await page.waitForLoadState('networkidle', { timeout: 20000 }).catch(() => {});
await page.waitForTimeout(1500);

const shot = `${config.screenshotsDir}/recon.png`;
await page.screenshot({ path: shot, fullPage: true }).catch(() => page.screenshot({ path: shot }));
console.log('URL :', page.url());
console.log('SHOT:', shot);

// Optional: a sequence of steps before dumping, to walk into the flow.
//   node src/recon.mjs <url> 'click:<sel>' 'fill:<sel>::<value>' '<sel>'(=click)
for (const step of process.argv.slice(3)) {
  try {
    if (step.startsWith('fill:')) {
      const [, rest] = step.split(/^fill:/);
      const [sel, value] = rest.split('::');
      await page.locator(sel).first().fill(value, { timeout: 8000 });
      console.log('filled:', sel, '=', value);
    } else {
      const sel = step.replace(/^click:/, '');
      await page.locator(sel).first().click({ timeout: 8000 });
      console.log('clicked:', sel);
    }
    await page.waitForTimeout(1200);
    await page.screenshot({ path: shot });
  } catch (e) { console.log('step failed:', step, '—', e.message.split('\n')[0]); }
}

const els = await page.evaluate(() => {
  const sel = 'button, a, input, textarea, select, [role=button], [role=link], [role=tab], [role=menuitem], [contenteditable="true"]';
  const vis = (e) => e.offsetParent !== null || getComputedStyle(e).position === 'fixed';
  return [...document.querySelectorAll(sel)].filter(vis).map((e) => ({
    tag: e.tagName.toLowerCase(),
    role: e.getAttribute('role') || '',
    type: e.getAttribute('type') || '',
    text: (e.innerText || e.value || '').replace(/\s+/g, ' ').trim().slice(0, 45),
    aria: e.getAttribute('aria-label') || '',
    title: e.getAttribute('title') || '',
    testid: e.getAttribute('data-testid') || e.getAttribute('data-qa') || e.getAttribute('data-test') || '',
    name: e.getAttribute('name') || '',
    placeholder: e.getAttribute('placeholder') || '',
  }));
});
console.log('--- interactive elements ---');
for (const e of els) {
  const bits = [`<${e.tag}${e.type ? ' type=' + e.type : ''}${e.role ? ' role=' + e.role : ''}>`];
  if (e.text) bits.push(`text=${JSON.stringify(e.text)}`);
  if (e.aria) bits.push(`aria=${JSON.stringify(e.aria)}`);
  if (e.title) bits.push(`title=${JSON.stringify(e.title)}`);
  if (e.testid) bits.push(`testid=${JSON.stringify(e.testid)}`);
  if (e.name) bits.push(`name=${JSON.stringify(e.name)}`);
  if (e.placeholder) bits.push(`ph=${JSON.stringify(e.placeholder)}`);
  console.log('  ' + bits.join(' '));
}
await ctx.close();
