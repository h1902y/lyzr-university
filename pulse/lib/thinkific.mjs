// Thinkific public REST API client for the University Pulse — read-only.
// Auth: OAuth Bearer token. Token from THINKIFIC_TOKEN env (cloud/CI) or a local .env fallback (dev).
// Cloudflare fronts the API and 403s non-browser User-Agents, so we send a browser UA.
import { readFileSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const BASE = 'https://api.thinkific.com/api/public/v1';
const UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36';
const HERE = dirname(fileURLToPath(import.meta.url));

export function readToken() {
  if (process.env.THINKIFIC_TOKEN) return process.env.THINKIFIC_TOKEN.trim();
  // Dev fallback: lyzr-university/.env (pulse/ is one level under it) → TOKEN=...
  for (const p of [join(HERE, '../../.env'), join(HERE, '../.env')]) {
    if (existsSync(p)) {
      const m = readFileSync(p, 'utf8').match(/^\s*TOKEN\s*=\s*(.+)\s*$/m);
      if (m) return m[1].trim();
    }
  }
  throw new Error('No Thinkific token: set THINKIFIC_TOKEN or add TOKEN= to lyzr-university/.env');
}

export function makeClient(token = readToken()) {
  const headers = { Authorization: `Bearer ${token}`, 'User-Agent': UA };
  async function get(path, attempt = 0) {
    const res = await fetch(`${BASE}/${path}`, { headers });
    if (res.status === 429 && attempt < 5) {
      const wait = (parseInt(res.headers.get('retry-after') || '2', 10) || 2) * 1000;
      await new Promise((r) => setTimeout(r, wait));
      return get(path, attempt + 1);
    }
    if (!res.ok) throw new Error(`Thinkific ${res.status} on ${path}: ${(await res.text()).slice(0, 200)}`);
    return res.json();
  }
  // Page through a list endpoint until pagination.next_page is null.
  async function getAll(path) {
    const items = [];
    let page = 1;
    for (;;) {
      const sep = path.includes('?') ? '&' : '?';
      const d = await get(`${path}${sep}limit=250&page=${page}`);
      items.push(...(d.items || []));
      if (!d.meta?.pagination?.next_page) break;
      page += 1;
    }
    return items;
  }
  return { get, getAll };
}

// Σ lessons (contents) across a course's chapters.
export async function lessonCount(client, courseId) {
  const course = await client.get(`courses/${courseId}`);
  let n = 0;
  for (const chId of course.chapter_ids || []) {
    const ch = await client.get(`chapters/${chId}`);
    n += (ch.content_ids || []).length;
  }
  return n;
}
