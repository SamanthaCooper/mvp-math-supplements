# Instructions for Creating Supplemental Mathematics Instructional Materials

## Purpose

Create a clear, mathematically accurate companion to the specified Mathematics Vision Project (MVP) section. Students use the supplement alongside their packet to understand the mathematics, follow worked examples, and check their own work.

**When a section introduces genuinely new, fundamental ideas, provide definitions, explanations, and enough worked examples to teach those ideas to a student who missed class. Do not rely on the packet’s discovery exercises to supply the explanation.** Teach procedures explicitly and explain their meaning and reasoning where this helps understanding.

Depth depends on instructional need. Review material may need only a brief reminder, a link to earlier instruction, and an answer key. A complete standalone lesson is a deliberate choice for material that warrants it, not a requirement for every section or homework component. Mathematical explanations should be understandable on their own, while packet graphs, tables, and exercises may be referenced without reproduction.

## 1. Scope and source analysis

Generate **one numbered packet section per request**, unless the user explicitly requests otherwise. Do not start another section or broaden the task to a module overview. Each section is independently reviewable; combining approved lessons later should preserve their instructional content.

Read the complete module for context and examine the assigned main task and every Ready, Set, Go exercise. Identify previously introduced ideas, genuinely new material, review, extensions, and concepts reserved for later sections. Use a brief internal scope record to guide drafting. Check earlier packets or supplements before assuming that students know a method or notation.

Consult the cumulative curriculum map (`mvp_math1-3_complete_curriculum_map.xlsx`, with its searchable presentation in `curriculum-map.html`) to locate earlier instruction, distinguish new material from review, and find useful prerequisite links. Use it as a guide; verify relevant content against the actual packets, since the map may be incomplete or mistaken. Link students to published supplements that actually explain the needed ideas, rather than assuming that a mapped topic has adequate instruction.

Preserve the packet’s progression across sections. Within the assigned section, arrange ideas logically: introduce accessible ingredients before combining them. Do not introduce later techniques simply because they make a problem easier. Normally omit previews of unfamiliar future topics.

For example, Math II 2.1 should develop the parent parabola and individual transformations before combining them in vertex form; it should not begin with completing the square or a comparison of all quadratic forms.

**Check the packet and teacher notes critically.** They may contain incorrect mathematics, inconsistent representations, or poor wording. Teacher notes help establish intent but do not override the mathematics. Compare statements, graphs, tables, rules, and expected answers independently.

**Inspect source mathematics visually.** PDF text extraction can lose parentheses, variables, fractions, exponents, and equality signs. Verify expressions, graph scales, and original prompts against the actual page before writing solutions. In Math I 3.6, extraction led to misreading “find p(t) = 128” as “find p(12)”; these ask different questions.

## 2. Lesson organization and instructional depth

Use one top-level group for the main task, titled **In class: [exact task label printed in the packet]**. Begin with a prominent note:

> This section explains some of the ideas you explored in class through the guided exercises. Use it alongside the “[exact task label]” portion of Section [number] in your MVP packet.

Use subsections within that group. Keep all Ready material in one Ready section, all Set material in one Set section, and all Go material in one Go section; use subsections where needed. Teach shared ideas once, then link back from homework. Keep homework-specific explanations and examples in the relevant homework component. Update headings, navigation, anchors, and coverage references together when reorganizing.

For genuinely new, fundamental material:

- Define unfamiliar terms near their first use; do not require a vocabulary list.
- Explain the concept and the purpose of its procedure.
- State the relevant rule and demonstrate it with suitable worked examples.
- Explain consequential distinctions or common mistakes.
- Include graphs or tables when they materially help understanding.

For familiar material, use the least explanation that usefully supports the exercises. Link to a specific earlier explanation when appropriate. Use neutral wording such as “For a refresher, see…” rather than “You have already learned…” Do not mention unfamiliar advanced methods simply to say they are unnecessary.

Reviewing every exercise does not require teaching or solving every exercise separately. Group repetitive exercises by skill. Do not add new practice problems automatically, including in Go. Add an original example only when it teaches something useful that existing explanations and exercises do not adequately support.

Keep worked solutions economical. Show the steps that clarify the method and enough arithmetic to follow it, without expanding routine calculations unnecessarily. Use ordinary student-friendly language and practical methods. For graphing a line, choose two easily computed points far enough apart for accurate drawing; use a point-and-slope construction when the task specifically calls for it.

The packet may mix review and extensions rather than follow one coherent instructional thread. Explain useful connections without pretending every homework component practices the same in-class technique. Record meaningful disconnects in `curriculum-coherence-notes.md`, identifying the section, packet pages and problem ranges, previously taught ideas, and the particular mismatch. Keep those observations provisional; they do not automatically become student-facing criticism or require redesigning a lesson.

