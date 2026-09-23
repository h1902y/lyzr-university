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
  console.log(" 📊 GETTING CHAPTER > LESSON COUNT FOR ALL PUBLISHED COURSES");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  await page.goto('https://lyzr.thinkific.com/manage/courses', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  // Extract all published courses and their edit URLs
  const publishedCourses = await page.evaluate(() => {
    const rows = Array.from(document.querySelectorAll('tr, [role="row"], div[class*="course-card"]'));
    const list = [];
    rows.forEach(r => {
      const text = r.innerText || '';
      if (text.includes('Published') && !text.includes('Draft')) {
        const link = r.querySelector('a[href*="/manage/courses/"]');
        if (link) {
          const href = link.getAttribute('href');
          const idMatch = href.match(/courses\/(\d+)/);
          const id = idMatch ? idMatch[1] : null;
          const title = text.split('\n')[0].replace('LYZR UNIVERSITY', '').trim();
          if (id && title) {
            list.push({ id, title, href });
          }
        }
      }
    });
    return list;
  });

  console.log(`Found ${publishedCourses.length} published courses on Thinkific.\n`);

  for (const course of publishedCourses) {
    await page.goto(`https://lyzr.thinkific.com/manage/courses/${course.id}/curriculum`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(5000);

    const frame = page.frames().find(f => f.url().includes('courses') || f.url().includes('hub')) || page.mainFrame();
    const counts = await frame.evaluate(() => {
      const chapters = document.querySelectorAll('div[class*="chapter-item"], div[class*="Chapter"], [data-qa*="chapter"]');
      const lessons = document.querySelectorAll('a[href*="/contents/"], [data-qa*="lesson"]');
      return {
        chapterCount: chapters.length || document.querySelectorAll('header:has(button)').length,
        lessonCount: lessons.length
      };
    });

    console.log(`📌 ${course.title} (#${course.id}): ${counts.chapterCount} Chapters · ${counts.lessonCount} Lessons`);
  }

  await context.close();
}

main().catch(console.error);
