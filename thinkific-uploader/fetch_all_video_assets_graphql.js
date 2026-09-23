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

  const introspectionData = await page.evaluate(async () => {
    const query = `
      query IntrospectVideoLesson {
        __type(name: "VideoLesson") {
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

  console.log("VideoLesson Fields:");
  console.log(JSON.stringify(introspectionData, null, 2));

  // Query all courses, chapters, lessons, and video assets using correct VideoLesson fields
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
                  ... on VideoLesson {
                    id
                    title
                    video {
                      id
                      filename
                      duration
                    }
                  }
                  ... on TextLesson {
                    id
                    title
                  }
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

  console.log("\nFull GraphQL Video Assets Query Result:");
  console.log(JSON.stringify(fullResult, null, 2).substring(0, 1500));

  const jsonPath = resolve(brainDir, 'gql_complete_thinkific_video_assets.json');
  writeFileSync(jsonPath, JSON.stringify(fullResult, null, 2), 'utf-8');
  console.log(`\nSaved complete result to: ${jsonPath}`);

  await context.close();
}

main().catch(console.error);
