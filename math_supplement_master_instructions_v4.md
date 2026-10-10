# Instructions for Creating Supplemental Mathematics Instructional Materials

## Objective

I will provide a mathematics curriculum packet (typically from the Mathematics Vision Project, or MVP). Your task is to create **high-quality, explicit instructional materials** that teach all the mathematical content covered by the **one numbered section I specify for the current request**.

The goal is to produce a **standalone, student-friendly mathematics lesson**, similar to a well-written traditional textbook chapter.

The instruction should be systematic, mathematically rigorous, conceptually clear, and accessible to a student learning the material independently.

**Use the curriculum to determine both what students need to learn AND when they encounter it. Preserve the packet’s section-by-section progression, while replacing discovery-based teaching with clear explicit instruction within each section.**

In particular, do not replicate the curriculum's discovery-based teaching approach. Teach the mathematical ideas explicitly, using clear explanations, rules, formulas, worked examples, and appropriate visualizations.

---

## 0. NON-NEGOTIABLE: One curriculum section per request; a daily companion, not a module review guide

**Default workflow: Generate exactly ONE numbered packet section per request.** Even if the attached packet contains the full module, do not generate the remaining sections unless I explicitly override this requirement.

- **Read the complete module for context**, including the immediately preceding and following sections, to understand what has already been taught, what belongs to the assigned day, and what must wait.
- **Produce student-facing instruction for only the requested section**, including its main task and all three Ready, Set, Go components. Its relevant prerequisite reviews belong within that day's lesson.
- **Do not silently broaden the assignment** to multiple sections, create a module-wide overview, or introduce later methods simply because the full PDF is available.
- **Treat each section as independently reviewable and approvable.** After I approve a section, develop the next section separately. Later, approved lessons may be assembled into a combined HTML file **without rewriting or compressing their instructional content**.
- Prioritize clarity and adequate depth within the selected section over brevity. Do not treat the one-section scope as permission to skip distinct Ready, Set, Go skills.


**This material is meant for a student to use on the day each packet section is taught in class.** A student reading lesson 2.1 may not have attended lesson 2.2 yet. This constraint overrides any general advice elsewhere in this document about reorganizing ideas, broad coverage, or presenting a mathematically elegant overview.

- Keep the original section numbering and **the sequence of instructional topics across sections**. Create a distinct, complete lesson for the **single requested section**. If I explicitly request an exception involving multiple sections, preserve separate full daily lessons rather than producing a compressed overview.
- Teach **only the new ideas introduced by the current packet section**, together with the prerequisites needed for its own tasks and Ready, Set, Go. Do not introduce techniques reserved for later sections, even if those techniques would solve today's problems more quickly.
- **Within** a section, reorganize ideas into an effective explicit-instruction sequence: start from familiar facts, teach one new concept at a time, show examples and graphs, and then combine the concepts. You may reorganize *within* the section, but must not transfer later content into earlier lessons.
- **Do not front-load a master formula, a table comparing all methods, or a module-wide vocabulary glossary.** Introduce a general rule *after* developing the individual ingredients it describes, unless the current lesson explicitly assumes that general rule has already been taught.
- A later lesson may review an earlier skill briefly. An earlier lesson must not require knowledge taught only in a later one. If future ideas must be mentioned, label them as a short optional preview, not as required instruction or a prerequisite for today's homework; normally omit them.
- A useful final test: **Could a student who has completed only the earlier packet sections understand today's lesson and do today's assigned problems?** If not, revise the sequence.

**Concrete example from MVP Math II, Module 2:** Section 2.1 should begin with the parent parabola and its features, then teach vertical translations, horizontal translations, and vertical scaling/reflection separately, with graphs and worked examples. Only **after** those explanations should it synthesize them into `y = a(x-h)^2 + k`. Section 2.1 must not begin with the combined vertex form or introduce completing the square, factoring, or the three quadratic forms. Section 2.2 may build explicitly on 2.1 and develop use of vertex form.

## 1. Analyze the original curriculum thoroughly

For the **one section requested**, carefully examine:

- The main Develop Understanding, Solidify Understanding, or Practice Understanding Task.
- Every problem in the Ready, Set, Go homework.
- The mathematical skills and concepts required to complete those exercises.
- Any prerequisite knowledge or review material that students are expected to use.

Identify the principal learning objectives and all supporting mathematical skills.

