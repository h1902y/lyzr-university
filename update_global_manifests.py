import os
import sys
import json
import re

university_dir = "/Users/hkc/Documents/lyzr/university"
manifest_md_path = os.path.join(university_dir, "revamp", "MASTER_CURRICULUM_MANIFEST.md")
plan_json_path = os.path.join(university_dir, "revamp_upload_plan.json")

print("==========================================================================")
print(" 📜 UPDATING GLOBAL MASTER CURRICULUM MANIFEST & UPLOAD PLAN")
print("==========================================================================")

# 1. Update revamp_upload_plan.json
plan_data = json.load(open(plan_json_path))

new_plan_entries = [
    {
        "index": 50,
        "course": "Lyzr Foundations",
        "chapter": "Chapter 01: Lyzr Platform & Ecosystem Overview",
        "lesson": "Lyzr Platform Pricing & Token Economics",
        "filename": "C01_CH01_L04_lyzr_platform_pricing.mp4",
        "filepath": "/Users/hkc/Documents/lyzr/university/revamp_branded/C01_CH01_L04_lyzr_platform_pricing.mp4",
        "thumbnail_path": "/Users/hkc/Documents/lyzr/university/revamp/thumbnails/C01_CH01_L04_lyzr_platform_pricing.png",
        "title": "Foundation C1 L4 | Lyzr Platform Pricing & Token Economics",
        "description": "Course: Lyzr Foundations\nChapter: Lyzr Platform & Ecosystem Overview\nLesson: Lyzr Platform Pricing & Token Economics\n\n============================================================\n📚 LESSON OVERVIEW & OBJECTIVES\n============================================================\n  • Learn how Lyzr is priced on transparent token usage (APCs - Agent Processing Credits).\n  • Understand the 1:1 input/output token calculation model.\n  • Compare Lyzr SaaS vs. On-Premise VPC deployment architectures.\n\n============================================================\n🔗 Important Links:\nBuild with Architect: https://hubs.ly/Q043pWTs0\nBuild your own AI agent → https://hubs.ly/Q03wb5Md0\nExplore our website → https://hubs.ly/Q03wbGVt0\nBuild agents for your company (Book a demo) → https://hubs.ly/Q03wbH0k0\nLearn how to build agents with Lyzr Academy → https://hubs.ly/Q03wqxFR0\n\n============================================================\n🏷️ HASHTAGS\n============================================================\n#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI",
        "playlist": "Lyzr Foundations — Master Course",
        "exists": True
    },
    {
        "index": 51,
        "course": "Lyzr for Technical Professionals",
        "chapter": "Chapter 04: Lyzr ADK & Open Source",
        "lesson": "GitAgent Harness: Repo as Source of Truth",
        "filename": "C03_CH04_L03_gitagent_harness.mp4",
        "filepath": "/Users/hkc/Documents/lyzr/university/revamp_branded/C03_CH04_L03_gitagent_harness.mp4",
        "thumbnail_path": "/Users/hkc/Documents/lyzr/university/revamp/thumbnails/C03_CH04_L03_gitagent_harness.png",
        "title": "Technical C4 L3 | GitAgent Harness: Repo as Source of Truth",
        "description": "Course: Lyzr for Technical Professionals\nChapter: Lyzr ADK & Open Source\nLesson: GitAgent Harness: Repo as Source of Truth\n\n============================================================\n📚 LESSON OVERVIEW & OBJECTIVES\n============================================================\n  • Understand how GitAgent transforms your Git repository into the primary agent specification.\n  • Inspect soul.md, rules.md, instructions.md, and agent.yaml.\n  • Learn how Lyzr Studio acts as a synchronized runtime reading directly from GitHub.\n\n============================================================\n🔗 Important Links:\nBuild with Architect: https://hubs.ly/Q043pWTs0\nBuild your own AI agent → https://hubs.ly/Q03wb5Md0\nExplore our website → https://hubs.ly/Q03wbGVt0\nBuild agents for your company (Book a demo) → https://hubs.ly/Q03wbH0k0\nLearn how to build agents with Lyzr Academy → https://hubs.ly/Q03wqxFR0\n\n============================================================\n🏷️ HASHTAGS\n============================================================\n#Lyzr #AIAgents #AgentStudio #LyzrADK #EnterpriseAI #AutonomousAgents #LLM #RAG #AI",
        "playlist": "Lyzr for Technical Professionals — Master Course",
        "exists": True
    }
]

