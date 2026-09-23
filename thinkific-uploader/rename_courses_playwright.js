import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { rmSync, existsSync, writeFileSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const brainDir = resolve('/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61');

for (const lockFile of ['SingletonLock', 'SingletonSocket', 'SingletonCookie']) {
  const p = resolve(userDataDir, lockFile);
  if (existsSync(p)) {
    try { rmSync(p, { force: true }); } catch (e) {}
  }
}

const courseRenames = [
  { id: 3489968, name: "Lyzr Foundations" },
  { id: 3489969, name: "Lyzr for Business Professionals" },
  { id: 3490173, name: "Lyzr for Business Professionals" },
  { id: 3489970, name: "Lyzr for Technical Professionals" }
];

async function main() {
  console.log("==========================================================================");
  console.log(" ✏️ RENAMING MASTER COURSES IN THINKIFIC CREATOR HUB");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  for (const course of courseRenames) {
    console.log(`\nNavigating to Course #${course.id} settings...`);
    await page.goto(`https://lyzr.thinkific.com/manage/courses/${course.id}/settings`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(4000);

    const titleInput = page.locator('input[name*="title"], input[name*="name"], input[id*="title"]').first();
    if (await titleInput.isVisible().catch(() => false)) {
      await titleInput.fill(course.name);
      console.log(`Filled title: '${course.name}'`);
      
      const saveBtn = page.locator('button:has-text("Save"), input[type="submit"][value*="Save"]').first();
      if (await saveBtn.isVisible().catch(() => false)) {
        await saveBtn.click();
        await page.waitForTimeout(3000);
        console.log(`Saved Course #${course.id}`);
      }
    } else {
      console.log(`Title input not directly found for #${course.id}, checking iframe...`);
      const iframeLoc = page.frameLocator('iframe[src*="courses"], iframe[src*="hub"]').first();
      const frameInput = iframeLoc.locator('input[name*="title"], input[name*="name"]').first();
      if (await frameInput.isVisible().catch(() => false)) {
        await frameInput.fill(course.name);
        const frameSave = iframeLoc.locator('button:has-text("Save")').first();
        if (await frameSave.isVisible().catch(() => false)) {
          await frameSave.click();
          await page.waitForTimeout(3000);
          console.log(`Saved inside frame for Course #${course.id}`);
        }
      }
    }
  }

  const ssPath = resolve(brainDir, 'master_courses_renamed_confirmation.png');
  await page.screenshot({ path: ssPath, fullPage: true });
  console.log(`\n📸 Saved screenshot: ${ssPath}`);

  await context.close();
}

main().catch(console.error);
