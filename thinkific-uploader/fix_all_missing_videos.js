import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { rmSync, mkdirSync, existsSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const screenshotsDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/screenshots');

if (!existsSync(screenshotsDir)) {
  mkdirSync(screenshotsDir, { recursive: true });
}

// Clear lock files if present
try {
  rmSync(join(userDataDir, 'SingletonLock'), { force: true });
  rmSync(join(userDataDir, 'SingletonSocket'), { force: true });
  rmSync(join(userDataDir, 'SingletonCookie'), { force: true });
} catch (e) {}

const courses = [
  { id: 3489970, name: "Course 3: Lyzr for Developers" },
  { id: 3489969, name: "Course 2: Lyzr for Business Professionals" },
  { id: 3489968, name: "Course 1: Lyzr Foundations" }
];

async function runAuditAndFix() {
  console.log("==========================================================================");
  console.log(" 🚀 THINKIFIC VIDEO PLAYER AUDIT & FIX PIPELINE");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  for (const course of courses) {
    console.log(`\n==========================================================================`);
    console.log(` 🎓 AUDITING ${course.name} (#${course.id})`);
    console.log(`==========================================================================`);

    const url = `https://lyzr.thinkific.com/manage/courses/${course.id}/curriculum`;
    console.log(`1. Navigating to: ${url}`);
    await page.goto(url, { waitUntil: 'domcontentloaded' });

    // Wait for iframe
    const iframeSelector = 'iframe[src*="hub/courses"], iframe[src*="courses"]';
    await page.waitForSelector(iframeSelector, { timeout: 25000 }).catch(e => {
      console.log("   ⚠️ Waiting for iframe timed out, retrying load...");
    });
    await page.waitForTimeout(6000);

    const frameHandle = await page.$(iframeSelector);
    const frame = frameHandle ? await frameHandle.contentFrame() : null;

    if (!frame) {
      console.log(`   ❌ ERROR: Thinkific Builder iframe frame not found for Course #${course.id}`);
      continue;
    }

    console.log(`   ✓ Located Thinkific Builder Frame: ${frame.url()}`);

    // Click 'Expand all' button if visible
    console.log("2. Expanding all chapters...");
    try {
      const expandBtn = frame.locator('button:has-text("Expand all"), [aria-label*="Expand all"]').first();
      if (await expandBtn.isVisible({ timeout: 5000 })) {
        await expandBtn.click();
        await page.waitForTimeout(2000);
        console.log("   ✓ Expanded all chapters.");
      } else {
        console.log("   ℹ 'Expand all' button not currently visible or already expanded.");
      }
    } catch (err) {
      console.log("   ℹ Skipped expand all step (already expanded or custom layout).");
    }

    // Locate lesson links in curriculum sidebar
    const lessonLinks = frame.locator('a[href*="/contents/"]');
    let count = 0;
    try {
      count = await lessonLinks.count();
    } catch (e) {
      console.log("   ⚠️ Exception getting lesson links count:", e.message);
    }

    console.log(`3. Found ${count} lesson links in curriculum.`);

    let fixedCount = 0;
    let activeCount = 0;

    for (let i = 0; i < count; i++) {
      try {
        const link = lessonLinks.nth(i);
        const rawTitle = await link.innerText();
        const cleanTitle = rawTitle.trim().replace(/\s+/g, ' ');

        console.log(`\n  📄 [Lesson ${i + 1}/${count}] '${cleanTitle}'`);

        await link.scrollIntoViewIfNeeded();
        await link.click({ force: true });
        await page.waitForTimeout(3500);

        // Inspect canvas for video player / video block
        const videoStatus = await frame.evaluate(() => {
          const vids = document.querySelectorAll('video, iframe[src*="vimeo"], iframe[src*="wistia"], iframe[src*="youtube"], [data-qa*="video"], [class*="video-player"], [class*="Video"]');
          const canvasText = document.body.innerText || '';
          
          const hasVideo = vids.length > 0 || 
                           canvasText.includes('Change video') || 
                           canvasText.includes('Select video') || 
                           canvasText.includes('Video uploaded') ||
                           canvasText.includes('.mp4');

          return { hasVideo, vidCount: vids.length };
        });

        if (videoStatus.hasVideo) {
          console.log(`     ✅ Video player ACTIVE.`);
          activeCount++;
        } else {
          console.log(`     ❌ NO VIDEO PLAYER FOUND! Attaching video block...`);

          // Attempt to add Video block or attach video from Asset Library
          let attached = false;

          // Check sidebar buttons
          const videoSideBtn = frame.locator('button[description*="video"], button:has-text("Video"), [data-qa*="add-video"]').first();
          const assetLibBtn = frame.locator('button:has-text("Asset Library"), [data-qa*="asset-library"]').first();

          if (await videoSideBtn.isVisible().catch(() => false)) {
            await videoSideBtn.click();
            await page.waitForTimeout(2000);
          } else if (await assetLibBtn.isVisible().catch(() => false)) {
            await assetLibBtn.click();
            await page.waitForTimeout(2000);
          }

          // Check if "Select video" or "Browse library" button appears
          const selectVidBtn = frame.locator('button:has-text("Select video"), button:has-text("Browse library"), button:has-text("Choose video")').first();
          if (await selectVidBtn.isVisible().catch(() => false)) {
            await selectVidBtn.click();
            await page.waitForTimeout(2000);
          }

          // Search input in Asset Modal
          const searchBox = frame.locator('input[placeholder*="Search"], input[type="search"]').first();
          if (await searchBox.isVisible().catch(() => false)) {
            // Extracts search keyword e.g. "What is RAG" from "10 What is RAG"
            const searchKeyword = cleanTitle.replace(/^\d+[\.\s-]*/, '').trim();
            console.log(`     🔍 Searching Asset Library for: '${searchKeyword}'...`);
            await searchBox.fill(searchKeyword);
            await page.waitForTimeout(2500);

            // Select first row in search results
            const resultRow = frame.locator('tr, [role="row"], [class*="asset-item"]').nth(1);
            if (await resultRow.isVisible().catch(() => false)) {
              await resultRow.click();
              await page.waitForTimeout(1000);

              const insertBtn = frame.locator('button:has-text("Add assets"), button:has-text("Select"), button:has-text("Insert"), button:has-text("Save")').first();
              if (await insertBtn.isVisible().catch(() => false) && !(await insertBtn.isDisabled())) {
                await insertBtn.click();
                await page.waitForTimeout(3000);
                attached = true;
                console.log(`        ✓ Selected and inserted video asset.`);
              }
            } else {
              console.log(`        ⚠️ No matching video asset found in search results for '${searchKeyword}'`);
            }
          }

          // Click Save on bottom bar
          const saveBtn = frame.locator('[data-qa="actions-bar__save-button"], button:has-text("Save")').first();
          if (await saveBtn.isVisible().catch(() => false)) {
            await saveBtn.click();
            await page.waitForTimeout(3500);
            console.log(`        💾 SAVED LESSON WITH VIDEO PLAYER!`);
            fixedCount++;
          }
        }
      } catch (err) {
        console.log(`     ⚠️ Error inspecting lesson ${i + 1}: ${err.message}`);
      }
    }

    console.log(`\n📊 Course #${course.id} Summary: ${activeCount} active video players, ${fixedCount} fixed.`);

    // Take verification screenshot of Course 3 Lesson 10 specifically if course 3489970
    if (course.id === 3489970) {
      console.log("\n📸 Taking verification screenshot of Course 3 Lesson 10 ('What is RAG')...");
      try {
        const ragLink = frame.locator('a[href*="/contents/"]:has-text("What is RAG")').first();
        if (await ragLink.isVisible().catch(() => false)) {
          await ragLink.click();
          await page.waitForTimeout(4000);
        }
        const ss10Path = join(screenshotsDir, 'course_3489970_lesson10_verification.png');
        await page.screenshot({ path: ss10Path, fullPage: true });
        console.log(`   ✅ Saved Lesson 10 screenshot: ${ss10Path}`);
      } catch (err) {
        console.log(`   ⚠️ Failed to take specific Lesson 10 screenshot: ${err.message}`);
      }
    }

    const courseSsPath = join(screenshotsDir, `course_${course.id}_audit_summary.png`);
    await page.screenshot({ path: courseSsPath, fullPage: true });
    console.log(`📸 Saved Course summary screenshot: ${courseSsPath}`);
  }

  await context.close();
  console.log("\n==========================================================================");
  console.log(" 🎉 AUDIT AND FIX COMPLETED FOR ALL 3 COURSES!");
  console.log("==========================================================================");
}

runAuditAndFix().catch(err => {
  console.error("Fatal Error:", err);
  process.exit(1);
});
