import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';
import { config, launchOpts } from './config.mjs';

const revampDir = '/Users/hkc/Documents/lyzr/university/revamp';
const videoFilename = 'C01_CH01_L01_introduction_to_lyzr_platform.mp4';
const videoPath = path.join(revampDir, videoFilename);
const thumbPath = path.join(revampDir, 'thumbnails', 'C01_CH01_L01_introduction_to_lyzr_platform.png');

const title = 'Foundation C1 L1 | Introduction to Lyzr Platform';
const description = `Course: Lyzr Foundations
Chapter: Lyzr Platform & Ecosystem Overview
Lesson: Introduction to Lyzr Platform

============================================================
📚 LESSON OVERVIEW & OBJECTIVES
============================================================
  • Understand the architecture of the Lyzr Agent Platform and its core building blocks.
  • Learn how Lyzr enables enterprise-grade AI automation with deterministic control and privacy.

============================================================
🔗 Important Links:
Build with Architect: https://hubs.ly/Q043pWTs0
Build your own AI agent → https://hubs.ly/Q03wb5Md0
Explore our website → https://hubs.ly/Q03wbGVt0
Build agents for your company (Book a demo) → https://hubs.ly/Q03wbH0k0
Learn how to build agents with Lyzr Academy → https://hubs.ly/Q03wqxFR0

============================================================
🏷️ HASHTAGS
============================================================
#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI`;

console.log("==========================================================================");
console.log(" 🧪 REDOING VIDEO 1 UPLOAD WITH EXPLICIT THUMBNAIL PNG SELECTION (V4)");
console.log("==========================================================================");

async function redoVideo1() {
  const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
  const page = ctx.pages()[0] || (await ctx.newPage());

  console.log("Navigating to YouTube Studio Dashboard...");
  await page.goto('https://studio.youtube.com/channel/UCzTVTxamWRuAYdNFwZnEO_g', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);

  try {
    console.log("Clicking Create / Upload videos button...");
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

    console.log("Uploading MP4 file...");
    const videoInput = page.locator('#select-files-button input[type="file"], input[type="file"]').first();
    await videoInput.setInputFiles(videoPath);
    console.log("  ✓ Video MP4 file uploaded. Processing details modal...");

    await page.waitForTimeout(8000);

    // Title
    const titleBox = page.locator('#textbox[contenteditable="true"]').nth(0);
    if (await titleBox.isVisible({ timeout: 15000 })) {
      await titleBox.click();
      await page.keyboard.press('Meta+A');
      await page.keyboard.press('Backspace');
      await titleBox.fill(title);
      console.log("  ✓ Title entered successfully.");
    }

    // Description
    const descBox = page.locator('#textbox[contenteditable="true"]').nth(1);
    if (await descBox.isVisible({ timeout: 5000 })) {
      await descBox.click();
      await page.keyboard.press('Meta+A');
      await page.keyboard.press('Backspace');
      await descBox.fill(description);
      console.log("  ✓ Description entered successfully.");
    }

    // Attach Custom Thumbnail PNG
    console.log("Attaching Custom Thumbnail PNG...");
    try {
      const fileInputs = page.locator('input[type="file"]');
      const count = await fileInputs.count();
      console.log(`  Total file inputs on page: ${count}`);

      let attached = false;
      for (let i = 0; i < count; i++) {
        const inp = fileInputs.nth(i);
        const id = await inp.getAttribute('id');
        const accept = await inp.getAttribute('accept');
        console.log(`  Input #${i}: id="${id}", accept="${accept}"`);
        if (id === 'file-loader' || (accept && accept.includes('image'))) {
          await inp.setInputFiles(thumbPath);
          console.log(`  🎨 Attached Custom Thumbnail PNG to input #${i}!`);
          attached = true;
          break;
        }
      }
      if (!attached && count > 1) {
        console.log("  Fallback: Setting file on second input element...");
        await fileInputs.nth(1).setInputFiles(thumbPath);
        console.log("  🎨 Attached Thumbnail PNG via fallback!");
      }
    } catch (te) {
      console.log(`  ⚠️ Thumbnail attachment warning: ${te.message}`);
    }

    await page.waitForTimeout(4000);

    // Audience (Not Made for Kids)
    const notForKids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"], ytcp-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
    if (await notForKids.first().isVisible({ timeout: 4000 })) {
      await notForKids.first().click();
      console.log("  ✓ Selected 'Not made for kids'.");
    }

    // Next Buttons
    for (let step = 1; step <= 3; step++) {
      await page.waitForTimeout(2500);
      const nextBtn = page.locator('ytcp-button#next-button, #next-button').first();
      if (await nextBtn.isVisible({ timeout: 5000 })) {
        await nextBtn.click();
        console.log(`  ✓ Clicked Next (Step ${step}).`);
      }
    }

    await page.waitForTimeout(2500);

    // Select Unlisted
    const unlistedRadio = page.locator('tp-yt-paper-radio-button[name="UNLISTED"], ytcp-radio-button[name="UNLISTED"]');
    if (await unlistedRadio.first().isVisible({ timeout: 4000 })) {
      await unlistedRadio.first().click();
      console.log("  ✓ Selected 'Unlisted' visibility.");
    }

    // Save
    await page.waitForTimeout(2000);
    const saveBtn = page.locator('ytcp-button#done-button, #done-button').first();
    await saveBtn.click();
    console.log("  🎉 Video 1 Published Successfully!");

    await page.waitForTimeout(6000);

    await page.screenshot({ path: '/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/redo_video_1_thumbnail_result.png' });
    console.log(" 📸 Verification screenshot saved to redo_video_1_thumbnail_result.png");

  } catch (err) {
    console.error(" ❌ Error during Video 1 redo:", err);
  } finally {
    await ctx.close();
  }
}

redoVideo1();
