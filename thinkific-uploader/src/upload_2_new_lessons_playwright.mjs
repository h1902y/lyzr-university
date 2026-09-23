import { chromium } from 'playwright';
import fs from 'fs';
import path from 'path';
import { config, launchOpts } from './config.mjs';

const revampDir = '/Users/hkc/Documents/lyzr/university/revamp';
const brandedDir = '/Users/hkc/Documents/lyzr/university/revamp_branded';

const newLessons = [
  {
    title: 'Foundation C1 L4 | Lyzr Platform Pricing & Token Economics',
    filepath: path.join(brandedDir, 'C01_CH01_L04_lyzr_platform_pricing.mp4'),
    thumbnail_path: path.join(revampDir, 'thumbnails', 'C01_CH01_L04_lyzr_platform_pricing.png'),
    description: `Course: Lyzr Foundations
Chapter: Lyzr Platform & Ecosystem Overview
Lesson: Lyzr Platform Pricing & Token Economics

============================================================
📚 LESSON OVERVIEW & OBJECTIVES
============================================================
  • Learn how Lyzr is priced on transparent token usage (APCs - Agent Processing Credits).
  • Understand the 1:1 input/output token calculation model with zero complexity multipliers or feature gating.
  • Compare Lyzr SaaS vs. On-Premise VPC deployment architectures and capacity scaling.
  • Explore BYOK (Bring Your Own Keys) vs. zero-markup pass-through model inference billing.

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
#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI`
  },
  {
    title: 'Technical C4 L3 | GitAgent Harness: Repo as Source of Truth',
    filepath: path.join(brandedDir, 'C03_CH04_L03_gitagent_harness.mp4'),
    thumbnail_path: path.join(revampDir, 'thumbnails', 'C03_CH04_L03_gitagent_harness.png'),
    description: `Course: Lyzr for Technical Professionals
Chapter: Lyzr ADK & Open Source
Lesson: GitAgent Harness: Repo as Source of Truth

============================================================
📚 LESSON OVERVIEW & OBJECTIVES
============================================================
  • Understand how GitAgent transforms your Git repository into the primary agent specification and harness.
  • Inspect the core declarative spec files: soul.md, rules.md, instructions.md, and agent.yaml.
  • Learn how Lyzr Studio acts as a synchronized runtime reading directly from GitHub.
  • Inherit native enterprise software controls: PR code reviews, CI/CD automated testing, and commit audit trails.

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
#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI`
  }
];

console.log("==========================================================================");
console.log(" 🚀 UPLOADING 2 NEW DESCRIPT LESSONS TO @LyzrAI YOUTUBE CHANNEL");
console.log("==========================================================================");

async function runUploader() {
  const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
  const page = ctx.pages()[0] || (await ctx.newPage());

  for (let idx = 0; idx < newLessons.length; idx++) {
    const item = newLessons[idx];
    const { title, description, filepath, thumbnail_path } = item;

    console.log(`\n======================================================`);
    console.log(`[${idx + 1}/${newLessons.length}] Uploading via Playwright: ${title}`);
    console.log(`Video File:     ${path.basename(filepath)} (${(fs.statSync(filepath).size / (1024*1024)).toFixed(1)} MB)`);
    console.log(`Thumbnail PNG:  ${path.basename(thumbnail_path)}`);
    console.log(`======================================================`);

    try {
      console.log("Navigating to clean Studio Dashboard...");
      await page.goto('https://studio.youtube.com/channel/UCzTVTxamWRuAYdNFwZnEO_g', { waitUntil: 'domcontentloaded', timeout: 60000 });
      await page.waitForTimeout(4000);

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

      const fileInput = page.locator('input[type="file"]').first();
      await fileInput.waitFor({ state: 'attached', timeout: 20000 });
      await fileInput.setInputFiles(filepath);
      console.log("  ✓ Video file uploaded to input. Processing details modal...");

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

      // Select Unlisted Visibility
      const unlistedRadio = page.locator('tp-yt-paper-radio-button[name="UNLISTED"], ytcp-radio-button[name="UNLISTED"]');
      if (await unlistedRadio.first().isVisible({ timeout: 4000 })) {
        await unlistedRadio.first().click();
        console.log("  ✓ Selected 'Unlisted' visibility.");
      }

      // Done / Save
      await page.waitForTimeout(2000);
      const saveBtn = page.locator('ytcp-button#done-button, #done-button').first();
      await saveBtn.click();
      console.log("  🎉 Video Published Successfully!");
      await page.waitForTimeout(6000);

    } catch (err) {
      console.error(`  ❌ Error uploading ${title}:`, err.message);
    }
  }

  console.log(`\n======================================================`);
  console.log(` 🎉 Upload Complete for Both New Lessons!`);
  console.log(`======================================================`);

  await ctx.close();
}

runUploader();
