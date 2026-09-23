import { chromium } from 'playwright';
import { resolve } from 'node:path';

const userDataDir = resolve('/Users/hkc/Documents/lyzr/university/thinkific-uploader/.browser-profile');
const courseId = 3489969;

const richCourse2Content = [
  {
    lessonNumber: "13",
    title: "13 Beyond Vectors: Structured Knowledge",
    html: `<h2>Lesson Overview: Beyond Vectors - Structured Knowledge</h2>
<p>Learn why pure vector search is often insufficient for enterprise AI, and how structured metadata filters, hybrid search, and semantic models overcome vector limitations.</p>

<h3>Limitations of Pure Vector Search</h3>
<ul>
  <li>Loss of exact keyword matching (part numbers, employee IDs, specific dates).</li>
  <li>Lack of relational context across document hierarchies.</li>
</ul>

<h3>Hybrid Solution</h3>
<p>Combine vector similarity with keyword BM25 scoring and SQL metadata filtering for 99%+ context retrieval accuracy.</p>`
  },
  {
    lessonNumber: "14",
    title: "14 Build a Knowledge Graph",
    html: `<h2>Lesson Overview: Build a Knowledge Graph</h2>
<p>Construct GraphRAG systems in Lyzr Studio to map complex relationships between entities, concepts, organizations, and policies.</p>

<h3>Core Concepts</h3>
<ul>
  <li><strong>Entity Extraction:</strong> Identifying nodes (People, Products, Rules) and edges (Manages, Requires, Conflicts With).</li>
  <li><strong>Graph Querying:</strong> Performing multi-hop reasoning across connected knowledge nodes.</li>
  <li><strong>GraphRAG Benefits:</strong> Superior performance on complex analytical and multi-document reasoning questions.</li>
</ul>`
  },
  {
    lessonNumber: "15",
    title: "15 The Semantic Model & Global Context",
    html: `<h2>Lesson Overview: The Semantic Model & Global Context</h2>
<p>Establish unified business definitions, terminology glossaries, and global system context across all enterprise AI agents.</p>

<h3>Key Components</h3>
<ul>
  <li><strong>Enterprise Business Glossary:</strong> Defining company metrics (e.g., ARR, CAC, Churn) so all agents interpret business terms identically.</li>
  <li><strong>Global Context Injector:</strong> Prepending company governance policies across every agent prompt automatically.</li>
  <li><strong>Brand & Voice Alignment:</strong> Ensuring consistent enterprise tone across internal and external agent communications.</li>
</ul>`
  },
  {
    lessonNumber: "16",
    title: "16 Responsible AI & Guardrails",
    html: `<h2>Lesson Overview: Responsible AI & Guardrails</h2>
<p>Implement comprehensive security guardrails, PII masking, toxic content blocking, and prompt injection defense in Lyzr Agent Studio.</p>

<h3>Guardrail Layers</h3>
<ul>
  <li><strong>Input Guardrails:</strong> Screen incoming user queries for prompt injection, jailbreak attempts, and prohibited topics.</li>
  <li><strong>Output Guardrails:</strong> Mask sensitive PII (SSNs, Credit Cards, API Keys) and verify hallucination scores before sending responses to users.</li>
  <li><strong>Compliance Auditing:</strong> Log all blocked attempts for security and compliance review.</li>
</ul>`
  },
  {
    lessonNumber: "17",
    title: "17 Agent Simulation & Observability",
    html: `<h2>Lesson Overview: Agent Simulation & Observability</h2>
<p>Test, evaluate, and monitor your AI agents in production using automated batch simulation benchmarks and telemetry dashboards.</p>

<h3>Evaluation Suite</h3>
<ul>
  <li><strong>Automated Benchmark Datasets:</strong> Run 100+ test scenarios automatically before deploying prompt changes to production.</li>
  <li><strong>Latency & Cost Telemetry:</strong> Track token usage, model costs, and end-to-end execution latency in real-time.</li>
  <li><strong>User Feedback Loops:</strong> Capture thumbs up/down and user edits to continuously fine-tune agent performance.</li>
</ul>`
  }
];

async function main() {
  console.log("==========================================================================");
  console.log(" 🚀 UPDATING LESSONS 13-17 WITH SCROLL-INTO-VIEW AUTO SCROLL");
  console.log("==========================================================================");

  const context = await chromium.launchPersistentContext(userDataDir, {
    channel: 'chrome',
    headless: true,
    viewport: { width: 1400, height: 1000 }
  });

  const page = context.pages()[0] || (await context.newPage());

  console.log(`Navigating to Thinkific Course 2 Curriculum (#${courseId})...`);
  await page.goto(`https://lyzr.thinkific.com/manage/courses/${courseId}/curriculum`, { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(6000);

  const iframe = page.frameLocator('iframe[src*="hub/courses"]');

  // Scroll iframe sidebar down
  const frame = page.frames().find(f => f.url().includes('hub/courses'));
  if (frame) {
    await frame.evaluate(() => {
      const scrollable = document.querySelector('aside, nav, div[class*="sidebar"], div[class*="curriculum"]');
      if (scrollable) scrollable.scrollTop = scrollable.scrollHeight;
      window.scrollTo(0, document.body.scrollHeight);
    });
    await page.waitForTimeout(2000);
  }

  for (const item of richCourse2Content) {
    console.log(`\n📄 Updating Lesson ${item.lessonNumber}: '${item.title}'...`);

    try {
      const lessonElem = iframe.locator('button, [role="button"], span, a').filter({
        hasText: new RegExp(`^${item.lessonNumber}\\b|${item.lessonNumber}\\s+`, 'i')
      }).first();

      if (await lessonElem.count() > 0) {
        await lessonElem.scrollIntoViewIfNeeded();
        await lessonElem.click();
        await page.waitForTimeout(2500);

        if (frame) {
          const updated = await frame.evaluate(({ htmlText }) => {
            const ed = document.querySelector('[contenteditable="true"], .ProseMirror');
            if (ed) {
              ed.innerHTML = htmlText;
              ed.dispatchEvent(new Event('input', { bubbles: true }));
              ed.dispatchEvent(new Event('change', { bubbles: true }));
              return true;
            }
            return false;
          }, { htmlText: item.html });

          if (updated) {
            await page.waitForTimeout(1000);
            const saveBtn = iframe.locator('[data-qa="actions-bar__save-button"], button:has-text("Save")').first();
            if (await saveBtn.isVisible()) {
              await saveBtn.click();
              await page.waitForTimeout(2500);
              console.log(`   ✓ Saved Rich HTML Content for Lesson ${item.lessonNumber}!`);
            }
          }
        }
      } else {
        console.log(`   ⚠️ Lesson ${item.lessonNumber} element not found in sidebar`);
      }
    } catch (e) {
      console.error(`   ⚠️ Error on Lesson ${item.lessonNumber}: ${e.message}`);
    }
  }

  await page.screenshot({ path: resolve('screenshots/course_2_rich_html_lessons_13_17_updated.png'), fullPage: true });
  console.log("\n📸 Saved verification screenshot: screenshots/course_2_rich_html_lessons_13_17_updated.png");

  await context.close();
  console.log("\n==========================================================================");
  console.log(" 🎉 LESSONS 13-17 RICH HTML UPDATE COMPLETE!");
  console.log("==========================================================================");
}

main().catch(err => {
  console.error("Fatal error:", err);
  process.exit(1);
});
