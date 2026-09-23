import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { writeFileSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');

async function inspectCourse3() {
  console.log("Connecting to Thinkific browser persistent profile...");
  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1400, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("Navigating to Course 3 Curriculum: https://lyzr.thinkific.com/manage/courses/3489970/curriculum...");
  await page.goto('https://lyzr.thinkific.com/manage/courses/3489970/curriculum', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const iframe = page.frameLocator('iframe[src*="hub/courses"]');

  // Grab body text and innerHTML or structural tree
  const bodyText = await iframe.locator('body').innerText().catch(e => `Error getting innerText: ${e.message}`);
  
  console.log("\n=== CURRICULUM TEXT ON THINKIFIC ===");
  console.log(bodyText);
  console.log("=====================================\n");

  // Take screenshot
  const ssPath = resolve('/Users/hkc/.gemini/antigravity/brain/f1bc1789-c106-4bdb-a8f9-b125bcb7b5db/course3_curriculum_status.png');
  await page.screenshot({ path: ssPath, fullPage: true });
  console.log(`Saved screenshot to ${ssPath}`);

  await context.close();
}

inspectCourse3().catch(err => {
  console.error("Error inspecting Course 3:", err);
  process.exit(1);
});
