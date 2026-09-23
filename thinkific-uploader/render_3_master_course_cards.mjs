import { generateCard, closeCardServer } from './src/cardgen.mjs';
import { join } from 'node:path';
import fs from 'node:fs';

const artifactDir = '/Users/hkc/.gemini/antigravity/brain/3a9872be-f9b7-47a1-a103-abcbbde59f61';

const coursesToGenerate = [
  {
    slug: 'master-lyzr-foundations',
    params: {
      eyebrow: 'FOUNDATIONS · MASTER COURSE',
      title: 'Lyzr',
      accent: 'Foundations',
      sub: 'with Lyzr Team · Enterprise Agent Platform Architecture',
      pills: 'off',
      icon: 'brain'
    }
  },
  {
    slug: 'master-lyzr-platform-studio',
    params: {
      eyebrow: 'PLATFORM STUDIO · MASTER COURSE',
      title: 'Lyzr Platform',
      accent: 'Studio',
      sub: 'with Lyzr Team · No-Code Workflows & SuperFlows',
      pills: 'off',
      icon: 'workflow'
    }
  },
  {
    slug: 'master-lyzr-code-libraries',
    params: {
      eyebrow: 'CODE LIBRARIES · MASTER COURSE',
      title: 'Lyzr Code',
      accent: 'Libraries',
      sub: 'with Lyzr Team · Python ADK SDK & Custom Tools',
      pills: 'off',
      icon: 'code'
    }
  }
];

console.log("==========================================================================");
console.log(" 🎨 RE-GENERATING 760x420px MASTER COURSE CARDS WITH NEW NAMES");
console.log("==========================================================================");

for (const c of coursesToGenerate) {
  try {
    const cardPath = await generateCard(c.params, c.slug);
    console.log(` ✅ Generated 760x420 Card for '${c.slug}': ${cardPath}`);
    
    // Copy to artifact directory for easy download
    if (fs.existsSync(artifactDir)) {
      const artPath = join(artifactDir, `${c.slug}.png`);
      fs.copyFileSync(cardPath, artPath);
      console.log(`    📁 Artifact Link: ${artPath}`);
    }
  } catch (err) {
    console.error(` ❌ Error generating thumbnail card for '${c.slug}':`, err);
  }
}

closeCardServer();
console.log("\n==========================================================================");
console.log(" 🎉 ALL 3 MASTER COURSE 760x420 CARDS RE-GENERATED SUCCESSFULLY!");
console.log("==========================================================================");
