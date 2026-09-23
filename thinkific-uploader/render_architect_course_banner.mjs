import http from 'node:http';
import { readFileSync, existsSync, statSync, mkdirSync, copyFileSync } from 'node:fs';
import { join, extname, resolve } from 'node:path';
import { spawn } from 'node:child_process';
import { fileURLToPath } from 'node:url';
import { dirname } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const ROOT = resolve(__dirname);
const UNIVERSITY = resolve(ROOT, '..');
const DEMO = join(UNIVERSITY, 'catalog-demo');
const CARDS_DIR = join(ROOT, 'cards');
const EXPORTS_DIR = join(UNIVERSITY, 'catalog-demo/banner/exports');
const COURSE_DIR = join(UNIVERSITY, 'thinkific-upload/1 - Tracks/Architect/20 Architect Fundamentals');
const ARTIFACT_DIR = '/Users/hkc/.gemini/antigravity/brain/95852f01-3507-4637-827a-c9f338755f10';

const MIME = {
  '.html': 'text/html',
  '.png': 'image/png',
  '.css': 'text/css',
  '.js': 'text/javascript',
  '.json': 'application/json',
  '.svg': 'image/svg+xml',
  '.jpg': 'image/jpeg'
};

let server = null;
const PORT = 8829;

function ensureServer() {
  if (server) return;
  server = http.createServer((req, res) => {
    const p = join(DEMO, decodeURIComponent(req.url.split('?')[0]));
    if (p.startsWith(DEMO) && existsSync(p) && statSync(p).isFile()) {
      res.setHeader('Content-Type', MIME[extname(p)] || 'application/octet-stream');
      res.end(readFileSync(p));
    } else {
      res.statusCode = 404;
      res.end('nf');
    }
  });
  server.listen(PORT, '127.0.0.1');
}

function closeServer() {
  if (server) {
    server.close();
    server = null;
  }
}

const run = (cmd, args) =>
  new Promise((res, rej) => {
    const p = spawn(cmd, args);
    p.on('close', res);
    p.on('error', rej);
  });

/**
 * Render player-card.html (760x420 @ 2x)
 */
async function generatePlayerCard(params, slug) {
  ensureServer();
  mkdirSync(CARDS_DIR, { recursive: true });
  const out = join(CARDS_DIR, `${slug}.png`);
  const qs = new URLSearchParams(params).toString();

  await run(CHROME, [
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--hide-scrollbars',
    '--force-device-scale-factor=2',
    '--window-size=760,420',
    '--virtual-time-budget=6000',
    '--default-background-color=00000000',
    '--run-all-compositor-stages-before-draw',
    `--screenshot=${out}`,
    `http://127.0.0.1:${PORT}/banner/player-card.html?${qs}`
  ]);
  return out;
}

/**
 * Render banner/index.html (Hero 1600x600, Social 1200x630, etc. @ 2x)
 */
async function generateBanner(params, slug, width, height) {
  ensureServer();
  mkdirSync(CARDS_DIR, { recursive: true });
  const out = join(CARDS_DIR, `${slug}.png`);
  const qs = new URLSearchParams({
    shot: '1',
    ...params
  }).toString();

  await run(CHROME, [
    '--headless=new',
    '--disable-gpu',
    '--no-sandbox',
    '--hide-scrollbars',
    '--force-device-scale-factor=2',
    `--window-size=${width},${height}`,
    '--virtual-time-budget=6000',
    '--default-background-color=00000000',
    '--run-all-compositor-stages-before-draw',
    `--screenshot=${out}`,
    `http://127.0.0.1:${PORT}/banner/index.html?${qs}`
  ]);
  return out;
}

