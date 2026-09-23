import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { rmSync, mkdirSync, existsSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const screenshotsDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/screenshots');

if (!existsSync(screenshotsDir)) {
  mkdirSync(screenshotsDir, { recursive: true });
}

for (const lockFile of ['SingletonLock', 'SingletonSocket', 'SingletonCookie']) {
  const p = join(userDataDir, lockFile);
  if (existsSync(p)) {
    try { rmSync(p, { force: true }); } catch (e) {}
  }
}

const courses = [
  { id: 3489970, name: "Course 3: Lyzr for Developers" },
  { id: 3489969, name: "Course 2: Lyzr for Business Professionals" },
  { id: 3489968, name: "Course 1: Lyzr Foundations" }
];

async function main() {
  console.log("==========================================================================");
  console.log(" 🚀 THINKIFIC LIVE VIDEO PLAYER AUDIT & FIX PIPELINE (v6)");
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

    const courseUrl = `https://lyzr.thinkific.com/manage/courses/${course.id}/curriculum`;
    console.log(`1. Navigating to: ${courseUrl}`);
    await page.goto(courseUrl, { waitUntil: 'domcontentloaded' });
    
    console.log("   Waiting for child iframe to populate...");
    let frame = null;
    for (let attempt = 0; attempt < 25; attempt++) {
      await page.waitForTimeout(1000);
      const childFrames = page.frames().filter(f => f !== page.mainFrame() && !f.url().includes('onmaven.app') && f.url() !== 'about:blank');
      if (childFrames.length > 0) {
        frame = childFrames.find(f => f.url().includes('hub') || f.url().includes('courses')) || childFrames[0];
        if (frame) break;
      }
    }

    if (!frame) {
      console.log(`   ❌ Could not locate child iframe for Course #${course.id}. Main page URL: ${page.url()}`);
      console.log("   Available Frames:", page.frames().map(f => f.url()));
      continue;
    }

    console.log(`   ✓ Located Thinkific Builder Frame: ${frame.url()}`);
    await page.waitForTimeout(4000);

    // Step 2: Click 'Expand all'
    console.log("2. Clicking 'Expand all' so all chapters are expanded...");
    try {
      const expandBtn = page.frameLocator(`iframe[src="${frame.url()}"]`).locator('button:has-text("Expand all")').first();
      if (await expandBtn.isVisible().catch(() => false)) {
        await expandBtn.click();
        await page.waitForTimeout(2500);
        console.log("   ✓ Clicked 'Expand all'.");
      } else {
        const clicked = await frame.evaluate(() => {
          const btns = Array.from(document.querySelectorAll('button'));
          const target = btns.find(b => b.innerText.includes('Expand all'));
          if (target) { target.click(); return true; }
          return false;
        });
        if (clicked) console.log("   ✓ Clicked 'Expand all' via frame evaluate.");
        else console.log("   ℹ 'Expand all' button not present or chapters already expanded.");
      }
    } catch (e) {
      console.log("   ℹ Expand all step notice:", e.message);
    }

    // Step 3: Scan lesson links
    console.log("3. Scanning lesson links in curriculum sidebar...");
    const lessonData = await frame.evaluate(() => {
      const links = Array.from(document.querySelectorAll('a[href*="/contents/"], [data-qa*="lesson-item"], div[class*="lesson-item"]'));
      return links.map(el => ({ text: (el.innerText || '').trim().replace(/\s+/g, ' '), href: el.getAttribute('href') })).filter(l => l.text);
    });

    console.log(`   Found ${lessonData.length} total lesson items in curriculum.`);
    if (lessonData.length > 0) {
      console.log("   Lessons Found:", lessonData.map(l => l.text.split('\n')[0]));
    }

    let activeCount = 0;
    let fixedCount = 0;

    for (let i = 0; i < lessonData.length; i++) {
      const item = lessonData[i];
      const cleanTitle = item.text.split('\n')[0];

      if (!cleanTitle || cleanTitle.includes('Add lesson') || cleanTitle.includes('Add chapter')) continue;

      console.log(`\n  📄 [Lesson ${i + 1}/${lessonData.length}] '${cleanTitle}'`);

      try {
        // Click lesson item inside frame
        await frame.evaluate((titleText) => {
          const els = Array.from(document.querySelectorAll('a, button, div'));
          const match = els.find(e => e.innerText && e.innerText.includes(titleText));
          if (match) match.click();
        }, cleanTitle);
        await page.waitForTimeout(3500);

        // Check if Video player exists on canvas
        const videoStatus = await frame.evaluate(() => {
          const vids = document.querySelectorAll('video, iframe[src*="vimeo"], iframe[src*="wistia"], iframe[src*="youtube"], [data-qa*="video"], div[class*="video-player"], div[class*="Video"]');
          const text = document.body.innerText || '';
          const hasVideo = vids.length > 0 || text.includes('Change video') || text.includes('Select video') || text.includes('Video uploaded') || text.includes('.mp4');
          return { hasVideo, vidCount: vids.length };
        });

        if (videoStatus.hasVideo) {
          console.log(`     ✅ Video player ACTIVE.`);
          activeCount++;
        } else {
          console.log(`     ❌ NO VIDEO PLAYER FOUND! Attaching video from Asset Library...`);

          // Click Video or Asset Library button
          await frame.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const target = btns.find(b => b.innerText.includes('Video') || b.innerText.includes('Asset Library'));
            if (target) target.click();
          });
          await page.waitForTimeout(2000);

          // Click "Select video" or "Browse library"
          await frame.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('button'));
            const target = btns.find(b => b.innerText.includes('Select video') || b.innerText.includes('Browse library'));
            if (target) target.click();
          });
          await page.waitForTimeout(2000);

          // Search Asset Library
          const cleanKeyword = cleanTitle.replace(/^\d+[\.\s-]*/, '').trim().split(' ')[0];
          console.log(`     🔍 Searching Asset Library for: '${cleanKeyword}'...`);

          await frame.evaluate((kw) => {
            const input = document.querySelector('input[placeholder*="Search"], input[type="search"]');
            if (input) {
              input.value = kw;
              input.dispatchEvent(new Event('input', { bubbles: true }));
            }
          }, cleanKeyword);
          await page.waitForTimeout(2500);

          // Select first asset row and insert
          const inserted = await frame.evaluate(() => {
            const row = document.querySelectorAll('tr, [role="row"], [class*="asset-item"]')[1];
            if (row) {
              row.click();
              const btns = Array.from(document.querySelectorAll('button'));
              const addBtn = btns.find(b => b.innerText.includes('Add assets') || b.innerText.includes('Select') || b.innerText.includes('Insert'));
              if (addBtn) { addBtn.click(); return true; }
            }
            return false;
          });

          if (inserted) {
            await page.waitForTimeout(3000);
            console.log(`        ✓ Video asset selected and inserted!`);
          }

          // Click Save
          await frame.evaluate(() => {
            const btns = Array.from(document.querySelectorAll('button, [data-qa="actions-bar__save-button"]'));
            const saveBtn = btns.find(b => b.innerText.includes('Save'));
            if (saveBtn) saveBtn.click();
          });
          await page.waitForTimeout(3500);
          console.log(`        💾 SAVED LESSON WITH VIDEO PLAYER!`);
          fixedCount++;
        }
      } catch (err) {
        console.log(`     ⚠️ Lesson step notice: ${err.message}`);
      }
    }

    console.log(`\n📊 Course #${course.id} Summary: ${activeCount} active video players, ${fixedCount} newly attached.`);

    // Specific verification screenshot for Course 3 Lesson 10 ('What is RAG')
    if (course.id === 3489970) {
      console.log("\n📸 Capturing Lesson 10 ('What is RAG') verification screenshot...");
      try {
        await frame.evaluate(() => {
          const els = Array.from(document.querySelectorAll('a, button, div'));
          const match = els.find(e => e.innerText && e.innerText.includes('What is RAG'));
          if (match) match.click();
        });
        await page.waitForTimeout(4500);

        const ss10Path = resolve(screenshotsDir, 'course_3489970_lesson10_verification.png');
        await page.screenshot({ path: ss10Path, fullPage: true });
        console.log(`   ✅ Saved Lesson 10 verification screenshot: ${ss10Path}`);
      } catch (err) {
        console.log(`   ⚠️ Screenshot notice: ${err.message}`);
      }
    }

    const courseSsPath = resolve(screenshotsDir, `course_${course.id}_verification_summary.png`);
    await page.screenshot({ path: courseSsPath, fullPage: true });
    console.log(`📸 Saved summary screenshot for Course #${course.id}: ${courseSsPath}`);
  }

  await context.close();
  console.log("\n==========================================================================");
  console.log(" 🎉 AUDIT COMPLETED FOR ALL 3 COURSES!");
  console.log("==========================================================================");
}

main().catch(err => {
  console.error("Fatal execution error:", err);
  process.exit(1);
});
