// Render the computed model into a Slack message: header/overall lines as mrkdwn, the per-course
// table inside a monospace code block (so columns align), then content pipeline + highlights.
import { istMonDay, istHM, isoWeekLabel } from './week.mjs';
const MON = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'];

const fmtDate = (iso) => `${istMonDay(iso)}`;
const fmtIST = (iso) => `${istMonDay(iso)}, ${istHM(iso)}`;   // "Jun 18, 13:00" (IST)
const liveLabel = (liveSince, nowISO) => {
  if (!liveSince) return '—';
  const d = new Date(liveSince), now = new Date(nowISO);
  const days = Math.max(0, Math.round((now - d) / 864e5));
  const age = days < 7 ? `${days}d` : `${Math.round(days / 7)}w`;
  return `${MON[d.getUTCMonth()]} ${d.getUTCDate()} · ${age}`;
};
const plus = (n) => (n ? ` (+${n})` : '');
const pad = (s, n) => String(s).padEnd(n);
const lpad = (s, n) => String(s).padStart(n);

// WoW formatters. A `wow` is { delta, pct } — pct is null when base < 5 or no prior; delta null = no prior.
const arrowPct = (p) => (p > 0 ? `▲${p}%` : p < 0 ? `▼${-p}%` : `▲0%`);
// "88 (+48, ▲120%)" — headline value with its weekly change. Bare value when flat or no prior.
const wfmt = (value, w) => {
  if (!w || w.delta == null || w.delta === 0) return `${value}`;
  const d = w.delta > 0 ? `+${w.delta}` : `${w.delta}`;
  return `${value} (${d}${w.pct == null ? '' : `, ${arrowPct(w.pct)}`})`;
};
// ", ▲67%" — a WoW growth suffix to drop inside an existing (rate%) paren; "" when unavailable.
const wsuffix = (w) => (!w || w.delta == null || w.delta === 0 || w.pct == null ? '' : `, ${arrowPct(w.pct)}`);
// "(+13, ▲57% WoW)" / "(+8)" / "" — a standalone WoW paren with an optional trailing label.
const wparen = (w, label) => {
  if (!w || w.delta == null || w.delta === 0) return '';
  const d = w.delta > 0 ? `+${w.delta}` : `${w.delta}`;
  return w.pct == null ? `(${d})` : `(${d}, ${arrowPct(w.pct)}${label ? ' ' + label : ''})`;
};
// " (+1)" / " (0)" / "" — per-course certificate delta cell (null = new course, no prior).
const cd = (d) => (d == null ? '' : d > 0 ? ` (+${d})` : d < 0 ? ` (${d})` : ' (0)');
// Start rate — engaged ÷ enrolled as a %, "—" when nobody's enrolled yet.
const startPct = (en, eng) => (en ? `${Math.round((eng / en) * 100)}%` : '—');
// "+13 learners" / "+5 completions" — a signed count with a pluralised noun; "" when flat/no prior.
const countDelta = (w, noun) => {
  if (!w || w.delta == null || w.delta === 0) return '';
  const n = Math.abs(w.delta) === 1 ? noun : `${noun}s`;
  return `${w.delta > 0 ? '+' : ''}${w.delta} ${n}`;
};

