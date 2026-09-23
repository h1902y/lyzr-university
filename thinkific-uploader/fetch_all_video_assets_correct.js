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
  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1440, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());
  await page.goto('https://lyzr.thinkific.com/manage/courses', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const fullAssetsQuery = `
    query GetCoursesAndVideoAssets {
      courses(first: 50) {
        nodes {
          id
          name
          status
          chapters {
            nodes {
              id
              name
              lessons {
                nodes {
                  __typename
                  ... on TextLesson { id name }
                  ... on VideoLesson { id name video { id filename } }
                  ... on PDFLesson { id name }
                }
              }
            }
          }
        }
      }
    }
  `;

  const fullResult = await page.evaluate(async (q) => {
    try {
      const res = await fetch('/api/graphql', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: q })
      });
      return await res.json();
    } catch (e) {
      return { error: e.message };
    }
  }, fullAssetsQuery);

  console.log("Raw GraphQL Response:");
  console.log(JSON.stringify(fullResult, null, 2).substring(0, 2000));

  const jsonPath = resolve(brainDir, 'gql_raw_response_dump.json');
  writeFileSync(jsonPath, JSON.stringify(fullResult, null, 2), 'utf-8');

  await context.close();
}

main().catch(console.error);