**Do not assume that the main activity adequately identifies everything students are expected to learn.** The homework may introduce or assess additional mathematical concepts that are not explicitly addressed in the main task.

Make sure every mathematical topic addressed in Ready, Set, Go is covered somewhere in the supplemental instruction.

Distinguish between material that requires substantial new instruction and material that needs only a brief review.

## 2. Organize the instruction into a coherent mathematical sequence

**Preserve the original packet section order. Inside each individual section, teach its mathematics in a logical explicit-instruction sequence; never reorganize the module so that later concepts appear early.**

Introduce prerequisite concepts before more advanced ones. Group closely related ideas together and arrange the lesson so that each concept builds naturally on what students have already learned.

Each section should read as a self-contained, coherent *daily textbook lesson*. When approved single-section lessons are eventually combined, the resulting document should preserve their original pace, depth, and curriculum sequence rather than becoming a compressed review chapter.

For each major concept:

1. Introduce the concept and explain its mathematical meaning.
2. State the relevant rules, formulas, or procedures.
3. Explain why those rules work when doing so contributes meaningfully to understanding.
4. Demonstrate the procedures through carefully chosen, fully worked examples.
5. Explain important distinctions and common mistakes.
6. Progress from straightforward examples to more challenging applications.

Students should not have to discover fundamental mathematical rules through trial and error before those rules are explained.

At the same time, avoid presenting mathematics as a collection of formulas to memorize. Include conceptual explanations that make the procedures understandable.

**The lesson must make sense independently of the original packet.**

## 3. Use mathematical vocabulary selectively

Define mathematical terms that are new or likely to be unfamiliar to students at this level.

Introduce terminology naturally, immediately before or near its first use.

Do not unnecessarily redefine concepts students should already know, such as variables, equations, exponents, basic algebraic operations, or familiar geometric shapes.

Prefer a short vocabulary list **inside each daily section**, with terms introduced near first use. Do not include a front-of-module glossary that defines vocabulary from later lessons. A combined alphabetical glossary, if desired, belongs at the end and should not function as an opening overview of future topics.

Avoid exhaustive vocabulary lists that distract from the mathematical instruction.

## 4. Include accurate, purposeful graphs and visual explanations

Use mathematical visualizations wherever they materially improve understanding.

Appropriate examples include:

- Graphs of functions and transformations.
- Multiple related functions shown on the same coordinate plane.
- Geometric diagrams.
- Tables illustrating mathematical relationships.
- Labeled illustrations of important features.
- Visual demonstrations of algebraic identities.

For graphs of functions:

- Use accurate, computer-generated plots.
- Label axes clearly.
- Choose scales that make the relevant features visible.
- Use distinct, consistent colors or line styles when comparing functions.
- Clearly identify significant points, such as vertices or intercepts, when relevant.

Use SVG, JavaScript, or another reliable HTML-compatible technology. Prefer self-contained graphics that work without an internet connection.

Place graphs near the explanations they illustrate.

**Every visualization should serve an instructional purpose.** Avoid decorative or redundant graphics.

## 5. Separate packet-specific clarifications from the main lesson

**This is a particularly important requirement.**

The main instructional material should read as a coherent, standalone mathematics lesson.

Sometimes the original packet contains:

- Confusing or awkward language.
- Unusual representations.
- Unstated assumptions.
- Ambiguous instructions.
- Mathematical statements that require qualification.

When students need help interpreting a particular packet problem, include a separate, visually distinctive note.

Use a shaded box labeled with the relevant section and problem number, for example:

> **Packet clarification — Section 2.2, Problem 1**

Each clarification should:

1. Identify the exact section and problem.
2. Explain what the exercise is intended to ask.
3. Clarify any assumptions required.
4. Explain the relevant mathematical distinction, when necessary.
5. Provide clearer wording if that would help students.

Do not present these notes as numbered instructional topics, and do not let them interrupt the logical progression of the lesson.

Use them selectively.

### Distinguish clarification from correction

If the packet uses unfamiliar or awkward wording, clarify it.

If the packet omits a mathematically necessary assumption, contains an error, or makes an unjustified claim, identify the problem explicitly.

For example, suppose the packet provides a finite table of values and expects students to identify the vertex of a quadratic function, without stating that the data come from a quadratic.

A suitable note would say:

