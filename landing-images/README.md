# Lyzr Academy — Landing Images (HTML/CSS)

Brand-locked HTML compositions for the Academy and SDK Track landing pages. Open in a browser, screenshot, drop into Thinkific or any other surface.

Built against the Lyzr Visual Style Guide V2 (`agentpreneur/lyzr-brand.md`) — Ferra accent, White Amber background, Playfair Display headings, Noto Sans body, matte premium feel, no neons, no tech-bro blue, no drop shadows.

## Layout

```
landing-images/
├── README.md          (this file)
├── styles.css         Brand tokens + shared utilities (fonts, palette, frame sizes)
├── index.html         Gallery — links to both pages
├── academy.html       6 frames for the Academy / Lyzr University landing page
└── sdk-track.html     6 frames for the Lyzr for Developers course landing page
```

## How to use

1. **Open `index.html` in any modern browser** (Chrome, Safari, Firefox, Edge).
2. Click into **Academy** or **SDK Track**.
3. **Maximise the browser window** — the frames render at full pixel dimensions (the widest is 2100×900) so don't shrink the window or you'll get a downscaled capture.
4. **Screenshot each frame**:
   - macOS — `⌘ + ⇧ + 4`, then drag a selection across the frame
   - Windows — `⊞ + ⇧ + S`, then drag a selection
5. Snap the selection to the frame edges. The dark canvas around each frame is just visual spacing — don't include it in the capture.

For a higher-DPI screenshot (recommended for hero banners), zoom the browser to 150% or 200% before capturing, then resize down in your image editor.

### Want a different size?

All frames use fixed pixel dimensions set by the `.frame--16x9` / `.frame--4x5` / `.frame--square` / `.frame--21x9` classes in `styles.css`. Edit those rules to change output dimensions globally.

## Frame inventory

### `academy.html`

| # | Frame | Size | Slot on landing page |
|---|---|---|---|
| 01 | Hero banner | 1600×900 (16:9) | Top of page |
| 02 | Craftsmanship / depth | 1000×1000 (square) | "What craftsmanship looks like" |
| 03 | Pedagogy diagram | 1600×900 (16:9) | "How we teach" |
| 04 | Course card "01" | 800×1000 (4:5) | "Currently in session" |
| 05 | Audience composition | 1600×900 (16:9) | "Who Lyzr Academy is for" |
| 06 | Closing banner | 2100×900 (21:9) | Final CTA strip |

### `sdk-track.html`

| # | Frame | Size | Slot on landing page |
|---|---|---|---|
| 01 | Hero banner | 1600×900 (16:9) | Top of page |
| 02 | Capstones grid | 1600×900 (16:9) | "What you'll build" |
| 03 | Curriculum schematic | 1000×1000 (square) | "The curriculum" |
| 04 | What's different | 1600×900 (16:9) | Differentiator section |
| 05 | How it works | 1000×1000 (square) | "How it works" |
| 06 | Closing banner | 2100×900 (21:9) | Final CTA |

## Editing copy

Each headline / eyebrow / sub-line is right there in the HTML — find the matching `<h1>`, `<p class="subhead">`, or `<div class="eyebrow">` and edit in place.

For Lesson 08 note: in `sdk-track.html` the curriculum row labelling matches the renamed **File generation** title from the lesson recording. Update if you decide otherwise.

## Brand notes

- Palette tokens live in `:root` inside `styles.css`. Don't introduce off-palette colours.
- Headings always Playfair Display, weight ≥500. Never the thin/regular weights.
- Body text always Noto Sans.
- Decorative depth elements follow the **Elevate** layered diagonal pattern from the brand guide — stacked planes at increasing opacity in Ferra-family tones. Implemented inline as SVG.
- No drop shadows, no glows, no 3D effects, no bright gradients. Matte throughout.

## What this is not

This is a *static asset generator* — twelve renderable images, captured once and dropped into the Thinkific landing surface. It is **not** the production landing page itself. The Markdown content for the actual landing pages lives in `lyzr-university/landing/`.
