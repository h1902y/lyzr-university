#!/usr/bin/env python3
"""
Generate small, on-brand "placeholder course" slide PDFs for every Lyzr University
coming-soon course, so each empty Thinkific shell ships with something intentional.

For each coming-soon course (from catalog-demo/catalog-data.json) this writes FOUR
16:9 landscape slide-deck PDFs into the course's bundle folder — one PDF per Thinkific
lesson (the Content Uploader makes one lesson per file):

    01 Welcome.pdf          cover · what it is · who it's for · format · coming soon
    02 What You Will Learn.pdf   outcomes built from the description's topic list + skill chips
    03 Course Outline.pdf        planned lessons numbered from the topic list + capstone teaser
    04 Coming Soon.pdf           status (no dates) · get notified · explore live courses · thanks

Content is uniform/templated but ENRICHED per course by splitting each `description`
("<lead> — topic, topic, …, and <last>.") into a real topic list that drives decks 02 + 03.

Folders follow the reorganized, collection-organized bundle: `target_folder(course)` →
`{1 - Tracks/<product> | 2 - Modules | 3 - Functions}/NN <Title><suffix>` (NN = catalog index).

Rules:
  - Skip any folder that already holds a real .mp4 (don't bury recorded lessons). Only the partial
    ADK Tools & Workflows course qualifies (lesson 16) → set --include-partial to override.
  - Never touch live courses (they aren't coming-soon, so they're never visited).
  - No fabricated launch dates anywhere (Lyzr University planning is phase-wise, not time-bound).
  - Also (re)writes `_UPLOAD-GUIDE.md` — the ordered upload checklist for all 34 courses.

Render path mirrors SDK-track/notes/_render_pdfs.py: headless Chrome --print-to-pdf.

Usage:  python3 thinkific-upload/_generate_placeholders.py [--only <slug>] [--include-partial]
"""
from __future__ import annotations
import base64, html, json, pathlib, re, subprocess, sys, tempfile, time

# ── Paths ───────────────────────────────────────────────────────────────────
HERE     = pathlib.Path(__file__).resolve().parent          # …/thinkific-upload
DEMO     = HERE.parent / "catalog-demo"
CATALOG  = DEMO / "catalog-data.json"
CATMETA  = DEMO / "category-meta.json"
LOGO     = DEMO / "lyzr-logo.png"
CHROME   = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

INCLUDE_PARTIAL = "--include-partial" in sys.argv

# ── Bundle layout — collection-organized, numbered leaf folders ───────────────
# The bundle mirrors the catalog's three collections; every course is a numbered leaf folder
# (NN = the course's 1-based index in catalog-data.json `courses[]`, the canonical order).
SECTION = {"track": "1 - Tracks", "module": "2 - Modules", "function": "3 - Functions"}
# Coming-soon courses that already hold recorded media → no placeholders, labelled "(Partial)".
# (None currently — 04 ADK Tools & Workflows is fully recorded/live as of 2026-06-01.)
PARTIAL = set()

def display_title(course):
    """Catalog name → filesystem-safe folder title: drop ':' , '&'→'and', single-space."""
    return re.sub(r"\s{2,}", " ", course["name"].replace(":", "").replace("&", "and")).strip()

def status_suffix(course):
    if course["status"] == "live":     return ""
    if course["slug"] in PARTIAL:      return " (Partial)"
    return " (Coming Soon)"

def target_folder(course):
    """Absolute path to this course's leaf folder in the reorganized bundle."""
    leaf = f"{NUM[course['slug']]:02d} {display_title(course)}{status_suffix(course)}"
    base = HERE / SECTION[course["collection"]]
    if course["collection"] == "track":
        base = base / course["product"]
    return base / leaf

# Build-surface phrasing per product (no retired "no-code" framing).
PRODUCT_SURFACE = {
    "ADK":       "the Lyzr Agent Development Kit (Python)",
    "Studio":    "Lyzr Agent Studio",
    "Architect": "Lyzr Architect, the AI Studio visual builder",
}

DECKS = ["01 Welcome", "02 What You Will Learn", "03 Course Outline", "04 Coming Soon"]

# ── Small helpers ─────────────────────────────────────────────────────────────
def esc(s: str) -> str:
    return html.escape(str(s), quote=False)