## 3. Packet references, clarifications, and teacher notes

Under major instructional headings, include a concise **In your MVP packet** reference strip giving the section, Main task or Ready/Set/Go, printed page number, and relevant problem range. Add smaller strips under subsections only when useful. References must match the nearby content and use verified printed page numbers, not PDF viewer indices.

Use descriptive navigation labels, such as “Ready: line intersections (1–4).” References are neutral signposts, not explanations or warnings. Avoid repeated broad ranges or restating the reference strip in the following paragraph.

Keep ordinary instruction separate from packet-specific clarifications. Place a clarification near the affected work, label its exact packet location, and give a short explanation or clearer wording when needed. Do not introduce a mathematical concept primarily through criticism of the packet.

**Be thorough in internal checking and selective in student-facing qualifications.** Address an issue when it could plausibly change a student’s answer, teach a wrong idea or method, or materially obscure the task. Accept normal classroom simplifications and clearly intended interpretations. Do not add warnings about remote alternatives, technically nonunique patterns, or routine unstated modeling assumptions.

Preserve meaningful distinctions, including units, input versus output, endpoint inclusion, sequence indices, discrete inputs versus discontinuities, and whole-number outputs versus domain restrictions. Distinguish verified errors from inferred intentions. Apply the same scrutiny to existing supplements.

Use ordinary clarification boxes for wording repairs. Reserve **light-red callouts** for substantial mathematical or instructional problems: false claims, misleading conceptual conflations, contradictory conditions, or ambiguity that prevents a meaningful answer. Follow the Math I Module 2 Sections 2.1–2.2 `.mvp-correction` styles. Include the exact location, explain the issue calmly, and provide a practical way forward where possible. An intentionally open-ended problem does not warrant a warning. Do not manufacture a callout for consistency.

At the end, include a concise teacher/parent review of serious packet problems, with locations, why they matter, and suggested corrections. If there are none, say so briefly. Keep broader observations about curricular organization in the coherence notes rather than expanding this review into general complaints about discovery learning.

## 4. Exercises and answer keys

Provide checked answers for Ready, Set, and Go. Preserve packet numbering, subpart letters, notation, and statement form; do not turn true/false statements into questions. Review every exercise against the matching source page. If information is missing or ambiguous, state the limitation and any reasonable interpretation instead of manufacturing a unique answer. Distinguish taught skills, linked review, assumed prerequisites, and deliberate omissions in coverage notes.

For routine numerical questions, give concise results. Explain answers when reasoning is requested, including each true/false response. Do not reproduce whole tables or every calculation unless that presentation serves the explanation.

When using a packet exercise as a worked solution, **clearly label Original problem and Answers or Worked solution**. Keep matching letters in both. Reproduce the original prompt when students need it to follow the solution. Do not duplicate complete task descriptions or datasets merely to make the supplement standalone; include a full table when it materially supports the explanation. Label invented examples and sample answers when confusion is possible.

Presentation conventions:

- Put compact checking keys in collapsed `details` elements with `class="answer-key"` and the established component IDs (`ready-answer-key`, `set-answer-key`, `go-answer-key`). Use descriptive summaries and `assets/answer-keys.css`.
- **Substantial worked solutions may remain visible in the main body.** Do not force them into disclosures when that makes formatting or reading awkward. Clearly associate them with their component and problem numbers.
- Briefly encourage students to study relevant worked examples, try the exercises independently, and then check the answers. Do not refer to worked examples when the component has none.
- Give each problem and subpart adequate space. Avoid crowded strings of answers, equations, and prose. Bare numerical answers do not need terminal periods; explanatory sentences do.
- If a required plot is omitted, give useful numerical results or sample points and explicitly say **Plot not shown**. Do not imply those results complete a graphing or construction task.
- For recursive rules, use a starting value and `f(n+1)` in terms of `f(n)`, with the appropriate index domain. Give recursive before explicit when both are requested.
- Verify units, scales, endpoint inclusion, domains, rounding, equivalent forms, and all real solutions. Use terminology introduced at this point in the course; explain unfamiliar terms if needed instead of assuming knowledge.

## 5. Graphs and diagrams

Use accurate, purposeful visualizations near their explanations. Prefer self-contained SVG or another reliable HTML-compatible format. Inspect the packet’s existing figures first; reproduce or add a figure only when it provides a concrete instructional benefit. A new worked example may need its own graph, while a review answer key may simply refer to the packet’s figure.