# Ensure no duplicate addition to plan_data
existing_filenames = [i['filename'] for i in plan_data]
for entry in new_plan_entries:
    if entry['filename'] not in existing_filenames:
        plan_data.append(entry)

with open(plan_json_path, 'w', encoding='utf-8') as f:
    json.dump(plan_data, f, indent=2)

print(f"  ✓ Updated {plan_json_path} (Total items: {len(plan_data)})")

# 2. Append entries to MASTER_CURRICULUM_MANIFEST.md
manifest_text = open(manifest_md_path, 'r', encoding='utf-8').read()

new_manifest_blocks = """

```yaml
---
course: "Lyzr Foundations"
chapter: "Chapter 01: Lyzr Platform & Ecosystem Overview"
lesson_id: "L04"
lesson_number: 4
lesson_code: "C01_CH01_L04"
title: "Lyzr Platform Pricing & Token Economics"
video_file_name: "C01_CH01_L04_lyzr_platform_pricing.mp4"
video_file_path: "university/revamp_branded/C01_CH01_L04_lyzr_platform_pricing.mp4"
descript_link: "https://share.descript.com/view/8oO6B0yXXiP"
---
```

### 📖 Lesson 04: Lyzr Platform Pricing & Token Economics

```text
C01_CH01_L04
```

> [!IMPORTANT]
> **Lesson Code:** `C01_CH01_L04` | **Video Asset:** [`C01_CH01_L04_lyzr_platform_pricing.mp4`](university/revamp_branded/C01_CH01_L04_lyzr_platform_pricing.mp4) | **Descript Share URL:** [https://share.descript.com/view/8oO6B0yXXiP](https://share.descript.com/view/8oO6B0yXXiP)

## 🎯 Learning Objectives
- Learn how Lyzr is priced on transparent token usage (APCs - Agent Processing Credits).
- Understand the 1:1 input/output token calculation model with zero complexity multipliers or feature gating.
- Compare Lyzr SaaS vs. On-Premise VPC deployment architectures and capacity scaling.

## 📚 Overview & Core Architecture
The traditional way to price AI platforms is per-agent or with arbitrary complexity tiers. Lyzr solves this by pricing on tokens—the exact same unit used by foundation model providers.

Key pricing highlights:
- **1 APC = 1 Token ≈ 4 Characters ≈ 0.75 Words**
- **Zero Feature Gating:** Every customer receives access to the complete enterprise platform.
- **BYOK vs. Pass-Through:** Zero markup on inference model costs.

---

```yaml
---
course: "Lyzr for Technical Professionals"
chapter: "Chapter 04: Lyzr ADK & Open Source"
lesson_id: "L03"
lesson_number: 3
lesson_code: "C03_CH04_L03"
title: "GitAgent Harness: Repo as Source of Truth"
video_file_name: "C03_CH04_L03_gitagent_harness.mp4"
video_file_path: "university/revamp_branded/C03_CH04_L03_gitagent_harness.mp4"
descript_link: "https://share.descript.com/view/8t4NpsxFDw8"
---
```

### 📖 Lesson 03: GitAgent Harness: Repo as Source of Truth

```text
C03_CH04_L03
```

> [!IMPORTANT]
> **Lesson Code:** `C03_CH04_L03` | **Video Asset:** [`C03_CH04_L03_gitagent_harness.mp4`](university/revamp_branded/C03_CH04_L03_gitagent_harness.mp4) | **Descript Share URL:** [https://share.descript.com/view/8t4NpsxFDw8](https://share.descript.com/view/8t4NpsxFDw8)

## 🎯 Learning Objectives
- Understand how GitAgent transforms your Git repository into the primary agent specification and harness.
- Inspect the core declarative spec files: `soul.md`, `rules.md`, `instructions.md`, and `agent.yaml`.
- Learn how Lyzr Studio acts as a synchronized runtime reading directly from GitHub.

## 📚 Overview & Core Architecture
Connecting an AI agent to a Git repository is often viewed simply as version control. In the GitAgent paradigm, the repository becomes the agent itself, while Lyzr Studio operates as the runtime environment.
"""

if "C01_CH01_L04" not in manifest_text:
    with open(manifest_md_path, 'a', encoding='utf-8') as f:
        f.write(new_manifest_blocks)
    print(f"  ✓ Appended new lessons to {manifest_md_path}")
else:
    print(f"  ✓ {manifest_md_path} already up-to-date")

print("\n==========================================================================")
print(" 🎉 GLOBAL MASTER MANIFEST & UPLOAD PLAN UPDATED SUCCESSFULLY!")
print("==========================================================================")
