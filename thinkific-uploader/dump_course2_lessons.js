import { chromium } from 'playwright';
import { resolve } from 'node:path';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const courseId = 3489969;

async function main() {
  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1400, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());
  await page.goto(`https://lyzr.thinkific.com/manage/courses/${courseId}/curriculum`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const frame = page.frames().find(f => f.url().includes('hub/courses'));
  if (frame) {
    const lessons = await frame.evaluate(() => {
      const elems = Array.from(document.querySelectorAll('button, a, div, span'));
      return elems.map(e => e.innerText ? e.innerText.trim() : '').filter(t => t.length > 0 && t.length < 100);
    });

    console.log("=== ALL SIDEBAR TEXT ELEMENTS IN COURSE 2 ===");
    const unique = Array.from(new Set(lessons));
    for (const item of unique) {
      if (item.match(/\d+/)) {
        console.log("ITEM:", item);
      }
    }
  }

  await context.close();
}

main().catch(console.error);
