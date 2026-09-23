#!/usr/bin/env python3
"""
Render Studio Track lesson-notes markdowns to brand-styled PDFs via headless Chrome.

Cloned from SDK-track/notes/_render_pdfs.py and re-pointed at the Studio Track. Same
study-companion template; differences are the Studio accent color, the phase eyebrow
(Studio is organized by lifecycle phase, not "Module N"), the "Lyzr University" brand
string, and the target course folder.

Template: Engineering-reference Study Companion.
  - Phase strip header (Studio-tonal background, full bleed)
  - Two-column body: main column for content, right column for sidebar takeaways
  - Sidebar callouts auto-pulled from the bolded lead-in of each Key Concepts paragraph
  - Distinctive Try-this CTA section (Ferra left rule + Playfair digits)
  - Running header on page 2+, page number in phase color in footer
  - "## Transcript" section is intentionally skipped — markdown keeps it as source-of-truth

Reads /Users/hkc/Documents/lyzr/lyzr-university/Studio-track/notes/*.md
Writes …/thinkific-upload/1 - Tracks/Studio/<NN Course>/NNb {Title} Notes.pdf
"""
import re, html, pathlib, subprocess, tempfile, sys, time

ROOT       = pathlib.Path("/Users/hkc/Documents/lyzr/university")
NOTES_DIR  = ROOT / "Studio-track" / "notes"
# The Studio Track is collection-organized under thinkific-upload/1 - Tracks/Studio/.
# The first course is the Foundations journey "Studio: The Agent Lifecycle" (folder 06).
UPLOAD_DIR = ROOT / "thinkific-upload" / "1 - Tracks" / "Studio"
CHROME     = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# ----------------------------------------------------------------------------
# Courses → lessons. One entry per Thinkific course.
# ----------------------------------------------------------------------------
# Each course carries its OWN notes dir, so lesson numbers (01, 02, …) are scoped
# per course and never collide across courses. Foundations lives flat in notes/;
# every later course gets its own notes/<slug>/ subdir (the flat glob is non-recursive,
# so Foundations only ever picks up its own 01–07).
#   notes_dir — where this course's NN-slug.md files live
#   chapter   — the course's folder under thinkific-upload/1 - Tracks/Studio/
#   phase     — eyebrow name + Studio-violet color ramp
#   lessons   — NN → display title (the in-PDF H1 comes from the markdown; this drives
#               the wayfinding strip, the <title>, and the output filename)
STUDIO_VIOLET = {"color": "#7A639D", "text_on": "#F3EFEA"}

COURSES = [
    {
        "notes_dir": NOTES_DIR,
        "chapter": "06 Studio The Agent Lifecycle",
        "phase": {"name": "Foundations · The Agent Lifecycle", **STUDIO_VIOLET},
        "lessons": {
            "01": "Welcome to Agent Studio & the lifecycle",
            "02": "Build — choose a type & create an agent",
            "03": "Equip — model, tool, knowledge",
            "04": "Govern — add guardrails",
            "05": "Test — run it in the Playground",
            "06": "Deploy — ship it",
            "07": "Project — one agent, full lifecycle",
        },
    },
    {
        "notes_dir": NOTES_DIR / "building-orchestrating",
        "chapter": "07 Studio Building and Orchestrating Agents",
        "phase": {"name": "Build", **STUDIO_VIOLET},
        "lessons": {
            "01": "What agent type should I build?",
            "02": "Lyzr Manager",
            "03": "Managers, part 2 — editing from the agent page",
            "04": "SuperFlow: Invoice Reconciliation",
            "05": "SuperFlow: Loops",
            "06": "Models in depth",
            "07": "Tools in production",
        },
    },
    {
        "notes_dir": NOTES_DIR / "grounding-knowledge",
        "chapter": "11 Studio Grounding Agents in Knowledge",
        "phase": {"name": "Ground", **STUDIO_VIOLET},
        "lessons": {
            "01": "RAG in Studio",
            "02": "Build a Knowledge Base",
            "03": "Document parsing & ingestion",
            "04": "Data Connectors as live sources",
            "05": "Agent memory in depth",
            "06": "Beyond vectors — structured knowledge",
            "07": "Build a Knowledge Graph",
            "08": "The Semantic Model",
            "09": "Project: document Q&A agent with memory",
        },
    },
    {
        "notes_dir": NOTES_DIR / "governing-testing",
        "chapter": "13 Studio Governing and Testing Agents",
        "phase": {"name": "Govern & Test", **STUDIO_VIOLET},
        "lessons": {
            "01": "Responsible AI in Studio",
            "02": "The Simulation Engine",
        },
    },
]

