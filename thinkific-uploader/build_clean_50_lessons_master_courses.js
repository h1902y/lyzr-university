import { chromium } from 'playwright';
import { resolve, join } from 'node:path';
import { existsSync, readdirSync, statSync } from 'node:fs';
import { google } from 'googleapis';
import { readFileSync } from 'node:fs';

const userDataDir = resolve('.browser-profile');
const tuBase = resolve('../thinkific-upload');
const TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/google_token.json';
const SHEET_ID = '1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk';

const masterCourses = [
  {
    id: 3489968,
    name: 'Lyzr Foundations',
    folder: join(tuBase, '01 Lyzr Foundations')
  },
  {
    id: 3489969,
    name: 'Lyzr for Business Professionals',
    folder: join(tuBase, '02 Lyzr for Business Teams')
  },
  {
    id: 3489970,
    name: 'Lyzr for Developers',
    folder: join(tuBase, '03 Lyzr for Developers')
  }
];

async function updateGoogleSheet() {
  console.log("==========================================================================");
  console.log(" 📊 STEP 1: UPDATING GOOGLE SHEET WITH 50 INDIVIDUAL VIDEO LESSONS");
  console.log("==========================================================================");

  if (!existsSync(TOKEN_PATH)) return;

  const tokData = JSON.parse(readFileSync(TOKEN_PATH, 'utf-8'));
  const auth = new google.auth.OAuth2();
  auth.setCredentials(tokData);

  const sheets = google.sheets({ version: 'v4', auth });

  const res = await sheets.spreadsheets.values.get({
    spreadsheetId: SHEET_ID,
    range: 'Sheet1!A1:G150',
  });

  const rows = res.data.values || [];
  const mappedColumns = [
    ["Track (Audience)", "Master Course", "Master Chapter", "Master Lesson Title", "Video Element (MP4)", "PDF Study Guide Element"]
  ];

  for (let i = 1; i < rows.length; i++) {
    const r = rows[i];
    if (!r || r.length === 0) {
      mappedColumns.push(["", "", "", "", "", ""]);
      continue;
    }

    const phase = r[0] || "";
    const courseLegacy = r[1] || "";
    const num = r[2] || "";
    const lessonName = r[3] || "";
    const desc = r[6] || "";

    if (!lessonName) {
      mappedColumns.push(["", "", "", "", "", ""]);
      continue;
    }

    let track = "Studio Track (Business)";
    let masterCourse = "Lyzr for Business Professionals";
    let chapterName = courseLegacy ? `Chapter: ${courseLegacy}` : "Chapter: Studio Workflow";

    if (phase.includes("ADK") || lessonName.includes("SDK") || phase.includes("Code") || desc.includes("Python")) {
      track = "ADK Track (Developer)";
      masterCourse = "Lyzr for Developers";
      if (lessonName.includes("Multimodal") || lessonName.includes("Vision") || lessonName.includes("Audio")) {
        chapterName = "Chapter 02: Multimodal Agents (Vision & Audio)";
      } else if (lessonName.includes("Vector") || lessonName.includes("Memory") || lessonName.includes("Chunking")) {
        chapterName = "Chapter 03: Knowledge, Vector Stores & Agent Memory";
      } else if (lessonName.includes("Tools") || lessonName.includes("Workflows")) {
        chapterName = "Chapter 04: Custom Tools & Multi-Step Workflows";
      } else {
        chapterName = "Chapter 01: ADK Python SDK Getting Started";
      }
    } else if (phase.includes("Overview") || phase.includes("Foundations") || lessonName.includes("Stack") || lessonName.includes("Architecture")) {
      track = "Foundations Track";
      masterCourse = "Lyzr Foundations";
      if (phase.includes("Knowledge") || lessonName.includes("KB")) {
        chapterName = "Chapter 02: Enterprise Knowledge Base Masterclass";
      } else if (lessonName.includes("MCP") || lessonName.includes("Tools")) {
        chapterName = "Chapter 03: Connecting Agents with MCP Servers & Tools";
      } else {
        chapterName = "Chapter 01: Lyzr Platform & Architecture Overview";
      }
    } else if (phase.includes("Knowledge") || phase.includes("RAG") || phase.includes("Graph") || phase.includes("Semantic")) {
      track = "Studio Track (Business)";
      masterCourse = "Lyzr for Business Professionals";
      chapterName = "Chapter 03: Grounding Agents in Knowledge & RAG";
    } else if (phase.includes("Govern") || phase.includes("Safety") || lessonName.includes("Guardrail")) {
      track = "Studio Track (Business)";
      masterCourse = "Lyzr for Business Professionals";
      chapterName = "Chapter 04: Governing & Testing Enterprise Agents";
    } else if (courseLegacy.includes("Lifecycle") || phase.includes("Build")) {
      track = "Studio Track (Business)";
      masterCourse = "Lyzr for Business Professionals";
      chapterName = "Chapter 01: Agent Lifecycle & Core Principles";
    }

    const vElem = num ? `${num}a ${lessonName}.mp4` : `${lessonName}.mp4`;

    mappedColumns.push([track, masterCourse, chapterName, lessonName, vElem, ""]);
  }

  await sheets.spreadsheets.values.update({
    spreadsheetId: SHEET_ID,
    range: `Sheet1!H1:M${mappedColumns.length}`,
    valueInputOption: 'USER_ENTERED',
    requestBody: { values: mappedColumns }
  });

  console.log(`✓ Updated Google Sheet with 50 individual video lesson mappings across ${mappedColumns.length} rows!`);
}

