import { generateCard, closeCardServer } from './src/cardgen.mjs';
import fs from 'node:fs';
import path from 'node:path';

const revampDir = '/Users/hkc/Documents/lyzr/university/revamp';
const jsonPath = '/Users/hkc/Documents/lyzr/university/revamp_upload_plan.json';
const thumbnailsDir = path.join(revampDir, 'thumbnails');

if (!fs.existsSync(thumbnailsDir)) {
  fs.mkdirSync(thumbnailsDir, { recursive: true });
}

console.log("==========================================================================");
console.log(" 🎨 RENDER ALL 49 LESSON THUMBNAIL CARDS (HIGH-END BRANDED CARDS)");
console.log("==========================================================================");

const planData = JSON.parse(fs.readFileSync(jsonPath, 'utf-8'));
console.log(`Loaded ${planData.length} lessons from plan JSON.`);

const ICON_MAP = {
  "Lyzr Foundations": "brain",
  "Lyzr for Business Professionals": "workflow",
  "Lyzr for Technical Professionals": "code"
};

function cleanNameNoNumbers(text) {
  if (!text) return "";
  let clean = text.replace(/^"|"$/g, '');
  clean = clean.replace(/^\s*Chapter\s*\d+\s*:\s*/i, '');
  clean = clean.replace(/^\s*Lesson\s*\d+\s*:\s*/i, '');
  clean = clean.replace(/^\s*C\d+_CH\d+_L\d+\s*/i, '');
  return clean.trim();
}

async function renderAllThumbnails() {
  let renderedCount = 0;

  for (let idx = 0; idx < planData.length; idx++) {
    const item = planData[idx];
    const courseName = item.course;
    const chName = cleanNameNoNumbers(item.chapter);
    const lTitle = cleanNameNoNumbers(item.lesson);
    const filename = item.filename;

    const slug = filename.replace(/\.mp4$/, '');
    const outPngPath = path.join(thumbnailsDir, `${slug}.png`);

    // Format Eyebrow: LYZR FOUNDATIONS · LESSON 01
    const shortCourse = courseName.replace("Lyzr for ", "").toUpperCase();
    const eyebrow = `${shortCourse} · LESSON ${String(idx + 1).padStart(2, '0')}`;

    // Title & Accent split
    const words = lTitle.split(/\s+/);
    const titleText = words.length > 1 ? words.slice(0, -1).join(' ') : '';
    const accentText = words.length > 1 ? words[words.length - 1] : lTitle;

    const subText = `with Lyzr Team · ${chName}`;
    const iconName = ICON_MAP[courseName] || 'brain';

    const cardParameters = {
      eyebrow: eyebrow,
      title: titleText,
      accent: accentText,
      sub: subText,
      pills: 'off',
      icon: iconName
    };

    console.log(`[${idx + 1}/${planData.length}] Rendering Thumbnail Card for '${slug}'...`);

    try {
      const generatedPath = await generateCard(cardParameters, `thumb_${slug}`);
      // Copy from cards/ to revamp/thumbnails/
      fs.copyFileSync(generatedPath, outPngPath);
      item['thumbnail_path'] = outPngPath;
      renderedCount++;
      console.log(`  ✓ Generated: ${outPngPath}`);
    } catch (err) {
      console.error(`  ❌ Error generating card for ${slug}:`, err.message);
    }
  }

  // Update revamp_upload_plan.json with thumbnail_path
  fs.writeFileSync(jsonPath, JSON.stringify(planData, null, 2), 'utf-8');

  closeCardServer();

  console.log("==========================================================================");
  console.log(` 🎉 Completed Rendering ${renderedCount}/49 Lesson Thumbnail Cards!`);
  console.log(`    Thumbnails Folder: ${thumbnailsDir}`);
  console.log("==========================================================================");
}

renderAllThumbnails();
