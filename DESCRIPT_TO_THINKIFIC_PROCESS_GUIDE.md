# 📘 Standard Operating Procedure (SOP): Descript Links to Thinkific Course Manifest

> **Document Purpose:** Canonical reference guide for converting raw Descript share links into production-grade Thinkific course manifests, complete with clean LMS-formatted lesson notes, strict chapter/lesson hierarchies, and media packaging.
> **Workspace Standard:** Strictly adheres to Lyzr University Course Building Guidelines (`Course > Chapter > Lesson`, plain-text LMS formatting without raw markdown `#` or `**`, zero usage of legacy term `Module`).

---

## 🔄 End-to-End Pipeline Overview

```
Raw Descript Links (share.descript.com/view/...)
   │
   ▼ [Step 1: Intake & Discovery]
Extract embedded <script id="metadata"> and <script id="document"> from share page HTML
   │  → Resolves video title, duration, timestamp offsets, and full word-level transcripts
   │  → Bypasses external 403 API authentication locks
   │
   ▼ [Step 2: Transcript Normalization & Brand Hygiene]
Regex text cleansing: Replace ASR errors ('Lizza'/'Lizer'/'Willizer' → 'Lyzr'/'Felipe with Lyzr')
   │  → Standardize product terms ('Lyzr Agent Studio', 'APC', 'SuperFlow')
   │
   ▼ [Step 3: Curriculum Architecture & Hierarchy]
Map lessons into logical Chapters (Course > Chapter > Lesson)
   │  → MANDATORY: Call them 'Chapter' (never 'Module') and 'Lesson'
   │  → 1 Video MP4 + 1 Formatted Text Block per lesson (never stack multiple videos)
   │
   ▼ [Step 4: Thinkific Text Block Authoring]
Author the 4 standard sections inside plain-text code fences (NO raw markdown # or **):
   │  1. LEARNING OBJECTIVES
   │  2. OVERVIEW
   │  3. STEP-BY-STEP WALKTHROUGH
   │  4. KEY TAKEAWAYS
   │
   ▼ [Step 5: Media Packaging & Naming Conventions]
Name files for deterministic ordering:
   │  → Video:  NNa <Title>.mp4
   │  → Notes:  NNb <Title> Notes.pdf (optional companion handout)
   │
   ▼ [Step 6: Master Manifest Generation & Publishing]
Assemble Master Manifest Markdown document with:
   │  → Metadata Header (Title, Subtitle, Slug, Track, Duration, Tags)
   │  → High-Level Syllabus Table
   │  → Ready-to-copy-paste lesson blocks for Thinkific Course Builder
```

---

## 🛠️ Detailed Step-by-Step Procedure

### Step 1: Intake & Descript Data Extraction

When presented with raw Descript share links (`https://share.descript.com/view/<ID>`):
1. **Do not rely on signed CloudFront/GCS download URLs directly via API**, as they frequently require session cookies or return `HTTP 403 Forbidden`.
2. **Inspect the share page HTML directly**: Descript embeds the entire recording state inside two `<script type="application/json">` blocks:
   - `<script type="application/json" id="metadata">`: Contains recording ID, display name, creation timestamp, and video duration.
   - `<script type="application/json" id="document">`: Contains the complete transcript timeline (`transcripts[0].timeline.superTau.taus`), word alignments, and markers.

#### Extraction Script Pattern (Python):
```python
import urllib.request, re, json

def fetch_descript_data(share_url):
    req = urllib.request.Request(share_url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
    
    meta_m = re.search(r'<script type="application/json" id="metadata">(.*?)</script>', html, re.DOTALL)
    doc_m = re.search(r'<script type="application/json" id="document">(.*?)</script>', html, re.DOTALL)
    
    meta = json.loads(meta_m.group(1)) if meta_m else {}
    doc = json.loads(doc_m.group(1)) if doc_m else {}
    
    # Extract full transcript string
    taus = doc.get('transcripts', [{}])[0].get('timeline', {}).get('superTau', {}).get('taus', [])
    transcript = ' '.join([t.get('text', {}).get('string', '') for t in taus if 'text' in t])
    return meta, transcript
```

---

### Step 2: Transcript Normalization & Brand Hygiene