def inline(text: str) -> str:
    """**bold** → <strong>, *italic* → <em>; everything else escaped."""
    text = esc(text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"(?<!\*)\*([^*\n]+)\*(?!\*)", r"<em>\1</em>", text)
    return text

def cap(s: str) -> str:
    s = s.strip()
    return s[:1].upper() + s[1:] if s else s

def sanitize(s: str) -> str:
    """Retire the deprecated 'no-code' framing in any learner-facing copy (AI Studio terminology)."""
    return re.sub(r"\bno[\s-]?code\b", "the AI Studio visual builder", s, flags=re.I)

def split_topics(description: str):
    """'<lead> — t, t, …, and <last>.' → (lead, [topics]); 'no-code' framing sanitized out."""
    parts = re.split(r"\s+[—–]\s+", description, maxsplit=1)
    if len(parts) == 2:
        lead, rest = parts[0].strip(), parts[1].strip()
    else:
        lead, rest = description.strip(), ""
    rest = rest.rstrip(".").strip()
    topics = []
    for chunk in re.split(r",\s+", rest):
        c = chunk.strip()
        c = re.sub(r"^and\s+(an?\s+)?", "", c)   # drop leading "and " / "and a " / "and an "
        if c:
            topics.append(sanitize(c))
    return sanitize(lead), topics

def balanced_chunks(items, max_per):
    """Split into balanced slides of at most max_per (avoids a lone trailing item)."""
    import math
    n = len(items)
    if n == 0:
        return []
    slides = max(1, math.ceil(n / max_per))
    per = math.ceil(n / slides)
    return [items[i:i+per] for i in range(0, n, per)]

def is_capstone(topic: str) -> bool:
    return bool(re.search(r"\b(project|capstone|build|bot|assistant|pipeline|walkthrough)\b", topic, re.I)) \
        and bool(re.search(r"\bproject\b|capstone|bot|assistant|pipeline", topic, re.I))

# ── Catalog + brand data ──────────────────────────────────────────────────────
DATA = json.loads(CATALOG.read_text())
META = json.loads(CATMETA.read_text())
LOGO_B64 = base64.b64encode(LOGO.read_bytes()).decode()

# Canonical course number = 1-based index in catalog order. Drives leaf-folder NN prefixes.
NUM = {c["slug"]: i + 1 for i, c in enumerate(DATA["courses"])}
LIVE = [c["name"] for c in DATA["courses"] if c.get("status") == "live"]

def cat_meta(course):
    """{color, icon} for the course's primary category, with a defensive fallback."""
    col = course["collection"]
    table, key = None, None
    if col == "track":
        table, key = META.get("products", {}), course.get("product")
    elif col == "module":
        table, key = META.get("modules", {}), (course.get("modules") or [course["name"]])[0]
    elif col == "function":
        table, key = META.get("usecases", {}), course.get("function")
    entry = (table or {}).get(key or "", {})
    return {"color": entry.get("color", "#71514F"), "icon": entry.get("icon", "")}

def badge_for(course):
    col, lvl = course["collection"], course.get("level", "")
    if col == "track":
        return f"{course['product']} Track" + (f" · {lvl}" if lvl else "")
    if col == "module":
        return "Module" + (f" · {lvl}" if lvl else "")
    return "Function" + (f" · {lvl}" if lvl else "")

def audience_for(course):
    col = course["collection"]
    if col == "track":
        surface = PRODUCT_SURFACE.get(course["product"], f"Lyzr {course['product']}")
        return f"Developers and builders who want to build agents hands-on with **{surface}**."
    if col == "module":
        return (f"Anyone leveling up the craft of **{course['name']}** — the concepts and patterns "
                f"apply across any stack, not tied to a single Lyzr product.")
    return (f"**{course['function']}** leaders and operators deciding where agentic AI fits — "
            f"strategy, use cases and ROI, not implementation.")

def format_line(course):
    n, dur, who = course.get("lessons", 0), course.get("duration", ""), course.get("instructor", "")
    bits = []
    if n:        bits.append(f"{n} lessons")
    if dur:      bits.append(dur)
    if who:      bits.append(f"with {who}")
    return " · ".join(bits)

