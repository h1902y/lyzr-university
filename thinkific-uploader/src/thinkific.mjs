// Thinkific admin — Classic Course Builder page object.
//
// Selectors below were captured from the LIVE admin (2026-06-17, university.lyzr.ai) via recon —
// mostly stable data-testids. We use the **Classic course** path (not "New course builder") because
// (a) it matches the chapter + video/PDF structure of the existing courses, and (b) new-builder
// courses are excluded from the REST API, which would break thinkific_verify.py.
//
// Media is uploaded through the bulk **"Upload content"** flow: one chapter's uploader takes ALL
// files at once via an OS file-chooser (handled by Playwright's filechooser event — no OS dialog),
// and Thinkific creates one lesson per file, named from the filename, ordered by the NNa/NNb prefix.
const UPLOAD_TIMEOUT = 60 * 60 * 1000;   // generous — many GB + transcoding kickoff
const UI = 25 * 1000;
const API = 'https://api.thinkific.com/api/public/v1/';
const API_UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124 Safari/537.36';

export class ThinkificAdmin {
  /** @param {import('playwright').Page} page */
  constructor(page, { adminUrl, token }) {
    this.page = page;
    this.base = new URL(adminUrl).origin;   // https://university.lyzr.ai (after redirect)
    this.adminUrl = adminUrl;
    this.token = token;
    this.step = '(init)';
    this.courseId = null;
  }
  _log(s) { this.step = s; process.stdout.write(`        · ${s}\n`); }

  /** The course's chapter ids via the public API — deterministic (no DOM render race). */
  async _apiChapterIds() {
    const h = { Authorization: `Bearer ${this.token}`, 'User-Agent': API_UA };
    const c = await (await fetch(`${API}courses/${this.courseId}`, { headers: h })).json();
    return c.chapter_ids || [];
  }

  /** Courses whose name starts with the given prefix (via API) — used to detect a new duplicate. */
  async _apiCoursesByName(prefix) {
    const h = { Authorization: `Bearer ${this.token}`, 'User-Agent': API_UA };
    const d = await (await fetch(`${API}courses?limit=250`, { headers: h })).json();
    return (d.items || []).filter((c) => c.name.toLowerCase().startsWith(prefix.toLowerCase()));
  }

  /** Ordered content ids across all of the course's chapters (via API). */
  async _apiContentIds() {
    const h = { Authorization: `Bearer ${this.token}`, 'User-Agent': API_UA };
    const course = await (await fetch(`${API}courses/${this.courseId}`, { headers: h })).json();
    const ids = [];
    for (const chid of course.chapter_ids || []) {
      const ch = await (await fetch(`${API}chapters/${chid}`, { headers: h })).json();
      ids.push(...(ch.content_ids || []));
    }
    return ids;
  }

  /** Count lessons in the course via the public API — the source of truth for upload completion. */
  async _apiContentCount() {
    const h = { Authorization: `Bearer ${this.token}`, 'User-Agent': API_UA };
    const course = await (await fetch(`${API}courses/${this.courseId}`, { headers: h })).json();
    let n = 0;
    for (const chid of course.chapter_ids || []) {
      const ch = await (await fetch(`${API}chapters/${chid}`, { headers: h })).json();
      n += (ch.content_ids || []).length;
    }
    return n;
  }

  /** Locate by Thinkific's test attribute — it uses data-qa (not data-testid); match either. */
  qa(name) { return this.page.locator(`[data-qa="${name}"], [data-testid="${name}"]`); }

  /** Click the first VISIBLE match of a locator (admin renders responsive desktop+mobile dupes). */
  async _clickVisible(locator, { timeout = UI } = {}) {
    const deadline = Date.now() + timeout;
    while (Date.now() < deadline) {
      const n = await locator.count();
      for (let i = 0; i < n; i++) {
        const el = locator.nth(i);
        if (await el.isVisible().catch(() => false)) {
          await el.scrollIntoViewIfNeeded({ timeout: 3000 }).catch(() => {});
          try { await el.click({ timeout: 6000 }); return; } catch { /* covered/animating — keep polling */ }
        }
      }
      await this.page.waitForTimeout(300);
    }
    throw new Error(`no visible element to click for step "${this.step}"`);
  }

