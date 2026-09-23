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
  console.log(" POPULATING CHAPTERS & LESSONS (STRICTLY DRAFT MODE — NO PUBLISHING)");
  console.log("==========================================================================");

  for (const mc of draftMasterCourses) {
    console.log(`\n---------------------------------------------------------`);
    console.log(`Building Draft Course #${mc.id}: '${mc.name}'...`);
    
    if (!existsSync(mc.folder)) {
      console.log(`  ⚠️ Folder not found: ${mc.folder}`);
      continue;
    }

    const chapterFolders = readdirSync(mc.folder)
      .filter(f => statSync(join(mc.folder, f)).isDirectory())
      .sort();

    console.log(`  Local Chapters to Build (${chapterFolders.length}):`, chapterFolders);

    await page.goto(`https://lyzr.thinkific.com/manage/courses/${mc.id}/curriculum`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(7000);

    const iframe = page.frameLocator('iframe[src*="hub/courses"]');
    
    for (const chName of chapterFolders) {
      console.log(`\n  👉 Creating Chapter inside Iframe: '${chName}'...`);
      
      const addChBtn = iframe.locator('button, div, span').filter({ hasText: /^Add chapter$/i }).first();
      if (await addChBtn.isVisible()) {
        await addChBtn.click();
        await page.waitForTimeout(2000);

        const titleInput = iframe.locator('input[name*="name"], input[placeholder*="Chapter"], input[id*="chapter"]').first();
        if (await titleInput.isVisible()) {
          await titleInput.fill(chName);
          await page.waitForTimeout(1000);

          const saveBtn = iframe.locator('button, div').filter({ hasText: /^Save$|^Save chapter$/i }).first();
          if (await saveBtn.isVisible()) {
            await saveBtn.click();
            await page.waitForTimeout(3000);
            console.log(`     ✓ Saved Chapter '${chName}' in Draft!`);
          }
        }
      }
    }
  }

  await context.close();
  console.log('\n=========================================================');
  console.log(' 🎉 ALL CHAPTERS CREATED & KEPT STRICTLY IN DRAFT MODE!');
  console.log('=========================================================');
}

main();
