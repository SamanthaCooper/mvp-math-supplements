# MVP Math Supplements

A static website of companion lessons with explicit instruction where needed for **Secondary Math I, II, and III** students using the Mathematics Vision Project (MVP) curriculum, organized by course, module, and section. Published with GitHub Pages; the home page is `index.html`.

Internal links are **relative**, so the site works both at `username.github.io/mvp-math-supplements/` and under a custom domain.

## Project layout

- `index.html` — website home page
- `curriculum-map.html` — searchable Math I–III skill and lesson map, generated from `mvp_math1-3_complete_curriculum_map.xlsx`
- `curriculum-coherence-notes.md` — working observations about connections and gaps between in-class tasks and homework; a companion to the curriculum map, not linked from the website
- `math-1/index.html`, `math-2/index.html`, `math-3/index.html` — course indexes
- `math-2/module-02/index.html` — module index
- `math-2/module-02/section-2-1.html` — Section 2.1 lesson
- `assets/site.css` — shared styling for the navigation pages (lessons carry their own embedded styles)
- `math_supplement_master_instructions.md` — the authoritative instructions used to author each lesson (in the repo, not linked from the site). Edit this file in place; Git preserves its history, so do not create version-suffixed copies.
- `.nojekyll` — tells GitHub Pages to serve files as-is
- `authoring/` — local-only working files (reference lesson, header template); excluded from the repo by `.gitignore`

The `MVP 1/`, `MVP 2/`, and `MVP 3/` folders hold local source PDFs and are excluded from Git.

Use the **honors student editions** as the source packets. `tools/mvp_packets.json` records the publisher's honors selection for every module; some modules share the same PDF with the standard edition. `honors-packets.html` links directly to these publisher PDFs. Superseded standard packets are archived locally under ignored `authoring/standard-packets/`. After changing the packet manifest, run `python3 tools/update_publisher_links.py`; verify printed and PDF page references against the replacement edition before rebuilding reference indexes.

## Cumulative curriculum map

The public `curriculum-map.html` page is generated from the Excel workbook in the project root. After editing the workbook, run `python3 tools/build_curriculum_map.py` to refresh the page. The map links to lessons that are already listed on published module indexes; unpublished drafts remain unlinked.

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

Group main-task instruction under **In class: [the packet’s exact task label]**, with a prominent note explaining that it revisits the guided class exercises as a companion to the corresponding MVP task. Keep all content for each of Ready, Set, and Go in its own section, using subsections where useful. New foundational ideas need definitions, explanations, and worked examples sufficient for a student who missed class; review may need only a brief reminder, a link to earlier teaching, and checked answers. Additional Go problems are optional. Check the corresponding MVP packet and update navigation and coverage references whenever ingesting or reorganizing a lesson. Record substantive curricular disconnects in `curriculum-coherence-notes.md`.

## Homework answer keys

Compact Ready, Set, and Go checking keys are collapsed beneath the relevant instruction. Substantial worked solutions may stay visible in the main body. Encourage students to use relevant examples and try exercises independently before checking answers. Clearly distinguish original prompts from solutions, and preserve packet numbering, subpart letters, notation, and statement wording. State when required plots are not shown. Check every answer against the actual source page, including visual verification of expressions that PDF extraction may misread. Follow `math_supplement_master_instructions.md` and verify final math rendering. Run `python3 tools/check_answer_keys.py` as an additional structural check, and inspect both expanded keys and visible solutions in a browser. The checker may need updating for intentionally visible solution layouts.

## Human review status

Lessons and supplementary resources awaiting thorough human review display a pale amber **Human review pending** banner beneath the lesson header. It remains visible in print. After reviewing a section for mathematical accuracy, clarity, and alignment with its MVP packet, remove that lesson’s `<aside class="review-pending" ...>...</aside>` block. Keep the banner on every other pending lesson. Include the same banner when adding new lessons or supplementary resources; its shared styles are in `assets/packet-navigation.css`.

After human review is explicitly completed, use the standard dated `human-review-complete` note beneath the header metadata. Run `python3 tools/update_review_badges.py` whenever review status or published navigation changes. Lesson buttons show green **Human reviewed** or red **Human review pending** badges; module and course buttons summarize published lessons and supplementary resources with green for all reviewed, yellow for some, and red for none, plus reviewed/total counts. Unpublished drafts are excluded. Courses without published lessons say **No lessons published**. The badges are static HTML, so they work without JavaScript.

## Publisher materials links

Every published lesson and supplementary resource has a prominent link beneath its header to its module’s original student PDF on the MVP website. Module pages repeat this link; course and home pages link to the official course materials. During every ingestion, run `python3 tools/update_publisher_links.py` after updating the indexes and before committing. This updates only resources listed in module indexes, leaving unpublished drafts alone. For a new module, verify its student-edition PDF URL and add it to `PACKETS` in that script first; use the edition that matches the supplement. Never upload local MVP PDFs.

### Lesson revision dates

Lessons display small **Last updated** dates at the top and bottom, separate from human-review dates. After editing a lesson, run `python3 tools/update_lesson_dates.py math-1/module-03/section-3-1.html` with the affected paths. Without paths, the tool uses Git history for unchanged published lessons and established drafts, and today’s date for edited or new lessons. Dates use America/Los_Angeles.

## Published packet reference index

`packet-reference-index.html` is linked from the home page. Rebuild it with `python3 tools/build_packet_reference_index.py`; curated entries are in `tools/packet_reference_index.json`. The 27 active student PDFs are distributed unchanged as attachments to the `mvp-student-packets-2026-10` GitHub release, with attribution and licensing information. Local PDFs and archived editions remain excluded from Git. The index and general download links use the publisher’s exact student PDF editions; index links include page anchors. Release attachments remain backup downloads. The builder also refreshes previously opened local authoring index pages with the same publisher links.
