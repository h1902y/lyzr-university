import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { existsSync } from 'node:fs';

const userDataDir = resolve('.browser-profile');
const draftIds = [3489968, 3489969, 3489970];

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
  console.log(" DELETING EMPTY 'UNTITLED CHAPTER' PLACEHOLDERS ACROSS DRAFT COURSES");
  console.log("==========================================================================");

  for (const cid of draftIds) {
    console.log(`\n---------------------------------------------------------`);
    console.log(`Cleaning empty chapters in Course #${cid}...`);
    await page.goto(`https://lyzr.thinkific.com/manage/courses/${cid}/curriculum`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(6000);

    const iframe = page.frameLocator('iframe[src*="hub/courses"]');

    let deletedCount = 0;
    while (true) {
      // Find all 'Untitled Chapter' text elements
      const untitledEl = iframe.locator('span:has-text("Untitled Chapter"), div:has-text("Untitled Chapter")').first();
      if (await untitledEl.count() === 0 || !(await untitledEl.isVisible())) {
        break;
      }

      try {
        // Hover over the untitled chapter text to reveal overflow menu
        await untitledEl.hover();
        await page.waitForTimeout(500);

        // Find chapter container
        const parentCard = iframe.locator('div[class*="chapter"]').filter({ has: untitledEl }).first();
        const overflowMenu = parentCard.locator('[data-qa="chapter-overflow-menu"], button[aria-label*="actions"]').first();
        
        if (await overflowMenu.count() > 0) {
          await overflowMenu.click({ force: true });
          await page.waitForTimeout(1000);

          const deleteBtn = iframe.locator('button, div, span').filter({ hasText: /^Delete chapter$|^Delete$/i }).first();
          if (await deleteBtn.isVisible()) {
            await deleteBtn.click();
            await page.waitForTimeout(1500);

            const confirmBtn = iframe.locator('button').filter({ hasText: /^Delete$|^Confirm$/i }).first();
            if (await confirmBtn.isVisible()) {
              await confirmBtn.click();
              await page.waitForTimeout(2000);
              deletedCount++;
              console.log(`  ✓ Deleted Untitled Chapter #${deletedCount}`);
              continue;
            }
          }
        }
      } catch (err) {
        console.log(`  Break or note: ${err.message}`);
        break;
      }
    }

    console.log(`🎉 Finished cleaning Course #${cid}! Total deleted: ${deletedCount}`);
  }

  await context.close();
  console.log('\n=========================================================');
  console.log(' 🎉 ALL EMPTY PLACEHOLDER CHAPTERS DELETED!');
  console.log('=========================================================');
}

main();
