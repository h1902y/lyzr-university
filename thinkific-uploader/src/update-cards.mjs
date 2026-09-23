// Refresh the course card image on every Lyzr University course on Thinkific:
// for each live course, match it to a catalog entry, generate the dark Player card, and upload it.
//
//   npm run cards:plan    # --plan: show which courses map to which catalog entry, no changes
//   npm run cards         # generate + upload each card via Playwright
//   ONLY="Design" npm run cards   # only courses whose name matches the substring
import { config, launchOpts } from './config.mjs';
import { loadCatalog } from './catalog.mjs';
import { cardForCourse, cardParams, closeCardServer } from './cardgen.mjs';

const PLAN = process.argv.includes('--plan');
const RENDER_ONLY = process.argv.includes('--render-only');
const INCLUDE_LEGACY = process.argv.includes('--include-legacy');   // also match "[Legacy] <name>" courses
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36';
const norm = (s) => (s || '').toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, ' ').trim();

const catalog = loadCatalog(config.catalog);
const h = { Authorization: `Bearer ${config.token}`, 'User-Agent': UA };
const data = await (await fetch('https://api.thinkific.com/api/public/v1/courses?limit=250', { headers: h })).json();
let live = data.items || [];
if (config.onlyMatch) live = live.filter((c) => c.name.toLowerCase().includes(config.onlyMatch.toLowerCase()));

// Match each Thinkific course to its catalog entry by EXACT normalized name. This precisely selects
// the live curriculum courses (whose Thinkific name == catalog name) and excludes [Legacy] courses,
// the old umbrella/cert courses, and TEMPLATE — all of which fail the exact match.
const catByNorm = new Map(catalog.map((c) => [norm(c.name), c]));
const stripPrefix = (s) => s.replace(/^\s*\[[^\]]+\]\s*/, '');   // drop a leading "[Legacy] " etc.
const matched = [];
for (const c of live) {
  let cat = catByNorm.get(norm(c.name)), legacy = false;
  if (!cat && INCLUDE_LEGACY) { cat = catByNorm.get(norm(stripPrefix(c.name))); legacy = !!cat; }
  if (cat) matched.push({ course: c, cat, legacy });
}
console.log(`Thinkific: ${live.length} course(s) · matched to catalog: ${matched.length}\n`);
for (const { course, cat } of matched) {
  const p = cardParams(cat);
  console.log(`■ ${course.name}  (#${course.id})  → "${cat.name}"`);
  console.log(`    eyebrow="${p.eyebrow}"  title="${p.title} ${p.accent}"  ${p.videos} · ${p.duration}  icon=${p.icon}`);
}
const unmatched = live.filter((c) => !matched.find((m) => m.course.id === c.id));
if (unmatched.length) console.log(`\nskipped (no catalog match): ${unmatched.map((c) => c.name).join(', ')}`);

if (PLAN) { console.log('\n(plan only — no cards generated or uploaded)'); process.exit(0); }

if (RENDER_ONLY) {
  console.log('\nrendering cards (no upload):');
  for (const { course, cat } of matched) {
    const card = await cardForCourse(cat);
    console.log(`  ✓ ${course.name}  → ${card}`);
  }
  closeCardServer();
  process.exit(0);
}

// ---- generate + upload ----
const { chromium } = await import('playwright');
const { ThinkificAdmin } = await import('./thinkific.mjs');
const ctx = await chromium.launchPersistentContext(config.userDataDir, launchOpts(config.headless));
const page = ctx.pages()[0] || (await ctx.newPage());
const admin = new ThinkificAdmin(page, { adminUrl: config.adminUrl, token: config.token });

let updated = 0, failed = 0;
try {
  await admin.gotoCourses();
  for (const { course, cat } of matched) {
    console.log(`\n■ ${course.name}`);
    try {
      const card = await cardForCourse(cat);
      admin.courseId = String(course.id);
      const ok = await admin.uploadThumbnail(card);
      if (ok) { updated++; console.log(`  ✓ card updated`); } else { failed++; }
    } catch (e) { failed++; console.error(`  ✗ ${e.message.split('\n')[0]}`); }
  }
} finally {
  console.log(`\nDone — updated ${updated}, failed ${failed}.`);
  closeCardServer();
  await ctx.close();
}
