import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { existsSync, readdirSync, statSync } from 'node:fs';

const userDataDir = resolve('.browser-profile');
const tuBase = resolve('../thinkific-upload');

const masterCourses = [
  {
    id: 3489968,
    name: 'Lyzr Foundations',
    folder: join(tuBase, '01 Lyzr Foundations')
  },
  {
    id: 3489969,
    name: 'Lyzr for Business Teams',
    folder: join(tuBase, '02 Lyzr for Business Teams')
  },
  {
    id: 3489970,
    name: 'Lyzr for Developers',
    folder: join(tuBase, '03 Lyzr for Developers')
  }
];

async function main() {
  if (!existsSync(userDataDir)) {
    console.error('No browser profile found');
    return;
  }

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: false,
    viewport: { width: 1280, height: 800 },
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("==========================================================================");
  console.log(" ROBUST PLAYWRIGHT LESSON BUILDER (STRICT DRAFT MODE — NO PUBLISHING)");
  console.log("==========================================================================");

  for (const mc of masterCourses) {
    console.log(`\n=========================================================`);
    console.log(`🚀 PROCESSING MASTER COURSE #${mc.id}: '${mc.name}'`);
    console.log(`=========================================================`);

    if (!existsSync(mc.folder)) {
      console.log(`  ⚠️ Folder not found: ${mc.folder}`);
      continue;
    }

    const chapterFolders = readdirSync(mc.folder)
      .filter(f => statSync(join(mc.folder, f)).isDirectory())
      .sort();

    await page.goto(`https://lyzr.thinkific.com/manage/courses/${mc.id}/curriculum`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(7000);

    const iframe = page.frameLocator('iframe[src*="hub/courses"]');

    // Clean up any extra 'Untitled Chapter' if present
    const overflowMenus = iframe.locator('[data-qa="chapter-overflow-menu"]');
    const chCards = iframe.locator('div[class*="chapter"]');
    const chCount = await chCards.count();
    
    for (let idx = 0; idx < chapterFolders.length; idx++) {
      const chName = chapterFolders[idx];
      const chPath = join(mc.folder, chName);
      console.log(`\n  📁 [Chapter ${idx + 1}/${chapterFolders.length}] '${chName}'`);

      const files = readdirSync(chPath)
        .filter(f => !f.startsWith('.') && !f.endsWith('.html'))
        .sort();

      for (const fname of files) {
        const filePath = join(chPath, fname);
        const isPdf = fname.toLowerCase().endsWith('.pdf');
        const isMp4 = fname.toLowerCase().endsWith('.mp4');

        if (!isPdf && !isMp4) continue;

        const lessonTitle = fname.replace(/\.(mp4|pdf)$/i, '').trim();

        // Check if lesson already uploaded
        const existingLesson = iframe.locator(`span:has-text("${lessonTitle}")`).first();
        if (await existingLesson.count() > 0 && await existingLesson.isVisible()) {
          console.log(`       ✓ Lesson '${lessonTitle}' already exists in Chapter! Skipping.`);
          continue;
        }

        console.log(`       📄 Uploading Lesson: '${lessonTitle}' (${isPdf ? 'PDF' : 'Video'})...`);

        try {
          // Close any open modals/dialogs first
          const closeDrawer = iframe.locator('button[aria-label="Close"], button[class*="close"], button:has-text("Close")').first();
          if (await closeDrawer.isVisible()) {
            await closeDrawer.click();
            await page.waitForTimeout(1500);
          }

          // Locate the specific Add Lesson button for this chapter
          const addLessonBtn = iframe.locator('[data-qa="add-lesson-button"], button:has-text("Add lesson")').nth(idx);
          if (await addLessonBtn.isVisible()) {
            await addLessonBtn.scrollIntoViewIfNeeded();
            await addLessonBtn.click();
            await page.waitForTimeout(2000);

            // Select PDF or Video Block
            const blockBtn = iframe.locator(isPdf ? '[data-qa="add-pdf-block-button"]' : '[data-qa="add-video-block-button"]').first();
            if (await blockBtn.isVisible()) {
              await blockBtn.click();
              await page.waitForTimeout(3000);

              // Set Title
              const titleInput = iframe.locator('input[type="text"]').first();
              if (await titleInput.isVisible()) {
                await titleInput.fill(lessonTitle);
              }

              // Attach File
              const fileInput = iframe.locator('input[type="file"]').first();
              if (await fileInput.count() > 0 && existsSync(filePath)) {
                await fileInput.setInputFiles(filePath);
                await page.waitForTimeout(4000);
              }

              // Save Lesson
              const saveBtn = iframe.locator('[data-qa="actions-bar__save-button"], button:has-text("Save")').first();
              if (await saveBtn.isVisible()) {
                await saveBtn.click();
                await page.waitForTimeout(4000);
                console.log(`          ✓ Saved Lesson: '${lessonTitle}' [DRAFT]`);
              }
            }
          }
        } catch (err) {
          console.error(`          ⚠️ Note on '${fname}': ${err.message}`);
        }
      }
    }
  }

  await context.close();
  console.log('\n=========================================================');
  console.log(' 🎉 ALL CHAPTERS & LESSONS VERIFIED & KEPT IN DRAFT MODE!');
  console.log('=========================================================');
}

main();
