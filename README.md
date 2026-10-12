# MVP Math Supplements

A static website of explicit, step-by-step companion lessons for **Secondary Math I, II, and III** students using the Mathematics Vision Project (MVP) curriculum, organized by course, module, and section. Published with GitHub Pages; the home page is `index.html`.

Internal links are **relative**, so the site works both at `username.github.io/mvp-math-supplements/` and under a custom domain.

## Project layout

- `index.html` — website home page
- `math-1/index.html`, `math-2/index.html`, `math-3/index.html` — course indexes
- `math-2/module-02/index.html` — module index
- `math-2/module-02/section-2-1.html` — Section 2.1 lesson
- `assets/site.css` — shared styling for the navigation pages (lessons carry their own embedded styles)
- `math_supplement_master_instructions.md` — the authoritative instructions used to author each lesson (in the repo, not linked from the site). Edit this file in place; Git preserves its history, so do not create version-suffixed copies.
- `.nojekyll` — tells GitHub Pages to serve files as-is
- `authoring/` — local-only working files (reference lesson, header template); excluded from the repo by `.gitignore`

The `MVP 1/`, `MVP 2/`, and `MVP 3/` folders hold local source PDFs and are excluded from Git.

## Naming conventions

Use zero-padded two-digit **module directories** (`module-01`, `module-02`, etc.) and lowercase, hyphenated **section files** (`section-2-1.html`, `section-1-10.html`, `section-2-8h.html` for honors). Section numbers are written exactly as printed in the packet (no zero-padding); the module `index.html` controls display order. Don't put lesson titles in file names, since titles change and links would break. Match the module numbering printed in the actual packet. Don't add modules or links until actual lessons are ready.

Put the descriptive name in the page `<title>`, which is what appears in browser tabs, bookmarks, search results, and printouts. Format: `Math II 2.1 — Transformers: Shifty y’s | MVP Supplement`.

Supplementary resources that cover several sections use descriptive, lowercase, hyphenated filenames without version suffixes (for example, `discrete-continuous-clarification.html`). List them separately under **Supplementary resources** on the module index, link them from the relevant lessons, and provide a link back to those lessons. Do not count them as numbered lessons.

## Adding a new lesson

1. Save its HTML into the correct module directory (any filename containing `Section_M_S`, e.g. `Section_4_3_Whatever.html`).
2. Run `python3 authoring/standardize_lessons.py` from the project root. It renames the file to `section-M-S.html` and applies the standard title, breadcrumbs (Home → Secondary Math [course] → Module [number] → Section [number]), and MVP disclaimer subheader. To do this by hand instead, use `authoring/lesson-template.txt`.
3. Add a tile for it on the module's `index.html`, and update that module's "Sections … available" count on the course index.
4. If the module is new, create its `index.html` (copy an existing module index) and add a tile for it on the course index.
5. **Every ingestion must refresh the affected course button on the main `index.html`,** including its smaller availability text. Describe the published sections or lesson count and module range accurately, and mention supplementary resources where useful. Count only lessons linked from module indexes, not untracked files or supplementary resources. Avoid wording that implies a whole module is complete when only some sections are published. This applies to additions, removals, and supplementary-resource updates, even when no new module is created.
6. Publish:

   ```sh
   git add -A
   git commit -m "Add Math II section 3.3"
   git push
   ```

7. After a minute or two, check the lesson on the live site: links work, equations are typeset, graphs display.

## Attribution and independence

This site is independently created to support students using MVP. It is **not an official publication** of or endorsed by the Mathematics Vision Project. Review licensing/attribution before incorporating textbook passages or images into published lessons.

Lessons typeset equations with MathJax from a CDN, so an internet connection is needed for formulas to display.

## Lesson organization

Group main-task instruction under **In class: [the packet’s exact task label]**, with a prominent note explaining that it revisits the guided class exercises in a more formal, step-by-step way. Keep Ready, Set, and Go separate. Link homework back to shared explanations instead of repeating them; keep homework-specific examples in its own section. Check the corresponding MVP packet and update navigation and coverage references whenever ingesting or reorganizing a lesson.

## Homework answer keys

Ready, Set, and Go answer keys are collapsed beneath their respective worked examples. Students should study the examples and try exercises independently before checking answers. Preserve packet numbering and statement wording; show numerical results where useful and state when required plots are not shown. Check every answer against the matching source packet and verify final math rendering. Follow the detailed conventions in `math_supplement_master_instructions.md`. Run `python3 tools/check_answer_keys.py` to check all published lessons for missing or malformed keys, broken answer links, and math-renderer setup; also expand the keys in a browser to verify actual rendering.

## Human review status

Lessons and supplementary resources awaiting thorough human review display a pale amber **Human review pending** banner beneath the lesson header. It remains visible in print. After reviewing a section for mathematical accuracy, clarity, and alignment with its MVP packet, remove that lesson’s `<aside class="review-pending" ...>...</aside>` block. Keep the banner on every other pending lesson. Include the same banner when adding new lessons or supplementary resources; its shared styles are in `assets/packet-navigation.css`.

## Publisher materials links

Every published lesson and supplementary resource has a prominent link beneath its header to its module’s original student PDF on the MVP website. Module pages repeat this link; course and home pages link to the official course materials. During every ingestion, run `python3 tools/update_publisher_links.py` after updating the indexes and before committing. This updates only resources listed in module indexes, leaving unpublished drafts alone. For a new module, verify its student-edition PDF URL and add it to `PACKETS` in that script first; use the edition that matches the supplement. Never upload local MVP PDFs.
