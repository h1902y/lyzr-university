import { chromium } from 'playwright';
import { resolve } from 'node:path';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');

async function debug() {
  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());
  console.log("Navigating to https://lyzr.thinkific.com/manage/courses/3489970/curriculum...");
  await page.goto('https://lyzr.thinkific.com/manage/courses/3489970/curriculum', { waitUntil: 'domcontentloaded' });

  for (let s = 1; s <= 15; s++) {
    await page.waitForTimeout(1000);
    const frames = page.frames();
    console.log(`[Second ${s}] Total Frames: ${frames.length}`);
    frames.forEach((f, i) => console.log(`  Frame ${i}: ${f.url()}`));
  }

  // Inspect element structure on main frame and any iframe
  const iframesInfo = await page.evaluate(() => {
    const iframes = Array.from(document.querySelectorAll('iframe'));
    return iframes.map((f, i) => ({
      index: i,
      src: f.src,
      id: f.id,
      name: f.name,
      className: f.className
    }));
  });

  console.log("\nIframes found in DOM:", JSON.stringify(iframesInfo, null, 2));

  await context.close();
}

debug().catch(console.error);
