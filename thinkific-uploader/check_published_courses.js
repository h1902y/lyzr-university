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
  console.log(" 🌐 CHECKING PUBLISHED COURSES & LIVE STOREFRONT CATALOG");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("1. Navigating to Thinkific Admin Courses List (https://lyzr.thinkific.com/manage/courses)...");
  await page.goto('https://lyzr.thinkific.com/manage/courses', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const courseList = await page.evaluate(() => {
    const rows = Array.from(document.querySelectorAll('tr, [role="row"], div[class*="course-card"], a[href*="/manage/courses/"]'));
    return rows.map(r => r.innerText ? r.innerText.trim().replace(/\s+/g, ' ') : '').filter(t => t.length > 0 && t.length < 200);
  });

  console.log("Admin Courses Summary:");
  courseList.slice(0, 20).forEach(c => console.log(" -", c));

  console.log("\n2. Navigating to Public Storefront Collections (https://lyzr.thinkific.com/collections)...");
  await page.goto('https://lyzr.thinkific.com/collections', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(5000);

  const publicCourses = await page.evaluate(() => {
    const cards = Array.from(document.querySelectorAll('.course-card, a[href*="/courses/"], header, h3, h2'));
    return cards.map(c => c.innerText ? c.innerText.trim().replace(/\s+/g, ' ') : '').filter(t => t.length > 0 && t.length < 150);
  });

  console.log("Public Storefront Collections:");
  publicCourses.slice(0, 20).forEach(c => console.log(" -", c));

  const ssPath = resolve('/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/published_catalog_status.png');
  await page.screenshot({ path: ssPath, fullPage: true });
  console.log(`\n📸 Saved storefront screenshot: ${ssPath}`);

  await context.close();
}

main().catch(console.error);
