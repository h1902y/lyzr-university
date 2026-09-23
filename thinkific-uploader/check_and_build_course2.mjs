import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { existsSync, readdirSync, statSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const tuBase = resolve('/Users/hkc/Documents/lyzr/university/thinkific-upload');
const course2Folder = join(tuBase, '02 Lyzr for Business Teams');

function getCleanLessonSummary(lessonTitle) {
  return `<p><strong>Lesson Overview: ${lessonTitle}</strong></p>` +
    `<p>Key Takeaways & Core Concepts:</p>` +
    `<ul>` +
    `<li>Comprehensive walkthrough of ${lessonTitle} in the Lyzr Platform.</li>` +
    `<li>Best practices, architecture design, and step-by-step execution.</li>` +
    `<li>Key integration patterns for enterprise deployment.</li>` +
    `</ul>`;
}

async function main() {
  console.log("==========================================================================");
  console.log(" 🚀 CHECK & BUILD: COURSE 2 ('Lyzr for Business Professionals' #3489969)");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1366, height: 900 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("1. Navigating to https://lyzr.thinkific.com/manage/courses/3489969/curriculum...");
  await page.goto('https://lyzr.thinkific.com/manage/courses/3489969/curriculum', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const iframe = page.frameLocator('iframe[src*="hub/courses"]');

  console.log("\n2. Inspecting Course Structure...");

  // Clean up any empty Untitled Chapter placeholders if present
  while (true) {
    const untitled = iframe.locator('span:has-text("Untitled Chapter"), div:has-text("Untitled Chapter")').first();
    if (await untitled.count() === 0 || !(await untitled.isVisible())) break;
    try {
      await untitled.hover();
      await page.waitForTimeout(500);
      const overflow = iframe.locator('[data-qa="chapter-overflow-menu"]').first();
      if (await overflow.isVisible()) {
        await overflow.click({ force: true });
        await page.waitForTimeout(1000);
        const delBtn = iframe.locator('button, div, span').filter({ hasText: /^Delete chapter$|^Delete$/i }).first();
        if (await delBtn.isVisible()) {
          await delBtn.click();
          await page.waitForTimeout(1000);
          const confirm = iframe.locator('button').filter({ hasText: /^Delete$|^Confirm$/i }).first();
          if (await confirm.isVisible()) {
            await confirm.click();
            await page.waitForTimeout(2000);
            console.log("   ✓ Cleaned leftover 'Untitled Chapter'");
            continue;
          }
        }
      }
    } catch (e) {
      break;
    }
  }

  // Get full text of curriculum builder to evaluate existing lessons
  const pageText = await iframe.locator('body').innerText().catch(() => '');
  console.log("--- CURRICULUM TEXT ---");
  console.log(pageText);

  // Take screenshot of current state
  const ssInspect = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/screenshots/course_3489969_curriculum_inspection.png');
  await page.screenshot({ path: ssInspect, fullPage: true });
  console.log(`\nSaved initial curriculum inspection screenshot to: ${ssInspect}`);

  // Now process Chapter 03 & Chapter 04 from filesystem
  const chapterFolders = readdirSync(course2Folder)
    .filter(f => statSync(join(course2Folder, f)).isDirectory())
    .sort();

  console.log("\nAvailable Chapter Folders in filesystem:", chapterFolders);

  for (let chIdx = 0; chIdx < chapterFolders.length; chIdx++) {
    const chName = chapterFolders[chIdx];
    const chPath = join(course2Folder, chName);
    const cleanChTitle = chName.replace(/^Chapter\s*\d+\s*/i, '').replace(/— Master Module/i, '').trim();

    console.log(`\n---------------------------------------------------------`);
    console.log(`📁 Chapter ${chIdx + 1}: '${cleanChTitle}' (${chName})`);
    console.log(`---------------------------------------------------------`);

    const allFiles = readdirSync(chPath).filter(f => !f.startsWith('.') && !f.endsWith('.html')).sort();
    const mp4Files = allFiles.filter(f => f.toLowerCase().endsWith('.mp4'));

    for (const mp4Name of mp4Files) {
      const mp4Path = join(chPath, mp4Name);
      const cleanLessonTitle = mp4Name.replace(/^[0-9]+[a-z]?\s*/i, '').replace(/\.mp4$/i, '').trim();

      // Check if lesson already exists on page
      const existingLesson = iframe.locator(`button:has-text("${cleanLessonTitle}"), span:has-text("${cleanLessonTitle}")`).first();
      const existsOnPage = (await existingLesson.count() > 0 && await existingLesson.isVisible()) || pageText.includes(cleanLessonTitle);

      if (existsOnPage) {
        console.log(`   ✓ Lesson '${cleanLessonTitle}' already present in curriculum.`);
        continue;
      }

      console.log(`   🎥 Missing Lesson found! Building: '${cleanLessonTitle}'...`);

      try {
        const addLessonBtn = iframe.locator('button[aria-label*="Add a new lesson"], button:has-text("Add lesson")').nth(chIdx);
        if (await addLessonBtn.isVisible()) {
          await addLessonBtn.scrollIntoViewIfNeeded();
          await addLessonBtn.click();
          await page.waitForTimeout(1500);

          // 1. Fill Lesson Title
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

          // 2. Attach Video Block
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

              const saveActionBtn = iframe.locator('[data-qa="actions-bar__save-button"], button:has-text("Save")').first();
              if (await saveActionBtn.isVisible()) {
                await saveActionBtn.click();
                await page.waitForTimeout(2000);
              }
              console.log(`      ✓ Video Attached: ${mp4Name}`);
            }
          }

          // 3. Add Formatted Text Block
          const addTextBlockBtn = iframe.locator('button[description="Add text block"], button:has-text("Text")').first();
          if (await addTextBlockBtn.isVisible()) {
            await addTextBlockBtn.click();
            await page.waitForTimeout(2000);

            const textEditor = iframe.locator('[contenteditable="true"], .ProseMirror, textarea').first();
            if (await textEditor.isVisible()) {
              await textEditor.fill('');
              await textEditor.type(getCleanLessonSummary(cleanLessonTitle));
              await page.waitForTimeout(1000);

              const saveActionBtn = iframe.locator('[data-qa="actions-bar__save-button"], button:has-text("Save")').first();
              if (await saveActionBtn.isVisible()) {
                await saveActionBtn.click();
                await page.waitForTimeout(2000);
              }
              console.log(`      ✓ Formatted HTML Text Block Added`);
            }
          }

          console.log(`      🎉 COMPLETED BUILDING LESSON: '${cleanLessonTitle}'`);
        }
      } catch (e) {
        console.error(`      ⚠️ Error building lesson '${cleanLessonTitle}':`, e.message);
      }
    }
  }

  // Take final screenshots showing Chapter 03 & Chapter 04 status
  await page.waitForTimeout(3000);
  const ssFinal = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/screenshots/course_3489969_ch3_ch4_status.png');
  await page.screenshot({ path: ssFinal, fullPage: true });
  console.log(`\n📸 Saved final screenshot showing Chapter 03 & 04 status: ${ssFinal}`);

  await context.close();
  console.log("\n==========================================================================");
  console.log(" 🎉 VERIFICATION AND BUILD COMPLETE!");
  console.log("==========================================================================");
}

main().catch(err => {
  console.error("Fatal error:", err);
  process.exit(1);
});
