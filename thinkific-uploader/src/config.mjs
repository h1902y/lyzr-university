// Tiny .env loader + config (no dotenv dependency).
import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, resolve } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, '..');                 // …/thinkific-uploader
const UNIVERSITY = resolve(ROOT, '..');                // …/lyzr-university

function loadEnvFile() {
  const p = resolve(ROOT, '.env');
  if (!existsSync(p)) return;
  for (const line of readFileSync(p, 'utf8').split('\n')) {
    const m = line.match(/^\s*([A-Z0-9_]+)\s*=\s*(.*)\s*$/);
    if (m && !(m[1] in process.env)) process.env[m[1]] = m[2].replace(/^["']|["']$/g, '');
  }
}
loadEnvFile();

// Default to the live Lyzr account discovered 2026-06-17 (lyzr.thinkific.com → university.lyzr.ai).
const subdomain = process.env.THINKIFIC_SUBDOMAIN || 'lyzr';

// The Thinkific API OAuth token lives in lyzr-university/.env (TOKEN) — used to poll the API for
// upload completion (the source of truth, vs the flaky UI progress signal).
function readToken() {
  const p = resolve(UNIVERSITY, '.env');
  if (!existsSync(p)) return '';
  const line = readFileSync(p, 'utf8').split('\n').find((l) => l.startsWith('TOKEN='));
  return line ? line.split('=', 2)[1].trim().replace(/^["']|["']$/g, '') : '';
}

export const config = {
  root: ROOT,
  university: UNIVERSITY,
  subdomain,
  loginUrl:  process.env.THINKIFIC_LOGIN_URL  || `https://${subdomain}.thinkific.com/manage`,
  adminUrl:  process.env.THINKIFIC_ADMIN_URL  || `https://${subdomain}.thinkific.com/manage/courses`,
  // Source bundle + catalog (the same artifacts the rest of the pipeline produces).
  bundleDir: resolve(UNIVERSITY, process.env.BUNDLE_DIR || 'thinkific-upload'),
  catalog:   resolve(UNIVERSITY, process.env.CATALOG || 'catalog-demo/catalog-data.json'),
  bannerDir: resolve(UNIVERSITY, process.env.BANNER_DIR || 'catalog-demo/banner/exports'),
  // Behaviour
  headless: /^true$/i.test(process.env.HEADLESS || ''),     // headed by default (watch + recover)
  publish:  /^true$/i.test(process.env.PUBLISH || ''),      // default: leave as draft, you publish
  onlyMatch: process.env.ONLY || '',                        // substring filter on course folder
  courseId: process.env.COURSE_ID || '',                    // reuse an existing course (skip create) — for tuning
  setThumbnail: /^true$/i.test(process.env.SET_THUMBNAIL || ''),  // off by default (uses Uppy modal; tune separately)
  token: readToken(),                                            // Thinkific API token (for completion polling)
  template: process.env.TEMPLATE === '' ? '' : (process.env.TEMPLATE || 'TEMPLATE'),  // course to DUPLICATE; '' = create from scratch
  certName: process.env.CERT || 'Cert',                          // certificate to select (does NOT inherit on duplicate)
  // State (gitignored)
  progressPath: resolve(ROOT, 'progress.json'),
  screenshotsDir: resolve(ROOT, 'screenshots'),
  // Persistent browser profile — retains the Cloudflare cf_clearance + Thinkific session from the
  // one manual `npm run auth` login (university.lyzr.ai is behind Cloudflare Turnstile, which blocks
  // scripted login). Delete this folder to force a fresh login. The tool never sees your password.
  userDataDir: resolve(ROOT, '.browser-profile'),
};

// Launch options that defeat the Cloudflare Turnstile "Verifying you are human" loop:
//  • channel:'chrome' uses your REAL installed Google Chrome (genuine fingerprint), not Playwright's
//    bundled Chromium, which Turnstile flags.
//  • ignoreDefaultArgs drops Playwright's --enable-automation, and --disable-blink-features=
//    AutomationControlled hides navigator.webdriver — the two signals Turnstile keys on.
// Uses our own userDataDir, so it never touches your day-to-day Chrome profile.
export function launchOpts(headless = false) {
  return {
    channel: 'chrome',
    headless,
    viewport: { width: 1280, height: 800 },
    ignoreDefaultArgs: ['--enable-automation'],
    args: ['--disable-blink-features=AutomationControlled'],
  };
}
