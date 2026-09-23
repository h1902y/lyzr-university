import os
import sys
import subprocess
import pathlib

university_dir = pathlib.Path("/Users/hkc/Documents/lyzr/university")
notes_dir = university_dir / "notes"
notes_dir.mkdir(parents=True, exist_ok=True)

print("==========================================================================")
print(" 📝 GENERATING HIGH-END BRANDED LESSON NOTES & PDFS")
print("==========================================================================")

# 1. Pricing Lesson Notes Markdown
pricing_md_content = """# 💰 Lyzr Platform Pricing & Token Economics

Understanding how Lyzr is priced, how Agent Processing Credits (APCs) work, and how to estimate deployment costs across SaaS and Virtual Private Cloud (VPC).

---

## 🎯 Executive Summary & Core Philosophy

The traditional way to price AI platforms is **per-agent** or with arbitrary **complexity tiers**. This approach creates friction because enterprise teams cannot accurately predict how many agents or tiers they will need prior to deployment.

Lyzr solves this by pricing on **tokens**—the exact same unit used by foundation model providers (OpenAI, Anthropic, Google). 

### Key Principles of Lyzr Pricing:
* **Parity with Model Pricing:** Cost is directly tied to token usage.
* **Zero Feature Gating:** Every customer receives access to the complete enterprise platform (RAG, Knowledge Graphs, SuperFlows, Guardrails, Memory).
* **Parity Across Deployments:** The exact same APC unit applies whether running on Lyzr SaaS or On-Premise VPC.
* **No Hidden Fees:** Zero markup on inference model costs.

---

## 🧠 What is an Agent Processing Credit (APC)?

An **Agent Processing Credit (APC)** is Lyzr's standardized billing unit. 

$$\\text{1 APC} = \\text{1 Token} \\approx \\text{4 Characters} \\approx \\text{0.75 Words}$$

### How a Single Execution Consumes APCs:
$$\\text{Total APCs} = \\text{Input Tokens} + \\text{Output Tokens}$$

1. **Input Tokens:** Includes user query, agent instructions/system prompt, conversation history, retrieved Knowledge Base context, and tool definitions.
2. **Output Tokens:** The agent's generated response, reasoning steps, and tool arguments.
3. **Symmetric Rate:** Input and output tokens are billed at the **exact same 1:1 APC rate**, making cost forecasting straightforward.

---

## ☁️ Deployment Models: SaaS vs. On-Premise VPC

| Metric / Dimension | Lyzr SaaS (Shared Cloud) | Lyzr VPC (Private Cloud / On-Prem) |
| :--- | :--- | :--- |
| **Data Perimeter** | Hosted on Lyzr multi-tenant infrastructure | 100% inside your private cloud / data center |
| **Setup Fee** | **$0** (Instant Onboarding) | One-time upfront deployment fee |
| **Annual Subscription Base** | $100,000 / year (5 Billion APCs) | $250,000 / year (50 Billion APCs) |
| **Volume Efficiency** | ~50 Billion APCs per $1M | ~200 Billion APCs per $1M (4x Capacity per $) |
| **Best For** | Fast quarterly deployment & experimentation | Regulated enterprise & strict data residency |

---

## 🔑 Model Cost & Billing Transparency (BYOK vs. Pass-Through)

Lyzr never marks up foundation model inference costs. You choose how model execution is handled:

### Option A: Bring Your Own Keys (BYOK)
* You configure your own OpenAI, Anthropic, or Google API keys inside Lyzr.
* You pay Lyzr only for APC platform credits.
* Model providers bill your enterprise directly under your negotiated rates.

### Option B: Pass-Through Provisioning
* Lyzr provisions foundation models on your behalf.
* Model costs pass through at **exact list price with zero markup** as an itemized line item.

---

## 🔄 Carry-Forward & Rollover Protection

To eliminate the risk of under-utilization, **unused APC subscription credits carry forward** into subsequent years. Enterprise teams can commit to long-term capacity without fearing lost budget during ramp-up phases.
"""