> **Packet clarification — Section 2.2, Ready, Set, Go, problems 26–29**
>
> These exercises are intended to use tables of values from quadratic functions, although the instructions do not explicitly say so.
>
> For these problems, assume the tables represent quadratic functions.
>
> In general, however, a finite table of values cannot establish that a function is quadratic. Even constant second differences do not prove that the function must be quadratic for every input.

Do not place a warning such as “first verify that the function is quadratic” in the main solution procedure when the information provided does not permit such verification.

The purpose is to help students understand the mathematics correctly, not to introduce unnecessary confusion.

## 6. Cover Ready, Set, Go comprehensively

Analyze all three homework components separately.

For each:

- Identify the mathematical skills being tested.
- Determine whether those skills are already covered in the main lesson.
- Add explicit instruction for any missing skills.
- Include examples sufficient to demonstrate the required procedures.

Ready may review prerequisite concepts.

Set may reinforce or extend the primary mathematical ideas.

Go may introduce additional review material or skills that are only loosely related to the main task.

**Do not omit material simply because it appears tangential to the main lesson.**

At the same time, use appropriate judgment about depth. Familiar prerequisite material may need only a brief refresher, while genuinely new concepts deserve fuller treatment.

The student should be equipped to complete the entire Ready, Set, Go assignment after studying the supplement.

It is not necessary to provide solutions to every exercise in the original packet.

## 7. Create additional, fully worked Go problems

For each section, create **at least two new problems** modeled on the mathematical skills tested in its Go homework.

Include:

**Problem A — Straightforward:** A relatively simple example that reinforces the fundamental procedure.

**Problem B — More challenging:** An example that requires additional reasoning, more complicated calculations, or a less obvious application of the same skill.

For every example:

- Present the complete problem.
- Show the solution step by step.
- Explain the reasoning behind important steps.
- Use correct mathematical notation.
- Point out common errors when relevant.

### When Go covers multiple skills

If the Go section tests several distinct mathematical skills, **add as many worked examples as necessary to cover them adequately**.

Do not artificially limit the instruction to two problems at the expense of completeness.

However, avoid unnecessary repetition. Each additional example should teach or reinforce something meaningful.

All problems should be original, not copies of exercises in the packet.

## 8. Include a concise teacher's review

At the end of the document, include a separate section intended for teachers or parents.

**Identify only serious problems with the original packet.**

These include:

### A. Seriously confusing wording

Questions whose intended meaning is difficult to determine, even for someone who understands the mathematics.

### B. Incomplete instructions

Exercises that require important assumptions that have not been stated.

### C. Genuine mathematical errors or ambiguities

Problems containing incorrect statements, insufficient information, contradictory conditions, or multiple defensible interpretations.

For each issue:

- Identify the exact section and problem number.
- Explain the problem briefly.
- Describe why it matters.
- Suggest a clearer formulation or correction.

Be selective. Do not manufacture criticisms simply to populate this section.

**Do not include general complaints about discovery learning, instructional philosophy, or minor stylistic issues.**

The teacher's review should be mathematically focused, specific, and constructive.

If there are no serious issues, say so.

## 9. Document format and visual design

Produce a **complete HTML document** that can be opened in a standard web browser.

The document should resemble an attractive, professionally designed mathematics textbook.

### Formatting requirements

- Large, readable text.
- Comfortable line spacing.
- Clear headings and visual hierarchy.
- Generous but reasonable whitespace.
- Well-formatted mathematical equations.
- Accurate and readable graphs.
- Clearly distinguished worked examples.
- Subtle emphasis for important mathematical rules.
- Visually distinct shaded boxes for packet clarifications.
- Separate student-facing instructional material and teacher commentary.
- Print-friendly CSS.

Use MathJax, KaTeX, or another high-quality mathematical typesetting solution.

Prefer a self-contained HTML file with embedded styling and graphics.

If mathematical rendering depends on an externally hosted library, state that an internet connection is needed. If practical, provide a fully offline-capable version.

Avoid excessive color, clutter, decorative elements, or unnecessarily complicated layouts.

### Mandatory mathematical typesetting and HTML escaping

**Mathematical typesetting must be validated, not merely included in the HTML source.** A document containing LaTeX commands does not necessarily display formatted mathematics. Visually verify it in a real browser whenever browser-rendering tools are available; otherwise follow the automated-validation fallback in Section 11 and disclose the limitation.

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

### Standard lesson header