# ── CSS (16:9 slides, Lyzr brand) ─────────────────────────────────────────────
CSS = """
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700;800&family=Noto+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');
:root{
  --ferra:#71514F; --amber:#F3EFEA; --cream:#E3D0C2; --congo:#4A2F2D; --black:#27272A;
  --t6:#BA998D; --t8:#9E7A73; --t4:#D2B7A8;
  --accent:#71514F;
}
*{box-sizing:border-box;margin:0;padding:0;}
html,body{-webkit-print-color-adjust:exact;print-color-adjust:exact;font-family:'Noto Sans',system-ui,sans-serif;color:var(--black);}
@page{size:13.333in 7.5in;margin:0;}
.slide{position:relative;width:13.333in;height:7.5in;overflow:hidden;page-break-after:always;break-after:page;}
.slide:last-child{page-break-after:auto;break-after:auto;}
.pad{position:relative;z-index:3;height:100%;padding:0.82in 0.95in;display:flex;flex-direction:column;}
.center{justify-content:center;}

/* themes */
.dark{background:radial-gradient(ellipse 60% 120% at 22% 50%,rgba(113,81,79,0.5) 0%,transparent 62%),linear-gradient(118deg,#3F2826 0%,#2A1817 56%,#1C0F0F 100%);color:var(--amber);}
.light{background:var(--amber);color:var(--black);}
.tint{background:linear-gradient(120deg,#F6F2ED 0%,#ECE2DA 60%,var(--cream) 100%);color:var(--black);}

/* Elevate bands */
.elevate{position:absolute;top:-40%;right:-16%;width:66%;height:182%;z-index:1;pointer-events:none;}
.elevate .b{position:absolute;inset:0;border-radius:120px;transform:rotate(-26deg);}
.dark .b1{background:#E3D0C2;opacity:.05;transform:rotate(-26deg) translateX(0);}
.dark .b2{background:#C6A89A;opacity:.08;transform:rotate(-26deg) translateX(8%);}
.dark .b3{background:#9E7A73;opacity:.14;transform:rotate(-26deg) translateX(16%);}
.dark .b4{background:#71514F;opacity:.26;transform:rotate(-26deg) translateX(24%);}
.dark .b5{background:#4A2F2D;opacity:.5;transform:rotate(-26deg) translateX(32%);}
.tint .b1{background:#DEC6B6;opacity:.3;transform:rotate(-26deg) translateX(0);}
.tint .b2{background:#C6A89A;opacity:.34;transform:rotate(-26deg) translateX(10%);}
.tint .b3{background:#9E7A73;opacity:.3;transform:rotate(-26deg) translateX(20%);}

/* watermark icon */
.wm{position:absolute;right:-0.9in;top:50%;transform:translateY(-50%);width:8.4in;height:8.4in;z-index:1;}
.wm svg{width:100%;height:100%;stroke-width:1.1;}
.dark .wm{color:#E3D0C2;opacity:.12;}
.tint .wm{color:var(--accent);opacity:.10;}

/* logo */
.logo-row{display:flex;align-items:center;gap:14px;position:absolute;top:0.7in;left:0.95in;z-index:4;}
.logo{height:38px;}
.dark .logo{filter:brightness(0) invert(1);}
.logo-div{width:1px;height:24px;background:currentColor;opacity:.32;}
.logo-lbl{font-family:'JetBrains Mono',monospace;font-weight:500;font-size:13px;letter-spacing:.26em;text-transform:uppercase;opacity:.85;}

/* type */
.eyebrow{font-family:'JetBrains Mono',monospace;font-weight:600;font-size:15px;letter-spacing:.2em;text-transform:uppercase;color:var(--accent);margin-bottom:18px;}
.dark .eyebrow{color:#DEC6B6;}
.bar{width:70px;height:5px;background:var(--accent);border-radius:3px;margin-bottom:22px;}
h1{font-family:'Playfair Display',Georgia,serif;font-weight:800;font-size:58px;line-height:1.07;letter-spacing:-.01em;max-width:9.5in;}
h1 em{font-style:italic;font-weight:500;color:var(--accent);}
.dark h1 em{color:#DEC6B6;}
h2{font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:40px;line-height:1.12;margin-bottom:18px;max-width:9in;}
.lead{font-size:22px;line-height:1.5;font-weight:400;opacity:.86;max-width:8.4in;}
.kicker{font-family:'JetBrains Mono',monospace;font-size:13px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin-top:20px;opacity:.9;}
.dark .kicker{color:#C9A99A;}

/* pill */
.pill{display:inline-flex;align-items:center;gap:9px;align-self:flex-start;padding:9px 18px;border-radius:999px;background:var(--accent);color:#F3EFEA;font-family:'JetBrains Mono',monospace;font-weight:600;font-size:14px;letter-spacing:.14em;text-transform:uppercase;margin-top:24px;}
.dark .pill{background:rgba(227,208,194,.16);color:#E3D0C2;border:1px solid rgba(227,208,194,.4);}

/* lists */
ul.feat{list-style:none;margin-top:8px;}
ul.feat li{position:relative;padding-left:30px;margin-bottom:18px;font-size:22px;line-height:1.45;max-width:8.6in;}
ul.feat li::before{content:"";position:absolute;left:0;top:11px;width:11px;height:11px;background:var(--accent);border-radius:2px;}

/* numbered outline */
ol.outline{list-style:none;counter-reset:l;margin-top:6px;}
ol.outline li{position:relative;padding-left:64px;margin-bottom:22px;min-height:40px;}
ol.outline li .n{position:absolute;left:0;top:-6px;font-family:'Playfair Display',serif;font-weight:700;font-size:40px;color:var(--accent);line-height:1;}
.dark ol.outline li .n{color:#C9A99A;}
ol.outline li .t{font-size:22px;line-height:1.4;display:block;padding-top:4px;}
.cap-tag{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--accent);border:1px solid var(--accent);border-radius:4px;padding:2px 8px;margin-left:10px;vertical-align:middle;}

/* chips */
.chips{display:flex;flex-wrap:wrap;gap:12px;margin-top:14px;}
.chip{display:inline-flex;align-items:center;gap:9px;padding:10px 16px;border-radius:999px;border:1.5px solid var(--accent);font-family:'JetBrains Mono',monospace;font-weight:500;font-size:15px;letter-spacing:.04em;color:var(--accent);}
.dark .chip{border-color:rgba(227,208,194,.5);color:#E3D0C2;}
.chip svg{width:18px;height:18px;}

/* meta grid */
.meta{display:flex;gap:0.7in;margin-top:14px;}
.meta .m .k{font-family:'JetBrains Mono',monospace;font-size:12px;letter-spacing:.18em;text-transform:uppercase;opacity:.6;margin-bottom:8px;}
.meta .m .v{font-family:'Playfair Display',serif;font-weight:600;font-size:34px;color:var(--accent);}
.dark .meta .m .v{color:#DEC6B6;}

.foot{position:absolute;bottom:0.55in;left:0.95in;right:0.95in;display:flex;justify-content:space-between;font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:.16em;text-transform:uppercase;opacity:.55;z-index:4;}
"""

