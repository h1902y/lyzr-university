// One-time interactive login into a PERSISTENT browser profile.
//
//   npm run auth
//
// A real Chrome window opens at the Thinkific admin. Log in YOURSELF (email/password + the
// Cloudflare "verify you are human" check + any 2FA) — these bot defenses block scripted login,
// so a human does this once. The session + Cloudflare clearance persist in .browser-profile/ and
// are reused by `npm run upload`. The tool never sees your password.
import { chromium } from 'playwright';
import readline from 'node:readline';
import { config, launchOpts } from './config.mjs';

const context = await chromium.launchPersistentContext(config.userDataDir, launchOpts(false));
const page = context.pages()[0] || (await context.newPage());

console.log(`\nOpening ${config.loginUrl}`);
console.log('→ Log in in the window. Pass the Cloudflare check + any 2FA by hand.');
await page.goto(config.loginUrl, { waitUntil: 'domcontentloaded' }).catch(() => {});

// A logged-in admin page sits under /manage and is NOT the sign-in route.
const loggedIn = () => {
  const u = page.url();
  return u.includes('/manage') && !/sign_in|\/login/i.test(u);
};

// Wait for login. With a real terminal, let the user confirm with Enter (their call on
// when Cloudflare/2FA is done). Without a TTY (e.g. launched from a non-interactive shell
// via the `!` prefix), poll the URL so login still completes without stdin.
if (process.stdin.isTTY) {
  const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
  await new Promise((res) =>
    rl.question('\nWhen you can see the admin dashboard (Manage → Courses), press Enter here… ', res));
  rl.close();
} else {
  console.log('\n(no interactive terminal detected — I\'ll wait until you reach the admin');
  console.log(' dashboard in the window; up to 5 minutes. Finish the Cloudflare check + 2FA.)');
  const deadline = Date.now() + 5 * 60 * 1000;
  while (Date.now() < deadline && !loggedIn()) {
    await page.waitForTimeout(2000);
  }
  if (loggedIn()) await page.waitForTimeout(1500); // let cookies/clearance flush to disk
}

const url = page.url();
console.log(`\nCurrent URL: ${url}`);
console.log(loggedIn()
  ? '✓ Looks logged in. Profile saved — run `npm run plan` then `npm run upload`.'
  : '⚠ Not on a /manage page yet. Finish logging in, then re-run if needed.');

await context.close();