Automated Speech Recognition (ASR) engines routinely mishear proprietary names and technical terms. Apply regex substitutions before drafting lesson copy:

| ASR Mishearing | Canonical Correction | Context / Rule |
|---|---|---|
| `Lizza`, `Lizer`, `Leiser`, `Lysr` | `Lyzr` | Company & platform name |
| `Felipe Willizer`, `Felipe Wolizer` | `Felipe with Lyzr` | Video narrator sign-off |
| `Lyzr Academy` | `Lyzr University` | Current branding standard |
| `No-code` / `Low-code` | `Lyzr Agent Studio` / `visual builder` | Preferred platform framing |
| `APC`, `credit` | `Agent Processing Credits (APC)` | Official credit currency |
| `super flow` | `SuperFlow` | Deterministic pipeline engine |

---

### Step 3: Curriculum Architecture & Hierarchy

Lyzr University enforces a strict 3-tier hierarchy:
```
Course (e.g. Lyzr Agent Studio: Operations, Governance & FinOps)
 └── Chapter (e.g. Chapter 01: Voice Agents & Telephony Integration)
      └── Lesson (e.g. Lesson 01: Voice Agents End-to-End)
```

> [!IMPORTANT]
> **Strict Hierarchy Rules:**
> 1. **Zero 'Module' Usage:** Strictly use the word **'Chapter'** for groupings and **'Lesson'** for items. Never use 'Module'.
> 2. **One Video Per Lesson:** Exactly 1 Video MP4 + 1 Formatted Plain Text Block per lesson. Never combine or stack multiple videos onto a single Thinkific lesson page.
> 3. **Chronological Numbering:** Lessons and videos must use two-digit zero-padded numbers (`01`, `02`, `03`...) matching the exact syllabus order.

---

### Step 4: Thinkific Text Block Authoring (No-Markdown Rule)

Thinkific's web text editor parses raw markdown (`###`, `**bold**`, `*italic*`) as literal plaintext characters or broken HTML code. Therefore:
- Format all lesson notes as **clean, plain-text blocks** inside fenced code blocks (` ```text `).
- Use UPPERCASE headers.
- Use unicode bullet points (`•`) instead of `-` or `*`.

#### Required Structure for Every Lesson Text Block:
```text
LEARNING OBJECTIVES
• Concrete outcome bullet point 1
• Concrete outcome bullet point 2
• Concrete outcome bullet point 3

OVERVIEW
1-2 comprehensive paragraphs explaining the business problem, architectural principle, and enterprise impact.

STEP-BY-STEP WALKTHROUGH
1. First numbered action item following on-screen UI steps.
2. Second numbered action item with exact UI labels.
3. Third numbered action item verifying outputs.

KEY TAKEAWAYS
• Core architectural or operational takeaway 1.
• Core architectural or operational takeaway 2.
```

---

### Step 5: Media & Asset Packaging Conventions

To ensure Thinkific's Content Uploader sorts files in exact chronological order:
1. **Video naming:** `NNa <Title>.mp4` (e.g. `01a Voice Agents End-to-End.mp4`)
2. **Companion Handout naming (if generated):** `NNb <Title> Notes.pdf` (e.g. `01b Voice Agents End-to-End Notes.pdf`)
3. **Directory Path:** Place assets in the appropriate track directory:
   `university/thinkific-upload/1 - Tracks/<Track>/<Course Folder>/`

---

### Step 6: Master Manifest Assembly & Upload

Combine all elements into a master markdown document containing:
1. **Metadata Header:** Course Title, Subtitle, Slug, Category/Track, Total Duration, Audience, and Source Descript URLs.
2. **High-Level Syllabus Table:** Table mapping Lesson Number, Chapter, Lesson Title, Duration, Video Filename, and Handout.
3. **Thinkific Builder Guide:** Clear section breaks with `📂 Chapter NN: <Name>` and `📖 Lesson NN: <Title>`, with copy-pasteable blocks.
4. **Deployment:**
   - **Manual:** Open Thinkific Course Builder → Create Chapter → Add Lesson → Attach Video → Paste Text Block.
   - **Automated:** Use `university/thinkific-uploader/` (Playwright automated upload tool) targeting the course folder.