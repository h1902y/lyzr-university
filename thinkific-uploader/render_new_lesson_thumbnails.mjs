import { generateCard, closeCardServer } from './src/cardgen.mjs';
import fs from 'node:fs';
import path from 'node:path';

const revampDir = '/Users/hkc/Documents/lyzr/university/revamp';
const thumbnailsDir = path.join(revampDir, 'thumbnails');

if (!fs.existsSync(thumbnailsDir)) {
  fs.mkdirSync(thumbnailsDir, { recursive: true });
}

console.log("==========================================================================");
console.log(" 🎨 RENDERING THUMBNAIL CARDS FOR 2 NEW DESCRIPT LESSONS");
console.log("==========================================================================");

const newCards = [
  {
    slug: 'C01_CH01_L04_lyzr_platform_pricing',
    params: {
      eyebrow: 'FOUNDATIONS · LESSON 04',
      title: 'Lyzr Platform Pricing & Token',
      accent: 'Economics',
      sub: 'with Lyzr Team · Lyzr Platform & Ecosystem Overview',
      pills: 'off',
      icon: 'banknote'
    }
  },
  {
    slug: 'C03_CH04_L03_gitagent_harness',
    params: {
      eyebrow: 'TECHNICAL · LESSON 18',
      title: 'GitAgent Harness: Repo as Source of',
      accent: 'Truth',
      sub: 'with Lyzr Team · Lyzr ADK & Open Source',
      pills: 'off',
      icon: 'git-branch'
    }
  }
];

async function run() {
  for (const c of newCards) {
    try {
      const generatedPath = await generateCard(c.params, `thumb_${c.slug}`);
      const destPath = path.join(thumbnailsDir, `${c.slug}.png`);
      fs.copyFileSync(generatedPath, destPath);
      console.log(`  ✓ Generated Thumbnail Card: ${destPath}`);
    } catch (err) {
      console.error(`  ❌ Error generating card for ${c.slug}:`, err);
    }
  }
  closeCardServer();
}

run();