Label axes clearly and choose scales that show the relevant features. For ordinary coordinate graphs teaching slope, use equal physical lengths for equal x- and y-units and a square plotting region where practical. Contextual quantities may require different scales; make those scales clear. Keep comparisons controlled and use consistent colors or line styles. Label important points when relevant, and avoid unnecessary equation annotations on graphs. Typeset fractions properly; do not use slash notation or single-character fraction glyphs as substitutes for readable mathematical fractions.

**Construct geometry from mathematical constraints, not visual approximation.** Record the givens and claimed relationships, derive coordinates, and verify relevant lengths, angles, incidences, parallelism, perpendicularity, congruence, and circle intersections computationally. Use exact calculations where practical or an explicit appropriate tolerance. Generate markers and auxiliary lines from the same data. Preserve aspect ratio so circles remain circular and right angles remain right angles.

Maintain one mathematical specification for every substantive numerical example or figure. Rules, coordinates, tables, headings, labels, captions, and answers must all agree with it. This applies to function graphs as well as geometry. Simplify visuals without sacrificing mathematical accuracy or introducing later concepts. Label genuinely schematic elements appropriately; never use a disclaimer to conceal an inaccurate claimed relationship.

Render and inspect every new diagram for readability, clipping, label overlap, endpoint markers, and agreement with the surrounding explanation. Check the final embedded figure, not just an intermediate drawing. Section 8 governs final validation.

## 6. HTML format, navigation, and publication

Produce a complete HTML lesson in the established site style, with readable typography, generous spacing, clear heading hierarchy, distinguished worked examples and clarification boxes, and print-friendly CSS. Use the approved reference lesson when provided; do not redesign unnecessarily. Keep student instruction, packet references, clarifications, and teacher commentary visibly distinct.

The standard header identifies the course, module number/title, section number, and original lesson title. Use the subtitle:

> Supplement for Mathematics Vision Project (MVP) curriculum · Secondary Math [course], Module [number], Section [number]

Include the established independence statement and breadcrumbs back to module, course, and home. Place a prominent publisher-packet link beneath the header, linking to the matching student-edition module PDF, with a smaller official course-materials link. Never upload the local `MVP 1/`, `MVP 2/`, or `MVP 3/` source PDFs.

Begin useful mathematical content promptly after the header and navigation. Avoid boilerplate about colors, document organization, or how to read a textbook. Keep the requested in-class note and exercise-checking guidance concise.

### Mathematical typesetting

**Mathematical typesetting must be validated, not merely included in the HTML source.** A document containing LaTeX commands does not necessarily display formatted mathematics. Visually verify it in a real browser whenever browser-rendering tools are available; otherwise follow the automated-validation fallback in Section 8 and disclose the limitation.

- Choose one mathematics renderer (MathJax or KaTeX), configure it correctly, and use its supported delimiters consistently throughout the document.
- For MathJax with LaTeX `\(...\)` and `\[...\]` delimiters, the *JavaScript source* must double-escape the backslashes. For example:

  ```html
  <script>
  window.MathJax = {
    tex: {
      inlineMath: [['\\(', '\\)']],
      displayMath: [['\\[', '\\]']]
    }
  };
  </script>
  <script defer src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-chtml.js"></script>
  ```

  The doubled backslashes shown above are part of the actual JavaScript source, not an optional formatting convention. **Never use** `['\(', '\)']` in a JavaScript string: JavaScript silently removes those backslashes.
- **Escape HTML special characters in all mathematical content before inserting LaTeX into HTML**, including inside tables. In particular, write `<` as `&lt;` and `>` as `&gt;` in HTML text; escape `&` as `&amp;` when it is literal text. For example:

  ```html
  <td>\(0&lt;a&lt;1\)</td>
  ```

  Do **not** generate `<td>\(0<a<1\)</td>`: its comparison signs can be parsed as HTML tags, corrupting the table. Take care not to double-escape existing HTML entities or damage legitimate LaTeX commands.
- When generating HTML from Python, JavaScript, or templates, account for **every escaping layer** (programming-language string → generated HTML → browser HTML parser → math renderer). Prefer raw strings or an escaping-safe template, and inspect the actual output file rather than assuming that the source-code literals survived unchanged.
- Escape all user-facing text and attribute values for HTML; do not concatenate unescaped mathematical expressions into HTML markup.
- Do not treat graph labels as a substitute for typeset mathematical expressions: equations in tables, callouts, captions, and worked solutions all must render correctly.

### Review status and project maintenance

New drafts awaiting cursory review use `section-M-S-pending-cursory-review.html` and the corresponding pending banner. After cursory review, use the regular lesson filename and retain a banner that thorough human review is pending. Preserve existing review status during unrelated edits; automated checks do not constitute human review.

