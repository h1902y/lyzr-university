import { chromium } from 'playwright';
import path from 'path';
import fs from 'fs';
import { config, launchOpts } from './config.mjs';

const revampDir = '/Users/hkc/Documents/lyzr/university/revamp';
const videoFilename = 'C01_CH01_L01_introduction_to_lyzr_platform.mp4';
const videoPath = path.join(revampDir, videoFilename);

const title = 'Introduction to Lyzr Platform — Lyzr Foundations';
const description = `Course: Lyzr Foundations
Chapter: Lyzr Platform & Ecosystem Overview
Lesson: Introduction to Lyzr Platform

============================================================
📚 LESSON OVERVIEW & OBJECTIVES
============================================================
  • Understand the architecture of the Lyzr Agent Platform and its core building blocks.
  • Learn how Lyzr enables enterprise-grade AI automation with deterministic control and privacy.

============================================================
🔗 USEFUL LYZR RESOURCES & LINKS
============================================================
🌐 Lyzr Enterprise Agent Platform: https://lyzr.ai
📖 Official Lyzr Documentation:  https://docs.lyzr.ai
💻 Lyzr ADK Python SDK (GitHub): https://github.com/LyzrCore/lyzr-core
🚀 Lyzr Agent Studio:             https://studio.lyzr.ai

============================================================
🏷️ HASHTAGS
============================================================
#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI`;

console.log("==========================================================================");
console.log(" 🧪 TESTING 1-VIDEO AUTOMATED UPLOAD VIA PLAYWRIGHT BROWSER (V2)");
console.log("==========================================================================");
console.log(`Video File: ${videoFilename} (${(fs.statSync(videoPath).size / (1024*1024)).toFixed(1)} MB)`);
console.log(`Title:      ${title}\n`);

async function testSingleUpload() {
  const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
  const page = ctx.pages()[0] || (await ctx.newPage());

  console.log("Navigating to YouTube Studio Dashboard...");
  await page.goto('https://studio.youtube.com/channel/UCzTVTxamWRuAYdNFwZnEO_g', { waitUntil: 'domcontentloaded', timeout: 60000 });
  await page.waitForTimeout(5000);

  console.log(`Current Studio URL: ${page.url()}`);
  console.log(`Current Page Title: ${await page.title()}`);

  try {
    // Look for Upload Videos button or Create button
    console.log("Locating Upload button on YouTube Studio...");
    
    let uploadClicked = false;
    const createBtn = page.locator('#create-icon, ytcp-button#create-button, #create-button');
    if (await createBtn.first().isVisible({ timeout: 5000 })) {
      console.log("  ✓ Found Create button. Clicking...");
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
        console.log("  ✓ Found Upload videos button. Clicking...");
        await uploadBtn.first().click();
        uploadClicked = true;
      }
    }

    await page.waitForTimeout(4000);

    // Wait for file input inside upload dialog
    console.log("Waiting for file input dialog...");
    const fileInput = page.locator('input[type="file"]');
    await fileInput.waitFor({ state: 'attached', timeout: 20000 });
    
    console.log("Selecting video MP4 file in input...");
    await fileInput.setInputFiles(videoPath);
    console.log("  ✓ Video file uploaded to input. Waiting for details modal...");

    await page.waitForTimeout(8000);

    // Title Field
    console.log("Entering Video Title...");
    const titleBox = page.locator('#textbox[contenteditable="true"]').nth(0);
    if (await titleBox.isVisible({ timeout: 15000 })) {
      await titleBox.click();
      await page.keyboard.press('Meta+A');
      await page.keyboard.press('Backspace');
      await titleBox.fill(title);
      console.log("  ✓ Title entered successfully.");
    }

    // Description Field
    console.log("Entering Video Description...");
    const descBox = page.locator('#textbox[contenteditable="true"]').nth(1);
    if (await descBox.isVisible({ timeout: 5000 })) {
      await descBox.click();
      await page.keyboard.press('Meta+A');
      await page.keyboard.press('Backspace');
      await descBox.fill(description);
      console.log("  ✓ Description entered successfully.");
    }

    // Made for Kids (NOT MFK)
    console.log("Setting Audience (Not Made for Kids)...");
    const notForKids = page.locator('tp-yt-paper-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"], ytcp-radio-button[name="VIDEO_MADE_FOR_KIDS_NOT_MFK"]');
    if (await notForKids.first().isVisible({ timeout: 4000 })) {
      await notForKids.first().click();
      console.log("  ✓ Selected 'Not made for kids'.");
    }

    // Click Next (Video elements)
    const nextBtn = page.locator('#next-button');
    await nextBtn.click();
    console.log("  ✓ Clicked Next (Elements).");
    await page.waitForTimeout(2000);

    // Click Next (Checks)
    await nextBtn.click();
    console.log("  ✓ Clicked Next (Checks).");
    await page.waitForTimeout(2000);

    // Click Next (Visibility tab)
    await nextBtn.click();
    console.log("  ✓ Clicked Next (Visibility tab).");
    await page.waitForTimeout(2000);

    // Select Unlisted
    const unlistedRadio = page.locator('tp-yt-paper-radio-button[name="UNLISTED"], ytcp-radio-button[name="UNLISTED"]');
    if (await unlistedRadio.first().isVisible({ timeout: 4000 })) {
      await unlistedRadio.first().click();
      console.log("  ✓ Selected 'Unlisted' visibility.");
    }

    // Click Save / Done
    const saveBtn = page.locator('#done-button');
    await saveBtn.click();
    console.log("  🎉 Video Published Successfully!");

    await page.waitForTimeout(8000);

    // Take verification screenshot
    await page.screenshot({ path: '/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/youtube_single_upload_test_result.png' });
    console.log(" 📸 Verification screenshot saved to youtube_single_upload_test_result.png");

  } catch (err) {
    console.error(" ❌ Error during single video test upload:", err);
  } finally {
    await ctx.close();
  }
}

testSingleUpload();
