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
  console.log(" 🔍 DEEP SCRAPE OF THINKIFIC VIDEO & ASSET LIBRARY");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("1. Navigating to Thinkific Admin Video Library (https://lyzr.thinkific.com/manage/videos)...");
  await page.goto('https://lyzr.thinkific.com/manage/videos', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  // If redirect or iframe, wait for page elements
  const currentUrl = page.url();
  console.log("Current Page URL:", currentUrl);

  // Take full page screenshot of Video Library
  const ss1 = resolve(brainDir, 'thinkific_video_library_admin_page.png');
  await page.screenshot({ path: ss1, fullPage: true });
  console.log(`📸 Saved Video Library Admin Screenshot: ${ss1}`);

  // Extract all video items from main frame and any child frames
  const allText = await page.evaluate(() => document.body.innerText || '');
  console.log("\nVideo Library Page Text Snippet:\n", allText.substring(0, 800));

  // Extract table rows / video cards
  const videoItems = await page.evaluate(() => {
    const selector = 'tr, [role="row"], div[class*="video"], div[class*="asset"]';
    const elements = Array.from(document.querySelectorAll(selector));
    const items = [];
    elements.forEach(el => {
      const txt = (el.innerText || '').trim().replace(/\s+/g, ' ');
      if (txt && txt.length > 5 && txt.length < 300 && !txt.includes('Title Duration') && !txt.includes('Search videos')) {
        items.push(txt);
      }
    });
    return items;
  });

  console.log(`\nFound ${videoItems.length} video rows/cards in Thinkific Video Library:`);
  videoItems.forEach((item, idx) => {
    console.log(` ${idx + 1}. ${item}`);
  });

  // Save report artifact
  const reportPath = resolve(brainDir, 'thinkific_complete_asset_library_report.md');
  const reportMd = `# 📹 Thinkific Complete Video & Asset Library Report

**Execution Timestamp:** ${new Date().toISOString()}  
**Video Library URL:** https://lyzr.thinkific.com/manage/videos  
**Total Scraped Video Items:** ${videoItems.length}  

---

## 1. Video Library Screenshot Artifact

![Thinkific Video Library Admin Page](file://${ss1})

---

## 2. Scraped Video Asset List

${videoItems.map((item, idx) => `### ${idx + 1}. ${item}`).join('\n\n')}
`;

  writeFileSync(reportPath, reportMd, 'utf-8');
  console.log(`\n📝 Saved complete asset library report artifact to: ${reportPath}`);

  await context.close();
}

main().catch(console.error);
