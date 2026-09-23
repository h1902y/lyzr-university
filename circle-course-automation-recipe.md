# Circle Course Creation — Deterministic Automation Recipe (Playwright)

Captured live on `academy.lyzr.ai` (Circle, Eclipse release) on 2026-06-29 while building a dummy course.
Goal: replace AI-native browser clicking with a **deterministic Playwright script**, mirroring the role the
`thinkific-uploader` plays today. Selectors below are **stable accessible names / roles / URL patterns**, not
pixel coordinates.

> **Auth note:** login is **email OTP** (`login.circle.so/sign_in?request_host=academy.lyzr.ai`). A headless
> Playwright run needs either a persisted authenticated storage state (cookies) captured after a human OTP
> login, or Circle's SSO/Headless auth. Do **not** script OTP entry.

## Hybrid strategy (API + Playwright)
- **Course shell + sections:** **Playwright only** — Circle's Admin API v2 is GET-only for courses/sections;
  v1 cannot create the course shell. (Open Circle feature request "Create Course in V2 API".)
- **Lessons (text/HTML/embed body):** **API-able** — Admin API **v1 has a POST create-lesson** taking
  `body_html` (assemble Vimeo/YouTube/PDF as HTML). No native media-file param.
- **Native media upload (mp4/pdf):** **Playwright** — but the uploader is a real `<input type="file">`, so
  `locator('input[type=file]').setInputFiles(path)` works (no drag-drop simulation needed). This is the big win.
- **Read/verify:** Admin API v1 — `GET /api/v1/course_sections`, `GET /api/v1/course_lessons` (note the
  `course_section_id` filter param is ignored — filter by `section_id` client-side), `GET /api/v1/space_members?space_id=` (enrollment proxy, has `count`).

## URL patterns
- Course (member/builder root): `https://academy.lyzr.ai/c/<course-slug>`
- Lesson/quiz editor: `https://academy.lyzr.ai/c/<course-slug>/edit-lesson/sections/<sectionId>/lessons/<lessonId>`
- Settings hub icon-rail: `/settings/{dashboard,emails,workflows,analytics,paywalls,affiliates_settings,plans,home,files}`, `/settings/ai-agents/{knowledge,agents}`, `/audience/manage`.

## Step-by-step (course shell + section + lesson)

```js
// 0) Pre: authenticated context (storageState from a prior human OTP login).
const page = await context.newPage();
await page.goto('https://academy.lyzr.ai/feed');

// 1) Open create-space menu (one "+" per space group; aria-label is stable)
await page.getByRole('button', { name: 'Add space or space group' }).first().click();
await page.getByText('Create space', { exact: true }).click();

// 2) Choose space type → Course
await page.getByRole('button', { name: 'Course' }).click();   // modal "Choose space type"
await page.getByRole('button', { name: 'Next' }).click();

// 3) Choose course type (Self-paced is preselected) → Next
await page.getByText('Self-paced').click();                   // or 'Structured' / 'Scheduled'
await page.getByRole('button', { name: 'Next' }).click();

// 4) Create a course space  (creates in DRAFT, hidden from members)
await page.getByPlaceholder('Your space name').fill('My Course Name');
// optional: space group dropdown; leave "Add members from this space group" toggle OFF
await page.getByRole('button', { name: 'Create space' }).click();
// → navigates to /c/<slug> (course dashboard). Capture slug from page.url().

// 5) Open the builder
await page.getByRole('button', { name: 'Edit lessons' }).click();   // → Lessons tab

// 6) Add a section, name it
await page.getByRole('button', { name: '+ Add section' }).click();
await page.getByRole('textbox').fill('Section 1 — Getting Started'); // inline section name field
await page.locator('button[type=submit]').near(theField).click();    // the ✓ confirm button

// 7) Add a lesson under the section
await page.getByRole('button', { name: '+ Add new' }).click();
await page.getByText('Lesson', { exact: true }).click();             // menu: Lesson | Quiz
// name + confirm (✓), then open editor:
await page.getByRole('button', { name: 'Edit' }).click();            // → edit-lesson URL

// 8) Lesson editor — media + body
//    Featured media is a real file input:
await page.locator('input[type=file]').setInputFiles('/path/to/video.mp4');
//    Body is a slash-command block editor (contenteditable). For text:
await page.locator('[contenteditable=true]').click();
await page.keyboard.type('Lesson body text...');
//    Settings (left panel) are radios/checkboxes by accessible name:
//      getByRole('radio', { name: 'Published' }), 'Enable featured media', 'Enforce video completion', etc.
await page.getByRole('button', { name: 'Save' }).click();
await page.getByRole('button', { name: 'Close' }).click();           // back to Lessons
```

## Quiz (optional, under a section)
- `+ Add new` → `Quiz` → name → `Edit`.
- Quiz settings (left panel): `Set a passing grade` (checkbox) + a `%` number input (e.g. 70);
  `Enforce passing grade to proceed`; `Hide answers on result page`.
- `Add question` modal: **Question type** = `Single answer` | `Multiple answer`; optional `Add video`/`Add image`;
  `Enter your question`; `Responses` options (radio = correct for single-answer); submit `Add question`.

## Publish / go-live (when ready — NOT done in the test run)
- Course status Draft→Published from the course dashboard / Customize; per-lesson Draft/Published radio.
- Set course **access** (it's created hidden) via the course members/access settings.

## Selector stability notes
- Prefer `getByRole`/`getByText`/`getByPlaceholder` (Circle's accessible names are consistent across the SPA).
- Inline name fields (section/lesson) render with a ✓ (submit) and ✕ (cancel) button pair — target the
  `button[type=submit]` within the editing row.
- The builder loads as a transition over the dashboard — add `waitForURL(/\/edit-lesson\//)` / `waitForSelector`
  rather than fixed sleeps.
- `descript-to-thinkific` mapping: today's **video.mp4 + notes.pdf** pair → a Circle lesson with the **mp4 as
  featured media** + the **notes rendered into the HTML body** (or attached under the Files tab). The renderer
  (`SDK-track/notes/_render_pdfs.py`) would need a Circle variant emitting an HTML body instead of a PDF.