export function renderText(m, config) {
  const o = m.overall;
  const L = [];
  // Header — one line: title · window (no clock noise) · ISO week
  L.push(`🎓 ${config.title}   ·   ${fmtDate(m.windowFrom)} → ${fmtDate(m.generatedAt)} · ${isoWeekLabel(m.generatedAt)}${m.isBaseline ? ' · baseline' : ''}`);
  L.push('');

  // TL;DR — the week in one line for skimmers
  const tldr = [countDelta(m.wow.learners, 'learner'), countDelta(m.wow.completed, 'completion')].filter(Boolean);
  if (m.content?.newCourses?.length) tldr.push(`${m.content.newCourses.join(', ')} shipped`);
  if (tldr.length) L.push(`📊 *TL;DR*  ${tldr.join(' · ')}`);

  // Activation signal — the one number that needs attention
  const gap = o.enrolled - o.engaged;
  if (gap > 0) L.push(`⚠️  ${gap} of ${o.enrolled} enrollments (${Math.round((gap / o.enrolled) * 100)}%) haven't started a lesson — activation is the gap`);
  L.push('');

  // FUNNEL — enrollments → started → completed, the core health story
  L.push('🔻 *FUNNEL* (vs last week)');
  L.push(`📝 Enrollments  ${wfmt(o.enrolled, m.wow.enrollments)}   ·   👥 ${wfmt(o.learners, m.wow.learners)} unique learners`);
  L.push(`▶️ Started      ${o.engaged}  ·  ${o.engagedRate}% of enrollments${wsuffix(m.wow.engaged)}`);
  const complP = wparen(m.wow.completed);
  L.push(`🏅 Completed     ${o.certificates}  ·  ${o.certRate == null ? '—' : `${o.certRate}%`} rate${complP ? ` ${complP}` : ''}`);
  const wap = o.learners ? Math.round((o.active / o.learners) * 100) : 0;
  L.push(`🔥 Active this week ${o.active}  ·  ${wap}% of learners`);
  if (m.certsByCollection?.length) L.push(`🎓 Certs by track  ${m.certsByCollection.map((g) => `${g.label} ${g.total}${cd(g.delta)}`).join(' · ')}`);
  L.push('');

  // Per-course table (monospace)
  const head = `${pad('BY COURSE', 28)}${pad('Live since', 13)}${pad('Enr(+new)', 11)}${pad('Start%', 7)}${pad('Done(+Δ)', 9)}${pad('Done%', 6)}Act`;
  const rows = [head];
  for (const c of m.courses) {
    rows.push(
      pad(c.name, 28) +
      pad(liveLabel(c.liveSince, m.generatedAt), 13) +
      pad(`${c.enrolled}${plus(c.newEnrolled)}`, 11) +
      pad(startPct(c.enrolled, c.engaged), 7) +
      pad(`${c.completed}${cd(c.certDelta)}`, 9) +
      pad(c.rate == null ? '—' : `${c.rate}%`, 6) + c.active,
    );
  }
  const lg = m.legacy;
  const lgDelta = m.certsByCollection?.find((g) => g.label === 'Legacy')?.delta ?? null;
  rows.push(
    pad(`— ${config.legacyLabel} (${lg.courseCount})`, 28) + pad('—', 13) +
    pad(`${lg.enrolled}${plus(lg.newEnrolled)}`, 11) +
    pad(startPct(lg.enrolled, lg.engaged), 7) + pad(`${lg.completed}${cd(lgDelta)}`, 9) + pad(lg.rate == null ? '—' : `${lg.rate}%`, 6) + lg.active,
  );
  L.push('```\n' + rows.join('\n') + '\n```');
  L.push('');

  // Content pipeline
  const ct = m.content;
  if (ct.baseline) {
    L.push(`📚 CONTENT  ${ct.liveCourseCount} live courses · ${ct.totalLessons} lessons  (baseline)`);
  } else {
    const news = ct.newCourses.length ? `  ·  new: ${ct.newCourses.join(', ')}` : '';
    const nc = ct.newCourses.length, nl = ct.lessonsAdded;
    L.push(`📚 CONTENT  ${ct.liveCourseCount} live courses · ${ct.totalLessons} lessons  →  +${nc} course${nc === 1 ? '' : 's'} · +${nl} lesson${nl === 1 ? '' : 's'} this week${news}`);
  }

  // Highlights
  const topNew = [...m.courses].filter((c) => c.newEnrolled > 0).sort((a, b) => b.newEnrolled - a.newEnrolled)[0];
  const best = [...m.courses].filter((c) => c.enrolled > 0 && c.rate != null).sort((a, b) => b.rate - a.rate)[0];
  const hl = [];
  if (topNew) hl.push(`🚀 Top enrollments: ${topNew.name} (+${topNew.newEnrolled})`);
  if (best) hl.push(`🏆 Best completion: ${best.name} (${best.rate}%)`);
  if (hl.length) L.push(hl.join('     '));

  // Footnote — be honest that "certs" is the completion proxy (the API exposes no real issuance).
  L.push('');
  L.push('_Certs = course completions (Thinkific issues a certificate on completion). WoW % hidden when prior week < 5._');
  return L.join('\n');
}

// Slack webhook payload. Whole message as one mrkdwn section keeps the code-block table aligned;
// `text` is the notification fallback.
export function renderSlack(m, config) {
  const text = renderText(m, config);
  return {
    text: `${config.title} · ${fmtDate(m.generatedAt)}`,
    blocks: [{ type: 'section', text: { type: 'mrkdwn', text } }],
  };
}
