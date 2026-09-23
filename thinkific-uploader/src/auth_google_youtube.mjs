import { chromium } from 'playwright';
import { config, launchOpts } from './config.mjs';

console.log("==========================================================================");
console.log(" 🔑 YOUTUBE STUDIO PLAYWRIGHT ONE-TIME BROWSER AUTHENTICATION");
console.log("==========================================================================");

async function authGoogle() {
  console.log("Launching headed Chrome browser...");
  const ctx = await chromium.launchPersistentContext(config.userDataDir, {
    ...launchOpts(false),
    headless: false // Headed mode so user can sign in
  });

  const page = ctx.pages()[0] || (await ctx.newPage());
  console.log("Navigating to https://studio.youtube.com ...");
  await page.goto('https://studio.youtube.com/channel/UCzTVTxamWRuAYdNFwZnEO_g', { waitUntil: 'domcontentloaded' });

  console.log("\n👉 PLEASE SIGN IN TO GOOGLE / YOUTUBE STUDIO IN THE OPENED BROWSER WINDOW.");
  console.log("Waiting up to 120 seconds for login completion...");

  for (let i = 0; i < 60; i++) {
    await page.waitForTimeout(2000);
    const url = page.url();
    if (url.includes('studio.youtube.com/channel/')) {
      console.log(`\n🎉 SUCCESS! Authenticated to YouTube Studio: ${url}`);
      await page.waitForTimeout(3000);
      break;
    }
  }

  await ctx.close();
  console.log("Browser context saved.");
}

authGoogle();
