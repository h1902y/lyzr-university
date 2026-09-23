import { chromium } from 'playwright';
import { resolve } from 'node:path';
import { rmSync, existsSync, writeFileSync } from 'node:fs';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const brainDir = resolve('/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61');

for (const lockFile of ['SingletonLock', 'SingletonSocket', 'SingletonCookie']) {
  const p = resolve(userDataDir, lockFile);
  if (existsSync(p)) {
    try { rmSync(p, { force: true }); } catch (e) {}
  }
}

async function main() {
  console.log("==========================================================================");
  console.log(" 🌐 QUERYING OFFICIAL THINKIFIC REST/GRAPHQL API FOR ALL ASSETS");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("1. Navigating to Thinkific Admin to initialize session...");
  await page.goto('https://lyzr.thinkific.com/manage/courses', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  console.log("2. Querying Thinkific API via authenticated session...");
  const apiResult = await page.evaluate(async () => {
    const results = {};

    // 1. Try Thinkific REST API /api/v1/assets
    try {
      const res = await fetch('/api/v1/assets?page=1&limit=100');
      if (res.ok) {
        results.assetsV1 = await res.json();
      } else {
        results.assetsV1Error = `Status ${res.status}: ${res.statusText}`;
      }
    } catch (e) {
      results.assetsV1Error = e.message;
    }

    // 2. Try Thinkific REST API /api/public/v1/assets
    try {
      const res = await fetch('/api/public/v1/assets?page=1&limit=100');
      if (res.ok) {
        results.assetsPublicV1 = await res.json();
      } else {
        results.assetsPublicV1Error = `Status ${res.status}: ${res.statusText}`;
      }
    } catch (e) {
      results.assetsPublicV1Error = e.message;
    }

    // 3. Try Thinkific GraphQL API
    try {
      const gqlRes = await fetch('/api/graphql', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          query: `{
            assets(first: 100) {
              edges {
                node {
                  id
                  filename
                  name
                  status
                  duration
                  createdAt
                }
              }
            }
          }`
        })
      });
      if (gqlRes.ok) {
        results.gqlAssets = await gqlRes.json();
      }
    } catch (e) {
      results.gqlError = e.message;
    }

    return results;
  });

  console.log("API Query Results Summary:");
  console.log(JSON.stringify(apiResult, null, 2));

  const jsonPath = resolve(brainDir, 'thinkific_official_api_assets.json');
  writeFileSync(jsonPath, JSON.stringify(apiResult, null, 2), 'utf-8');
  console.log(`\n💾 Saved API output to: ${jsonPath}`);

  await context.close();
}

main().catch(console.error);
