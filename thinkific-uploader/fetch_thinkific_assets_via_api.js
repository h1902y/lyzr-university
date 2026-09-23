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
  console.log(" 🔍 FETCHING ALL ASSETS VIA THINKIFIC INTERNAL API");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  await page.goto('https://lyzr.thinkific.com/manage/courses/3489970/curriculum', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  // Execute fetch against internal Thinkific API
  const apiAssets = await page.evaluate(async () => {
    try {
      const res = await fetch('/api/v1/assets?limit=100');
      if (res.ok) {
        const data = await res.json();
        return data;
      }
    } catch (e) {}

    try {
      const res2 = await fetch('https://university.lyzr.ai/manage/videos');
      if (res2.ok) {
        const text = await res2.text();
        return { rawTextSnippet: text.substring(0, 500) };
      }
    } catch (e) {}

    return null;
  });

  console.log("API Assets Result:", JSON.stringify(apiAssets, null, 2));

  // Navigate to Video Library admin page if present
  console.log("\nNavigating to Video Library admin page (https://lyzr.thinkific.com/manage/videos)...");
  await page.goto('https://lyzr.thinkific.com/manage/videos', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(5000);

  const videos = await page.evaluate(() => {
    const rows = Array.from(document.querySelectorAll('tr, [role="row"], div[class*="video-item"]'));
    return rows.map(r => r.innerText ? r.innerText.trim().replace(/\s+/g, ' ') : '').filter(t => t.length > 0 && t.length < 200);
  });

  console.log(`Found ${videos.length} items on Video Library admin page:\n`);
  videos.slice(0, 30).forEach((v, i) => console.log(` ${i + 1}. ${v}`));

  const ssPath = resolve('/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/thinkific_video_library.png');
  await page.screenshot({ path: ssPath, fullPage: true });
  console.log(`\n📸 Saved Video Library screenshot: ${ssPath}`);

  await context.close();
}

main().catch(console.error);
