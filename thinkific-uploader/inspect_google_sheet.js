import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { rmSync, existsSync, writeFileSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const brainDir = resolve('/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61');

for (const lockFile of ['SingletonLock', 'SingletonSocket', 'SingletonCookie']) {
  const p = resolve(userDataDir, lockFile);
  if (existsSync(p)) {
    try { rmSync(p, { force: true }); } catch (e) {}
  }
}

async function main() {
  console.log("==========================================================================");
  console.log(" 📊 INSPECTING HARSHIT'S GOOGLE SHEET");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  const sheetUrl = 'https://docs.google.com/spreadsheets/d/1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk/edit?gid=0#gid=0';
  console.log(`Navigating to Google Sheet: ${sheetUrl}`);
  await page.goto(sheetUrl, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const ssPath = resolve(brainDir, 'google_sheet_live_view.png');
  await page.screenshot({ path: ssPath, fullPage: true });
  console.log(`📸 Saved Google Sheet screenshot: ${ssPath}`);

  // Check title
  const pageTitle = await page.title();
  console.log(`Google Sheet Page Title: '${pageTitle}'`);

  await context.close();
}

main().catch(console.error);
