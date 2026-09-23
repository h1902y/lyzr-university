import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { rmSync, mkdirSync, existsSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const brainDir = resolve('/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61');

for (const lockFile of ['SingletonLock', 'SingletonSocket', 'SingletonCookie']) {
  const p = resolve(userDataDir, lockFile);
  if (existsSync(p)) {
    try { rmSync(p, { force: true }); } catch (e) {}
  }
}

const courses = [
  { id: 3489968, name: "Course 1: Lyzr Foundations", code: "foundations" },
  { id: 3489969, name: "Course 2: Lyzr for Business Professionals", code: "business" },
  { id: 3489970, name: "Course 3: Lyzr for Developers", code: "developers" }
];

async function main() {
  console.log("==========================================================================");
  console.log(" 📸 CAPTURING LMS STUDENT PLAYER VIEWS FOR ALL 3 MASTER COURSES");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  for (const course of courses) {
    console.log(`\nNavigating to Course Builder Preview for ${course.name}...`);
    await page.goto(`https://lyzr.thinkific.com/manage/courses/${course.id}/curriculum`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(6000);

    const ssPath = resolve(brainDir, `lms_view_course_${course.id}.png`);
    await page.screenshot({ path: ssPath, fullPage: true });
    console.log(`📸 Saved LMS View Screenshot: ${ssPath}`);
  }

  await context.close();
  console.log("Done!");
}

main().catch(console.error);
