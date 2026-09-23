import { google } from 'googleapis';
import { readFileSync, existsSync } from 'node:fs';

const TOKEN_PATH = '/Users/hkc/.gemini/antigravity-ide/google_token.json';
const SHEET_ID = '1p2vAr_hP7cGhMJR7YkZ-YxKGlxOGT5bY9ynLskOMxPk';

async function main() {
  console.log("==========================================================================");
  console.log(" STEP 1: UPDATING GOOGLE SHEET MAPPING (COLUMNS H TO M)");
  console.log("==========================================================================");

  if (!existsSync(TOKEN_PATH)) {
    console.error("Token missing.");
    return;
  }

  const tokData = JSON.parse(readFileSync(TOKEN_PATH, 'utf-8'));
  const auth = new google.auth.OAuth2();
  auth.setCredentials(tokData);

  const sheets = google.sheets({ version: 'v4', auth });

  // 1. Fetch current Sheet1 values
  const res = await sheets.spreadsheets.values.get({
    spreadsheetId: SHEET_ID,
    range: 'Sheet1!A1:G150',
  });

  const rows = res.data.values || [];
  console.log(`✓ Read ${rows.length} existing rows from Sheet1 (Columns A:G preserved).`);

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
    let masterCourse = "Lyzr for Business Teams";
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
      masterCourse = "Lyzr for Business Teams";
      chapterName = "Chapter 03: Grounding Agents in Knowledge & RAG";
    } else if (phase.includes("Govern") || phase.includes("Safety") || lessonName.includes("Guardrail")) {
      track = "Studio Track (Business)";
      masterCourse = "Lyzr for Business Teams";
      chapterName = "Chapter 04: Governing & Testing Enterprise Agents";
    } else if (courseLegacy.includes("Lifecycle") || phase.includes("Build")) {
      track = "Studio Track (Business)";
      masterCourse = "Lyzr for Business Teams";
      chapterName = "Chapter 01: Agent Lifecycle & Orchestration";
    }

    const vElem = num ? `${num}a ${lessonName}.mp4` : `${lessonName}.mp4`;
    const pdfElem = num ? `${num}b ${lessonName} Notes.pdf` : `${lessonName} Notes.pdf`;

    mappedColumns.push([track, masterCourse, chapterName, lessonName, vElem, pdfElem]);
  }

  // Update Columns H to M for all rows
  await sheets.spreadsheets.values.update({
    spreadsheetId: SHEET_ID,
    range: `Sheet1!H1:M${mappedColumns.length}`,
    valueInputOption: 'USER_ENTERED',
    requestBody: { values: mappedColumns }
  });

  console.log(`🎉 STEP 1 COMPLETE: Updated Columns H:M (Track > Course > Chapter > Lesson > Elements) across ${mappedColumns.length} rows!`);
}

main();