def page(slides_html: str, accent: str) -> str:
    return (f"<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'>"
            f"<style>{CSS}</style></head>"
            f"<body style='--accent:{accent}'>{slides_html}</body></html>")

def logo_row(label="University"):
    return (f"<div class='logo-row'><img class='logo' src='data:image/png;base64,{LOGO_B64}' alt='Lyzr'>"
            f"<span class='logo-div'></span><span class='logo-lbl'>{esc(label)}</span></div>")

def wm(icon):
    return f"<div class='wm'>{icon}</div>" if icon else ""

def elevate(theme):
    if theme == "dark":
        return "<div class='elevate'><div class='b b1'></div><div class='b b2'></div><div class='b b3'></div><div class='b b4'></div><div class='b b5'></div></div>"
    return "<div class='elevate'><div class='b b1'></div><div class='b b2'></div><div class='b b3'></div></div>"

def foot(course):
    return f"<div class='foot'><span>Lyzr University</span><span>{esc(course['name'])}</span></div>"

# ── Deck builders ─────────────────────────────────────────────────────────────
def deck_welcome(course, meta, lead, topics):
    icon = meta["icon"]
    s = []
    # 1 — cover
    s.append(f"<section class='slide dark'>{elevate('dark')}{wm(icon)}{logo_row()}"
             f"<div class='pad center'><div class='eyebrow'>{esc(badge_for(course))}</div>"
             f"<h1>{inline(course['name'])}</h1>"
             f"<div class='pill'>Coming soon</div></div></section>")
    # 2 — what this course is
    s.append(f"<section class='slide light'>{elevate('tint')}<div class='pad'>"
             f"<div class='eyebrow'>What this course is</div><div class='bar'></div>"
             f"<h2>{inline(cap(lead))}.</h2>"
             f"<p class='lead'>A focused, hands-on course in the Lyzr University catalog — "
             f"part of the <strong>{esc(badge_for(course))}</strong> collection.</p>"
             f"{foot(course)}</div></section>")
    # 3 — who it's for
    s.append(f"<section class='slide tint'>{wm(icon)}<div class='pad center'>"
             f"<div class='eyebrow'>Who it's for</div><div class='bar'></div>"
             f"<p class='lead'>{inline(audience_for(course))}</p>{foot(course)}</div></section>")
    # 4 — format
    n, dur, who = course.get("lessons", 0), course.get("duration", ""), course.get("instructor", "")
    cells = []
    if n:   cells.append(("Lessons", str(n)))
    cells.append(("Duration" if n else "Format", dur or "—"))
    if who: cells.append(("Instructor", who))
    meta_html = "".join(f"<div class='m'><div class='k'>{esc(k)}</div><div class='v'>{esc(v)}</div></div>" for k, v in cells)
    s.append(f"<section class='slide light'>{elevate('tint')}<div class='pad'>"
             f"<div class='eyebrow'>The format</div><div class='bar'></div>"
             f"<h2>What to expect</h2><div class='meta'>{meta_html}</div>"
             f"<p class='lead' style='margin-top:28px'>Short, practical lessons you can follow end to end.</p>"
             f"{foot(course)}</div></section>")
    # 5 — coming soon
    s.append(f"<section class='slide dark'>{elevate('dark')}{wm(icon)}{logo_row()}<div class='pad center'>"
             f"<div class='eyebrow'>Lyzr University</div>"
             f"<h1>Almost <em>here</em>.</h1>"
             f"<p class='lead' style='margin-top:18px'>This course is in active production. "
             f"Enroll to be notified the moment it goes live.</p></div></section>")
    return page("".join(s), meta["color"])

