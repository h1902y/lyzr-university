// University Pulse — weekly Slack analytics digest.
//   node pulse.mjs --dry-run        # compute + print message, no Slack, no snapshot write
//   node pulse.mjs --channel-test   # post to SLACK_WEBHOOK_URL, do NOT write a snapshot
//   node pulse.mjs                   # post + write snapshot (the GitHub Action commits it back)
import { readFileSync, writeFileSync, existsSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import { makeClient } from './lib/thinkific.mjs';
import { compute, toSnapshot } from './lib/compute.mjs';
import { renderText, renderSlack } from './lib/render.mjs';

const HERE = dirname(fileURLToPath(import.meta.url));
const SNAP_DIR = join(HERE, 'snapshots');
const LATEST = join(SNAP_DIR, 'latest.json');
const args = new Set(process.argv.slice(2));
const DRY = args.has('--dry-run');
const TEST = args.has('--channel-test');
const EMIT = args.has('--emit');   // print message + write snapshot, do NOT auto-post (manual/connector post)

const config = JSON.parse(readFileSync(join(HERE, 'config.json'), 'utf8'));
const nowISO = new Date().toISOString();
const prev = existsSync(LATEST) ? JSON.parse(readFileSync(LATEST, 'utf8')) : null;

const client = makeClient();
console.error('fetching enrollments…');
const enrollments = await client.getAll('enrollments');
console.error(`  ${enrollments.length} enrollments`);
console.error('computing (lesson counts per course)…');
const model = await compute(client, config, enrollments, prev, nowISO);

if (DRY || EMIT) {
  console.log('\n' + renderText(model, config) + '\n');
  console.error(prev ? `(window since ${prev.generatedAt})` : '(first run — baseline, no deltas)');
  if (EMIT) {
    mkdirSync(SNAP_DIR, { recursive: true });
    const snap = toSnapshot(model);
    writeFileSync(join(SNAP_DIR, `${nowISO.slice(0, 10)}.json`), JSON.stringify(snap, null, 2));
    writeFileSync(LATEST, JSON.stringify(snap, null, 2));
    console.error(`✓ snapshot written (next week diffs against this)`);
  }
  process.exit(0);
}

// Post to Slack — bot token (chat.postMessage) preferred; incoming webhook as fallback.
const payload = renderSlack(model, config);
const botToken = process.env.SLACK_BOT_TOKEN;
const channel = process.env.SLACK_CHANNEL || config.channelId;
const webhook = process.env.SLACK_WEBHOOK_URL;
if (botToken && channel) {
  const res = await fetch('https://slack.com/api/chat.postMessage', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=utf-8', Authorization: `Bearer ${botToken}` },
    body: JSON.stringify({ channel, ...payload }),
  });
  const j = await res.json().catch(() => ({}));
  if (!res.ok || !j.ok) {
    const hint = j.error === 'not_in_channel' ? ' (invite the bot to the channel)' : '';
    console.error(`✗ Slack chat.postMessage failed: ${j.error || res.status}${hint}`);
    process.exit(1);
  }
  console.error(`✓ posted to Slack (${channel})`);
} else if (webhook) {
  const res = await fetch(webhook, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!res.ok) { console.error(`✗ Slack ${res.status}: ${await res.text()}`); process.exit(1); }
  console.error('✓ posted to Slack (webhook)');
} else {
  console.error('✗ No Slack destination: set SLACK_BOT_TOKEN (+ SLACK_CHANNEL or config.channelId), or SLACK_WEBHOOK_URL');
  process.exit(1);
}

if (TEST) { console.error('(--channel-test: snapshot NOT written)'); process.exit(0); }

// Persist snapshot (dated + latest) — the workflow commits these back to the repo.
mkdirSync(SNAP_DIR, { recursive: true });
const snap = toSnapshot(model);
const dated = join(SNAP_DIR, `${nowISO.slice(0, 10)}.json`);
writeFileSync(dated, JSON.stringify(snap, null, 2));
writeFileSync(LATEST, JSON.stringify(snap, null, 2));
console.error(`✓ snapshot written: ${dated.replace(HERE + '/', '')}`);
