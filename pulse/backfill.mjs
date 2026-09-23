// One-off historical backfill: reconstruct a week-by-week trajectory from the first enrollment to now.
// Precisely reconstructable from timestamps: cumulative + weekly-new enrollments, learners, completions,
// completion rate, and courses-live (by launch date). NOT reconstructable (current-state only, so omitted):
// "≥1 lesson" engagement and "active this week".
//   node backfill.mjs           # markdown weekly table
import { readFileSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { makeClient, lessonCount } from './lib/thinkific.mjs';
import { istShift as toIST, istMonDay as istLabel, isoWeekLabel } from './lib/week.mjs';

const HERE = dirname(fileURLToPath(import.meta.url));
const config = JSON.parse(readFileSync(join(HERE, 'config.json'), 'utf8'));
const liveSince = Object.fromEntries(config.liveCourses.map((c) => [c.id, c.liveSince]));
const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

const IST = 5.5 * 3600 * 1000;
// Monday 00:00 IST on/this week of the given instant, expressed as a UTC ms boundary.
function istMondayStart(ms) {
  const d = toIST(ms);
  const dow = (d.getUTCDay() + 6) % 7;                                 // Mon=0
  const midnight = Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), d.getUTCDate()) - dow * 864e5;
  return midnight - IST;                                               // back to real UTC ms
}

const client = makeClient();
console.error('fetching enrollments…');
const enr = await client.getAll('enrollments');
console.error(`  ${enr.length} enrollments`);

const created = (e) => new Date(e.created_at).getTime();
const doneAt = (e) => (e.completed_at ? new Date(e.completed_at).getTime() : null);
// Course launch = config liveSince for the 6 live; else earliest enrollment (proxy) for legacy/retired.
const launch = {};
for (const e of enr) { const t = created(e); if (!(e.course_id in launch) || t < launch[e.course_id]) launch[e.course_id] = t; }
for (const c of config.liveCourses) launch[c.id] = new Date(liveSince[c.id]).getTime();

const firstMs = Math.min(...enr.map(created));
const now = Date.now();
let weekStart = istMondayStart(firstMs);
const weeks = [];
for (let n = 1; weekStart <= now; n++) {
  const weekEnd = weekStart + 7 * 864e5;
  const upTo = (ts) => ts != null && ts < weekEnd;
  const inWeek = (ts) => ts != null && ts >= weekStart && ts < weekEnd;
  const cumEnr = enr.filter((e) => upTo(created(e)));
  const newEnr = enr.filter((e) => inWeek(created(e)));
  const learners = new Set(cumEnr.map((e) => e.user_id)).size;
  const newLearners = new Set(newEnr.map((e) => e.user_id).filter((u) => !new Set(enr.filter((x) => created(x) < weekStart).map((x) => x.user_id)).has(u))).size;
  const cumCmpl = enr.filter((e) => upTo(doneAt(e))).length;
  const newCmpl = enr.filter((e) => inWeek(doneAt(e))).length;
  const coursesLive = Object.values(launch).filter((t) => t < weekEnd).length;
  const newCourses = Object.entries(launch).filter(([, t]) => t >= weekStart && t < weekEnd).length;
  weeks.push({
    n, start: weekStart, end: weekEnd,
    newEnr: newEnr.length, cumEnr: cumEnr.length, learners, newLearners,
    newCmpl, cumCmpl, rate: cumEnr.length ? Math.round((cumCmpl / cumEnr.length) * 100) : 0,
    coursesLive, newCourses,
    current: now >= weekStart && now < weekEnd,
  });
  weekStart = weekEnd;
}

// Render markdown
const rows = weeks.map((w) =>
  `| ${isoWeekLabel(w.start)}${w.current ? ' *(curr)*' : ''} | ${istLabel(w.start)}–${istLabel(w.end - 864e5)} | +${w.newEnr} | ${w.cumEnr} | ${w.learners}${w.newLearners ? ` (+${w.newLearners})` : ''} | +${w.newCmpl} | ${w.cumCmpl} | ${w.rate}% | ${w.coursesLive}${w.newCourses ? ` (+${w.newCourses})` : ''} |`,
);
console.log(`## Lyzr University — Weekly history (ISO weeks, Mon–Sun, IST)\n`);
console.log(`| ISO Week | Dates | New enr | Σ Enr | Learners | New cmpl | Σ Cmpl | Cmpl rate | Courses |`);
console.log(`|---|---|--:|--:|--:|--:|--:|--:|--:|`);
console.log(rows.join('\n'));
console.log(`\n_Σ = cumulative through that week. “≥1 lesson” and “active” are current-state only in the Thinkific API, so they're excluded from history. Course count uses launch dates (live curriculum = config; legacy = first-enrollment proxy)._`);