Every lesson must include:

- The course name, module number, and module title.
- The section number and original MVP lesson title.
- A subtitle explaining that the document provides supplementary instruction for students in the relevant course (for example, Secondary Math II) using the Mathematics Vision Project (MVP) curriculum.
- A clearly visible statement that the material was independently created and is not affiliated with or endorsed by the Mathematics Vision Project.

Follow the exact header styling and layout of the approved HTML reference file, when provided.

### Preserve the established visual style

**When I provide a previous supplement as a formatting reference, use it as the visual template.**

Match its general:

- Typography and spacing.
- Heading structure.
- Equation formatting.
- Graph presentation.
- Worked-example styling.
- Packet-clarification boxes.
- Overall visual hierarchy and readability.

Do not redesign the document unnecessarily.

The HTML supplement developed for MVP Math 2, Module 2, sections 2.1 and 2.2 is the preferred reference when available.

## 10. Maintain a clean distinction between instruction and commentary

The document should have three clearly identifiable kinds of content.

**Main instructional material:** The primary textbook-style explanation of the mathematics. It should be organized logically, independent of the packet's narrative, and free of unnecessary commentary about the curriculum.

**Packet clarifications:** Student-facing notes about specific exercises that require interpretation, qualification, or correction. They must be visibly distinguished from the lesson and must identify the relevant problem numbers.

**Teacher's review:** A separate end section identifying only egregious problems in the packet.

Do not mix these three functions.

In particular, do not introduce a mathematical concept primarily through a criticism of the curriculum when it could be taught directly and clearly.

## 11. Quality control

Before delivering the document, review it carefully.

### Mathematical correctness

- Verify every worked example.
- Check all calculations and algebraic manipulations.
- Verify plotted coordinates and graph shapes.
- Check vertices, intercepts, transformations, and other labeled features.
- Ensure that mathematical terminology is used correctly.
- Distinguish rigorous mathematical conclusions from assumptions or observations based on examples.

### Instructional completeness

- Confirm that every major topic in the assigned main tasks is covered.
- Review every Ready, Set, Go problem for skills that may have been overlooked.
- Confirm that all necessary prerequisite material is available.
- Verify that genuinely new concepts are explained explicitly.
- Ensure that there are enough worked examples to demonstrate all important procedures.

### Instructional coherence and daily-lesson pacing

For every lesson, build an internal **scope ledger** before drafting: (a) previously taught prerequisites, (b) new concepts introduced in this exact packet section, (c) this section's Ready/Set/Go review skills, and (d) future concepts that must NOT be taught yet. Use the ledger to keep the chapter within its daily boundary. Do not include the ledger in the student-facing lesson unless a short coverage map helps.

For each section, confirm that:
- The first substantial instructional paragraph begins with an accessible concept, not a fully generalized rule that students have not learned to interpret.
- Every new idea gets its own explanation and at least one worked example; supply a graph when it substantially improves understanding.
- Today's main task and all its Ready/Set/Go topics are covered in this section, not deferred to a different section merely for narrative neatness.
- Concepts from later packet sections are not used to explain earlier lessons.
- The lesson is substantial enough to **teach** its content, not simply summarize it. Do not sacrifice the explanation, distinct transformations, graphs, and worked examples to fit an arbitrary page count or to generate a large module in one pass.
- A student can read this section directly after the previous day's lesson and complete today's exercises without reading ahead.

### Instructional coherence

**Read the document as a student would encounter it.** Check that:

- Each concept is introduced before it is used.
- The instructional sequence develops naturally.
- Examples follow logically from the explanations.
- New terminology is defined when needed.
- Packet-specific clarifications do not interrupt the narrative.
- The level of detail is appropriate for the intended students.
- The lesson can be understood without consulting the original packet.

### Presentation quality

- Confirm that equations render correctly.
- Check that graphs are legible and accurate.
- Ensure that text is not clipped or overlapping.
- Check that the document displays well at ordinary browser widths.
- Verify that the print layout is readable.
- Confirm that all packet references are accurate.

### Mandatory rendering checks or explicitly disclosed validation fallback

**Whenever browser-rendering tools are available, open the generated HTML in a real browser and visually inspect the rendered result.** Do not rely on source-code inspection alone when a browser is available. If browser rendering is unavailable, perform the automated HTML and mathematical-syntax checks described below and **explicitly report that visual browser rendering was not verified**. Never claim to have tested in a browser unless you actually inspected its rendered output.

