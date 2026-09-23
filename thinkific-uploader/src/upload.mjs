// Bundle + catalog driven uploader. Reads thinkific-upload/ + catalog-data.json, then for each
// course drives the Thinkific admin: create (or open) → details → thumbnail → chapter → lessons →
// price → collection → publish. Idempotent via progress.json (resume after a crash or a fixed
// selector). Dry-run prints the full plan and needs no browser/Playwright.
//
//   npm run plan      # --dry-run: print exactly what WOULD happen, no browser
//   npm run upload    # do it (requires `npm run auth` first)
//   ONLY="Design" npm run upload   # only courses whose folder matches the substring
import { existsSync, readFileSync, writeFileSync, mkdirSync, statSync } from 'node:fs';
import { config, launchOpts } from './config.mjs';
import { readBundle, summarize } from './bundle.mjs';
import { loadCatalog, resolveMeta } from './catalog.mjs';
import { cardForCourse, closeCardServer } from './cardgen.mjs';

const DRY = process.argv.includes('--dry-run');
const mb = (f) => { const b = statSync(f).size; return b < 1024 * 1024 ? (b / 1024).toFixed(0) + 'KB' : (b / 1024 / 1024).toFixed(0) + 'MB'; };
const loadProgress = () => existsSync(config.progressPath) ? new Set(JSON.parse(readFileSync(config.progressPath, 'utf8'))) : new Set();
const saveProgress = (d) => writeFileSync(config.progressPath, JSON.stringify([...d], null, 2));

if (!existsSync(config.bundleDir)) { console.error(`✗ bundle not found: ${config.bundleDir}`); process.exit(1); }

let courses = readBundle(config.bundleDir);
if (config.onlyMatch) courses = courses.filter((c) => c.folder.toLowerCase().includes(config.onlyMatch.toLowerCase()));
const catalog = existsSync(config.catalog) ? loadCatalog(config.catalog) : [];
const s = summarize(courses);

console.log(`Bundle:  ${config.bundleDir}`);
console.log(`Catalog: ${existsSync(config.catalog) ? config.catalog : '(none — titles only)'}`);
console.log(`Account: ${config.subdomain}.thinkific.com   publish=${config.publish}  headless=${config.headless}`);
console.log(`Plan:    ${s.courses} course(s) · ${s.lessons} lesson(s) (${s.video} video, ${s.pdf} pdf)\n`);

// ---- Dry run -----------------------------------------------------------------------------------
if (DRY) {
  for (const c of courses) {
    const m = resolveMeta(c, catalog, config.bannerDir);
    console.log(`■ COURSE: ${m.name}   [${c.collection}${c.product ? ' · ' + c.product : ''}]`);
    console.log(`    catalog match: ${m.matched ? 'yes' : 'NO (title-only fallback)'}   publish: ${m.publish}   free: ${m.free}`);
    console.log(`    subtitle:  ${m.subtitle || '—'}`);
    console.log(`    desc:      ${(m.description || '—').slice(0, 80)}${m.description.length > 80 ? '…' : ''}`);
    console.log(`    card:      ${m.card ? m.card.split('/').pop() : 'NONE (no thumbnail)'}`);
    console.log(`    collection:${m.collectionName || '—'}`);
    for (const ch of c.chapters) {
      console.log(`    └ CHAPTER: ${ch.title}`);
      for (const l of ch.lessons) console.log(`        • ${l.type.toUpperCase().padEnd(5)} ${l.title}  (${mb(l.file)})`);
    }
    console.log('');
  }
  console.log('(plan only — nothing created)');
  process.exit(0);
}

// ---- Real run ----------------------------------------------------------------------------------
if (!existsSync(config.userDataDir)) { console.error('✗ no saved browser profile. Run `npm run auth` first.'); process.exit(1); }
mkdirSync(config.screenshotsDir, { recursive: true });
const done = loadProgress();

// Lazy import so the dry run needs neither Playwright nor a browser download.
const { chromium } = await import('playwright');
const { ThinkificAdmin } = await import('./thinkific.mjs');

