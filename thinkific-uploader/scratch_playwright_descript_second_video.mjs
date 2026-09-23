import { chromium } from 'playwright';

async function main() {
  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage();
  
  const urls = [];
  page.on('request', req => urls.push(req.url()));
  
  const url = "https://web.descript.com/60fb07e9-ef3f-4bc2-9880-d35901025d65/cd0e8?kind=video_project&lite=false";
  console.log(`Navigating to ${url}...`);
  
  try {
    await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
  } catch (e) {
    console.log("Load finished or timed out:", e.message);
  }
  
  console.log(`Captured ${urls.length} network requests.`);
  
  const m3u8 = urls.filter(u => u.includes('.m3u8'));
  const docs = urls.filter(u => u.includes('document-') || u.includes('.json'));
  const cf = urls.filter(u => u.includes('cloudfront.net'));
  
  console.log("\n--- HLS (.m3u8) URLs ---");
  m3u8.forEach(u => console.log(u));
  
  console.log("\n--- Document / JSON URLs ---");
  docs.slice(0, 15).forEach(u => console.log(u));
  
  console.log("\n--- CloudFront URLs ---");
  cf.slice(0, 15).forEach(u => console.log(u));
  
  const title = await page.title();
  console.log("\nPage Title:", title);
  
  await browser.close();
}

main().catch(console.error);
