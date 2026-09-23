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

  const queryInfo = await page.evaluate(async () => {
    const query = `
      query IntrospectQuery {
        __type(name: "Query") {
          name
          fields {
            name
            type {
              name
              kind
            }
          }
        }
      }
    `;

    try {
      const res = await fetch('/api/graphql', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query })
      });
      return await res.json();
    } catch (e) {
      return { error: e.message };
    }
  });

  console.log("Root Query Fields on Thinkific GraphQL API:");
  const fields = queryInfo.data.__type.fields.map(f => f.name);
  console.log(fields);

  // Now query courses with chapters -> lessons -> video asset
  const fullCoursesQuery = `
    query GetCoursesAndLessons {
      courses(first: 50) {
        nodes {
          id
          name
          slug
          status
          chapters {
            id
            name
            lessons {
              __typename
              id
              name
              ... on VideoLesson {
                video {
                  id
                  filename
                  duration
                  downloadUrl
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
  }, fullCoursesQuery);

  console.log("\nFull Courses & Video Assets Result:");
  console.log(JSON.stringify(fullResult, null, 2).substring(0, 1000));

  const jsonPath = resolve(brainDir, 'thinkific_graphql_full_catalog_assets.json');
  writeFileSync(jsonPath, JSON.stringify(fullResult, null, 2), 'utf-8');
  console.log(`\nSaved output to ${jsonPath}`);

  await context.close();
}

main().catch(console.error);