When the user explicitly completes human review, replace the pending banner with the standard light-green `human-review-complete` note immediately after the header metadata, before the publisher box. Include the user-approved date using a machine-readable `time` element. Follow Math I 3.1’s established placement and shared styling.

Run `python3 tools/update_review_badges.py` after changing review status or published index links. It refreshes lesson review badges and module/course aggregate counts from the published lessons and supplementary resources; cursory review does not count as completed human review.

Follow the README’s ingestion and naming conventions. Publish only approved lessons on module indexes. Refresh the module/course availability text and the affected home-page course button whenever lessons or supplementary resources are added or removed. Run `python3 tools/update_publisher_links.py` after updating indexes. Refresh the curriculum map with `python3 tools/build_curriculum_map.py` when the workbook or published lesson links change.

Edit this instructions file in place. Git preserves history; do not create version-suffixed instruction copies. Publication, committing, and pushing follow the user’s authorization. Preserve unrelated work and exclude local-only files.

## 7. Additional learning resources

Research resources during source analysis and choose specific, age-appropriate explanations or practice that closely match the mathematics and methods of the current section. **Prefer Khan Academy when it offers a good match, and put the best matches first.** Written material from Paul’s, OpenStax, or another reputable source may be useful when suitably scoped. There is no required search for Professor Leonard or any fixed provider quota; omit advanced or significantly broader material that would distract students.

Link to the specific lesson, video, article, or practice set, not a homepage. Verify the title, destination, relevant content, and prerequisite level. Briefly explain what each link supports and any small scope difference. Do not claim an exact method match unless verified; do not invent timestamps or content boundaries. Use a compact table or similarly readable format, consistent with the site.

A few useful links are enough. **If no resource fits well, leave the resources section empty or omit recommendations.** Do not fill it with weak matches simply to provide reading, video, and practice categories.

## 8. Quality control and delivery

Validate the exact final HTML before delivery. Keep a concise internal report of substantive mathematical checks and visual observations, using PASS, FAIL, or NOT CHECKED with actual evidence. Do not claim a check passed merely because the same data generated both the figure and its expected results.

1. **Mathematics and source alignment:** independently check worked solutions and answers, including any consequential interpretations. Compare every numerical figure/example with its source or specification and with the actual final-file rules, tables, headings, labels, and captions. Fix inconsistencies and rerun affected checks. Verify computational geometry constraints from Section 5.
2. **Instructional fit:** confirm that new foundational concepts are defined and explained, review has appropriate depth, needed earlier explanations are linked, and no later methods are assumed. Confirm worthwhile main-task and homework skills are supported. Do not force coherence where the packet mixes topics; document substantive disconnects in the project notes.
3. **HTML and math syntax:** use a standards-aware parser or validator to check structure, table rows, unexpected tags, duplicate IDs, local links, and escaped comparison signs. Check math delimiters and emitted renderer configuration. Delimiter counts and successful parsing alone do not prove correct rendering.
4. **Browser rendering:** when browser tools are available, inspect the final lesson after typesetting completes. Check inline and display mathematics, fractions, inequalities, tables, callouts, and graphs. Open every collapsed answer key and also inspect visible solutions. Test representative beginning/middle/end content, desktop and narrow widths, navigation, dependencies, and print layout.
5. **Fallback:** if browser rendering is unavailable, perform HTML/math-syntax checks, independently validate mathematics, and render and inspect generated diagrams separately. Disclose that final browser rendering was not verified. Do not label an unperformed browser check PASS.

A failed mathematical constraint, contradictory representation, or known broken rendering blocks delivery as a completed/verified lesson. Correct the affected output and check it again. Do not loosen tolerances, suppress failures, or alter only prose to disguise incorrect mathematics. Report material validation limitations accurately.

Run `python3 tools/check_answer_keys.py` for published lessons as an additional structural check. The checker does not replace source verification or browser inspection. If a deliberate visible-solution layout is not supported by a checker, update or report the tooling limitation rather than changing an instructionally sound layout merely to satisfy it.

Include a concise end-of-lesson coverage table mapping Main task, Ready, Set, and Go problem groups to the relevant explanations, links, or answer keys. Identify ambiguous exercises and deliberate omissions honestly. Keep it a coverage record, not lengthy commentary.

Deliver the requested HTML with a brief explanation of its review status and material validation limitations. The lesson should contain the needed instruction, appropriately scoped examples, checked exercises, useful packet clarifications, and selected resources where suitable. Additional Go practice and full standalone teaching are included only when warranted or requested.

## Materials for a request

- Full module packet for context.
- One section number to cover.
- Course/grade if not clear from the packet.
- Approved reference supplement, if available.

If these are already clear from project context, proceed without unnecessary clarification.