  /** Fill the first VISIBLE match (handles responsive dupes + focus quirks). */
  async _fillVisible(locator, value, { timeout = UI } = {}) {
    const deadline = Date.now() + timeout;
    while (Date.now() < deadline) {
      const n = await locator.count();
      for (let i = 0; i < n; i++) {
        const el = locator.nth(i);
        if (await el.isVisible().catch(() => false)) {
          await el.scrollIntoViewIfNeeded().catch(() => {});
          await el.click({ timeout: 5000 }).catch(() => {});
          await el.fill(value, { timeout: 8000 });
          return;
        }
      }
      await this.page.waitForTimeout(250);
    }
    throw new Error(`no visible field to fill for step "${this.step}"`);
  }

  async gotoCourses() {
    this._log('open admin → courses');
    await this.page.goto(this.adminUrl, { waitUntil: 'domcontentloaded' });
    await this._settle();
    if (/\/(users\/)?sign_in|login/i.test(this.page.url()))
      throw new Error('not logged in — run `npm run auth` (session/Cloudflare clearance expired)');
    this.base = new URL(this.page.url()).origin;
  }

  /** If a course with this exact name exists, adopt its id (via the API — deterministic, unlike
   *  matching a course-card link in the UI, which spawned duplicates). Else return false. */
  async findExistingCourse(name) {
    this._log(`look for existing course "${name}"`);
    const h = { Authorization: `Bearer ${this.token}`, 'User-Agent': API_UA };
    const data = await (await fetch(`${API}courses?limit=250`, { headers: h })).json();
    const hit = (data.items || []).find((c) => c.name === name);
    if (hit) { this.courseId = String(hit.id); return true; }
    return false;
  }

