import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { config, launchOpts } from './config.mjs';

const jsonPath = '/Users/hkc/Documents/lyzr/university/revamp_upload_plan.json';

const args = process.argv.slice(2);
let startIndex = 0;
let limit = 15;

for (let i = 0; i < args.length; i++) {
  if (args[i] === '--start' && args[i + 1]) startIndex = parseInt(args[i + 1], 10);
  if (args[i] === '--limit' && args[i + 1]) limit = parseInt(args[i + 1], 10);
}

console.log("==========================================================================");
console.log(` 🚀 PLAYWRIGHT AUTOMATED YOUTUBE STUDIO UPLOADER (START: ${startIndex}, LIMIT: ${limit})`);
console.log("==========================================================================");

async function runUploader() {
  const planData = JSON.parse(fs.readFileSync(jsonPath, 'utf-8'));
  const itemsToUpload = planData.slice(startIndex, startIndex + limit);
  console.log(`Loaded ${itemsToUpload.length} videos to process.`);

  const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
  const page = ctx.pages()[0] || (await ctx.newPage());

  let uploadedCount = 0;

  for (let idx = 0; idx < itemsToUpload.length; idx++) {
    const item = itemsToUpload[idx];
    const { title, description, filepath, filename, exists, thumbnail_path } = item;

    if (!exists || !fs.existsSync(filepath)) {
      console.log(`⚠️ Video file not found: ${filepath}`);
      continue;
    }

    console.log(`\n======================================================`);
    console.log(`[${startIndex + idx + 1}/${planData.length}] Uploading via Playwright: ${title}`);
    console.log(`Video File:     ${filename} (${(fs.statSync(filepath).size / (1024*1024)).toFixed(1)} MB)`);
    console.log(`Thumbnail PNG:  ${thumbnail_path || 'None'}`);
    console.log(`======================================================`);

    try {
      // 1. Reset to clean Studio Dashboard to clear any open overlays/modals
      console.log("Navigating to clean Studio Dashboard...");
      await page.goto('https://studio.youtube.com/channel/UCzTVTxamWRuAYdNFwZnEO_g', { waitUntil: 'domcontentloaded', timeout: 60000 });
      await page.waitForTimeout(4000);

      // 2. Click Create / Upload Videos
      let uploadClicked = false;
      const createBtn = page.locator('#create-icon, ytcp-button#create-button, #create-button');
      if (await createBtn.first().isVisible({ timeout: 5000 })) {
        await createBtn.first().click();
        await page.waitForTimeout(1500);
        const uploadItem = page.locator('tp-yt-paper-item:has-text("Upload videos"), ytcp-text-menu-item:has-text("Upload videos")');
        if (await uploadItem.first().isVisible({ timeout: 3000 })) {
          await uploadItem.first().click();
          uploadClicked = true;
        }
      }

      if (!uploadClicked) {
        const uploadBtn = page.locator('#upload-icon, ytcp-button:has-text("Upload videos"), button:has-text("Upload videos")');
        if (await uploadBtn.first().isVisible({ timeout: 5000 })) {
          await uploadBtn.first().click();
          uploadClicked = true;
        }
      }

      await page.waitForTimeout(4000);

      // 3. Upload Video File
      const fileInput = page.locator('input[type="file"]').first();
      await fileInput.waitFor({ state: 'attached', timeout: 20000 });
      await fileInput.setInputFiles(filepath);
      console.log("  ✓ Video file uploaded to input. Processing details modal...");

      await page.waitForTimeout(8000);

      // 4. Fill Title
      const titleBox = page.locator('#textbox[contenteditable="true"]').nth(0);
      if (await titleBox.isVisible({ timeout: 15000 })) {
        await titleBox.click();
        await page.keyboard.press('Meta+A');
        await page.keyboard.press('Backspace');
        await titleBox.fill(title);
        console.log("  ✓ Title entered successfully.");
      }

      // 5. Fill Description
      const descBox = page.locator('#textbox[contenteditable="true"]').nth(1);
      if (await descBox.isVisible({ timeout: 5000 })) {
        await descBox.click();
        await page.keyboard.press('Meta+A');
        await page.keyboard.press('Backspace');
        await descBox.fill(description);
        console.log("  ✓ Description entered successfully.");
      }

      // 6. Attach Custom Thumbnail PNG
      if (thumbnail_path && fs.existsSync(thumbnail_path)) {
        try {
          const fileInputs = page.locator('input[type="file"]');
          const count = await fileInputs.count();
          let attached = false;
          for (let i = 0; i < count; i++) {
            const inp = fileInputs.nth(i);
            const id = await inp.getAttribute('id');
            const accept = await inp.getAttribute('accept');
            if (id === 'file-loader' || (accept && accept.includes('image'))) {
              await inp.setInputFiles(thumbnail_path);
              console.log(`  🎨 Custom Thumbnail PNG Attached Successfully!`);
              attached = true;
              break;
            }
          }
          if (!attached && count > 1) {
            await fileInputs.nth(1).setInputFiles(thumbnail_path);
            console.log("  🎨 Custom Thumbnail PNG Attached via fallback!");
          }
        } catch (te) {
          console.log(`  ⚠️ Thumbnail attachment warning: ${te.message}`);
        }
      }

      // 7. Select Audience (Not Made for Kids)
      const notForKids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"], ytcp-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
      if (await notForKids.first().isVisible({ timeout: 4000 })) {
        await notForKids.first().click();
        console.log("  ✓ Selected 'Not made for kids'.");
      }

      // 8. Robust Next Buttons (Elements -> Checks -> Visibility)
      for (let step = 1; step <= 3; step++) {
        await page.waitForTimeout(2500);
        const nextBtn = page.locator('ytcp-button#next-button, #next-button').first();
        if (await nextBtn.isVisible({ timeout: 5000 })) {
          await nextBtn.click();
          console.log(`  ✓ Clicked Next (Step ${step}).`);
        }
      }

      await page.waitForTimeout(2500);

      // 9. Select Unlisted Visibility
      const unlistedRadio = page.locator('tp-yt-paper-radio-button[name="UNLISTED"], ytcp-radio-button[name="UNLISTED"]');
      if (await unlistedRadio.first().isVisible({ timeout: 4000 })) {
        await unlistedRadio.first().click();
        console.log("  ✓ Selected 'Unlisted' visibility.");
      }

      // 10. Publish / Save
      await page.waitForTimeout(2000);
      const saveBtn = page.locator('ytcp-button#done-button, #done-button').first();
      await saveBtn.click();
      console.log("  🎉 Video Published Successfully!");

      uploadedCount++;
      await page.waitForTimeout(6000);

    } catch (err) {
      console.error(`  ❌ Error uploading ${title}:`, err.message);
    }
  }

  console.log(`\n======================================================`);
  console.log(` 🎉 Batch Upload Complete! (${uploadedCount}/${itemsToUpload.length} uploaded)`);
  console.log(`======================================================`);

  await ctx.close();
}

runUploader();
