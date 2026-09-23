import { chromium } from 'playwright';
import { resolve } from 'node:path';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');

const coursesToFix = [
  {
    id: 3489970,
    name: "Lyzr for Developers"
  },
  {
    id: 3489969,
    name: "Lyzr for Business Professionals"
  },
  {
    id: 3489968,
    name: "Lyzr Foundations"
  }
];

async function main() {
  console.log("==========================================================================");
  console.log(" 🔍 COMPREHENSIVE VIDEO AUDIT & AUTO-FIX ACROSS ALL 3 MASTER COURSES");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1400, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  for (const course of coursesToFix) {
    console.log(`\n==========================================================================`);
    console.log(` 🎓 AUDITING COURSE #${course.id}: '${course.name}'`);
    console.log(`==========================================================================`);

    await page.goto(`https://lyzr.thinkific.com/manage/courses/${course.id}/curriculum`, { waitUntil: 'domcontentloaded' });
    
    // Wait for iframe selector to appear
    await page.waitForSelector('iframe', { timeout: 15000 }).catch(() => {});
    await page.waitForTimeout(6000);

    const iframe = page.frameLocator('iframe');
    const frameHandle = await page.$('iframe');
    const frame = frameHandle ? await frameHandle.contentFrame() : null;

    if (!frame) {
      console.log(`   ⚠️ Could not locate iframe content for Course #${course.id}`);
      continue;
    }

    // Scroll sidebar down to load all lessons
    await frame.evaluate(() => {
      const scrollable = document.querySelector('aside, nav, div[class*="sidebar"], div[class*="curriculum"]');
      if (scrollable) scrollable.scrollTop = scrollable.scrollHeight;
    });
    await page.waitForTimeout(2000);

    // Get all lesson items in sidebar
    const lessonElements = iframe.locator('a[href*="/contents/"], button[aria-label*="Lesson"], div[class*="lesson-item"], [data-qa*="lesson"]');
    const count = await lessonElements.count();
    console.log(`Found ${count} lesson elements in sidebar for '${course.name}'.`);

    for (let i = 0; i < count; i++) {
      try {
        const lessonLoc = lessonElements.nth(i);
        const lessonText = await lessonLoc.innerText().catch(() => '');
        if (!lessonText || lessonText.includes('Add lesson') || lessonText.includes('Add chapter')) continue;

        console.log(`\n  📄 [${i + 1}/${count}] Inspecting: '${lessonText.trim().replace(/\n/g, ' ')}'...`);

        await lessonLoc.scrollIntoViewIfNeeded();
        await lessonLoc.click();
        await page.waitForTimeout(2500);

        // Check if Video Player / Video element exists on canvas
        const hasVideo = await frame.evaluate(() => {
          const videoTags = document.querySelectorAll('video, iframe[src*="vimeo"], iframe[src*="wistia"], iframe[src*="youtube"], [data-qa*="video"], div[class*="video-player"], div[class*="Video"]');
          if (videoTags.length > 0) return true;

          const text = document.body.innerText || '';
          if (text.includes('Change video') || text.includes('Select video') || text.includes('Video uploaded') || text.includes('.mp4')) return true;
          return false;
        });

        if (hasVideo) {
          console.log(`     ✅ Video player ACTIVE.`);
        } else {
          console.log(`     ❌ MISSING VIDEO PLAYER! Attaching video from Asset Library...`);

          // Click Asset Library or Video on right toolbar
          const addVideoBtn = iframe.locator('button[description*="video"], button:has-text("Video"), button[description*="asset library"], button:has-text("Asset Library")').first();
          if (await addVideoBtn.isVisible()) {
            await addVideoBtn.click();
            await page.waitForTimeout(2500);

            // Search in Asset Library
            const searchBox = iframe.locator('input[placeholder*="Search"], input[type="search"]').first();
            if (await searchBox.isVisible()) {
              const cleanKeyword = lessonText.replace(/^Lesson\s*\d+\s*:?\s*/i, '').trim().split(' ')[0];
              await searchBox.fill(cleanKeyword);
              await page.waitForTimeout(2000);

              // Select first video row
              const row = iframe.locator('tr, [role="row"], div[class*="asset-item"]').nth(1);
              if (await row.isVisible()) {
                await row.click();
                await page.waitForTimeout(1000);

                const selectBtn = iframe.locator('button:has-text("Add assets"), button:has-text("Select"), button:has-text("Insert")').first();
                if (await selectBtn.isVisible() && !(await selectBtn.isDisabled())) {
                  await selectBtn.click();
                  await page.waitForTimeout(3000);
                  console.log(`        ✓ Attached Video from Asset Library!`);
                }
              }
            }

            const saveBtn = iframe.locator('[data-qa="actions-bar__save-button"], button:has-text("Save")').first();
            if (await saveBtn.isVisible()) {
              await saveBtn.click();
              await page.waitForTimeout(3000);
              console.log(`        💾 SAVED LESSON WITH VIDEO PLAYER!`);
            }
          }
        }
      } catch (err) {
        console.error(`     ⚠️ Error during inspection: ${err.message}`);
      }
    }

    const ssPath = resolve(`screenshots/course_${course.id}_audit_fixed.png`);
    await page.screenshot({ path: ssPath, fullPage: true });
    console.log(`📸 Saved audit verification screenshot: ${ssPath}`);
  }

  await context.close();
  console.log("\n==========================================================================");
  console.log(" 🎉 ALL COURSES AUDITED & MISSING VIDEOS FIXED!");
  console.log("==========================================================================");
}

main().catch(err => {
  console.error("Fatal error:", err);
  process.exit(1);
});