async function main() {
  console.log("==========================================================================");
  console.log(" 🎨 RENDERING LYZR ARCHITECT COURSE BANNERS & CARDS");
  console.log("    Using Official Lyzr University Template Pipeline (player-card & banner)");
  console.log("==========================================================================\n");

  const results = [];

  // 1. Official Course Card (760x420 @ 2x) with video & duration pills
  console.log("1. Generating Player Card (760x420 @ 2x)...");
  const card1 = await generatePlayerCard(
    {
      eyebrow: 'ARCHITECT · TRACK',
      title: 'Architect',
      accent: 'Fundamentals',
      sub: 'with Suyash & Lyzr Team · Lyzr Architect',
      videos: '17 Videos',
      duration: '47 Minutes',
      icon: 'drafting-compass'
    },
    'track-architect-fundamentals'
  );
  console.log(`   ✓ Player Card: ${card1}`);
  results.push({ path: card1, name: 'track-architect-fundamentals.png' });

  // 2. Master Course Card variant (pills: 'off') matching master-lyzr-* series
  console.log("2. Generating Master Course Card (760x420 @ 2x, pills off)...");
  const card2 = await generatePlayerCard(
    {
      eyebrow: 'ARCHITECT · MASTER COURSE',
      title: 'Architect',
      accent: 'Fundamentals',
      sub: 'with Suyash & Lyzr Team · Lyzr Architect',
      pills: 'off',
      icon: 'drafting-compass'
    },
    'master-lyzr-architect'
  );
  console.log(`   ✓ Master Course Card: ${card2}`);
  results.push({ path: card2, name: 'master-lyzr-architect.png' });

  // 3. Thinkific Hero Course Banner (Dark Theme - 1600x600 @ 2x)
  console.log("3. Generating Hero Course Banner Dark (1600x600 @ 2x)...");
  const bannerDark = await generateBanner(
    {
      theme: 'dark',
      size: 'hero',
      src: 'architect',
      eyebrow: 'ARCHITECT · TRACK',
      headline: 'Architect *Fundamentals*',
      sub: 'Build full-stack agentic apps with no code — from visual flow to deployed enterprise agents.'
    },
    'architect-banner-dark-1600x600',
    1600,
    600
  );
  console.log(`   ✓ Hero Banner Dark: ${bannerDark}`);
  results.push({ path: bannerDark, name: 'architect-banner-dark-1600x600.png' });

  // 4. Thinkific Hero Course Banner (Light Theme - 1600x600 @ 2x)
  console.log("4. Generating Hero Course Banner Light (1600x600 @ 2x)...");
  const bannerLight = await generateBanner(
    {
      theme: 'light',
      size: 'hero',
      src: 'architect',
      eyebrow: 'ARCHITECT · TRACK',
      headline: 'Architect *Fundamentals*',
      sub: 'Build full-stack agentic apps with no code — from visual flow to deployed enterprise agents.'
    },
    'architect-banner-light-1600x600',
    1600,
    600
  );
  console.log(`   ✓ Hero Banner Light: ${bannerLight}`);
  results.push({ path: bannerLight, name: 'architect-banner-light-1600x600.png' });

  // 5. Social & 16:9 Banner (Dark Theme - 1200x630 @ 2x)
  console.log("5. Generating Social / 16:9 Banner (1200x630 @ 2x)...");
  const bannerSocial = await generateBanner(
    {
      theme: 'dark',
      size: 'social',
      src: 'architect',
      eyebrow: 'ARCHITECT · TRACK',
      headline: 'Architect *Fundamentals*',
      sub: 'Build full-stack agentic apps with no code — from visual flow to deployed enterprise agents.'
    },
    'architect-banner-social-1200x630',
    1200,
    630
  );
  console.log(`   ✓ Social Banner: ${bannerSocial}`);
  results.push({ path: bannerSocial, name: 'architect-banner-social-1200x630.png' });

  // Distribute files to Course Upload folder, Exports folder, and Artifact folder
  console.log("\n📦 Distributing generated assets to target destinations...");
  for (const item of results) {
    if (existsSync(COURSE_DIR)) {
      copyFileSync(item.path, join(COURSE_DIR, item.name));
      console.log(`   → Copied to Course Folder: ${join(COURSE_DIR, item.name)}`);
    }
    if (existsSync(EXPORTS_DIR)) {
      copyFileSync(item.path, join(EXPORTS_DIR, item.name));
      console.log(`   → Copied to Exports Folder: ${join(EXPORTS_DIR, item.name)}`);
    }
    if (existsSync(ARTIFACT_DIR)) {
      copyFileSync(item.path, join(ARTIFACT_DIR, item.name));
    }
  }

  // Also create standardized aliases in course folder
  if (existsSync(COURSE_DIR)) {
    copyFileSync(card1, join(COURSE_DIR, 'course-card.png'));
    copyFileSync(bannerDark, join(COURSE_DIR, 'course-banner.png'));
    console.log(`   → Created standard aliases: 'course-card.png' and 'course-banner.png' in course folder`);
  }

  console.log("\n==========================================================================");
  console.log(" 🎉 ALL ARCHITECT COURSE BANNERS & CARDS GENERATED SUCCESSFULLY!");
  console.log("==========================================================================");

  closeServer();
}

main().catch((err) => {
  console.error("❌ Fatal Error:", err);
  closeServer();
  process.exit(1);
});
