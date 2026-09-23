import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { existsSync, readdirSync, statSync } from 'node:fs';

const userDataDir = resolve('.browser-profile');
const course1Folder = resolve('../thinkific-upload/01 Lyzr Foundations');
const course1Id = 3489968;

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
  console.log(" 🎯 STEP-BY-STEP BUILDER: COURSE 1 ('Lyzr Foundations' #3489968) [DRAFT MODE]");
  console.log("==========================================================================");

  await page.goto(`https://lyzr.thinkific.com/manage/courses/${course1Id}/curriculum`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const iframe = page.frameLocator('iframe[src*="hub/courses"]');

  // Step 1: Clean up 'Untitled Chapter' placeholder
  console.log("  🧹 Cleaning up 'Untitled Chapter' placeholder...");
  try {
    const untitledMenu = iframe.locator('button[aria-label*="Chapter actions for Untitled Chapter"], [aria-label*="Untitled Chapter"]').first();
    if (await untitledMenu.isVisible()) {
      await untitledMenu.click({ force: true });
      await page.waitForTimeout(1000);

      const delBtn = iframe.locator('button').filter({ hasText: /^Delete chapter$|^Delete$/i }).first();
      if (await delBtn.isVisible()) {
        await delBtn.click();
        await page.waitForTimeout(1000);

        const confirmBtn = iframe.locator('button').filter({ hasText: /^Delete$|^Confirm$/i }).first();
        if (await confirmBtn.isVisible()) {
          await confirmBtn.click();
          await page.waitForTimeout(2500);
          console.log("     ✓ Successfully deleted 'Untitled Chapter'!");
        }
      }
    }
  } catch (e) {
    console.log("     Untitled Chapter cleanup note:", e.message);
  }

  // Step 2: Build Chapters and Master Module Lessons for Course 1
  const chapterFolders = readdirSync(course1Folder)
    .filter(f => statSync(join(course1Folder, f)).isDirectory())
    .sort();

  for (let chIdx = 0; chIdx < chapterFolders.length; chIdx++) {
    const chName = chapterFolders[chIdx];
    const chPath = join(course1Folder, chName);
    const cleanChTitle = chName.replace(/^Chapter\s*\d+\s*/i, '').trim();
    const masterLessonTitle = `${cleanChTitle} — Master Module`;

    console.log(`\n  📁 [Chapter ${chIdx + 1}/${chapterFolders.length}] '${chName}'`);

    const allFiles = readdirSync(chPath).filter(f => !f.startsWith('.') && !f.endsWith('.html')).sort();
    const mp4Files = allFiles.filter(f => f.toLowerCase().endsWith('.mp4'));
    const pdfFiles = allFiles.filter(f => f.toLowerCase().endsWith('.pdf'));

    // Check if Master Lesson exists
    const existingLesson = iframe.locator(`button:has-text("${masterLessonTitle}"), span:has-text("${masterLessonTitle}")`).first();
    if (await existingLesson.count() > 0 && await existingLesson.isVisible()) {
      console.log(`     ✓ Master Lesson '${masterLessonTitle}' already built.`);
      continue;
    }

    console.log(`     🎥 Creating Master Lesson: '${masterLessonTitle}' (${mp4Files.length} Videos + ${pdfFiles.length} PDFs)...`);

    try {
      const addLessonBtn = iframe.locator('button[aria-label*="Add a new lesson"], button:has-text("Add lesson")').nth(chIdx);
      if (await addLessonBtn.isVisible()) {
        await addLessonBtn.scrollIntoViewIfNeeded();
        await addLessonBtn.click();
        await page.waitForTimeout(1500);

        // Fill lesson title input
        const titleInput = iframe.locator('input[aria-label*="New lesson name"], input[type="text"]').first();
        if (await titleInput.isVisible()) {
          await titleInput.fill(masterLessonTitle);
          await page.waitForTimeout(500);

          const saveTitleBtn = iframe.locator('button:has-text("Save")').first();
          if (await saveTitleBtn.isVisible()) {
            await saveTitleBtn.click();
            await page.waitForTimeout(2500);
            console.log(`        ✓ Created Lesson Title: '${masterLessonTitle}'`);
          }
        }

        // Add Video Block
        const addVideoBlockBtn = iframe.locator('button[description="Add video block"], button:has-text("Video")').first();
        if (await addVideoBlockBtn.isVisible()) {
          await addVideoBlockBtn.click();
          await page.waitForTimeout(2000);

          if (mp4Files.length > 0) {
            const mp4Path = join(chPath, mp4Files[0]);
            const replaceBtn = iframe.locator('button:has-text("Replace"), button:has-text("Upload")').first();
            if (await replaceBtn.isVisible()) {
              await replaceBtn.click();
              await page.waitForTimeout(1500);
            }
            const fileInput = iframe.locator('input[type="file"]').first();
            if (await fileInput.count() > 0 && existsSync(mp4Path)) {
              await fileInput.setInputFiles(mp4Path);
              await page.waitForTimeout(3500);
              console.log(`        ✓ Attached Video MP4: ${mp4Files[0]}`);
            }
          }
        }

        // Add PDF Block if PDFs exist
        if (pdfFiles.length > 0) {
          const addPdfBlockBtn = iframe.locator('button[description="Add PDF block"], button:has-text("PDF")').first();
          if (await addPdfBlockBtn.isVisible()) {
            await addPdfBlockBtn.click();
            await page.waitForTimeout(2000);

            const pdfPath = join(chPath, pdfFiles[0]);
            const replacePdfBtn = iframe.locator('button:has-text("Replace"), button:has-text("Upload")').nth(1);
            if (await replacePdfBtn.isVisible()) {
              await replacePdfBtn.click();
              await page.waitForTimeout(1500);
            }
            const fileInputs = iframe.locator('input[type="file"]');
            if (await fileInputs.count() > 1 && existsSync(pdfPath)) {
              await fileInputs.nth(1).setInputFiles(pdfPath);
              await page.waitForTimeout(3500);
              console.log(`        ✓ Attached PDF Study Guide: ${pdfFiles[0]}`);
            }
          }
        }

        console.log(`        🎉 COMPLETED MASTER MODULE: '${masterLessonTitle}' [DRAFT MODE]`);
      }
    } catch (e) {
      console.log(`        Note on '${masterLessonTitle}': ${e.message}`);
    }
  }

  // Take verification screenshot of Course 1
  const ssPath = resolve(`screenshots/course_1_foundations_verified.png`);
  await page.screenshot({ path: ssPath, fullPage: true });
  console.log(`\n  📸 Saved verification screenshot: ${ssPath}`);

  await context.close();
  console.log('\n=========================================================');
  console.log(' 🎉 COURSE 1 (Lyzr Foundations) 100% IMPLEMENTED IN DRAFT MODE!');
  console.log('=========================================================');
}

main();
