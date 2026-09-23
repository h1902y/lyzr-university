// Turn the Lyzr University upload bundle into a structured course list.
//
// Current bundle layout (collection-organized, no chapter subfolder):
//   thinkific-upload/<Collection>/<Product?>/<NN Course Title>/NNa <Lesson>.mp4
//                                                              NNb <Lesson> Notes.pdf
// e.g.  1 - Tracks/Studio/07 Studio Design and Create/01a What agent type....mp4
//
// A "course" is any leaf folder that DIRECTLY contains NNa/NNb media files. Coming-soon folders
// hold only placeholder decks ("01 Welcome.pdf" — no a/b), so they don't match and are skipped.
// Each course is one implicit chapter (our bundle has no chapter level).
import { readdirSync, statSync } from 'node:fs';
import { join, relative, sep } from 'node:path';

const FILE_RE = /^(\d{2})([ab])\s+(.+)\.(mp4|pdf)$/;          // NNa Title.mp4 / NNb Title Notes.pdf
const isDir  = (p) => { try { return statSync(p).isDirectory(); } catch { return false; } };
const entries = (p) => readdirSync(p).sort();

function lessonsIn(dir) {
  const lessons = [];
  for (const name of entries(dir)) {
    const full = join(dir, name);
    if (isDir(full)) continue;
    const m = name.match(FILE_RE);
    if (!m) continue;
    const [, num, part, title, ext] = m;
    lessons.push({
      order: Number(num) * 10 + (part === 'a' ? 0 : 1),     // video (a) before its notes (b)
      num,
      type: ext === 'mp4' ? 'video' : 'pdf',
      title: title.replace(/\s+Notes$/, ''),                // drop the structural "Notes" suffix
      file: full,
      key: `${relative_(dir)}//${num}${part}`,              // stable id for resume
    });
  }
  return lessons.sort((a, b) => a.order - b.order);
}

let BUNDLE_ROOT = '';
const relative_ = (p) => relative(BUNDLE_ROOT, p);

// "07 Studio Design and Create" -> "Studio Design and Create"; chapter name drops the product word.
const stripIndex = (s) => s.replace(/^\d{2,}\s+/, '').replace(/\s+\(Coming Soon\)$/i, '').trim();
const chapterName = (courseTitle) => courseTitle.replace(/^(ADK|Studio|Architect)\s+/i, '').trim() || courseTitle;

function walk(dir, acc) {
  const here = lessonsIn(dir);
  if (here.length) {
    const rel = relative(BUNDLE_ROOT, dir);
    const parts = rel.split(sep);                            // [<Collection>, <Product?>, <NN Course>]
    const collection = parts[0]?.replace(/^\d+\s*-\s*/, '') || '';   // "1 - Tracks" -> "Tracks"
    const product = parts.length >= 3 ? parts[1] : '';       // "Studio" / "ADK" / ""
    const title = stripIndex(parts[parts.length - 1]);
    acc.push({
      title,
      folder: parts[parts.length - 1],
      collection,
      product,
      dir,
      chapters: [{ title: chapterName(title), lessons: here }],
    });
    return;                                                   // leaf course — don't descend further
  }
  for (const name of entries(dir)) {
    const full = join(dir, name);
    if (isDir(full)) walk(full, acc);
  }
}

export function readBundle(bundleDir) {
  BUNDLE_ROOT = bundleDir;
  const courses = [];
  walk(bundleDir, courses);
  return courses.sort((a, b) => a.folder.localeCompare(b.folder));
}

export function summarize(courses) {
  let video = 0, pdf = 0;
  for (const c of courses) for (const ch of c.chapters) for (const l of ch.lessons) (l.type === 'video' ? video++ : pdf++);
  return { courses: courses.length, video, pdf, lessons: video + pdf };
}