  /** New course → Classic course → land on the auto-created editor. Adopt its id. */
  async createCourse() {
    this._log('create Classic course');
    await this.page.goto(`${this.base}/manage/courses`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    await this._clickVisible(this.page.getByRole('button', { name: 'New course' }));
    await this._clickVisible(this.page.getByText('Classic course', { exact: true }));
    // "Classic course" opens an AI outline wizard — skip it to create a blank course.
    await this._clickVisible(this.page.getByText(/skip\b.*blank product/i));
    await this.page.waitForURL(/\/manage\/courses\/\d+/, { timeout: UI });
    await this._settle();
    this.courseId = (this.page.url().match(/\/courses\/(\d+)/) || [])[1];
    if (!this.courseId) throw new Error('created course but could not read its id from the URL');
    return this.courseId;
  }

  /** Duplicate a configured TEMPLATE course (inherits pricing/collection/card/landing design, NOT
   *  certificate or chapters). The "Are you sure…?" is a native confirm — auto-accepted by the
   *  dialog handler set in upload.mjs. Adopts the new "Copy of <template>" id. */
  /** A course can only be duplicated from the active Courses list. If the TEMPLATE has been
   *  archived (to keep the active list tidy), restore it first. Verified 2026-06-30. */
  async _unarchiveIfArchived(name) {
    await this.page.goto(`${this.base}/manage/courses`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    if (await this.page.getByRole('button', { name: `Actions for ${name}` }).count()) return;
    this._log(`"${name}" not in active courses — unarchiving`);
    await this.page.goto(`${this.base}/manage/courses/archived`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    const act = this.page.getByRole('button', { name: `Actions for ${name}` });
    if (!(await act.count())) throw new Error(`template "${name}" not found in active OR archived courses`);
    await this._clickVisible(act.first());
    await this.page.waitForTimeout(800);
    await this._clickVisible(this.page.getByRole('menuitem', { name: /unarchive/i }));
    await this.page.waitForTimeout(800);
    const confirm = this.page.getByRole('button', { name: /^unarchive$/i });
    if (await confirm.count()) await this._clickVisible(confirm.first());  // confirm modal
    await this.page.waitForTimeout(3000);
  }

  async duplicateTemplate(templateName) {
    this._log(`duplicate template "${templateName}"`);
    const prefix = `Copy of ${templateName}`;
    const before = (await this._apiCoursesByName(prefix)).map((c) => c.id);
    await this._unarchiveIfArchived(templateName);
    await this.page.goto(`${this.base}/manage/courses`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    await this.page.getByRole('button', { name: `Actions for ${templateName}` }).first().click();
    await this.page.waitForTimeout(900);
    await this._clickVisible(this.page.getByText('Duplicate', { exact: true }));
    // duplication is async; poll the API for the new copy
    for (let t = 0; t < 25; t++) {
      await this.page.waitForTimeout(3000);
      const fresh = (await this._apiCoursesByName(prefix)).filter((c) => !before.includes(c.id));
      if (fresh.length) { this.courseId = String(fresh[0].id); this._log(`→ copy #${this.courseId}`); return this.courseId; }
    }
    throw new Error('duplicate did not appear within 75s (was the confirm dialog accepted?)');
  }

  /** Enable Completion certificates and select a certificate by name (Settings tab). */
  async setCertificate(certName) {
    if (!certName) return;
    this._log(`certificate: ${certName}`);
    await this.page.goto(`${this.base}/manage/courses/${this.courseId}/settings`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    await this.page.waitForTimeout(1200);
    try {
      const on = await this.page.evaluate(() => {
        const lab = [...document.querySelectorAll('label,div')].find((e) => /^completion certificates$/i.test((e.innerText || '').trim()));
        let p = lab; for (let i = 0; i < 3 && p; i++) { const c = p.querySelector('input[type=checkbox]'); if (c) return c.checked; p = p.parentElement; }
        return false;
      });
      if (!on) { await this.page.getByText('Completion certificates', { exact: true }).first().click(); await this.page.waitForTimeout(1500); }
      await this.page.getByText('Select a certificate', { exact: false }).first().click();
      await this.page.waitForTimeout(1000);
      await this._clickVisible(this.page.getByText(certName, { exact: true }));
      await this.page.waitForTimeout(800);
      await this._clickVisible(this.page.getByRole('button', { name: /save settings/i }));
      await this._settle();
    } catch (e) { process.stdout.write(`          ⚠ certificate skipped: ${e.message.split('\n')[0]}\n`); }
  }

  /** Rename lessons to clean titles (strip the NNa/NNb filename prefixes). `titles` is ordered to
   *  match the chapter's content_ids (video then its notes, per lesson). */
  async renameLessons(titles) {
    const ids = await this._apiContentIds();
    const n = Math.min(ids.length, titles.length);
    this._log(`rename ${n} lessons`);
    for (let i = 0; i < n; i++) {
      await this.page.goto(`${this.base}/manage/courses/${this.courseId}/contents/${ids[i]}`, { waitUntil: 'domcontentloaded' });
      await this._settle();
      await this.page.waitForTimeout(700);
      try {
        await this._fillVisible(this.qa('lesson-form-title-field'), titles[i]);
        await this._clickVisible(this.qa('actions-bar__save-button'));
        await this.page.waitForTimeout(700);
      } catch (e) { process.stdout.write(`          ⚠ rename #${i} skipped: ${e.message.split('\n')[0]}\n`); }
    }
  }

  /** Set a unique landing-page URL slug (Landing page tab → Edit URL). */
  async setSlug(slug) {
    if (!slug) return;
    this._log(`landing-page slug: ${slug}`);
    await this.page.goto(`${this.base}/manage/courses/${this.courseId}/landing_page`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    await this.page.waitForTimeout(2000);
    try {
      await this._clickVisible(this.page.getByText('Edit URL', { exact: false }));
      await this.page.waitForTimeout(1000);
      await this._fillVisible(this.qa('landing-page-url-input'), slug);
      await this._clickVisible(this.page.getByRole('button', { name: /^save$/i }));
      await this._settle();
    } catch (e) { process.stdout.write(`          ⚠ slug skipped: ${e.message.split('\n')[0]}\n`); }
  }

  async _gotoHubSettings() {
    await this.page.goto(`${this.base}/manage/courses/${this.courseId}/hub`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    await this._clickVisible(this.page.locator('[data-qa="course-hub-settings-tab-button"]'));
    await this._settle();
  }

  /** Settings tab: course name, description, and card image. */
  async setDetails({ name, description, cardPath }) {
    this._log('settings: name + description + thumbnail');
    await this._gotoHubSettings();
    
    if (name) {
      // Basic settings (active by default)
      await this._fillVisible(this.qa('course-name__input'), name);
      await this._clickVisible(this.page.getByRole('button', { name: /save settings/i }));
      await this._settle();
    }
    
    if (description || cardPath) {
      // Click Image and description sub-tab link
      await this._clickVisible(this.page.locator('a').getByText('Image and description', { exact: true }));
      await this.page.waitForTimeout(1000);
      
      if (description) {
        await this._fillVisible(this.qa('image-and-description-textarea'), description);
      }
      if (cardPath) {
        await this._doThumbnailUpload(cardPath);
      }
      
      await this._clickVisible(this.page.getByRole('button', { name: /save settings/i }));
      await this._settle();
    }
  }

  /** Upload ONLY the course card image (Settings tab) + Save. For updating cards on existing courses. */
  async uploadThumbnail(cardPath) {
    this._log('settings: course card image');
    await this._gotoHubSettings();
    // Click Image and description sub-tab link
    await this._clickVisible(this.page.locator('a').getByText('Image and description', { exact: true }));
    await this.page.waitForTimeout(1000);
    const ok = await this._doThumbnailUpload(cardPath);
    await this._clickVisible(this.page.getByRole('button', { name: /save settings/i }));
    await this._settle();
    return ok;
  }

  /** Open the Course-image Filestack picker, feed the file via the OS dialog, and commit the crop.
   *  Assumes we're already on the Settings tab. Returns true on success. */
  async _doThumbnailUpload(cardPath) {
    try {
      this._log('upload course card image');
      // The Filestack image modal opens INTERMITTENTLY on the (visible) Course-image "Upload"
      // click, so retry until its drop area (.fsp-drop-area-container) appears.
      let picker = null;
      for (let attempt = 0; attempt < 4 && !picker; attempt++) {
        await this._clickVisible(this.page.getByRole('button', { name: /^upload$/i }));
        picker = await this._findInFrames((f) => f.locator('.fsp-drop-area-container'), { timeout: 8000 });
        if (!picker) { await this.page.keyboard.press('Escape').catch(() => {}); await this.page.waitForTimeout(1000); }
      }
      if (!picker) throw new Error('Filestack image modal did not open after retries');
      // Filestack's hidden input rejects setInputFiles, but clicking the drop area opens the OS
      // file dialog → caught by Playwright's filechooser. (Per Harshit's tip.)
      const [chooser] = await Promise.all([
        this.page.waitForEvent('filechooser', { timeout: 15000 }),
        picker.click(),
      ]);
      await chooser.setFiles(cardPath);
      await this.page.waitForTimeout(3500);                       // crop/preview renders
      // Commit: the crop view's "Upload" is span.fsp-button--primary (visibility flaky → force-click).
      let committed = false;
      const dl = Date.now() + 30000;
      while (Date.now() < dl && !committed) {
        for (const f of this.page.frames()) {
          const b = f.locator('.fsp-button--primary');
          if (await b.count().catch(() => 0)) { await b.first().click({ force: true }).catch(() => {}); committed = true; break; }
        }
        if (!committed) await this.page.waitForTimeout(500);
      }
      if (!committed) throw new Error('crop "Upload" (.fsp-button--primary) not found in any frame');
      await this.page.waitForTimeout(6000);                       // image uploads + modal closes
      return true;
    } catch (e) {
      process.stdout.write(`          ⚠ thumbnail skipped: ${e.message.split('\n')[0]}\n`);
      await this.page.keyboard.press('Escape').catch(() => {});   // close any modal so Save isn't blocked
      return false;
    }
  }

  /** Bulk-upload all files into one named chapter via "Upload content". */
  async uploadLessons(chapterTitle, files) {
    this._log(`curriculum: bulk-upload ${files.length} files into "${chapterTitle}"`);
    await this.page.goto(`${this.base}/manage/courses/${this.courseId}`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    await this.page.waitForTimeout(1500);                       // let the React curriculum paint
    // A course needs a chapter before you can upload. Only create one if the course is empty
    // (re-running on a course that already has the chapter must not duplicate it). "Add chapter"
    // opens a form ("Enter a chapter title" + Save); afterward the panel stays on the chapter, so
    // reload the curriculum LIST to reach the "Upload content" toolbar.
    const needChapter = (await this._apiChapterIds().catch(() => [])).length === 0;
    if (needChapter) {
      this._log('create chapter');
      await this._clickVisible(this.qa('add-chapter__btn'));
      await this.page.waitForTimeout(800);
      await this._fillVisible(this.page.getByPlaceholder('Enter a chapter title'), chapterTitle);
      await this._clickVisible(this.page.getByRole('button', { name: /^save$/i }));
      await this._settle();
      await this.page.waitForTimeout(1500);
      await this.page.goto(`${this.base}/manage/courses/${this.courseId}`, { waitUntil: 'domcontentloaded' });
      await this._settle();
      await this.page.waitForTimeout(1500);
    }
    // Open the uploader. The bottom "Upload content" may go to a bulk view first; if no file input
    // appears, click the (per-chapter) "Upload content" again to open the Uppy modal.
    this._log('open Upload content');
    await this.page.getByText('Upload content', { exact: true }).first().waitFor({ state: 'visible', timeout: 15000 });
    await this._clickVisible(this.page.getByText('Upload content', { exact: true }));
    await this.page.waitForTimeout(1500);
    if (!(await this.page.locator('input[type="file"]').count())) {
      this._log('open chapter uploader');
      await this._clickVisible(this.page.getByText('Upload content', { exact: true }).nth(1));
      await this.page.waitForTimeout(1500);
    }
    this._log(`selecting ${files.length} files`);
    await this._uploadViaModal(files);
  }

  async setPriceFree() {
    this._log('pricing: Free');
    await this.page.goto(`${this.base}/manage/courses/${this.courseId}/pricing`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    try {
      // The "Free" option is an opacity:0 radio behind a styled label — force-check it directly.
      await this.qa('free-pricing__btn').first().check({ force: true });
      await this._clickVisible(this.qa('save-block-action-button'));
      await this._settle();
    } catch (e) { process.stdout.write(`          ⚠ pricing skipped: ${e.message.split('\n')[0]}\n`); }
  }

  async publishCourse() {
    this._log('publish');
    await this.page.goto(`${this.base}/manage/courses/${this.courseId}`, { waitUntil: 'domcontentloaded' });
    await this._settle();
    try {
      // Course editor top bar: "Action Menu" → "Publish now" (a draft course) → confirm "Publish"
      // modal. (The old `publish-action-menu` data-qa hook was dropped by Thinkific; verified the
      // role-based path 2026-06-30.)
      await this._clickVisible(this.page.getByRole('button', { name: /Action Menu/i }).first());
      await this.page.waitForTimeout(800);
      await this._clickVisible(this.page.getByRole('menuitem', { name: /publish now|set live|present/i }));
      await this.page.waitForTimeout(1200);
      const confirm = this.page.getByRole('button', { name: /^publish$/i });
      if (await confirm.count()) await this._clickVisible(confirm.first());  // confirm modal
      await this._settle();
    } catch (e) { process.stdout.write(`          ⚠ publish skipped (publish by hand): ${e.message.split('\n')[0]}\n`); }
  }

  // ---- helpers -------------------------------------------------------------
  async _settle() { await this.page.waitForLoadState('networkidle', { timeout: UI }).catch(() => {}); }

  /** After a trigger opens Thinkific's Uppy "Select Files to Upload" modal: feed its hidden
   *  file input, wait for the upload, confirm/insert, and let the modal close. */
  /** Find the first visible element matching textRe across ALL frames (the Uppy modal is in an
   *  import iframe, and its controls aren't <button>s reachable from the main frame). */
  async _findInFrames(make, { timeout = UI } = {}) {
    const deadline = Date.now() + timeout;
    while (Date.now() < deadline) {
      for (const f of this.page.frames()) {
        const loc = typeof make === 'function' ? make(f) : f.getByText(make);
        const n = await loc.count().catch(() => 0);
        for (let i = 0; i < n; i++) {
          const el = loc.nth(i);
          if (await el.isVisible().catch(() => false)) return el;
        }
      }
      await this.page.waitForTimeout(300);
    }
    return null;
  }

  async _uploadViaModal(files) {
    const baseline = await this._apiContentCount().catch(() => 0);   // existing lessons (append-safe)
    const input = this.page.locator('input[type="file"]').last();
    await input.waitFor({ state: 'attached', timeout: UI });
    await input.setInputFiles(files);
    await this.page.waitForTimeout(2000);                       // let the file queue render
    // Files are only QUEUED — commit with Filestack's "Upload N" button (.fsp-button-upload) inside
    // the /import iframe. With GBs of video it can take a while to appear, so wait generously.
    this._log('click "Upload N" to start the transfer');
    const commit = await this._findInFrames((f) => f.locator('.fsp-button-upload'), { timeout: 120000 });
    if (!commit) throw new Error('could not find the Filestack "Upload N" button (.fsp-button-upload) in any frame');
    await commit.scrollIntoViewIfNeeded().catch(() => {});
    await commit.click();
    // The button hides INSTANTLY on click — useless as a completion signal. The real signal is
    // lessons appearing via the API. Poll until baseline+files.length exist, keeping the browser
    // OPEN (closing it mid-upload aborts the transfer).
    const target = baseline + files.length;
    this._log(`uploading ${files.length} files… polling API → ${target} (videos take minutes)`);
    // No stall guard: Thinkific commits the whole batch at once when all files finish, so the count
    // stays at baseline (often 0) for the entire transfer then jumps to target. Rely on the 60-min cap.
    const deadline = Date.now() + UPLOAD_TIMEOUT;
    let n = baseline;
    while (Date.now() < deadline) {
      await this.page.waitForTimeout(8000);
      n = await this._apiContentCount().catch(() => n);
      this._log(`  ${n}/${target} lessons live`);
      if (n >= target) return;
    }
    throw new Error(`upload incomplete: ${n}/${target} lessons after ${Math.round(UPLOAD_TIMEOUT / 60000)} min`);
  }

  /** Wait until the bulk uploader has created all lessons (count appears) and progress clears. */
  async _waitForUploadComplete(expected) {
    this._log(`waiting for ${expected} uploads to register…`);
    const busy = this.page.getByText(/uploading|processing|%/i).first();
    try { await busy.waitFor({ state: 'visible', timeout: 30000 }); } catch { /* small/fast */ }
    await busy.waitFor({ state: 'hidden', timeout: UPLOAD_TIMEOUT }).catch(() => {});
    await this.page.waitForTimeout(3000);
  }
}
