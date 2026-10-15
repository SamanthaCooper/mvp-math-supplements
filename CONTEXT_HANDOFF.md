# Handoff for a fresh chat

Snapshot: October 13, 2026. This is temporary project progress, not permanent authoring guidance. Recheck the working tree and lesson banners before acting; another chat also works in this repository.

## Read first

- `math_supplement_master_instructions.md`: current authoring preferences and validation requirements.
- `README.md`: ingestion, naming, and project workflows.
- `curriculum-analysis/README.md`: source coverage, counting, and curriculum comparison rules.
- `curriculum-coherence-notes.md`: provisional observations about disjointed packet components.

Use the honors packets selected in `tools/mvp_packets.json`. The local `MVP 1/`, `MVP 2/`, and `MVP 3/` folders must remain excluded from GitHub.

## Math I Module 5: ready for the user's cursory review

These three local drafts are complete and remain unpublished:

- `math-1/module-05/section-5-1-pending-cursory-review.html` — Pet Sitters: constraints, checked plans, and the $320 maximum daily income under the stated budget.
- `math-1/module-05/section-5-2-pending-cursory-review.html` — Too Big, or Not Too Big, That Is the Question: inequality boundaries, shading, and budget/space constraints.
- `math-1/module-05/section-5-3-pending-cursory-review.html` — Some of One, None of the Other: equivalent equation forms and graphing by intercepts.

Each has an attempt-first in-class banner, Ready/Set/Go checking keys, publisher links, packet references, and pending-review status. Numerical answers or sample points are provided where required plots are omitted, with the omission stated explicitly. Graphs use square plotting regions and equal physical units on the axes.

Source: `MVP 1/m1_mod5_seh_52016f.pdf`, PDF pages 4–16 (printed pages 1–13). The corresponding teacher purposes/notes were consulted. All twelve Main/Ready/Set/Go coverage records were updated in `curriculum-analysis/packet-coverage.json`.

Important verified source error: **5.3 Ready 4(c)** prints `(-3,2)`, which satisfies neither `y=2x+4` nor `x+y=-5`, contrary to the exercise's introductory claim. The supplement preserves the printed point, gives “neither,” and flags the contradiction. The suggested replacement `(-7,2)` is explicitly a possible repair, not claimed publisher intent.

Independent calculations, final SVG coordinates, HTML structure, local links, and MathJax configuration were checked. Desktop and 380px browser layouts were inspected with every checking key open. Print layout remains **NOT CHECKED**. Local reports: `authoring/math1-5-1-review.json`, `authoring/math1-5-2-review.json`, and `authoring/math1-5-3-review.json`; `authoring/` is local-only.

`math-1/module-05/index.html` exists for local breadcrumbs but has no draft lesson links. The three drafts have not been approved for publication or committed/pushed in this chat. Do not infer review approval from automated validation.

## Other work visible in the shared workspace

Math I Module 4 sections 4.1–4.9 now have regular published filenames. Sections 4.6, 4.7H, 4.8H, and 4.9H carry human-review completion dated October 13, 2026. Latest commit at this snapshot: `8703658` (“Publish Math I 4.9 as human reviewed”); local `main` and `origin/main` show no ahead/behind difference.

There are still uncommitted changes, including Math I 4.5 and 4.9, instructions, analysis work, and notes. Module 6 drafts and unrelated Math II files are also present; they were not evaluated as part of this handoff. Preserve them and inspect their provenance before including them in any commit. Do not stage the entire working tree by default.

The latest request authorized instruction cleanup and this handoff note. It did not request a commit or push. Resume with the user's chosen section or review task rather than automatically generating more lessons.
