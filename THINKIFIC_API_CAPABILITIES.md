# ⚙️ Thinkific API Capabilities & Automation Reference Manual

> [!NOTE]
> Comprehensive technical documentation of the official **Thinkific Admin REST API (v1)**, **GraphQL API**, **Asset Management endpoints**, and **Playwright automation standards** for Lyzr University.

---

## 1. Overview & Base URLs

* **Base REST API URL:** `https://api.thinkific.com/api/v1` (or `https://api.thinkific.com/api/public/v1`)
* **GraphQL Endpoint:** `https://university.lyzr.ai/api/graphql` or `https://lyzr.thinkific.com/api/graphql`
* **Authentication Headers:**
  ```http
  X-Auth-API-Key: <YOUR_THINKIFIC_API_KEY>
  X-Auth-Subdomain: lyzr
  Content-Type: application/json
  ```

---

## 2. Official REST API v1 Modules & Endpoints

### 📹 A. Asset Management API (`/v1/assets`)
Used for managing videos, PDFs, and audio files in the site's **Asset Library**:
* `GET /v1/assets` — List all uploaded assets (returns `id`, `file_name`, `status`, `duration_in_seconds`, `url`).
* `GET /v1/assets/:id` — Retrieve detailed metadata for a single video asset.
* `POST /v1/assets` — Initiate direct 3-step S3 upload (returns `signed_url`).
* `POST /v1/assets/:id/confirm` — Confirm video upload and trigger Thinkific transcoding.

### 📚 B. Courses, Chapters & Content API
* `GET /v1/courses` — List all courses (draft/published status, price, slug, card image).
* `GET /v1/courses/:id` — Retrieve detailed metadata for a course.
* `GET /v1/chapters` — List chapters belonging to a specific course.
* `GET /v1/contents` — List lesson content items within chapters.
* `PUT /v1/contents/:id` — Attach `asset_id` to a lesson page.

### 👤 C. Users & Custom Profile Fields API
* `GET /v1/users` / `POST /v1/users` — Create, retrieve, and manage student, instructor, and admin accounts.
* `PUT /v1/users/:id` — Update user roles, profile attributes, and access permissions.
* `GET /v1/custom_fields` — Manage custom profile fields (e.g., Company, Job Title, Partner ID).

### 🎓 D. Enrollments & Certificates API
* `GET /v1/enrollments` / `POST /v1/enrollments` — Enroll users into courses or bundles, set access expiry dates.
* `PUT /v1/enrollments/:id` — Update enrollment status, unenroll, or mark course completed.
* `GET /v1/certificates` — Retrieve issued course completion certificates and verification links.

### 📦 E. Categories, Collections & Bundles API
* `GET /v1/categories` — Manage course categories and storefront collections.
* `POST /v1/category_memberships` — Assign or remove courses from specific storefront categories.
* `GET /v1/bundles` — Manage multi-course bundles and tiered package pricing.

### 💳 F. Orders, Commerce & Coupons API
* `GET /v1/orders` — Access transaction receipts, order IDs, and payment references.
* `GET /v1/coupons` / `POST /v1/coupons` — Create and manage promotional discount codes.
* `GET /v1/promotions` — Query active sales promotions.

### 🏢 G. Groups & B2B Cohorts API
* `GET /v1/groups` / `POST /v1/groups` — Manage enterprise client groups.
* `POST /v1/group_users` — Bulk assign users to specific company cohorts.
* `GET /v1/group_analysts` — Assign group reporting analysts for B2B dashboards.

### 👨‍🏫 H. Instructors API
* `GET /v1/instructors` — Manage instructor profile bios, titles, and avatars.

### 📜 I. Site Scripts API
* `GET /v1/site_scripts` / `POST /v1/site_scripts` — Inject custom JavaScript tracking scripts into site header/footer (e.g., GTM, Google Analytics).

### 🔔 J. Webhooks API
* `GET /v1/webhooks` / `POST /v1/webhooks` — Subscribe to real-time event webhooks:
  * `user.signup`
  * `enrollment.created` / `enrollment.completed`
  * `order.created`
  * `subscription.cancelled`

---

## 3. Thinkific GraphQL API (`/api/graphql`)

Thinkific's modern Creator Hub API supports single-query data fetching and dynamic mutations:

### Asset Search Query:
```graphql
query SearchAssetLibrary($query: String!) {
  assets(filter: { search: $query, type: VIDEO }, first: 10) {
    edges {
      node {
        id
        filename
        status
        duration
      }
    }
  }
}
```

### Lesson Update Mutation:
```graphql
mutation AttachVideoToLesson($lessonId: ID!, $assetId: ID!, $htmlContent: String!) {
  lessonUpdate(
    id: $lessonId
    input: {
      assetId: $assetId
      body: $htmlContent
    }
  ) {
    lesson {
      id
      title
      asset {
        id
        filename
      }
    }
  }
}
```

---

## 4. API vs. Browser Automation Comparison Matrix

| Capability | Thinkific REST API | Thinkific GraphQL | Browser Automation (Playwright) |
| :--- | :---: | :---: | :---: |
| **User & Enrollment Mgmt** | ✅ Full Support | ✅ Full Support | ⚡ Slower |
| **Order & Transaction Data** | ✅ Full Support | ✅ Full Support | ❌ Not Needed |
| **Asset Library Upload** | ✅ 3-Step S3 Upload | ✅ Mutation | ✅ Full UI Support |
| **Creating Chapters/Lessons** | ⚠️ Read-Only / Limited | ✅ Full Support | ✅ Full UI Support |
| **Attaching Videos to Lessons** | ✅ Via `PUT /v1/contents` | ✅ `lessonUpdate` | ✅ Full UI Support |
| **Rich HTML Lesson Formatting** | ⚠️ Text Only | ✅ Full Support | ✅ ProseMirror DOM Support |
