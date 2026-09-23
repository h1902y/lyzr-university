// Per-course course-image generator. Derives card content from a catalog course entry and renders
// the dark "Player V1" template (catalog-demo/banner/player-card.html) to a 760x420@2x PNG via
// headless Chrome. Used by BOTH the create/update upload flow and the batch card refresh.
import http from 'node:http';
import { readFileSync, existsSync, statSync, mkdirSync } from 'node:fs';
import { join, extname } from 'node:path';
import { spawn } from 'node:child_process';
import { config } from './config.mjs';

const CHROME = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const DEMO = join(config.university, 'catalog-demo');
const CARDS = join(config.root, 'cards');
const MIME = { '.html':'text/html', '.png':'image/png', '.css':'text/css', '.js':'text/javascript', '.json':'application/json', '.svg':'image/svg+xml', '.jpg':'image/jpeg' };

let server = null, PORT = 8829;
function ensureServer() {
  if (server) return;
  server = http.createServer((req, res) => {
    const p = join(DEMO, decodeURIComponent(req.url.split('?')[0]));
    if (p.startsWith(DEMO) && existsSync(p) && statSync(p).isFile()) {
      res.setHeader('Content-Type', MIME[extname(p)] || 'application/octet-stream');
      res.end(readFileSync(p));
    } else { res.statusCode = 404; res.end('nf'); }
  });
  server.listen(PORT, '127.0.0.1');
}
export function closeCardServer() { if (server) { server.close(); server = null; } }

const run = (cmd, args) => new Promise((res, rej) => {
  const p = spawn(cmd, args); p.on('close', res); p.on('error', rej);
});

// Catalog course entry → card content. Eyebrow by collection/product, title split (last word = rust
// accent), instructor/product subtitle, video count, clean duration, and a per-collection icon.
function clean(s) { return (s || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, ''); }
function cleanDuration(d) {
  const m = String(d || '').match(/(\d+)\s*(hour|hr|h|min)/i);
  if (!m) return String(d || '').replace(/^~\s*/, '');
  const n = m[1], hr = /^h/i.test(m[2]);
  return hr ? `${n} ${n === '1' ? 'Hour' : 'Hours'}` : `${n} Minutes`;
}
// One distinctive icon per course (lucide names — see catalog-demo/banner/icons.js / build-icons.mjs).
// Falls back to a per-collection/product default for any slug not listed.
const ICON_BY_SLUG = {
  // ADK Track
  'track-adk-foundations': 'blocks', 'track-adk-multimodal': 'images',
  'track-adk-knowledge-memory': 'brain', 'track-adk-tools-workflows': 'wrench',
  'track-adk-gitagent-oss': 'git-branch',
  // Studio Track
  'track-studio-foundations': 'refresh-cw', 'track-studio-choosing-building': 'shapes',
  'track-studio-knowledge-rag': 'book-open', 'track-studio-orchestration': 'workflow',
  'track-studio-tools-models-mcp': 'plug', 'track-studio-voice': 'mic',
  'track-studio-knowledge-graph': 'share-2', 'track-studio-responsible-ai': 'shield-check',
  'track-studio-governance': 'scale', 'track-studio-test-simulate': 'flask-conical',
  'track-studio-evaluate-improve': 'trending-up', 'track-studio-deploy-scale': 'rocket',
  'track-studio-observability': 'activity', 'track-studio-reuse-distribute': 'package',
  // Architect
  'track-architect-fundamentals': 'drafting-compass',
  // Modules
  'module-agents': 'bot', 'module-models': 'cpu', 'module-memory': 'database',
  'module-knowledge-rag': 'book-open', 'module-tools-integrations': 'wrench',
  'module-orchestration': 'workflow', 'module-voice': 'mic',
  'module-responsible-ai': 'shield-check', 'module-evaluation': 'gauge',
  'module-multimodal': 'images', 'module-deployment': 'rocket',
  // Functions
  'function-hr': 'users', 'function-marketing': 'megaphone', 'function-sales': 'handshake',
  'function-procurement': 'shopping-cart', 'function-venture-capital': 'banknote',
  'function-ai-strategy': 'target',
  // Legacy
  'legacy-agent-building': 'hammer', 'legacy-agent-engineering-developers': 'code',
  'legacy-value-enablement-business': 'briefcase',
};

export function cardParams(c) {
  const coll = c.collection, product = c.product || '';
  const body = c.name.replace(/^(Studio|ADK|Architect)\s*:\s*/i, '').trim();
  const words = body.split(/\s+/);
  const title = words.length > 1 ? words.slice(0, -1).join(' ') : '';
  const accent = words.length > 1 ? words[words.length - 1] : body;
  let eyebrow;
  if (coll === 'track') eyebrow = `${product.toUpperCase()} · TRACK`;
  else if (coll === 'module') eyebrow = 'MODULE';
  else if (coll === 'function') eyebrow = 'USE CASE';
  else eyebrow = 'LYZR UNIVERSITY';
  const instr = c.instructor || 'Lyzr Team';
  const sub = product ? `with ${instr} · Lyzr ${product}` : `with ${instr} · All Products`;
  const icon = ICON_BY_SLUG[c.slug]
    || (product === 'ADK' ? 'code'
    : product === 'Studio' ? 'flow'
    : product === 'Architect' ? 'drafting-compass'
    : coll === 'module' ? 'blocks'
    : coll === 'function' ? 'target' : 'flow');
  return {
    eyebrow, title, accent, sub,
    videos: `${c.videos || c.lessons || 0} Videos`,
    duration: cleanDuration(c.duration),
    icon,
  };
}

/** Render the card PNG for a set of params. Returns the output path. */
export async function generateCard(params, slug) {
  ensureServer();
  mkdirSync(CARDS, { recursive: true });
  const out = join(CARDS, `${slug || clean(params.title + '-' + params.accent)}.png`);
  const qs = new URLSearchParams(params).toString();
  await run(CHROME, [
    '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
    '--force-device-scale-factor=2', '--window-size=760,420', '--virtual-time-budget=6000',
    '--default-background-color=00000000', '--run-all-compositor-stages-before-draw',
    `--screenshot=${out}`, `http://127.0.0.1:${PORT}/banner/player-card.html?${qs}`,
  ]);
  return out;
}

/** Convenience: catalog entry → rendered card PNG path. */
export async function cardForCourse(catalogCourse) {
  return generateCard(cardParams(catalogCourse), clean(catalogCourse.slug || catalogCourse.name));
}