// ---- Exemplar weekly digest: render one past week in the live Monday format ----
const EXN = Number(process.argv.find((a) => a.startsWith('--digest='))?.split('=')[1] || 5);
const EX = weeks.find((w) => w.n === EXN);
const prevW = weeks.find((w) => w.n === EXN - 1);
if (EX) {
  const { start: s, end: e } = EX;
  const upTo = (ts) => ts != null && ts < e;
  const inW = (ts) => ts != null && ts >= s && ts < e;
  const liveIds = new Set(config.liveCourses.map((c) => c.id));
  const lessons = {};
  for (const c of config.liveCourses) lessons[c.id] = await lessonCount(client, c.id);

  const pad = (x, n) => String(x).padEnd(n);
  const plus = (n) => (n ? ` (+${n})` : '');
  const wow = (cur, prev) => (prev == null ? '' : cur - prev > 0 ? ` (▲${cur - prev})` : cur - prev < 0 ? ` (▼${prev - cur})` : '');

  // per live course as-of week end
  const rows = [];
  for (const c of config.liveCourses) {
    if (launch[c.id] >= e) continue;                       // not live yet that week
    const es = enr.filter((x) => x.course_id === c.id);
    const enrolled = es.filter((x) => upTo(created(x))).length;
    const neu = es.filter((x) => inW(created(x))).length;
    const done = es.filter((x) => upTo(doneAt(x))).length;
    rows.push({ name: c.name, liveSince: c.liveSince, enrolled, neu, done, rate: enrolled ? Math.round((done / enrolled) * 100) : null });
  }
  const legEs = enr.filter((x) => !liveIds.has(x.course_id));
  const leg = { enrolled: legEs.filter((x) => upTo(created(x))).length, neu: legEs.filter((x) => inW(created(x))).length, done: legEs.filter((x) => upTo(doneAt(x))).length };
  leg.rate = leg.enrolled ? Math.round((leg.done / leg.enrolled) * 100) : null;
  const legCount = new Set(legEs.filter((x) => upTo(created(x))).map((x) => x.course_id)).size;

  const liveCur = config.liveCourses.filter((c) => launch[c.id] < e);
  const newCur = config.liveCourses.filter((c) => launch[c.id] >= s && launch[c.id] < e);
  const lessonsLive = liveCur.reduce((a, c) => a + lessons[c.id], 0);
  const newLessons = newCur.reduce((a, c) => a + lessons[c.id], 0);

  const T = [];
  T.push(`🎓 ${config.title}`);
  T.push(`📅 ${isoWeekLabel(s)} · ${istLabel(s)}–${istLabel(e - 864e5)} IST${prevW ? '  · vs prev week' : ''}`);
  T.push('');
  T.push('OVERALL');
  T.push(`👥 Learners ${EX.learners}${wow(EX.learners, prevW?.learners)}     📝 Enrollments ${EX.cumEnr}${plus(EX.newEnr)}`);
  T.push(`Funnel:  Enrolled ${EX.cumEnr} → ✅ Completed ${EX.cumCmpl} (${EX.rate}%)`);
  T.push(`🏅 Certificates ${EX.cumCmpl}${plus(EX.newCmpl)}`);
  T.push('');
  const head = `${pad('BY COURSE', 28)}${pad('Live since', 12)}${pad('Enr(+new)', 11)}${pad('Done', 6)}Rate`;
  const tbl = [head];
  for (const r of rows) tbl.push(pad(r.name, 28) + pad(r.liveSince.replace('2026-', '').replace('-', '/'), 12) + pad(`${r.enrolled}${plus(r.neu)}`, 11) + pad(r.done, 6) + (r.rate == null ? '—' : `${r.rate}%`));
  tbl.push(pad(`— ${config.legacyLabel} (${legCount})`, 28) + pad('—', 12) + pad(`${leg.enrolled}${plus(leg.neu)}`, 11) + pad(leg.done, 6) + (leg.rate == null ? '—' : `${leg.rate}%`));
  T.push('```\n' + tbl.join('\n') + '\n```');
  T.push('');
  T.push(`📚 CONTENT  ${liveCur.length} live courses · ${lessonsLive} lessons  →  +${newCur.length} course${newCur.length === 1 ? '' : 's'} · +${newLessons} lessons this week${newCur.length ? `  ·  new: ${newCur.map((c) => c.name).join(', ')}` : ''}`);

  console.log('\n\n──────────── EXEMPLAR: what lands every Monday (Week ' + EX.n + ') ────────────\n');
  console.log(T.join('\n'));
  console.log(`\n_Reconstructed from enrollment timestamps. The live Monday digest also shows a “≥1 lesson” funnel stage and an “active this week” column per course — those aren't historizable (Thinkific only exposes current progress), so they're omitted from this reconstruction._`);
}
