import { chromium } from 'playwright';
import { resolve } from 'node:path';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');

async function check() {
  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1400, height: 1000 }
  });
  const page = context.pages()[0] || (await context.newPage());
  console.log("Navigating to Thinkific manage page...");
  await page.goto('https://lyzr.thinkific.com/manage/courses/3489970/curriculum', { waitUntil: 'networkidle' });
  await page.waitForTimeout(5000);
  console.log("Current URL:", page.url());
  console.log("Page Title:", await page.title());
  
  const iframes = page.frames();
  console.log(`Found ${iframes.length} total frames.`);
  iframes.forEach((f, i) => console.log(` Frame ${i}: ${f.url()}`));

  const ssPath = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/screenshots/check_login.png');
  await page.screenshot({ path: ssPath, fullPage: true });
  console.log("Saved screenshot to:", ssPath);

  await context.close();
}

check().catch(console.error);