const context = await chromium.launchPersistentContext(config.userDataDir, launchOpts(config.headless));
const page = context.pages()[0] || (await context.newPage());
page.on('dialog', (d) => d.accept().catch(() => {}));   // auto-accept native confirm()s (course Duplicate)
const admin = new ThinkificAdmin(page, { adminUrl: config.adminUrl, token: config.token });
const slugify = (s) => s.toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');

let uploaded = 0, skipped = 0, failed = 0;
try {
  await admin.gotoCourses();
  for (const course of courses) {
    const m = resolveMeta(course, catalog, config.bannerDir);
    // Per-course idempotency: bulk upload is all-or-nothing, so a finished course is skipped whole
    // (re-uploading would duplicate its lessons).
    if (done.has(m.name)) { skipped++; console.log(`\n■ ${m.name}\n  · skip (already uploaded)`); continue; }
    console.log(`\n■ ${m.name}`);
    try {
      if (config.courseId) {
        admin.courseId = config.courseId;
        console.log(`  · reuse course #${config.courseId} (COURSE_ID set)`);
      } else if (config.template) {
        console.log(`  · duplicating template "${config.template}" …`);
        await admin.duplicateTemplate(config.template);
        console.log(`  · copy #${admin.courseId} (inherits pricing/collection/card/landing)`);
      } else {
        const existed = await admin.findExistingCourse(m.name);
        console.log(existed ? `  · opened existing course #${admin.courseId}` : `  · created course #${await admin.createCourse()}`);
      }
      const cardPath = m.cat ? await cardForCourse(m.cat) : null;   // generate the dark Player card
      await admin.setDetails({ name: m.name, description: m.description, cardPath });
      await admin.setCertificate(config.certName);                 // cert does NOT inherit on duplicate
      const ch = course.chapters[0];                 // bundle = one chapter per course
      const files = ch.lessons.map((l) => l.file);   // already ordered: NNa video, NNb notes …
      const titles = ch.lessons.map((l) => (l.type === 'video' ? l.title : `${l.title} Notes`));  // clean names
      console.log(`  └ ${ch.title}: bulk-uploading ${files.length} files`);
      await admin.uploadLessons(ch.title, files);
      await admin.renameLessons(titles);                           // strip NNa/NNb prefixes
      await admin.setSlug(slugify(m.name));                        // unique landing-page URL
      await admin.setPriceFree();
      if (m.name.includes("Overview")) {
        // Force publish for this hidden course
        console.log(`  · publishing course (required for hidden access) …`);
        await admin.publishCourse();
        
        // Hide course from storefront
        console.log(`  · toggling "Hidden course" checkbox on …`);
        await admin.page.goto(`${admin.base}/manage/courses/${admin.courseId}/settings`, { waitUntil: 'domcontentloaded' });
        await admin.page.waitForTimeout(5000);
        const wasChecked = await admin.page.evaluate(() => {
          const el = [...document.querySelectorAll('*')].find((e) => e.children.length <= 2 && (e.textContent || '').trim() === 'Hidden course');
          const scope = el?.closest('label,div,fieldset') || el?.parentElement;
          const inp = scope?.querySelector('input[type=checkbox]');
          return inp ? inp.checked : null;
        });
        if (wasChecked === false) {
          await admin.page.getByText('Hidden course', { exact: true }).first().click();
          await admin.page.waitForTimeout(600);
        }
        await admin.page.getByRole('button', { name: /save settings/i }).first().click();
        await admin.page.waitForTimeout(3500);
        console.log(`  · course set to hidden successfully!`);
      } else {
        if (config.publish && m.publish) await admin.publishCourse();
      }
      done.add(m.name); saveProgress(done); uploaded++;
      console.log(`  ✓ ${m.name} — uploaded`);
    } catch (err) {
      failed++;
      const shot = `${config.screenshotsDir}/fail-${Date.now()}.png`;
      await page.screenshot({ path: shot, fullPage: true }).catch(() => {});
      console.error(`  ✗ ${m.name}\n    step: ${admin.step}\n    ${err.message.split('\n')[0]}\n    shot: ${shot}`);
    }
  }
} finally {
  console.log(`\nDone — uploaded ${uploaded}, skipped ${skipped}, failed ${failed}.`);
  console.log('Verify:  python3 ../../.claude/skills/descript-to-thinkific/scripts/thinkific_verify.py');
  closeCardServer();
  await context.close();
}
