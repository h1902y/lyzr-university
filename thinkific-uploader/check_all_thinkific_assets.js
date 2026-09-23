import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { rmSync, existsSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');

for (const lockFile of ['SingletonLock', 'SingletonSocket', 'SingletonCookie']) {
  const p = resolve(userDataDir, lockFile);
  if (existsSync(p)) {
    try { rmSync(p, { force: true }); } catch (e) {}
  }
}

async function main() {
  console.log("==========================================================================");
  console.log(" 🔍 EXTRACTING ALL ASSETS FROM THINKIFIC ASSET LIBRARY");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("1. Navigating to Thinkific Course Builder...");
  await page.goto('https://lyzr.thinkific.com/manage/courses/3489970/curriculum', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  // Wait for iframe
  const iframeLoc = page.frameLocator('iframe[src*="courses"], iframe[src*="hub"]').first();

  console.log("2. Opening Asset Library modal...");
  const assetLibBtn = iframeLoc.locator('button:has-text("Asset Library"), button[description*="asset library"]').first();
  if (await assetLibBtn.isVisible().catch(() => false)) {
    await assetLibBtn.click();
    await page.waitForTimeout(3000);
  } else {
    // Try main page button
    const btn = page.locator('button:has-text("Asset Library")').first();
    if (await btn.isVisible().catch(() => false)) {
      await btn.click();
      await page.waitForTimeout(3000);
    }
  }

  // Extract all assets from modal DOM
  const assets = await page.evaluate(() => {
    const rows = Array.from(document.querySelectorAll('tr, [role="row"], div[class*="asset-item"], li[class*="asset"]'));
    return rows.map(r => r.innerText ? r.innerText.trim().replace(/\s+/g, ' ') : '').filter(t => t.length > 0 && t.length < 200);
  });

  console.log(`Extracted ${assets.length} assets from Asset Library view:\n`);
  assets.forEach((a, i) => console.log(` ${i + 1}. ${a}`));

  const ssPath = resolve('/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/thinkific_asset_library_inspection.png');
  await page.screenshot({ path: ssPath, fullPage: true });
  console.log(`\n📸 Saved Asset Library inspection screenshot: ${ssPath}`);

  await context.close();
}

main().catch(console.error);