1. **With a browser, check that the mathematics renderer actually runs.** Wait for MathJax/KaTeX to finish loading and typesetting. Confirm that several equations have become rendered math elements, rather than remaining visible as raw `\(`, `\)`, `\[`, `\]`, `\frac`, `\ne`, superscript carets, or other LaTeX syntax. Test inline and display equations, including the first vocabulary table.
2. **With a browser, inspect representative pages by screenshot or rendered browser view:** the beginning, middle, and end; at least one table containing inequalities; a worked example containing fractions, radicals, or multi-line algebra; a graph; and a packet-clarification box. For long documents, test examples from multiple lessons rather than checking only the first lesson.
3. **Validate HTML structure.** Look for malformed or unknown tags and broken table rows, especially when expressions contain `<`, `>`, or ampersands. Ensure table cells are intact and math has not been mistaken for HTML markup.
4. **Check delimiter integrity.** Make sure math delimiters are balanced and rendered as intended in ordinary text, tables, worked examples, and callouts. A count of delimiter strings is only a preliminary check, not a rendering test.
5. **With a browser, check functionality and printing.** Confirm diagrams, links, layout, and print styling work without clipped content. Check at both desktop and narrow-screen widths.
6. **Check dependencies.** If math rendering uses a CDN, verify that it loads under the intended viewing conditions when browser/network testing is available; otherwise note that it was not tested and disclose the internet requirement. For an offline-required document, bundle or use a genuine offline renderer instead of merely embedding the mathematical source.
7. **Fix and retest.** Do not knowingly deliver a file with raw LaTeX, broken mathematical tables, or failed rendering. If visual rendering cannot be verified, explicitly report that limitation instead of claiming the file was browser-tested.
8. **If browser rendering is unavailable, run automated fallback checks:** parse the HTML with a standards-aware parser or validator; inspect for invalid or unexpected tags, malformed table structure, and unescaped comparison signs; verify that LaTeX delimiters are balanced and consistent; inspect the emitted JavaScript MathJax/KaTeX configuration for correct escaping; and scan the entire document for common raw-LaTeX and broken-markup patterns. These checks reduce risk but **do not establish that visual rendering is correct**.

**Acceptance test:** On opening the HTML in the intended browser environment, the reader should see mathematical notation such as *f(x) = ax² + bx + c*, correctly arranged inequalities such as *0 < a < 1*, readable fractions and square roots, and intact tables and graphs—not unprocessed LaTeX commands.

## 12. Include a coverage table

At the end of the document, include a concise table mapping the original curriculum to the supplemental material. **List sections separately and verify that none teaches content first introduced later in the packet.**

The table should identify:

- The main task and its mathematical objectives.
- The skills addressed by Ready.
- The skills addressed by Set.
- The skills addressed by Go.
- Where each skill is taught in the supplemental lesson.

The purpose is to verify instructional completeness, not to provide a lengthy commentary on every original exercise.

Group related problems where appropriate.

## 13. Research and recommend additional learning resources

For **each curriculum section**, research and provide carefully selected external learning resources covering the same mathematical concepts. Do this research during the initial curriculum analysis rather than adding generic links afterward.

Prioritize sources in this order:

1. **Paul's Online Math Notes** — Preferred for written explanations, worked examples, and practice problems with solutions.
2. **Khan Academy** — Preferred for short instructional videos and interactive practice.
3. **Professor Leonard** — Preferred for comprehensive, traditional classroom-style lectures.
4. **OpenStax** — Useful as an alternative textbook reference, though often denser to read.
5. **Other reputable resources** — Include when they offer an especially strong explanation, visualization, or practice opportunity unavailable from the preferred sources.

### Professor Leonard: required search, optional recommendation

For **every lesson**, actively search for a Professor Leonard lecture that addresses the lesson's specific mathematical content. Do not rely on general searches that might overlook his videos.

- When a suitable lecture exists, include it as an **optional extended-learning resource**, with a direct link to the specific lecture.
- Identify the precise relevant segment or timestamps **when they can be verified**. If timestamps cannot be verified, say so and describe the relevant portion without inventing timestamps.
- Assess how much of the lecture extends beyond the current lesson, and explicitly tell students what to watch or skip when feasible.
- If no appropriately matched lecture can be found, omit it rather than including a vaguely related lecture simply to feature Professor Leonard.