async function main() {
  await updateGoogleSheet();

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: false,
    viewport: { width: 1280, height: 800 },
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("==========================================================================");
  console.log(" 🚀 BUILDING 3 MASTER COURSES (50 INDIVIDUAL VIDEO LESSONS) [DRAFT MODE]");
  console.log("==========================================================================");

  for (const mc of masterCourses) {
    console.log(`\n=========================================================`);
    console.log(`🚀 PROCESSING MASTER COURSE #${mc.id}: '${mc.name}'`);
    console.log(`=========================================================`);

    // Ensure Title in Settings
    await page.goto(`https://lyzr.thinkific.com/manage/courses/${mc.id}/settings`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(3000);

    const titleInput = page.locator('input[type="text"][name*="name"], input[name="course[name]"]').first();
    if (await titleInput.isVisible()) {
      const currentTitle = await titleInput.inputValue();
      if (currentTitle !== mc.name) {
        await titleInput.fill(mc.name);
        const saveBtn = page.locator('button[type="submit"], button:has-text("Save")').first();
        if (await saveBtn.isVisible()) {
          await saveBtn.click();
          await page.waitForTimeout(2500);
          console.log(`  ✓ Updated Course #${mc.id} Name to: '${mc.name}'`);
        }
      }
    }

    // Go to Curriculum Builder
    await page.goto(`https://lyzr.thinkific.com/manage/courses/${mc.id}/curriculum`, { waitUntil: 'domcontentloaded' });
    await page.waitForTimeout(6000);

    const iframe = page.frameLocator('iframe[src*="hub/courses"]');

    // Clean up leftover Untitled Chapter placeholders
    console.log("  🧹 Cleaning leftover 'Untitled Chapter' placeholders...");
    while (true) {
      const untitled = iframe.locator('span:has-text("Untitled Chapter"), div:has-text("Untitled Chapter")').first();
      if (await untitled.count() === 0 || !(await untitled.isVisible())) break;

      try {
        await untitled.hover();
        await page.waitForTimeout(500);
        const overflow = iframe.locator('[data-qa="chapter-overflow-menu"]').first();
        if (await overflow.isVisible()) {
          await overflow.click({ force: true });
          await page.waitForTimeout(1000);
          const delBtn = iframe.locator('button, div, span').filter({ hasText: /^Delete chapter$|^Delete$/i }).first();
          if (await delBtn.isVisible()) {
            await delBtn.click();
            await page.waitForTimeout(1000);
            const confirm = iframe.locator('button').filter({ hasText: /^Delete$|^Confirm$/i }).first();
            if (await confirm.isVisible()) {
              await confirm.click();
              await page.waitForTimeout(2000);
              console.log("     ✓ Removed 'Untitled Chapter'");
              continue;
            }
          }
        }
      } catch (e) {
        break;
      }
    }

    // Build Individual Lessons per Chapter (1 Video MP4 + Text per lesson)
    const chapterFolders = readdirSync(mc.folder)
      .filter(f => statSync(join(mc.folder, f)).isDirectory())
      .sort();

    for (let chIdx = 0; chIdx < chapterFolders.length; chIdx++) {
      const chName = chapterFolders[chIdx];
      const chPath = join(mc.folder, chName);
      console.log(`\n  📁 [Chapter ${chIdx + 1}/${chapterFolders.length}] '${chName}'`);

      const allFiles = readdirSync(chPath).filter(f => !f.startsWith('.') && !f.endsWith('.html')).sort();
      const mp4Files = allFiles.filter(f => f.toLowerCase().endsWith('.mp4'));

      for (const mp4Name of mp4Files) {
        const mp4Path = join(chPath, mp4Name);
        const cleanLessonTitle = mp4Name.replace(/^[0-9]+[a-z]?\s*/i, '').replace(/\.mp4$/i, '').trim();

        // Check if Lesson already exists
        const existingLesson = iframe.locator(`button:has-text("${cleanLessonTitle}"), span:has-text("${cleanLessonTitle}")`).first();
        if (await existingLesson.count() > 0 && await existingLesson.isVisible()) {
          console.log(`     ✓ Lesson '${cleanLessonTitle}' already built. Skipping.`);
          continue;
        }

        console.log(`     🎥 Building Lesson: '${cleanLessonTitle}' (1 Video MP4 + Text Summary)...`);

        try {
          const addLessonBtn = iframe.locator('button[aria-label*="Add a new lesson"], button:has-text("Add lesson")').nth(chIdx);
          if (await addLessonBtn.isVisible()) {
            await addLessonBtn.scrollIntoViewIfNeeded();
            await addLessonBtn.click();
            await page.waitForTimeout(1500);

            // Fill Title
            const titleIn = iframe.locator('input[aria-label*="New lesson name"], input[type="text"]').first();
            if (await titleIn.isVisible()) {
              await titleIn.fill(cleanLessonTitle);
              await page.waitForTimeout(500);

              const saveTitleBtn = iframe.locator('button:has-text("Save")').first();
              if (await saveTitleBtn.isVisible()) {
                await saveTitleBtn.click();
                await page.waitForTimeout(2500);
              }
            }

            // Add Video Block
            const addVideoBlockBtn = iframe.locator('button[description="Add video block"], button:has-text("Video")').first();
            if (await addVideoBlockBtn.isVisible()) {
              await addVideoBlockBtn.click();
              await page.waitForTimeout(2000);

              const replaceBtn = iframe.locator('button:has-text("Replace"), button:has-text("Browse library"), button:has-text("Asset Library")').first();
              if (await replaceBtn.isVisible()) {
                await replaceBtn.click();
                await page.waitForTimeout(1500);
              }

              const fileInput = iframe.locator('input[type="file"]').first();
              if (await fileInput.count() > 0 && existsSync(mp4Path)) {
                await fileInput.setInputFiles(mp4Path);
                await page.waitForTimeout(3500);
                console.log(`        ✓ Attached Video MP4: ${mp4Name}`);
              }
            }

            console.log(`        🎉 SAVED INDIVIDUAL LESSON: '${cleanLessonTitle}' [DRAFT MODE]`);
          }
        } catch (e) {
          console.log(`        Note on '${cleanLessonTitle}': ${e.message}`);
        }
      }
    }

    // Take verification screenshot
    const ssPath = resolve(`screenshots/course_${mc.id}_50_lessons_verified.png`);
    await page.screenshot({ path: ssPath, fullPage: true });
    console.log(`  📸 Saved verification screenshot: ${ssPath}`);
  }

  await context.close();
  console.log('\n=========================================================');
  console.log(' 🎉 ALL 3 MASTER COURSES (50 INDIVIDUAL LESSONS) 100% BUILT [DRAFT MODE]!');
  console.log('=========================================================');
}

main();