def safe_title(t: str) -> str:
    """Filesystem-safe title for output filenames — avoid ':' (Thinkific Content
    Uploader + clean sort); render it as an em dash instead."""
    return t.replace(": ", " — ").replace(":", " — ")

# ----------------------------------------------------------------------------
# Markdown → HTML — scoped to what these notes use
# ----------------------------------------------------------------------------
def esc(s: str) -> str:
    return html.escape(s, quote=False)

def render_inline(text: str) -> str:
    """Inline markdown: `code`, **bold**, *italic*. Code spans first to protect them."""
    placeholders = []
    def stash(m):
        placeholders.append(f"<code>{esc(m.group(1))}</code>")
        return f"\x00{len(placeholders)-1}\x00"
    text = re.sub(r"`([^`]+)`", stash, text)
    text = esc(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    text = re.sub(r"\x00(\d+)\x00", lambda m: placeholders[int(m.group(1))], text)
    return text

def parse_blocks(md: str):
    """Yield ('h1'|'h2'|'p'|'ul'|'ol'|'code', payload) blocks. Skips Transcript section."""
    lines = md.split("\n")
    i = 0
    in_transcript = False
    while i < len(lines):
        line = lines[i]

        # H2 — also gate the transcript section
        m = re.match(r"^##\s+(.+)$", line)
        if m:
            heading = m.group(1).strip()
            if heading.lower() == "transcript":
                in_transcript = True
                # Skip to EOF or next H2/H1
                i += 1
                while i < len(lines) and not re.match(r"^#{1,2}\s+", lines[i]):
                    i += 1
                continue
            in_transcript = False
            yield ("h2", heading)
            i += 1
            continue
        if in_transcript:
            i += 1; continue

        # Fenced code
        m = re.match(r"^```(\w*)\s*$", line)
        if m:
            lang = m.group(1)
            code = []
            i += 1
            while i < len(lines) and not re.match(r"^```\s*$", lines[i]):
                code.append(lines[i]); i += 1
            i += 1
            yield ("code", (lang, "\n".join(code)))
            continue

        # H1
        m = re.match(r"^#\s+(.+)$", line)
        if m:
            yield ("h1", m.group(1).strip()); i += 1; continue

        # Ordered list
        if re.match(r"^\d+\.\s+", line):
            items = []
            while i < len(lines) and re.match(r"^\d+\.\s+", lines[i]):
                items.append(re.sub(r"^\d+\.\s+", "", lines[i])); i += 1
            yield ("ol", items); continue

        # Unordered list
        if re.match(r"^- +", line):
            items = []
            while i < len(lines) and re.match(r"^- +", lines[i]):
                items.append(re.sub(r"^- +", "", lines[i])); i += 1
            yield ("ul", items); continue

        # Blank
        if line.strip() == "":
            i += 1; continue

        # Paragraph
        para = [line]; i += 1
        while i < len(lines):
            nxt = lines[i]
            if (nxt.strip() == "" or
                re.match(r"^#{1,2}\s+", nxt) or
                re.match(r"^- +", nxt) or
                re.match(r"^\d+\.\s+", nxt) or
                re.match(r"^```", nxt)):
                break
            para.append(nxt); i += 1
        yield ("p", " ".join(para))

# ----------------------------------------------------------------------------
# Build HTML for one lesson
# ----------------------------------------------------------------------------
def section_class(heading: str) -> str:
    h = heading.lower()
    if "you'll learn" in h or "you ll learn" in h: return "sec-learn"
    if "key concept" in h:                         return "sec-keyconcepts"
    if "code shown" in h or h == "code":           return "sec-code"
    if "try this" in h:                            return "sec-tryThis"
    return "sec-other"

def pull_takeaway(paragraph_html: str):
    """If the paragraph leads with <strong>…</strong>, return that as the sidebar text."""
    m = re.match(r"^\s*<strong>([^<]+?)</strong>", paragraph_html)
    if m:
        return m.group(1).strip().rstrip(".") + "."
    return None

def build_body(md: str) -> str:
    out = []
    current_section = None
    blocks = list(parse_blocks(md))
    # Group blocks under section H2s so we can apply per-section CSS
    i = 0
    while i < len(blocks):
        kind, payload = blocks[i]
        if kind == "h1":
            out.append(f'<h1 class="lesson-title">{render_inline(payload)}</h1>')
            i += 1
            # Eyebrow paragraph (italic *Lesson NN · Module M — Name*) immediately follows
            if i < len(blocks) and blocks[i][0] == "p":
                eyebrow_html = render_inline(blocks[i][1])
                # The eyebrow paragraph uses italic wrapping `*...*` — render_inline converts to <em>
                out.append(f'<p class="lesson-eyebrow">{eyebrow_html}</p>'); i += 1
            continue

        if kind == "h2":
            section_id = section_class(payload)
            out.append(f'<section class="{section_id}">')
            out.append(f'<h2 class="section-heading">{render_inline(payload)}</h2>')
            i += 1
            # Render every block until the next h2
            while i < len(blocks) and blocks[i][0] != "h2":
                k, p = blocks[i]
                if k == "p":
                    para_html = render_inline(p)
                    if section_id == "sec-keyconcepts":
                        takeaway = pull_takeaway(para_html)
                        if takeaway:
                            out.append('<div class="kc-row">')
                            out.append(f'<p>{para_html}</p>')
                            out.append(f'<aside class="takeaway"><div class="takeaway__label">Takeaway</div><div class="takeaway__body">{esc(takeaway)}</div></aside>')
                            out.append('</div>')
                        else:
                            out.append(f'<p>{para_html}</p>')
                    else:
                        out.append(f'<p>{para_html}</p>')
                elif k == "ul":
                    out.append("<ul>")
                    for item in p: out.append(f'<li>{render_inline(item)}</li>')
                    out.append("</ul>")
                elif k == "ol":
                    if section_id == "sec-tryThis":
                        out.append('<ol class="try-this">')
                        for idx, item in enumerate(p, 1):
                            out.append(f'<li><span class="try-num">{idx}</span><span class="try-body">{render_inline(item)}</span></li>')
                        out.append('</ol>')
                    else:
                        out.append('<ol>')
                        for item in p: out.append(f'<li>{render_inline(item)}</li>')
                        out.append('</ol>')
                elif k == "code":
                    lang, code = p
                    label = lang.upper() if lang else ""
                    label_html = f'<div class="code-label">{label}</div>' if label else ""
                    out.append(f'{label_html}<pre><code>{esc(code)}</code></pre>')
                i += 1
            out.append('</section>')
            continue

        i += 1  # safety
    return "\n".join(out)

# ----------------------------------------------------------------------------
# HTML page template
# ----------------------------------------------------------------------------
def page_html(num: str, body_html: str, lessons: dict, phase: dict) -> str:
    mod_color = phase["color"]
    mod_text  = phase["text_on"]
    mod_name  = phase["name"]
    title     = lessons[num]
    strip_right       = f"Lesson {num} · {mod_name}"
    strip_right_text  = strip_right          # template wraps in quotes for CSS content()
    footer_left_text  = title                # template wraps in quotes for CSS content()

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>{esc(title)}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Noto+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
  :root {{
    --ferra:        #71514F;
    --white-amber:  #F3EFEA;
    --cream-skin:   #E3D0C2;
    --congo-brown:  #4A2F2D;
    --lyzr-black:   #27272A;
    --module:       {mod_color};
    --module-text:  {mod_text};
  }}

  /* ---- Page setup ----
     @page margins reserve space on every printed page.
     @top-* / @bottom-* margin boxes render repeating wayfinding text
     (Chrome CSS Paged Media — reliable across every page including the first). */
  @page {{
    size: A4;
    margin: 18mm 18mm 16mm 18mm;

    @top-left {{
      content: "Lyzr University";
      font-family: 'JetBrains Mono', ui-monospace, monospace;
      font-weight: 500;
      font-size: 8pt;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--module);
      padding-bottom: 4mm;
    }}
    @top-right {{
      content: "{strip_right_text}";
      font-family: 'JetBrains Mono', ui-monospace, monospace;
      font-weight: 500;
      font-size: 8pt;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--module);
      padding-bottom: 4mm;
    }}
    @bottom-left {{
      content: "{footer_left_text}";
      font-family: 'JetBrains Mono', ui-monospace, monospace;
      font-weight: 500;
      font-size: 8pt;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--congo-brown);
      padding-top: 4mm;
    }}
    @bottom-right {{
      content: "studio.lyzr.ai";
      font-family: 'JetBrains Mono', ui-monospace, monospace;
      font-weight: 500;
      font-size: 8pt;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--module);
      padding-top: 4mm;
    }}
  }}

  /* Page 1 has the static colored module strip — suppress the duplicate
     wayfinding text from the @page top boxes there. */
  @page :first {{
    @top-left  {{ content: ""; }}
    @top-right {{ content: ""; }}
  }}

  * {{ box-sizing: border-box; }}
  html, body {{
    background: var(--white-amber);
    color: var(--lyzr-black);
    font-family: 'Noto Sans', system-ui, sans-serif;
    font-weight: 400;
    font-size: 10.5pt;
    line-height: 1.55;
    margin: 0;
    padding: 0;
    -webkit-font-smoothing: antialiased;
  }}

  /* ----- Module color band — page 1 only, full-bleed across the @page content area ----- */
  .module-strip {{
    background: var(--module);
    color: var(--module-text);
    height: 10mm;
    margin: -2mm -18mm 14pt -18mm;   /* extend slightly above and to page edges */
    padding: 0 18mm;
    display: flex; align-items: center; justify-content: space-between;
    font-family: 'JetBrains Mono', ui-monospace, monospace;
    font-weight: 500;
    font-size: 9pt;
    letter-spacing: 0.22em;
    text-transform: uppercase;
  }}

  /* No extra wrapper padding — content flows in the @page content area. */
  .page {{ padding: 0; margin: 0; }}

  /* ----- Lesson title block ----- */
  .lesson-title {{
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 700;
    font-size: 28pt;
    line-height: 1.08;
    color: var(--lyzr-black);
    letter-spacing: -0.01em;
    margin: 4pt 0 4pt 0;
    max-width: 75%;
  }}
  .lesson-eyebrow {{
    font-size: 0;  /* hide raw text — em inside re-shows */
    margin: 0 0 22pt 0;
  }}
  .lesson-eyebrow em {{
    font-family: 'JetBrains Mono', ui-monospace, monospace;
    font-weight: 500;
    font-style: normal;
    font-size: 9.5pt;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--ferra);
  }}

  /* ----- Section headings ----- */
  section {{ margin-top: 18pt; }}
  .section-heading {{
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 600;
    font-size: 16pt;
    line-height: 1.2;
    color: var(--module);
    margin: 0 0 12pt 0;
    page-break-after: avoid;
    break-after: avoid;
  }}

  /* ----- Body paragraphs ----- */
  p {{ margin: 0 0 11pt 0; max-width: 100%; }}
  strong {{ font-weight: 600; color: var(--lyzr-black); }}
  em {{ font-style: italic; color: var(--congo-brown); }}

  /* ----- What you'll learn — bullet list ----- */
  .sec-learn ul {{
    list-style: none;
    padding: 0;
    margin: 0 0 10pt 0;
  }}
  .sec-learn ul li {{
    position: relative;
    padding: 0 0 0 14pt;
    margin-bottom: 7pt;
    line-height: 1.5;
  }}
  .sec-learn ul li::before {{
    content: "";
    position: absolute;
    left: 0; top: 6pt;
    width: 5pt; height: 5pt;
    background: var(--ferra);
  }}

  /* ----- Key concepts — paragraph + side-by-side takeaway, table layout -----
     Using display:table avoids float overlap between adjacent rows. */
  .sec-keyconcepts .kc-row {{
    display: table;
    width: 100%;
    table-layout: fixed;
    border-spacing: 0;
    margin-bottom: 14pt;
    page-break-inside: auto;
    break-inside: auto;
  }}
  .sec-keyconcepts .kc-row > p {{
    display: table-cell;
    width: 68%;
    padding-right: 8mm;
    vertical-align: top;
    margin: 0;
  }}
  .sec-keyconcepts .takeaway {{
    display: table-cell;
    width: 32%;
    vertical-align: top;
    padding-top: 6pt;
    border-top: 1.2pt solid var(--module);
  }}
  .takeaway__label {{
    font-family: 'JetBrains Mono', ui-monospace, monospace;
    font-weight: 600;
    font-size: 7.5pt;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: var(--module);
    margin-bottom: 4pt;
  }}
  .takeaway__body {{
    font-family: 'Noto Sans', sans-serif;
    font-weight: 500;
    font-size: 9pt;
    line-height: 1.45;
    color: var(--congo-brown);
  }}

  /* ----- Code blocks ----- */
  code {{
    font-family: 'JetBrains Mono', ui-monospace, monospace;
    background: var(--cream-skin);
    padding: 1pt 4pt;
    border-radius: 3px;
    font-size: 0.92em;
    color: var(--congo-brown);
  }}
  .code-label {{
    font-family: 'JetBrains Mono', ui-monospace, monospace;
    font-weight: 600;
    font-size: 8pt;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: var(--module);
    margin: 14pt 0 4pt 0;
  }}
  pre {{
    background: var(--congo-brown);
    color: var(--white-amber);
    padding: 12pt 14pt;
    border-radius: 4px;
    margin: 0 0 12pt 0;
    page-break-inside: avoid;
    break-inside: avoid;
    font-size: 9pt;
    line-height: 1.5;
    overflow: hidden;
  }}
  pre code {{
    background: transparent;
    color: inherit;
    padding: 0;
    border-radius: 0;
    font-size: inherit;
  }}

  /* ----- Try this — distinctive CTA ----- */
  .sec-tryThis {{
    margin-top: 24pt;
    padding-left: 14pt;
    border-left: 2pt solid var(--ferra);
  }}
  .sec-tryThis .section-heading {{
    font-family: 'JetBrains Mono', ui-monospace, monospace;
    font-weight: 600;
    font-size: 11pt;
    letter-spacing: 0.16em;
    text-transform: uppercase;
    color: var(--ferra);
    margin-bottom: 14pt;
  }}
  .try-this {{
    list-style: none;
    padding: 0;
    margin: 0;
    counter-reset: t;
  }}
  .try-this li {{
    position: relative;
    padding-left: 38pt;
    min-height: 28pt;
    margin-bottom: 14pt;
    line-height: 1.55;
  }}
  .try-this .try-num {{
    position: absolute;
    left: 0; top: -4pt;
    font-family: 'Playfair Display', Georgia, serif;
    font-weight: 700;
    font-size: 22pt;
    color: var(--ferra);
    line-height: 1;
  }}
  .try-this .try-body {{ display: block; }}

