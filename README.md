# MVP Math Supplements

A static website of explicit, step-by-step companion lessons for **Secondary Math I, II, and III** students using the Mathematics Vision Project (MVP) curriculum, organized by course, module, and section. Published with GitHub Pages; the home page is `index.html`.

All links are **relative**, so the site works both at `username.github.io/mvp-math-supplements/` and under a custom domain.

## Project layout

- `index.html` — website home page
- `math-1/index.html`, `math-2/index.html`, `math-3/index.html` — course indexes
- `math-2/module-02/index.html` — module index
- `math-2/module-02/section-2-1.html` — Section 2.1 lesson
- `assets/site.css` — shared styling for the navigation pages (lessons carry their own embedded styles)
- `math_supplement_master_instructions_v4.md` — instructions used to author each lesson (in the repo, not linked from the site)
- `.nojekyll` — tells GitHub Pages to serve files as-is
- `authoring/` — local-only working files (reference lesson, header template); excluded from the repo by `.gitignore`

## Naming conventions

Use zero-padded two-digit **module directories** (`module-01`, `module-02`, etc.) and lowercase, hyphenated **section files** (`section-2-1.html`, `section-1-10.html`, `section-2-8h.html` for honors). Section numbers are written exactly as printed in the packet (no zero-padding); the module `index.html` controls display order. Don't put lesson titles in file names, since titles change and links would break. Match the module numbering printed in the actual packet. Don't add modules or links until actual lessons are ready.

Put the descriptive name in the page `<title>`, which is what appears in browser tabs, bookmarks, search results, and printouts. Format: `Math II 2.1 — Transformers: Shifty y’s | MVP Supplement`.

## Adding a new lesson

1. Save its HTML into the correct module directory with its standard filename.
2. Apply the standard header from `authoring/lesson-template.txt`: title, breadcrumbs (Home → Secondary Math [course] → Module [number] → Section [number]), and the MVP disclaimer subheader.
3. Add a tile for it on the module's `index.html`, and update the "available" counts on the course index and home page.
4. If the module is new, create its `index.html` (copy an existing module index) and add it to the course index and the home page's "Available now" list.
5. Publish:

   ```sh
   git add -A
   git commit -m "Add Math II section 3.3"
   git push
   ```

6. After a minute or two, check the lesson on the live site: links work, equations are typeset, graphs display.

## Attribution and independence

This site is independently created to support students using MVP. It is **not an official publication** of or endorsed by the Mathematics Vision Project. Review licensing/attribution before incorporating textbook passages or images into published lessons.

Lessons typeset equations with MathJax from a CDN, so an internet connection is needed for formulas to display.
