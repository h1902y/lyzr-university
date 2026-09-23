import { generateCard, closeCardServer } from './src/cardgen.mjs';
import fs from 'node:fs';
import path from 'node:path';

const revampDir = '/Users/hkc/Documents/lyzr/university/revamp';
const thumbnailsDir = path.join(revampDir, 'thumbnails');

if (!fs.existsSync(thumbnailsDir)) {
  fs.mkdirSync(thumbnailsDir, { recursive: true });
}

console.log("==========================================================================");
console.log(" 🎨 RENDERING SAMPLE LESSON THUMBNAIL CARD (LESSON 01)");
console.log("==========================================================================");

const sampleParams = {
  eyebrow: 'FOUNDATIONS · LESSON 01',
  title: 'Introduction to Lyzr',
  accent: 'Platform',
  sub: 'with Lyzr Team · Lyzr Platform & Ecosystem Overview',
  pills: 'off',
  icon: 'brain'
};

const slug = 'C01_CH01_L01_introduction_to_lyzr_platform';
const outPngPath = path.join(thumbnailsDir, `${slug}.png`);

try {
  const generatedPath = await generateCard(sampleParams, `thumb_${slug}`);
  fs.copyFileSync(generatedPath, outPngPath);
  console.log(` ✅ Generated Sample Thumbnail Card:`);
  console.log(`    📁 File Path: ${outPngPath}`);
} catch (err) {
  console.error(` ❌ Error generating sample card:`, err);
}

closeCardServer();
