// Launch Playwright's interactive recorder against the live admin, reusing your saved login.
//
//   npm run codegen
//
// Click through "create a course → add a chapter → add a video lesson → upload → publish" once.
// Playwright prints the locators it generates; paste/refine them into src/thinkific.mjs where a
// best-effort locator misses. (This is the one step that needs the live DOM — selectors are
// unknowable from outside and drift between Thinkific releases.)
import { chromium } from 'playwright';
import { config, launchOpts } from './config.mjs';

const context = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
const page = context.pages()[0] || (await context.newPage());
await page.goto(config.adminUrl, { waitUntil: 'domcontentloaded' }).catch(() => {});
// @ts-ignore — pause() opens the Inspector with the locator recorder.
await page.pause();
await context.close();
