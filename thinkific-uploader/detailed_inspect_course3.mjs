import { chromium } from 'playwright';
import { resolve } from 'node:path';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');

async function detailedInspect() {
  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1400, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("Navigating to https://lyzr.thinkific.com/manage/courses/3489970/curriculum...");
  await page.goto('https://lyzr.thinkific.com/manage/courses/3489970/curriculum', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const iframe = page.frameLocator('iframe[src*="hub/courses"]');

  // Let's get all chapters and lessons elements inside the iframe
  const structure = await iframe.evaluate(() => {
    const chapters = [];
    // Chapters usually have headings or container divs
    const chapterEls = document.querySelectorAll('[data-qa="chapter-item"], [class*="chapter"]');
    chapterEls.forEach((ch, idx) => {
      const title = ch.querySelector('[class*="title"], h3, h4, span')?.innerText || ch.innerText;
      chapters.push({ index: idx, text: title.split('\n')[0] });
    });

    const lessons = [];
    const lessonEls = document.querySelectorAll('[data-qa="lesson-item"], [class*="lesson"]');
    lessonEls.forEach((l, idx) => {
      lessons.push({ index: idx, text: l.innerText.split('\n')[0] });
    });

    return { chapters, lessons, fullText: document.body.innerText };
  });

  console.log("CHAPTERS FOUND:", JSON.stringify(structure.chapters, null, 2));
  console.log("LESSONS FOUND:", JSON.stringify(structure.lessons, null, 2));
  console.log("\nFULL TEXT:\n", structure.fullText);

  await context.close();
}

detailedInspect().catch(err => {
  console.error(err);
  process.exit(1);
});
