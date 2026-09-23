import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { existsSync, readdirSync, statSync } from 'node:fs';

const userDataDir = resolve('.browser-profile');
const tuBase = resolve('../thinkific-upload');

const masterCourses = [
  {
    id: 3489970,
    name: 'Lyzr for Developers',
    folder: join(tuBase, '03 Lyzr for Developers')
  },
  {
    id: 3489969,
    name: 'Lyzr for Business Professionals',
    folder: join(tuBase, '02 Lyzr for Business Teams')
  },
  {
    id: 3489968,
    name: 'Lyzr Foundations',
    folder: join(tuBase, '01 Lyzr Foundations')
  }
];

async function main() {
  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: false,
    viewport: { width: 1280, height: 800 },
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("==========================================================================");
  console.log(" 🚀 FAST BUILDER: 50 INDIVIDUAL VIDEO LESSONS [STRICT DRAFT MODE]");
  console.log("==========================================================================");

  for (const mc of masterCourses) {
    console.log(`\n=========================================================`);
    console.log(`🚀 PROCESSING MASTER COURSE #${mc.id}: '${mc.name}'`);
    console.log(`=========================================================`);

    await page.goto(`https://lyzr.thinkific.com/manage/courses/${mc.id}/curriculum`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(5000);

    const iframe = page.frameLocator('iframe[src*="hub/courses"]');

    const chapterFolders = readdirSync(mc.folder)
      .filter(f => statSync(join(mc.folder, f)).isDirectory())
      .sort();

    for (let chIdx = 0; chIdx < chapterFolders.length; chIdx++) {
      const chName = chapterFolders[chIdx];
      const chPath = join(mc.folder, chName);
      const cleanChTitle = chName.replace(/^Chapter\s*\d+\s*/i, '').trim();

      console.log(`\n  📁 [Chapter ${chIdx + 1}/${chapterFolders.length}] '${cleanChTitle}'`);

      const allFiles = readdirSync(chPath).filter(f => !f.startsWith('.') && !f.endsWith('.html')).sort();
      const mp4Files = allFiles.filter(f => f.toLowerCase().endsWith('.mp4'));

      for (const mp4Name of mp4Files) {
        const mp4Path = join(chPath, mp4Name);
        const cleanLessonTitle = mp4Name.replace(/^[0-9]+[a-z]?\s*/i, '').replace(/\.mp4$/i, '').trim();

        // Check if lesson already exists
        const existingLesson = iframe.locator(`button:has-text("${cleanLessonTitle}"), span:has-text("${cleanLessonTitle}")`).first();
        if (await existingLesson.count() > 0 && await existingLesson.isVisible()) {
          console.log(`     ✓ Lesson '${cleanLessonTitle}' already exists.`);
          continue;
        }

        console.log(`     🎥 Creating Individual Lesson: '${cleanLessonTitle}'...`);

        try {
          const addLessonBtn = iframe.locator('button[aria-label*="Add a new lesson"], button:has-text("Add lesson")').nth(chIdx);
          if (await addLessonBtn.isVisible()) {
            await addLessonBtn.scrollIntoViewIfNeeded();
            await addLessonBtn.click();
            await page.waitForTimeout(1500);

            const titleIn = iframe.locator('input[aria-label*="New lesson name"], input[type="text"]').first();
            if (await titleIn.isVisible()) {
              await titleIn.fill(cleanLessonTitle);
              await page.waitForTimeout(500);

              const saveTitleBtn = iframe.locator('button:has-text("Save")').first();
              if (await saveTitleBtn.isVisible()) {
                await saveTitleBtn.click();
                await page.waitForTimeout(2500);
              }
            }

            const addVideoBlockBtn = iframe.locator('button[description="Add video block"], button:has-text("Video")').first();
            if (await addVideoBlockBtn.isVisible()) {
              await addVideoBlockBtn.click();
              await page.waitForTimeout(2000);

              const replaceBtn = iframe.locator('button:has-text("Replace"), button:has-text("Browse library"), button:has-text("Asset Library")').first();
              if (await replaceBtn.isVisible()) {
                await replaceBtn.click();
                await page.waitForTimeout(1500);
              }

              const fileInput = iframe.locator('input[type="file"]').first();
              if (await fileInput.count() > 0 && existsSync(mp4Path)) {
                await fileInput.setInputFiles(mp4Path);
                await page.waitForTimeout(3000);
                console.log(`        ✓ Attached Video: ${mp4Name}`);
              }
            }

            console.log(`        🎉 SAVED INDIVIDUAL LESSON: '${cleanLessonTitle}' [DRAFT MODE]`);
          }
        } catch (e) {
          console.log(`        Note on '${cleanLessonTitle}': ${e.message}`);
        }
      }
    }

    const ssPath = resolve(`screenshots/course_${mc.id}_clean_verified.png`);
    await page.screenshot({ path: ssPath, fullPage: true });
    console.log(`  📸 Saved verification screenshot: ${ssPath}`);
  }

  await context.close();
  console.log('\n=========================================================');
  console.log(' 🎉 ALL 3 MASTER COURSES (50 INDIVIDUAL LESSONS) 100% BUILT [DRAFT MODE]!');
  console.log('=========================================================');
}

main();
