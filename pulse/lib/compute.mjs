// Aggregate Thinkific enrollments + catalog into the Pulse stats.
// The "week" window is "since the last snapshot" (snapshot-to-snapshot), so mid-week uploads and
// missed runs both behave correctly. First run (no prior snapshot) falls back to a 7-day window and
// records a baseline — historical courses are the starting line, not "shipped this week".
import { lessonCount } from './thinkific.mjs';

const pct = (e) => parseFloat(e.percentage_completed || '0');
const isEngaged = (e) => pct(e) > 0;              // completed ≥1 lesson
const isDone = (e) => pct(e) >= 1 || e.completed; // finished all / certified

// WoW delta + growth %. `pct` is null when there is no comparable prior OR the base is < 5 — too
// small to quote a meaningful percentage (keeps a 4→12 jump from screaming "+200%").
const wowPct = (cur, prevVal) => {
  if (prevVal == null) return { delta: null, pct: null };
  const delta = cur - prevVal;
  return { delta, pct: prevVal < 5 ? null : Math.round((delta / prevVal) * 100) };
};

function funnel(enrs, sinceISO) {
  const since = sinceISO ? new Date(sinceISO) : null;
  const inWindow = (ts) => ts && (!since || new Date(ts) > since);
  return {
    enrolled: enrs.length,
    engaged: enrs.filter(isEngaged).length,
    completed: enrs.filter(isDone).length,
    newEnrolled: enrs.filter((e) => inWindow(e.created_at)).length,
    newCompleted: enrs.filter((e) => isDone(e) && inWindow(e.completed_at)).length,
    active: new Set(enrs.filter((e) => inWindow(e.updated_at)).map((e) => e.user_id)).size,
  };
}

// Build the full computed model. `prev` is the previous snapshot (or null on first run).
export async function compute(client, config, enrollments, prev, nowISO) {
  const liveIds = new Set(config.liveCourses.map((c) => c.id));
  const prevCourses = prev?.courses || {};                    // for per-course WoW + content diff
  const sinceISO = prev?.generatedAt || null;                 // window boundary
  const fallback7d = !sinceISO ? new Date(new Date(nowISO) - 7 * 864e5).toISOString() : null;
  const windowFrom = sinceISO || fallback7d;

  // Per live course
  const courses = [];
  let totalLessons = 0;
  for (const c of config.liveCourses) {
    const enrs = enrollments.filter((e) => e.course_id === c.id);
    const lessons = await lessonCount(client, c.id);
    totalLessons += lessons;
    const f = funnel(enrs, windowFrom);
    courses.push({
      id: c.id, name: c.name, collection: c.collection,
      liveSince: c.liveSince, lessons,
      ...f,
      rate: f.enrolled ? Math.round((f.completed / f.enrolled) * 100) : null,
      certDelta: prevCourses[c.id]?.completed != null ? f.completed - prevCourses[c.id].completed : null,
    });
  }

  // Legacy / retired rollup = everything not in the live set
  const legacyEnrs = enrollments.filter((e) => !liveIds.has(e.course_id));
  const legacyCourseCount = new Set(legacyEnrs.map((e) => e.course_id)).size;
  const legacy = {
    ...funnel(legacyEnrs, windowFrom),
    courseCount: legacyCourseCount,
    rate: legacyEnrs.length ? Math.round((legacyEnrs.filter(isDone).length / legacyEnrs.length) * 100) : null,
  };

  // Overall (all enrollments)
  const overallF = funnel(enrollments, windowFrom);
  const overall = {
    learners: new Set(enrollments.map((e) => e.user_id)).size,
    ...overallF,
    certificates: overallF.completed,
    rate: overallF.enrolled ? Math.round((overallF.completed / overallF.enrolled) * 100) : null,
  };
  overall.certRate = overall.rate;                                                                  // completed ÷ enrolled (cert block)
  overall.engagedRate = overallF.enrolled ? Math.round((overallF.engaged / overallF.enrolled) * 100) : 0;

  // Per-collection certificate rollup (live collections in config order + a Legacy bucket), each with
  // a WoW delta derived from the prior snapshot's per-course completions.
  const colMap = new Map();
  for (const c of courses) {
    const g = colMap.get(c.collection) || { label: c.collection, total: 0, prev: 0, prevKnown: false };
    g.total += c.completed;
    const pc = prevCourses[c.id]?.completed;
    if (pc != null) { g.prev += pc; g.prevKnown = true; }
    colMap.set(c.collection, g);
  }
  const liveCompleted = courses.reduce((s, c) => s + c.completed, 0);
  const prevLiveCompleted = courses.reduce((s, c) => s + (prevCourses[c.id]?.completed ?? 0), 0);
  const legacyCompleted = overall.completed - liveCompleted;
  const legacyPrevCompleted = prev?.overall ? prev.overall.completed - prevLiveCompleted : null;
  const certsByCollection = [
    ...[...colMap.values()].map((g) => ({ label: g.label, total: g.total, delta: g.prevKnown ? g.total - g.prev : null })),
    { label: 'Legacy', total: legacyCompleted, delta: legacyPrevCompleted == null ? null : legacyCompleted - legacyPrevCompleted },
  ];

  // Content pipeline = diff vs previous snapshot (baseline on first run)
  const newCourses = config.liveCourses.filter((c) => !(c.id in prevCourses));
  const lessonsAdded = prev
    ? courses.reduce((s, c) => s + (c.lessons - (prevCourses[c.id]?.lessons ?? c.lessons)), 0)
       + newCourses.reduce((s, c) => s + (courses.find((x) => x.id === c.id)?.lessons || 0), 0)
    : 0;
  const content = {
    liveCourseCount: config.liveCourses.length,
    totalLessons,
    newCourses: prev ? newCourses.map((c) => c.name) : [],
    lessonsAdded: prev ? lessonsAdded : 0,
    baseline: !prev,
  };

  // WoW deltas + growth % for the headline metrics (null on first run / when base < 5).
  const pw = prev?.overall || null;
  const wow = {
    learners: wowPct(overall.learners, pw?.learners ?? null),
    enrollments: wowPct(overall.enrolled, pw?.enrolled ?? null),
    engaged: wowPct(overall.engaged, pw?.engaged ?? null),
    completed: wowPct(overall.completed, pw?.completed ?? null),
  };

  return {
    generatedAt: nowISO,
    windowFrom,
    week: (prev?.week || 0) + 1,   // sequential tracked-week number
    isBaseline: !prev,
    overall, courses, legacy, content, wow, certsByCollection,
  };
}

// Reduce a computed model to the persisted snapshot shape (what the next run diffs against).
export function toSnapshot(model) {
  const courses = {};
  for (const c of model.courses) courses[c.id] = { name: c.name, lessons: c.lessons, enrolled: c.enrolled, completed: c.completed };
  return {
    generatedAt: model.generatedAt,
    week: model.week,
    overall: { learners: model.overall.learners, enrolled: model.overall.enrolled, engaged: model.overall.engaged, completed: model.overall.completed, active: model.overall.active },
    courses,
    totalLessons: model.content.totalLessons,
    liveCourseCount: model.content.liveCourseCount,
  };
}