</style>
</head>
<body>
  <!-- Static module strip — appears at top of page 1 only.
       Pages 2+ get wayfinding text via @page margin boxes. -->
  <div class="module-strip">
    <div>Lyzr University</div>
    <div>{esc(strip_right)}</div>
  </div>

  <div class="page">
{body_html}
  </div>
</body>
</html>
"""

# ----------------------------------------------------------------------------
# Render driver
# ----------------------------------------------------------------------------
def render_one(num: str, md_path: pathlib.Path, lessons: dict, phase: dict, chapter_name: str) -> pathlib.Path:
    md = md_path.read_text()
    body = build_body(md)
    full = page_html(num, body, lessons, phase)
    chapter = UPLOAD_DIR / chapter_name
    chapter.mkdir(parents=True, exist_ok=True)
    pdf_path = chapter / f"{num}b {safe_title(lessons[num])} Notes.pdf"
    with tempfile.TemporaryDirectory() as td:
        html_file = pathlib.Path(td) / f"{num}.html"
        html_file.write_text(full)
        cmd = [
            CHROME,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--no-pdf-header-footer",
            f"--print-to-pdf={pdf_path}",
            html_file.as_uri(),
        ]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if r.returncode != 0 and "--no-pdf-header-footer" in (r.stderr or ""):
            cmd = [c for c in cmd if c != "--no-pdf-header-footer"]
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        if r.returncode != 0:
            print(f"[{num}] Chrome failed: {r.stderr[-400:]}", file=sys.stderr)
        return pdf_path

def main():
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
    # Optional arg: a substring of a chapter folder to render just that course
    # (e.g. "07 Studio Design and Create" to avoid re-touching shipped courses).
    only = sys.argv[1] if len(sys.argv) > 1 else None
    for course in COURSES:
        if only and only not in course["chapter"]:
            continue
        for md in sorted(course["notes_dir"].glob("[0-9][0-9]-*.md")):
            m = re.match(r"^(\d{2})-", md.name)
            if not m: continue
            num = m.group(1)
            if num not in course["lessons"]: continue
            t0 = time.time()
            pdf = render_one(num, md, course["lessons"], course["phase"], course["chapter"])
            size_kb = pdf.stat().st_size / 1024 if pdf.exists() else 0
            print(f"[{course['chapter']}] {pdf.name} — {size_kb:.0f} KB in {time.time()-t0:.1f}s")

if __name__ == "__main__":
    main()
