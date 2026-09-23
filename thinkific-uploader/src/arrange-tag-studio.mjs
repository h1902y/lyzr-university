// Phase C — add the 2 Studio courses to the "Studio Track" category (currently 0 products) so the
// public /collections/track-studio page populates. Uses the category editor's product combobox + Add.
import { config, launchOpts } from './config.mjs';

const CAT_EDIT = 'https://lyzr.thinkific.com/manage/collections/1445649/edit';   // Studio Track
const COURSES = ['Studio: The Agent Lifecycle', 'Studio: Design & Create'];

const { chromium } = await import('playwright');
const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
const page = ctx.pages()[0] || (await ctx.newPage());
page.setDefaultTimeout(35000);

await page.goto(CAT_EDIT, { waitUntil: 'domcontentloaded' });
await page.waitForTimeout(5000);

for (const name of COURSES) {
  console.log(`adding: ${name}`);
  const combo = page.locator('[role=combobox]').first();
  await combo.click();
  await page.waitForTimeout(800);
  await page.keyboard.type(name.slice(0, 18), { delay: 30 });   // type enough to filter
  await page.waitForTimeout(2500);
  // pick the matching option from the listbox
  const opt = page.getByRole('option', { name: new RegExp(name.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i') }).first();
  if (await opt.count()) { await opt.click(); }
  else { await page.getByText(name, { exact: false }).last().click(); }   // fallback
  await page.waitForTimeout(800);
  // click the Add button next to the combobox
  await page.getByRole('button', { name: /^Add$/ }).first().click();
  await page.waitForTimeout(1500);
  console.log(`  + added to list`);
}

// Save the category
await page.getByRole('button', { name: /^Update$/ }).first().click();
await page.waitForTimeout(4000);
console.log('Saved category. URL:', page.url());
await ctx.close();
