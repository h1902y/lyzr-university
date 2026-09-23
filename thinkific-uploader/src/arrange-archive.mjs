// Phase A — archive the non-curriculum clutter products so the catalog shows only the 6 live
// courses (+ Lyzr Community). Drives /manage/courses: open each row's "Actions" menu -> Archive.
// Allowlist-guarded: it will ONLY archive a name in CLUTTER; the 6 curriculum courses can never match.
import { config, launchOpts } from './config.mjs';

const CLUTTER = new Set([
  'TEMPLATE',
  'Lyzr for Developers — the SDK Track',
  'Building Production-Ready AI Agents',
  'AI Agent Management on Lyzr Certification',
  '[Legacy] Lyzr Value Enablement for Business Users',
  '[Legacy] Lyzr Agent Engineering for Developers',
  '[Legacy] Lyzr Agent Building',
  'New course',                       // two scaffolds, both clutter
]);

const { chromium } = await import('playwright');
const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
const page = ctx.pages()[0] || (await ctx.newPage());
page.setDefaultTimeout(40000);
page.on('dialog', (d) => d.accept().catch(() => {}));   // accept any native confirm()

const settle = () => page.waitForTimeout(2500);

// Filter the courses list by a search term so the target row is on-screen (avoids pagination).
async function search(term) {
  await page.goto('https://lyzr.thinkific.com/manage/courses', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(4000);
  const open = page.getByRole('button', { name: /open search/i }).first();
  if (await open.count()) { await open.click().catch(() => {}); await page.waitForTimeout(800); }
  const box = page.locator('input[type=search], input[placeholder*="Search" i], [role=searchbox]').first();
  await box.click();
  await box.fill('');
  await box.type(term, { delay: 20 });
  await page.waitForTimeout(3500);
}

// Archive every visible row whose name is in CLUTTER. Returns count archived this pass.
async function archiveVisibleClutter() {
  const buttons = await page.getByRole('button', { name: /^Actions for / }).all();
  for (const b of buttons) {
    const label = (await b.getAttribute('aria-label')) || '';
    const name = label.replace(/^Actions for /, '').trim();
    if (!CLUTTER.has(name) || !(await b.isVisible().catch(() => false))) continue;
    console.log(`archiving: ${name}`);
    await b.click();
    await page.waitForTimeout(1200);
    await page.getByRole('menuitem', { name: 'Archive', exact: true }).first().click();
    await page.waitForTimeout(1200);
    const confirm = page.getByRole('button', { name: /^(archive|confirm|yes|ok)/i }).first();
    if (await confirm.count().catch(() => 0)) { await confirm.click().catch(() => {}); }
    await settle();
    return name;   // list refreshed — re-search and continue
  }
  return null;
}

let archived = 0;
try {
  for (const term of ['SDK Track', 'New course', 'Building Production', 'AI Agent Management', 'Legacy', 'TEMPLATE']) {
    for (let i = 0; i < 6; i++) {        // loop until this term yields no more clutter
      await search(term);
      const done = await archiveVisibleClutter();
      if (!done) break;
      archived++;
      console.log(`  ✓ archived (${archived})`);
    }
  }
} finally {
  console.log(`\nDone — archived ${archived} product(s) this run.`);
  await ctx.close();
}
