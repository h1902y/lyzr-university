import { chromium } from 'playwright';
import { config, launchOpts } from './thinkific-uploader/src/config.mjs';

console.log("==========================================================================")
console.log(" 🔍 CHECKING YOUTUBE STUDIO SESSION VIA PLAYWRIGHT BROWSER CONTEXT")
console.log("==========================================================================")

try {
  const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
  const page = ctx.pages()[0] || (await ctx.newPage());

  console.log("Navigating to https://studio.youtube.com/ ...");
  await page.goto('https://studio.youtube.com/', { waitUntil: 'domcontentloaded', timeout: 30000 });
  await page.waitForTimeout(4000);

  const url = page.url();
  const title = await page.title();
  console.log(`Current Page URL:   ${url}`);
  console.log(`Current Page Title: ${title}`);

  if (url.includes('studio.youtube.com')) {
    console.log(" ✅ Playwright is LOGGED IN to YouTube Studio!");
    // Take screenshot
    await page.screenshot({ path: '/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/youtube_studio_session.png' });
    console.log(" 📸 Screenshot saved to youtube_studio_session.png");
  } else if (url.includes('accounts.google.com')) {
    console.log(" ⚠️ Redirected to Google Login.");
    await page.screenshot({ path: '/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61/google_login_redirect.png' });
  }

  await ctx.close();
} catch (err) {
  console.error(" ❌ Playwright error:", err);
}
