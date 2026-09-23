# Lyzr University — Thinkific theme (local mirror)

Local, git-tracked source of the Lyzr University storefront theme, so we edit the theme
**code** (Liquid + SCSS + JS) with real tools and version history — then sync to Thinkific.

## Theme IDs (Thinkific → Channels → Website → Theme Library)
| Theme | ID | Role |
|---|---|---|
| **Vogue** | `639418` | **PUBLISHED — live for ~199 learners. Never edit directly.** |
| **Vogue (Copy 1)** | `649350` | **Working sandbox — all edits + preview happen here.** |

Editor URL: `https://university.lyzr.ai/manage/custom_site_themes/649350/edit`
(reached via **Channels → Website → Theme Library → ⋮ → Edit code**).

## Structure (217 files)
`layouts/ · sections/ · site_pages/ · snippets/ · styles/ · assets/ · manifest.json`
Each file = a "view" with a numeric `key` (e.g. `sections/banner` → key `60721526`).

## Sync workflow (verified 2026-07-08)
- **Pull (full):** browser → `…/649350/export` downloads a theme **zip** → unzip here. ✅
- **Pull (single file, read-only):** in the editor, click the file → `window.themeStore.editor.getValue()`.
  (Read URL the editor uses = `…/view?view_id=<key>`.)
- **Push = zip RE-IMPORT (the reliable channel):** edit locally → zip the theme → import into the copy
  (`CustomSiteThemeImporter` / theme-editor Import). One upload covers all changed files.
- **Preview the copy:** `https://university.lyzr.ai?ctid=649350` (renders home with the draft theme).
- **Publish:** Theme Library → Vogue (Copy 1) → **Publish** (swaps it live) — only on approval.

### ⚠️ What does NOT work (don't retry)
- `editor.setValue(...)` + **Save All** does **not** persist — the app tracks dirty state in its own
  React state, not Ace's, so scripted edits are skipped by Save (verified: no `update_view` POST;
  preview unchanged). Reading via `getValue()` works; writing through the editor does not.
- Raw scripted `fetch('…/view?…')` is blocked by the browser privacy guard (query-string data).

## Golden rule
Live theme `639418` stays published + untouched. Build on `649350` → **Preview** → **Publish**
only on explicit approval.

## Internal API (editor-only, from `window.themeStore`)
- `themePath` `/manage/custom_site_themes/649350/theme`
- `getViewPath` `…/view` · `updateViewPath` `…/update_view`
- `exportThemePath` `…/export` · `updateSettingsPath` `…/update_settings`