# 2. GitAgent Harness Lesson Notes Markdown
gitagent_md_content = """# 🛠️ GitAgent Harness: Repo as Source of Truth & Runtime

Treating AI agents as code repositories—how GitAgent transforms Git into the agent harness and GitHub into the enterprise governance engine.

---

## 🎯 Executive Summary & Overview

Connecting an AI agent to a Git repository is often viewed simply as "version control." However, in the GitAgent paradigm, **the repository becomes the agent itself**, while Lyzr Studio operates as the runtime environment.

Instead of managing agents via web UI forms, every aspect of the agent is declared as plain text files in an open specification format.

---

## 📄 The GitAgent File Architecture

When an agent connects to Git, Studio generates four core configuration files:

```text
my-agent-repo/
├── soul.md       # Who the agent is (Identity, Tone, Expertise)
├── rules.md      # What the agent must NEVER do (Guardrails & Policies)
├── instructions.md # How the agent behaves & steps to execute
└── agent.yaml    # Declarative configuration (Model, Temperature, Tools, Features)
```

---

## ⚡ Key Paradigm Shifts

### 1. File-Based Specification Over UI Fields
Because the agent is defined by files, changes can originate from anywhere:
* An engineer submitting a GitHub Pull Request.
* An automated CI script updating `agent.yaml`.
* A peer AI agent refactoring `rules.md`.

### 2. Studio as a Synchronized Runtime
Lyzr Studio watches the Git repository. A single click (`Pull from GitHub`) synchronizes Studio's state with the repository's latest commit hash, ensuring the repository remains the immutable **Source of Truth**.

### 3. Native Enterprise Governance
Instead of building custom administrative workflows, AI agents inherit your enterprise's existing software delivery controls:
* **Peer Code Reviews:** PR approvals required before policy merged to main.
* **CI/CD Testing:** Automated simulation suites trigger on every agent commit.
* **Audit Trails:** Complete history of every agent behavior with author name and timestamp.

---

## 💡 Summary takeaway

> *"Stop asking how to manage agents, and start asking what you would do if an agent were just code—because now it is."*
"""

pricing_md_path = notes_dir / "pricing_lesson_notes.md"
gitagent_md_path = notes_dir / "gitagent_harness_lesson_notes.md"

with open(pricing_md_path, 'w', encoding='utf-8') as f:
    f.write(pricing_md_content)

with open(gitagent_md_path, 'w', encoding='utf-8') as f:
    f.write(gitagent_md_content)

print(f"  ✓ Written Markdown: {pricing_md_path.name}")
print(f"  ✓ Written Markdown: {gitagent_md_path.name}")

# Convert Markdown to HTML & Render PDF via Headless Chrome
def render_pdf(md_file, pdf_file):
    html_file = md_file.with_suffix('.html')
    md_text = open(md_file, 'r', encoding='utf-8').read()
    
    # Wrap in clean high-end HTML template
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:ital,wght@1,700&family=JetBrains+Mono&display=swap');
  body {{
    font-family: 'Inter', sans-serif;
    color: #1a1a1a;
    line-height: 1.6;
    padding: 40px;
    max-width: 800px;
    margin: 0 auto;
  }}
  h1 {{ font-family: 'Playfair Display', serif; font-style: italic; color: #111; font-size: 32px; border-bottom: 2px solid #E05638; padding-bottom: 12px; }}
  h2 {{ color: #E05638; font-size: 22px; margin-top: 28px; }}
  h3 {{ color: #333; font-size: 18px; }}
  code, pre {{ font-family: 'JetBrains Mono', monospace; background: #f4f4f5; padding: 2px 6px; border-radius: 4px; font-size: 14px; }}
  pre {{ padding: 16px; display: block; overflow-x: auto; }}
  table {{ width: 100%; border-collapse: collapse; margin: 20px 0; }}
  th, td {{ border: 1px solid #e4e4e7; padding: 10px 14px; text-align: left; }}
  th {{ background: #f4f4f5; color: #111; font-weight: 600; }}
  blockquote {{ border-left: 4px solid #E05638; margin: 20px 0; padding: 10px 20px; background: #fafafa; font-style: italic; }}
  .header-badge {{ background: #E05638; color: white; padding: 4px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; letter-spacing: 1px; display: inline-block; margin-bottom: 12px; }}
</style>
</head>
<body>
  <div class="header-badge">LYZR UNIVERSITY · OFFICIAL LESSON NOTES</div>
  {md_text.replace('# ', '<h1>').replace('## ', '<h2>').replace('### ', '<h3>')}
</body>
</html>"""

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    chrome_cmd = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "--headless", "--disable-gpu", f"--print-to-pdf={pdf_file}", str(html_file)
    ]
    subprocess.run(chrome_cmd, capture_output=True)
    if pdf_file.exists():
        print(f"  ✓ Rendered PDF: {pdf_file.name} ({pdf_file.stat().st_size / 1024:.1f} KB)")

pricing_pdf_path = notes_dir / "pricing_lesson_notes.pdf"
gitagent_pdf_path = notes_dir / "gitagent_harness_lesson_notes.pdf"

render_pdf(pricing_md_path, pricing_pdf_path)
render_pdf(gitagent_md_path, gitagent_pdf_path)

print("\n🎉 Lesson Notes & PDFs Generated Successfully!")
