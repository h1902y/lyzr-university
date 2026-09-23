import { chromium } from 'playwright';
import { resolve } from 'node:path';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');

async function testDOM() {
  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1400, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log("Navigating to https://lyzr.thinkific.com/manage/courses/3489970/curriculum...");
  await page.goto('https://lyzr.thinkific.com/manage/courses/3489970/curriculum', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const iframe = page.frameLocator('iframe[src*="hub/courses"]');

  // Let's inspect buttons, inputs, contenteditable elements, and menus
  const info = await iframe.evaluate(() => {
    const buttons = Array.from(document.querySelectorAll('button')).map(b => ({
      text: b.innerText.trim(),
      ariaLabel: b.getAttribute('aria-label'),
      qa: b.getAttribute('data-qa'),
      description: b.getAttribute('description')
    }));

    const editable = Array.from(document.querySelectorAll('[contenteditable="true"]')).map(el => ({
      tagName: el.tagName,
      className: el.className,
      html: el.innerHTML.slice(0, 100)
    }));

    const inputs = Array.from(document.querySelectorAll('input')).map(i => ({
      type: i.type,
      name: i.name,
      value: i.value,
      ariaLabel: i.getAttribute('aria-label')
    }));

    return { buttons, editable, inputs };
  });

  console.log("Found Inputs:", JSON.stringify(info.inputs, null, 2));
  console.log("Found ContentEditables:", JSON.stringify(info.editable, null, 2));
  console.log("Found Sample Buttons (first 15):", JSON.stringify(info.buttons.slice(0, 15), null, 2));

  await context.close();
}

testDOM().catch(err => {
  console.error(err);
  process.exit(1);
});
