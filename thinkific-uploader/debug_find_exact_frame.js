import { chromium } from 'playwright';
import { resolve } from 'node:path';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');

async function main() {
  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());
  await page.goto('https://lyzr.thinkific.com/manage/courses/3489970/curriculum', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(8000);

  console.log("=== ALL FRAMES ON PAGE ===");
  page.frames().forEach((f, i) => {
    console.log(`Frame ${i}: ${f.url()}`);
  });

  for (const f of page.frames()) {
    try {
      const lessonLinks = await f.evaluate(() => {
        const links = Array.from(document.querySelectorAll('a, button, div, span'));
        return links.map(l => l.innerText ? l.innerText.trim() : '').filter(t => t.includes('What is RAG') || t.includes('Quickstart') || t.includes('Lesson') || t.includes('Chapter'));
      });
      if (lessonLinks.length > 0) {
        console.log(`\n✅ MATCH FOUND IN FRAME: ${f.url()}`);
        console.log("Sample elements:", lessonLinks.slice(0, 10));
      }
    } catch (e) {}
  }

  await context.close();
}

main().catch(console.error);
