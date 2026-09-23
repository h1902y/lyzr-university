// Match each bundle course to its catalog-data.json metadata + its generated card image,
// so the uploader can fill course details, set the thumbnail, price, collection, and publish state
// with no manual data entry.
import { readFileSync, existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const norm = (s) => (s || '').toLowerCase().replace(/&/g, 'and').replace(/[^a-z0-9]+/g, ' ').trim();
const toks = (s) => new Set(norm(s).split(' ').filter(Boolean));
const overlap = (a, b) => { let n = 0; for (const t of a) if (b.has(t)) n++; return n; };

export function loadCatalog(catalogPath) {
  const data = JSON.parse(readFileSync(catalogPath, 'utf8'));
  return data.courses || [];
}

// Best course match by token overlap on the folder/title vs catalog course name.
export function matchCourse(course, catalogCourses) {
  const ct = toks(`${course.title} ${course.product}`);
  let best = null, bs = 0;
  for (const c of catalogCourses) {
    const sc = overlap(ct, toks(c.name));
    if (sc > bs) { bs = sc; best = c; }
  }
  return bs >= 2 ? best : null;
}

// Find the generated card banner (760x420) whose filename tokens overlap the course.
export function findCard(course, bannerDir) {
  if (!existsSync(bannerDir)) return null;
  const ct = toks(`${course.title} ${course.product}`);
  let best = null, bs = 0;
  for (const f of readdirSync(bannerDir)) {
    if (!/card.*\.png$/i.test(f)) continue;
    const sc = overlap(ct, toks(f.replace(/card.*$/i, '')));
    if (sc > bs) { bs = sc; best = join(bannerDir, f); }
  }
  return bs >= 2 ? best : null;
}

// Resolve the full publish-time metadata for a course (catalog + card), with safe fallbacks.
export function resolveMeta(course, catalogCourses, bannerDir) {
  const cat = matchCourse(course, catalogCourses);
  const card = findCard(course, bannerDir);
  return {
    name: cat?.name || course.title,
    subtitle: cat?.subtitle || '',
    description: cat?.description || '',
    slug: cat?.slug || '',
    collectionName: cat?.collection || course.collection || '',  // Tracks/Modules/Functions
    free: true,                                                  // Lyzr University courses are free
    publish: (cat?.status || '') === 'live',
    card,
    cat,                                                         // matched catalog entry (for card generation)
    matched: !!cat,
  };
}
