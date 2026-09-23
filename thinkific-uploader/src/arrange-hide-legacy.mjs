// Phase A fix — archiving did NOT remove the (published) legacy courses from the public catalog.
// Set "Hidden course" = true on each so they leave /collections. (They stay accessible by direct link
// for any existing enrollments.)
import { config, launchOpts } from './config.mjs';

const LEGACY = [
  { id: '3447255', name: '[Legacy] Lyzr Agent Building' },
  { id: '3447258', name: '[Legacy] Lyzr Agent Engineering for Developers' },
  { id: '3447264', name: '[Legacy] Lyzr Value Enablement for Business Users' },
];

const { chromium } = await import('playwright');
const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
const page = ctx.pages()[0] || (await ctx.newPage());
page.setDefaultTimeout(35000);

for (const c of LEGACY) {
  console.log(`hiding: ${c.name}`);
  await page.goto(`https://lyzr.thinkific.com/manage/courses/${c.id}/settings`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(5000);
  // Toggle the "Hidden course" checkbox on (only if currently off)
  const wasChecked = await page.evaluate(() => {
    const el = [...document.querySelectorAll('*')].find((e) => e.children.length <= 2 && (e.textContent || '').trim() === 'Hidden course');
    const scope = el?.closest('label,div,fieldset') || el?.parentElement;
    const inp = scope?.querySelector('input[type=checkbox]');
    return inp ? inp.checked : null;
  });
  if (wasChecked === false) {
    await page.getByText('Hidden course', { exact: true }).first().click();
    await page.waitForTimeout(600);
  }
  await page.getByRole('button', { name: /save settings/i }).first().click();
  await page.waitForTimeout(3500);
  // confirm it stuck
  const nowChecked = await page.evaluate(() => {
    const el = [...document.querySelectorAll('*')].find((e) => e.children.length <= 2 && (e.textContent || '').trim() === 'Hidden course');
    const scope = el?.closest('label,div,fieldset') || el?.parentElement;
    return scope?.querySelector('input[type=checkbox]')?.checked;
  });
  console.log(`  Hidden course = ${nowChecked} (was ${wasChecked})`);
}
await ctx.close();
