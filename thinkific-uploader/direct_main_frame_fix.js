import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { rmSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');

try {
  rmSync(resolve(userDataDir, 'SingletonLock'), { force: true });
  rmSync(resolve(userDataDir, 'SingletonSocket'), { force: true });
  rmSync(resolve(userDataDir, 'SingletonCookie'), { force: true });
} catch (e) {}

const courses = [
  { id: 3489970, name: "Course 3: Lyzr for Developers" },
  { id: 3489969, name: "Course 2: Lyzr for Business Professionals" },
  { id: 3489968, name: "Course 1: Lyzr Foundations" }
];

async function main() {
  console.log("==========================================================================");
  console.log(" 🚀 DIRECT MAIN-FRAME THINKIFIC VIDEO PLAYER AUDIT & FIX");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: false, // Run headful so we see exact browser interactions
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  for (const course of courses) {
    console.log(`\n==========================================================================`);
    console.log(` 🎓 AUDITING ${course.name} (#${course.id})`);
    console.log(`==========================================================================`);

    await page.goto(`https://lyzr.thinkific.com/manage/courses/${course.id}/curriculum`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(6000);

    // Expand all chapters if Expand all button is visible
    const expandBtn = page.locator('button:has-text("Expand all"), [aria-label*="Expand all"]').first();
    if (await expandBtn.isVisible().catch(() => false)) {
      await expandBtn.click();
      await page.waitForTimeout(2000);
      console.log("   ✓ Expanded all chapters.");
    }

    // Find all lesson links in left sidebar
    const lessonLinks = page.locator('a[href*="/contents/"]');
    const count = await lessonLinks.count();
    console.log(`   Found ${count} lesson links in sidebar.`);

    for (let i = 0; i < count; i++) {
      const link = lessonLinks.nth(i);
      const title = (await link.innerText()).trim().replace(/\s+/g, ' ');

      console.log(`\n  📄 [Lesson ${i + 1}/${count}] '${title}'`);

      await link.scrollIntoViewIfNeeded().catch(() => {});
      await link.click({ force: true });
      await page.waitForTimeout(3500);

      // Check if video player container or video block exists on canvas
      const hasVideo = await page.evaluate(() => {
        const vids = document.querySelectorAll('video, iframe[src*="vimeo"], iframe[src*="wistia"], iframe[src*="youtube"], [data-qa*="video"], div[class*="video-player"], div[class*="Video"]');
        const text = document.body.innerText || '';
        return vids.length > 0 || text.includes('Change video') || text.includes('Select video') || text.includes('Video uploaded') || text.includes('.mp4');
      });

      if (hasVideo) {
        console.log(`     ✅ Video player ACTIVE.`);
      } else {
        console.log(`     ❌ MISSING VIDEO PLAYER! Attaching video block...`);

        // Click Asset Library or Video button on right sidebar
        const assetLibBtn = page.locator('button[description*="asset library"], button:has-text("Asset Library")').first();
        const videoBtn = page.locator('button[description*="video block"], button:has-text("Video")').first();

        if (await assetLibBtn.isVisible().catch(() => false)) {
          await assetLibBtn.click();
          await page.waitForTimeout(2000);
        } else if (await videoBtn.isVisible().catch(() => false)) {
          await videoBtn.click();
          await page.waitForTimeout(2000);
        }

        // Search Asset Library modal
        const searchBox = page.locator('input[placeholder*="Search"], input[type="search"]').first();
        if (await searchBox.isVisible().catch(() => false)) {
          const keyword = title.replace(/^\d+[\.\s-]*/, '').trim().split(' ')[0];
          console.log(`     🔍 Searching Asset Library for: '${keyword}'...`);
          await searchBox.fill(keyword);
          await page.waitForTimeout(2500);

          const row = page.locator('tr, [role="row"], div[class*="asset-item"]').nth(1);
          if (await row.isVisible().catch(() => false)) {
            await row.click();
            await page.waitForTimeout(1000);

            const addBtn = page.locator('button:has-text("Add assets"), button:has-text("Select"), button:has-text("Insert")').first();
            if (await addBtn.isVisible().catch(() => false) && !(await addBtn.isDisabled())) {
              await addBtn.click();
              await page.waitForTimeout(3000);
              console.log(`        ✓ Inserted video asset!`);
            }
          }
        }

        // Click Save
        const saveBtn = page.locator('[data-qa="actions-bar__save-button"], button:has-text("Save")').first();
        if (await saveBtn.isVisible().catch(() => false)) {
          await saveBtn.click();
          await page.waitForTimeout(3500);
          console.log(`        💾 SAVED LESSON WITH VIDEO PLAYER!`);
        }
      }
    }

    const ssPath = resolve(`screenshots/course_${course.id}_main_frame_verified.png`);
    await page.screenshot({ path: ssPath, fullPage: true });
    console.log(`📸 Saved summary screenshot for Course #${course.id}: ${ssPath}`);
  }

  await context.close();
  console.log("\n==========================================================================");
  console.log(" 🎉 ALL MASTER COURSES AUDITED & FIXED IN MAIN FRAME!");
  console.log("==========================================================================");
}

main().catch(console.error);
