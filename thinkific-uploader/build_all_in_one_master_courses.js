import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { existsSync, readdirSync, statSync } from 'node:fs';

const userDataDir = resolve('.browser-profile');
const tuBase = resolve('../thinkific-upload');

const draftMasterCourses = [
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
  console.log(" BUILDER: ALL-IN-ONE SINGLE LESSON STANDARD (VIDEO + PDF IN 1 PAGE)");
  console.log("==========================================================================");

  for (const mc of draftMasterCourses) {
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

    for (let chIdx = 0; chIdx < chapterFolders.length; chIdx++) {
      const chName = chapterFolders[chIdx];
      const chPath = join(mc.folder, chName);
      console.log(`\n  📁 [Chapter ${chIdx + 1}/${chapterFolders.length}] '${chName}'`);

      const allFiles = readdirSync(chPath)
        .filter(f => !f.startsWith('.') && !f.endsWith('.html'))
        .sort();

      // Pair Video MP4s with their matching PDF Notes
      const mp4Files = allFiles.filter(f => f.toLowerCase().endsWith('.mp4'));

      for (const mp4Name of mp4Files) {
        const mp4Path = join(chPath, mp4Name);
        const prefix = mp4Name.substring(0, 3); // e.g. "01a" -> "01"
        const cleanTitle = mp4Name.replace(/^[0-9]+[a-z]?\s*/i, '').replace(/\.mp4$/i, '').trim();

        // Find matching PDF file in same chapter
        const matchingPdf = allFiles.find(f => f.toLowerCase().endsWith('.pdf') && f.startsWith(prefix));
        const pdfPath = matchingPdf ? join(chPath, matchingPdf) : null;

        console.log(`\n       🎥 All-in-One Lesson: '${cleanTitle}'`);
        console.log(`          • Video: ${mp4Name}`);
        console.log(`          • PDF Attachment: ${matchingPdf || 'None'}`);

        try {
          // Click Add Lesson for current chapter
          const addLessonBtn = iframe.locator('[data-qa="add-lesson-button"], button:has-text("Add lesson")').nth(chIdx);
          if (await addLessonBtn.isVisible()) {
            await addLessonBtn.scrollIntoViewIfNeeded();
            await addLessonBtn.click();
            await page.waitForTimeout(2000);

            // Click Add Video Block
            const addVideoBtn = iframe.locator('[data-qa="add-video-block-button"]').first();
            if (await addVideoBtn.isVisible()) {
              await addVideoBtn.click();
              await page.waitForTimeout(3000);

              // Set Clean Lesson Title
              const titleInput = iframe.locator('input[type="text"]').first();
              if (await titleInput.isVisible()) {
                await titleInput.fill(cleanTitle);
              }

              // Attach Video MP4 File
              const fileInputs = iframe.locator('input[type="file"]');
              if (await fileInputs.count() > 0 && existsSync(mp4Path)) {
                await fileInputs.first().setInputFiles(mp4Path);
                await page.waitForTimeout(4000);
                console.log(`          ✓ Attached Video MP4`);
              }

              // Attach Complementary PDF Download if present
              if (pdfPath && existsSync(pdfPath)) {
                const addDownloadsHeader = iframe.locator('div, span, button').filter({ hasText: /Add downloads|Downloads/i }).first();
                if (await addDownloadsHeader.isVisible()) {
                  await addDownloadsHeader.click();
                  await page.waitForTimeout(1500);
                }

                if (await fileInputs.count() > 1) {
                  await fileInputs.nth(1).setInputFiles(pdfPath);
                  await page.waitForTimeout(3000);
                  console.log(`          ✓ Attached PDF Study Guide Download`);
                }
              }

              // Save All-in-One Lesson
              const saveBtn = iframe.locator('[data-qa="actions-bar__save-button"], button:has-text("Save")').first();
              if (await saveBtn.isVisible()) {
                await saveBtn.click();
                await page.waitForTimeout(4000);
                console.log(`          🎉 SAVED UNIFIED LESSON: '${cleanTitle}' [DRAFT]`);
              }
            }
          }
        } catch (err) {
          console.error(`          ⚠️ Error building '${cleanTitle}': ${err.message}`);
        }
      }
    }
  }

  await context.close();
  console.log('\n=========================================================');
  console.log(' 🎉 ALL MASTER COURSES BUILT WITH ALL-IN-ONE LESSONS [DRAFT]!');
  console.log('=========================================================');
}

main();