### Resource selection requirements

- Point to the **exact section, lesson, video, exercise set, or other specific content**, not a site homepage or broad course.
- Check that every link resolves to the intended material.
- Describe in one or two sentences what the resource teaches and which topics or packet exercises it supports.
- Indicate whether it is a close match, a partial match, prerequisite review, or more advanced than the current lesson.
- Prefer resources covering the current lesson without unnecessary advanced material.
- If a resource extends beyond the assigned topic, identify the relevant portion, examples, or timestamps when they can be verified.
- Do not invent video timestamps, lesson titles, section numbers, or precise content boundaries.
- Omit weak matches rather than filling a quota.
- Give special consideration to Paul's **practice problems with worked solutions**, not only his explanatory notes.

### Evaluate scope and potential for confusion

**For every recommended resource, assess both its instructional quality and how closely its content matches the current lesson.** These are separate dimensions: an excellent resource may nevertheless be a poor assignment if most of it assumes unfamiliar material.

Include a **“Scope / What to skip”** column in the resource table, using these categories:

- **Close match:** Almost all the content is directly relevant.
- **Some extra material:** The resource is helpful but includes topics not covered in the current lesson.
- **Significantly broader:** Substantial portions extend beyond the lesson or assume knowledge students may not yet have.

For resources with extra material:

1. Identify the specific topics or examples outside the current scope.
2. Explain which portions students should use and which they should skip.
3. Give exact headings, example numbers, or video timestamps **when verified**.
4. Distinguish harmless exposure to different concepts from genuinely premature content requiring mathematics not yet learned.
5. Do not assign an entire long resource when only a small portion is relevant unless you can clearly identify that portion.

**Prefer a close curricular match over an otherwise excellent but substantially broader resource.** For example, Paul's general section on transformations includes nonquadratic examples such as square root functions; do not present the whole page as though every example belongs to a lesson specifically about quadratic transformations.

### Presentation in the HTML

At the end of **each student-facing lesson**, add an **Additional Learning Resources** section matching the document's visual style.

Usually include two or three carefully selected primary resources:

- Recommended reading.
- Recommended video.
- Optional practice or extended explanation.

Add further links selectively for distinct prerequisite or extension skills.

Present resources in a compact table or similarly scannable format with:

| Resource and direct link | What it covers / why use it | Scope / What to skip |
|---|---|---|
| Specific section or video | Closely mapped lesson content | Close match, some extra material, or significantly broader; give precise guidance |

Keep resource recommendations separate from the main lesson and packet clarifications. A few precisely targeted resources are better than a long list of vaguely related links.

## 14. Final deliverable

Provide a downloadable **HTML document for only the requested numbered section**, containing:

1. Coherent, explicit student-facing mathematics lessons.
2. Definitions of important new terminology.
3. Fully worked examples throughout the instruction.
4. Accurate mathematical graphs and diagrams where useful.
5. Additional fully worked Go problems, with sufficient coverage of distinct skills.
6. Selective, clearly labeled packet clarifications referencing specific exercises.
7. Curated additional learning resources **for each section**, with specific links and explicit scope/skip guidance.
8. A concise teacher's review of serious problems.
9. A coverage table demonstrating that all intended mathematical content has been addressed.

Use the attached curriculum for determining content coverage and the previous supplement, if supplied, for maintaining visual consistency.

Do not ask unnecessary clarifying questions. If the assigned sections and packet are provided, proceed with the analysis and document creation.

---

## Materials for this request

**Full curriculum module (for context, not for expanding the output scope):** [ATTACH PDF OR OTHER DOCUMENT]

**Section to cover in this request (one only):** [INSERT SECTION NUMBER]

**Grade or course:** [INSERT IF NOT OBVIOUS FROM PACKET]

**Previously approved HTML supplement for visual reference:** [OPTIONALLY ATTACH]

---

## Guiding principle

**Treat the original curriculum as a specification of what students need to learn, not as a template for how they should be taught.**

Each finished supplement should be one coherent, mathematically accurate, visually clear, independently useful **daily textbook lesson**, matched to the requested packet section and usable by a student attending that day’s class. Completeness must never come at the cost of introducing later material prematurely.

Packet-specific confusion should be handled separately, and external resources should be assigned precisely enough that students can benefit from them without wandering into material beyond the current lesson.