def deck_learn(course, meta, lead, topics):
    icon = meta["icon"]
    s = []
    s.append(f"<section class='slide dark'>{elevate('dark')}{wm(icon)}{logo_row()}<div class='pad center'>"
             f"<div class='eyebrow'>{esc(badge_for(course))}</div><h1>What you'll <em>learn</em></h1></div></section>")
    # outcome slides — balanced, up to 3 topics per slide
    groups = balanced_chunks(topics, 3) or [[lead]]
    for gi, grp in enumerate(groups):
        items = "".join(f"<li>{inline(cap(t))}</li>" for t in grp)
        head = "By the end, you'll have worked through:" if gi == 0 else "…and:"
        s.append(f"<section class='slide light'>{elevate('tint')}<div class='pad'>"
                 f"<div class='eyebrow'>What you'll learn</div><div class='bar'></div>"
                 f"<h2>{esc(head)}</h2><ul class='feat'>{items}</ul>{foot(course)}</div></section>")
    # skill chips slide
    tags = course.get("modules") or ([course["function"]] if course.get("function") else [])
    chips = ""
    for t in tags:
        ic = (META.get("modules", {}).get(t) or META.get("usecases", {}).get(t) or {}).get("icon", "")
        chips += f"<span class='chip'>{ic}{esc(t)}</span>"
    if chips:
        s.append(f"<section class='slide tint'><div class='pad'>"
                 f"<div class='eyebrow'>Skills you'll build</div><div class='bar'></div>"
                 f"<h2>Part of the Lyzr University skill map</h2>"
                 f"<div class='chips'>{chips}</div>"
                 f"<p class='lead' style='margin-top:30px'>Stack courses across the catalog toward a "
                 f"Specialist credential.</p>{foot(course)}</div></section>")
    return page("".join(s), meta["color"])

