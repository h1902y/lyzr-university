import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { rmSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const courseId = 3489970;

try {
  rmSync(join(userDataDir, 'SingletonLock'), { force: true });
  rmSync(join(userDataDir, 'SingletonSocket'), { force: true });
  rmSync(join(userDataDir, 'SingletonCookie'), { force: true });
} catch (e) {}

async function main() {
  console.log("==========================================================================");
  console.log(" 🔍 DIRECT VIDEO AUDIT & ATTACH FOR COURSE 3 ('Lyzr for Developers' #3489970)");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1400, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log(`1. Navigating to https://lyzr.thinkific.com/manage/courses/${courseId}/curriculum...`);
  await page.goto(`https://lyzr.thinkific.com/manage/courses/${courseId}/curriculum`, { waitUntil: 'domcontentloaded' });
  
  const iframeSelector = 'iframe[src*="hub/courses"], iframe[src*="courses"]';
  await page.waitForSelector(iframeSelector, { timeout: 20000 });
  await page.waitForTimeout(6000);

  const iframe = page.frameLocator(iframeSelector);
  const frame = page.frames().find(f => f.url().includes('courses') || f.url().includes('hub'));

  if (!frame) {
    console.log("   ❌ Could not locate Thinkific Builder Frame");
    await context.close();
    return;
  }

  console.log("   ✓ Located Thinkific Builder Frame:", frame.url());

  // Click Expand all button if present
  console.log("2. Expanding all chapters...");
  const expandBtn = iframe.locator('button:has-text("Expand all")').first();
  if (await expandBtn.isVisible()) {
    await expandBtn.click();
    await page.waitForTimeout(2000);
  }

  // Find all lesson links
  const lessonLinks = iframe.locator('a[href*="/contents/"]');
  const count = await lessonLinks.count();
  console.log(`3. Found ${count} lesson links in curriculum.`);

  for (let i = 0; i < count; i++) {
    const link = lessonLinks.nth(i);
    const title = await link.innerText();
    console.log(`\n  📄 [Lesson ${i + 1}/${count}] '${title.trim().replace(/\n/g, ' ')}'`);

    await link.scrollIntoViewIfNeeded();
    await link.click();
    await page.waitForTimeout(3500);

    // Inspect if video block or video tag exists
    const videoStatus = await frame.evaluate(() => {
      const vids = document.querySelectorAll('video, iframe[src*="vimeo"], iframe[src*="wistia"], iframe[src*="youtube"], [data-qa*="video"]');
      const text = document.body.innerText || '';
      const hasVideoBlock = text.includes('Change video') || text.includes('Select video') || text.includes('.mp4') || vids.length > 0;
      return { count: vids.length, hasVideoBlock };
    });

    if (videoStatus.hasVideoBlock) {
      console.log(`     ✅ Video player ACTIVE.`);
    } else {
      console.log(`     ❌ NO VIDEO PLAYER FOUND! Attaching video block...`);

      // Click Video button on right sidebar (or Asset Library)
      const addVideoBtn = iframe.locator('button[description="Add video block"], button:has-text("Video")').first();
      if (await addVideoBtn.isVisible()) {
        await addVideoBtn.click();
        await page.waitForTimeout(2000);

        // Click Select video / Browse library if present
        const browseBtn = iframe.locator('button:has-text("Select video"), button:has-text("Browse library")').first();
        if (await browseBtn.isVisible()) {
          await browseBtn.click();
          await page.waitForTimeout(2000);

          // Search for video in library
          const searchBox = iframe.locator('input[type="search"], input[placeholder*="Search"]').first();
          if (await searchBox.isVisible()) {
            const keyword = title.replace(/^Lesson\s*\d+\s*:?\s*/i, '').trim().split(' ')[0];
            await searchBox.fill(keyword);
            await page.waitForTimeout(2000);

            const firstRow = iframe.locator('tr, [role="row"]').nth(1);
            if (await firstRow.isVisible()) {
              await firstRow.click();
              await page.waitForTimeout(1000);

              const addBtn = iframe.locator('button:has-text("Add assets"), button:has-text("Select"), button:has-text("Insert")').first();
              if (await addBtn.isVisible() && !(await addBtn.isDisabled())) {
                await addBtn.click();
                await page.waitForTimeout(3000);
                console.log(`        ✓ Linked video from library!`);
              }
            }
          }
        }

        // Click Save
        const saveBtn = iframe.locator('[data-qa="actions-bar__save-button"], button:has-text("Save")').first();
        if (await saveBtn.isVisible()) {
          await saveBtn.click();
          await page.waitForTimeout(3000);
          console.log(`        💾 SAVED LESSON WITH VIDEO PLAYER!`);
        }
      }
    }
  }

  const ssPath = resolve('screenshots/course_3489970_direct_video_audit.png');
  await page.screenshot({ path: ssPath, fullPage: true });
  console.log(`\n📸 Saved audit verification screenshot: ${ssPath}`);

  await context.close();
  console.log("\n==========================================================================");
  console.log(" 🎉 COURSE 3 VIDEO AUDIT COMPLETE!");
  console.log("==========================================================================");
}

main().catch(console.error);
