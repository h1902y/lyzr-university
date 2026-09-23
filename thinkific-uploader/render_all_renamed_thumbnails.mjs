import { generateCard, closeCardServer } from './src/cardgen.mjs';
import fs from 'node:fs';
import path from 'node:path';

const revampDir = '/Users/hkc/Documents/lyzr/university/revamp';
const thumbnailsDir = path.join(revampDir, 'thumbnails');
const planJsonPath = '/Users/hkc/Documents/lyzr/university/revamp_upload_plan.json';

if (!fs.existsSync(thumbnailsDir)) {
  fs.mkdirSync(thumbnailsDir, { recursive: true });
}

console.log("==========================================================================");
console.log(" 🎨 REGENERATING THUMBNAIL PNG CARDS WITH NEW COURSE NAMES");
console.log("==========================================================================");

const planData = JSON.parse(fs.readFileSync(planJsonPath, 'utf8'));

async function run() {
  let count = 0;
  for (const item of planData) {
    const c = item.course.strip ? item.course.strip() : item.course;
    const slug = item.filename.replace('.mp4', '');
    
    let eyebrow = 'FOUNDATIONS';
    let icon = 'brain';

    if (c === 'Lyzr Platform Studio') {
      eyebrow = 'PLATFORM STUDIO';
      icon = 'workflow';
    } else if (c === 'Lyzr Code Libraries') {
      eyebrow = 'CODE LIBRARIES';
      icon = 'code';
    }

    // Parse lesson number
    const match = item.filename.match(/L(\d+)/);
    const lessonNum = match ? match[1] : '01';
    eyebrow = `${eyebrow} · LESSON ${lessonNum}`;

    // Clean title & accent
    const titleParts = item.lesson.split(':');
    let titleStr = titleParts[0].trim();
    let accentStr = titleParts.length > 1 ? titleParts[1].trim() : '';

    if (!accentStr && titleStr.includes(' ')) {
      const words = titleStr.split(' ');
      accentStr = words.pop();
      titleStr = words.join(' ');
    }

    const params = {
      eyebrow: eyebrow,
      title: titleStr,
      accent: accentStr || titleStr,
      sub: `with Lyzr Team · ${item.chapter}`,
      pills: 'off',
      icon: icon
    };

    try {
      const generatedPath = await generateCard(params, `thumb_${slug}`);
      const destPath = path.join(thumbnailsDir, `${slug}.png`);
      fs.copyFileSync(generatedPath, destPath);
      count++;
      console.log(`  ✓ [${count}/${planData.length}] Regenerated Card: ${path.basename(destPath)} (${eyebrow})`);
    } catch (err) {
      console.error(`  ❌ Error generating card for ${slug}:`, err.message);
    }
  }

  closeCardServer();
  console.log("\n==========================================================================");
  console.log(` 🎉 REGENERATED ALL ${count} THUMBNAIL PNG CARDS WITH NEW COURSE NAMES!`);
  console.log("==========================================================================");
}

run();