def deck_outline(course, meta, lead, topics):
    icon = meta["icon"]
    s = []
    s.append(f"<section class='slide dark'>{elevate('dark')}{wm(icon)}{logo_row()}<div class='pad center'>"
             f"<div class='eyebrow'>{esc(badge_for(course))}</div><h1>Course <em>outline</em></h1>"
             f"<p class='lead' style='margin-top:16px'>The planned lesson path for this course.</p></div></section>")
    items = topics or [lead]
    groups = balanced_chunks(list(enumerate(items, 1)), 4)
    for grp in groups:
        lis = ""
        for n, t in grp:
            tag = "<span class='cap-tag'>Capstone</span>" if is_capstone(t) else ""
            lis += f"<li><span class='n'>{n}</span><span class='t'>{inline(cap(t))}{tag}</span></li>"
        s.append(f"<section class='slide light'>{elevate('tint')}<div class='pad'>"
                 f"<div class='eyebrow'>Planned lessons</div><div class='bar'></div>"
                 f"<ol class='outline'>{lis}</ol>{foot(course)}</div></section>")
    # closing teaser
    s.append(f"<section class='slide tint'>{wm(icon)}<div class='pad center'>"
             f"<div class='eyebrow'>Build along</div><div class='bar'></div>"
             f"<h2>Every lesson ends with something you can run.</h2>"
             f"<p class='lead'>Final outline may shift as the course is recorded.</p>{foot(course)}</div></section>")
    return page("".join(s), meta["color"])

def deck_coming(course, meta, lead, topics):
    icon = meta["icon"]
    live_html = "".join(f"<li>{esc(name)}</li>" for name in LIVE)
    s = []
    s.append(f"<section class='slide dark'>{elevate('dark')}{wm(icon)}{logo_row()}<div class='pad center'>"
             f"<div class='eyebrow'>Status</div><h1>In <em>production</em></h1>"
             f"<p class='lead' style='margin-top:18px'>We're recording and editing this course now. "
             f"No placeholder fluff for long — real lessons are on the way.</p></div></section>")
    s.append(f"<section class='slide tint'><div class='pad center'>"
             f"<div class='eyebrow'>Get notified</div><div class='bar'></div>"
             f"<h2>Be first in when it launches.</h2>"
             f"<p class='lead'>Enroll now and Lyzr University will let you know the moment "
             f"<strong>{esc(course['name'])}</strong> goes live.</p>{foot(course)}</div></section>")
    s.append(f"<section class='slide light'>{elevate('tint')}<div class='pad'>"
             f"<div class='eyebrow'>Available now</div><div class='bar'></div>"
             f"<h2>Start building today</h2>"
             f"<p class='lead' style='margin-bottom:14px'>Live courses you can take right now:</p>"
             f"<ul class='feat'>{live_html}</ul>{foot(course)}</div></section>")
    s.append(f"<section class='slide dark'>{elevate('dark')}{logo_row()}<div class='pad center'>"
             f"<h1>See you in <em>class</em>.</h1>"
             f"<div class='kicker'>Lyzr University · Learn to build with Lyzr</div></div></section>")
    return page("".join(s), meta["color"])

BUILDERS = {
    "01 Welcome": deck_welcome,
    "02 What You Will Learn": deck_learn,
    "03 Course Outline": deck_outline,
    "04 Coming Soon": deck_coming,
}

# ── Render ────────────────────────────────────────────────────────────────────
def render_pdf(html_str: str, out_path: pathlib.Path):
    with tempfile.TemporaryDirectory() as td:
        hf = pathlib.Path(td) / "deck.html"
        hf.write_text(html_str)
        cmd = [CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
               "--no-pdf-header-footer", f"--print-to-pdf={out_path}", hf.as_uri()]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if r.returncode != 0 and "--no-pdf-header-footer" in (r.stderr or ""):
            cmd = [c for c in cmd if c != "--no-pdf-header-footer"]
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=90)
        if r.returncode != 0:
            print(f"   ! Chrome failed: {(r.stderr or '')[-300:]}", file=sys.stderr)

# ── Upload guide ──────────────────────────────────────────────────────────────
def rel(course):
    return target_folder(course).relative_to(HERE).as_posix()

def status_label(course):
    if course["status"] == "live":   return "live"
    if course["slug"] in PARTIAL:    return "partial"
    return "coming-soon"

def categories_for(course):
    col = course["collection"]
    if col == "track":
        tags = ["Track", course["product"]] + course.get("modules", [])
    elif col == "module":
        tags = ["Module"] + (course.get("modules") or [course["name"]])
    else:
        tags = ["Function", course["function"]]
    seen = []
    for t in tags:
        if t and t not in seen:
            seen.append(t)
    return " · ".join(seen)

def files_to_drag(course):
    if course["status"] == "live":
        n = course.get("videos") or course.get("lessons") or 0
        return f"{n} video + {n} notes ({n * 2} files)"
    if course["slug"] in PARTIAL:
        return "partial — recorded lessons only"
    return "4 placeholder PDFs"

def write_upload_guide():
    cats = DATA["categories"]
    N = len(DATA["courses"])
    L = []
    L.append("# Lyzr University — Thinkific upload guide\n")
    L.append(f"Turnkey checklist for creating all {N} courses on Thinkific. Each course is one folder — "
             "open it, select every file, drag into the **Content Uploader** (one file → one lesson). "
             "Work top to bottom.\n")
    L.append("> Generated by `_generate_placeholders.py`; don't hand-edit — re-run to refresh.\n")

    L.append("## 1 · Create these Categories first")
    L.append("In **Settings → Categories**, create the full set below before uploading, so you can tag "
             "each course without stopping mid-session:\n")
    L.append(f"- **Collection:** Track · Module · Function")
    L.append(f"- **Product:** {' · '.join(cats['products'])}")
    L.append(f"- **Module ({len(cats['modules'])}):** {' · '.join(cats['modules'])}")
    L.append(f"- **Function ({len(cats['functions'])}):** {' · '.join(cats['functions'])}")
    L.append("\n> `Multimodal` is in the catalog's module list but missing from `category-meta.json` — "
             "cosmetic only (it affects a deck watermark icon, not the Thinkific category). Create the "
             "`Multimodal` category normally.\n")

    L.append("## 2 · Courses (in upload order)\n")
    L.append("| # | Course (Thinkific title) | Status | Folder | Categories to tag | Drag in |")
    L.append("|---|---|---|---|---|---|")
    for c in DATA["courses"]:
        L.append(f"| {NUM[c['slug']]:02d} | {c['name']} | {status_label(c)} | `{rel(c)}` "
                 f"| {categories_for(c)} | {files_to_drag(c)} |")
    L.append("")

    L.append("## 3 · How to upload one course\n")
    L.append("1. **Products → Courses → New course** — name it the course title above (or open the existing one).")
    L.append("2. Tag it with the Categories listed in its row.")
    L.append("3. Open the folder, select all files (`⌘A`), drag into the **Content Uploader**. One file → one lesson; "
             "don't leave the tab mid-upload.")
    L.append("4. Reorder / rename lessons as needed (8-dot handle).")
    L.append("5. **Coming-soon courses** publish with a *Coming soon* marker. When real lessons are recorded, "
             "delete the `0N *.pdf` placeholders first, then upload the real videos + notes.\n")
    L.append(f"> **Two number systems:** the folder prefix `NN` is the course index (01–{N:02d}). Inside "
             "`1 - Tracks/ADK/04 ADK Tools and Workflows/` the files keep their SDK-track lesson "
             "numbers (`16a`/`16b`) — that's correct, don't renumber them.")

    (HERE / "_UPLOAD-GUIDE.md").write_text("\n".join(L) + "\n")
    print("✓ wrote _UPLOAD-GUIDE.md")

# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    only = None
    if "--only" in sys.argv:
        only = sys.argv[sys.argv.index("--only") + 1]
    coming = [c for c in DATA["courses"] if c.get("status") == "coming-soon"]
    made = skipped = 0
    for course in coming:
        if only and course["slug"] != only:
            continue
        folder = target_folder(course)
        if not INCLUDE_PARTIAL and folder.exists() and any(folder.glob("*.mp4")):
            print(f"— skip {course['slug']} (folder already has recorded video)")
            skipped += 1
            continue
        folder.mkdir(parents=True, exist_ok=True)
        meta = cat_meta(course)
        lead, topics = split_topics(course["description"])
        t0 = time.time()
        for deck in DECKS:
            html_str = BUILDERS[deck](course, meta, lead, topics)
            render_pdf(html_str, folder / f"{deck}.pdf")
        made += 1
        print(f"✓ {course['slug']:<34} → {folder.relative_to(HERE)}  (4 PDFs, {time.time()-t0:.1f}s)")
    if not only:
        write_upload_guide()
    print(f"\nDone: {made} placeholder courses ({made*4} PDFs), {skipped} skipped.")

if __name__ == "__main__":
    main()
