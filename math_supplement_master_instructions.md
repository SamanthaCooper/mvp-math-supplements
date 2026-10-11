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

Identify the worthwhile mathematical skills addressed in Ready, Set, Go and teach them at an appropriate depth. Apply the instructional judgment in Section 6; reviewing every exercise does not require teaching or solving every exercise separately.

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

### Do not add redundant or misleading graphs

**First inspect the graphs and diagrams already in the assigned MVP packet.** If a packet problem already provides a suitable illustration of the concept, do not automatically create another graph merely because the lesson discusses graphs or because visualizations are generally encouraged. Explain how to interpret the relevant features and refer students to the original problem. The supplemental lesson must still teach the mathematical idea clearly in its own prose; a packet reference alone is not an explanation.

Create or reproduce a visualization **only when it provides a concrete instructional benefit that the existing packet graphic does not**—for example, when the packet's image is unclear, when a new worked example requires its own figure, when a concept needs a more accurate drawing, or when a carefully controlled comparison significantly improves understanding. This rule applies to function graphs, geometry diagrams, tables, and other illustrations; it does not prohibit graphs that are genuinely necessary for explicit instruction.

For any new comparison graphic:

- **Isolate the concept being taught.** Keep unrelated variables, equations, scales, intercepts, and other properties the same when practical, so students are not distracted by incidental differences.
- **Connect it precisely to the instruction and packet problems.** Do not imply that an invented graph reproduces a particular packet problem when it does not. Label original examples as original, if confusion is possible.
- **Check pedagogical accuracy in addition to mathematical accuracy.** A technically correct graph can still be misleading, unnecessary, or poorly aligned with the explanation. Remove it rather than adding more prose to defend it.

**Example — Secondary Math I, Module 3, Section 3.1:** The original packet already includes graphs for comparing linear versus nonlinear and continuous versus discrete relationships (Set Problems 12–13). A new graph juxtaposing an unrelated line with offset discrete points distracts from the intended comparison. Prefer explaining how to make the comparisons using the packet's own graphs. If another graphic is truly needed, ensure its mathematical choices isolate the precise distinction being taught.

**Visual simplicity and curriculum progression:** Use the simplest visual that teaches the day's concept while preserving the curriculum's intended progression. Show only the geometric elements, labels, auxiliary lines, and construction steps needed for the current lesson. Do not add advanced constructions, notation, proof markings, or later-section concepts merely because they make a diagram more comprehensive or elegant. Simplicity never excuses inaccurate geometry: every relationship actually depicted or asserted must remain mathematically correct.

### Mandatory mathematically constrained geometry diagrams

**For instructional geometry, never rely on approximate, hand-positioned drawing coordinates to establish a mathematical claim.** Construct each diagram from mathematically defined relationships and verify those relationships before delivery. An illustration that merely *looks* perpendicular, congruent, tangent, parallel, symmetric, or equilateral is not sufficient.

Follow this workflow for every geometric diagram, including diagrams recreated or adapted from a curriculum packet:

1. **Choose the simplest instructionally sufficient figure.** Identify what students must understand *today* and omit unnecessary visual complexity or relationships belonging to later sections. Preserve the curriculum's intended order of ideas.
2. **Identify the mathematical constraints.** Before drawing, list the given and claimed geometric relationships that the image must accurately represent: incidences, intersection points, collinearity, lengths, equal radii, midpoints, angle measures, bisectors, parallelism, perpendicularity, congruence, and so on. Distinguish explicit givens from relationships that only appear plausible in the packet's picture. Never silently treat a visual impression as a given.
3. **Construct coordinates from those constraints.** Choose convenient exact coordinates and derive the remaining points through valid geometric constructions or formulas. For example, for an equilateral triangle with side length \(s\), use \(A=(0,0)\), \(B=(s,0)\), and \(C=(s/2,\sqrt{3}s/2)\). For intersecting circles, calculate their intersections from the circle equations, rather than moving dots until they look aligned. Use exact or symbolic expressions where practical and only round at final rendering.
4. **Verify the claimed geometry computationally.** Use a suitable tool such as Python with SymPy (or equally reliable calculations) to test each relevant relationship: equality of distances or radii; zero dot products for perpendicularity; zero 2D cross products for parallelism/collinearity; midpoint coordinate averages; point-on-circle distance equations; equal angle measures for angle bisectors; valid intersections; and triangle congruence conditions. For numerical checks, use an explicit tolerance suited to the drawing scale. A failed check means **fix the construction**, not the assertion or the test.
5. **Generate SVG or another scalable vector format directly from verified coordinates.** Preserve the mathematical aspect ratio: use equal scaling on both axes, so a true perpendicular intersection displays as a right angle and a circle remains circular. Calculate all auxiliary rays, arcs, congruence ticks, arrowheads, right-angle squares, dashed construction circles, and highlighted segments from the same geometric data. Make labels and markers consistent with the verified relationships.
6. **Render and visually inspect *every* diagram.** Export or rasterize each generated graphic and examine the result, not just its code. Check for clipped vertices, overlapping labels, misplaced angle arcs, misleading tick marks, wrong endpoint labels, excessive line extension, invisible intersections, unclear construction order, and legibility at normal HTML and print sizes. Adjust *label placement and styling* without altering the proven geometry; regenerate and reinspect as necessary.
7. **Audit diagrams against the lesson narrative and packet.** Verify that every stated or implied geometric fact in the surrounding explanation is reflected accurately in the drawing and that diagram labels match the prose. If the packet itself contains an inconsistent, underspecified, or impossible construction, do not force a false illustration: clarify the issue in a separately labeled packet clarification and teacher's review as appropriate.
8. **Validate the final embedded version.** Inspect the SVG as it appears in the produced HTML, accounting for resizing, `viewBox`, responsive CSS, and printing. Checks performed on an intermediate image do not replace checking the final embedded graphic. If real-browser inspection is unavailable, rasterize and inspect all generated diagrams separately, run geometric and structural validations, and clearly disclose that the completed HTML was not browser-verified.

**Geometry diagram acceptance test:** Every meaningful length, angle, circle, incidence, alignment, construction marker, and labeled relationship must either be mathematically correct by construction or explicitly marked as schematic/not to scale. Do not label a figure as mathematically verified unless the required constraints were actually tested. Prefer rebuilding an inaccurate diagram over nudging individual points by eye.

**One mathematical specification across every representation:** For every figure or worked example containing numerical relationships, maintain a canonical record of the givens and derived quantities (for example, dilation center, original vertices, scale factor, and derived image vertices). Generate coordinates and figure annotations from this record whenever possible. The same principle applies to function plots, numerical tables, axes, captions, example headings, formulas, and solutions. A mathematically correct SVG is **not** sufficient if the example text, title, legend, or caption describes a different value. Check the completed HTML across all these representations using the blocking consistency gate in Section 11.

This requirement applies to **all** geometry diagrams in the main lesson, worked examples, Ready/Set/Go supplements, and packet clarifications. It complements the requirements for accurate function graphs and does not authorize introducing concepts from later sections.

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

### Light-red callouts for serious instructional problems

Use the light-red boxes in **Secondary Math I, Module 2, Sections 2.1–2.2** as the visual and editorial reference. Reserve them for the really problematic cases: a false or misleading mathematical explanation, a conflation of distinct concepts, a missing assumption that materially changes the answer, or a question that cannot be answered uniquely as written. Serious instructional ambiguity can warrant a red box even when there is no simple factual error.

**Use these sparingly.** Ordinary awkward phrasing, unfamiliar notation, routine modeling assumptions, or a preference for a different teaching approach do not warrant a red warning. Use an ordinary packet-clarification box when a short neutral explanation is enough. Do not manufacture criticism or add a red box to every lesson for consistency.

Each red callout should:

1. Identify the exact section, task or Ready/Set/Go component, and problem numbers; include the printed page when available. Identify teacher notes explicitly when they are the source of the issue.
2. Explain the substantive problem precisely and calmly, distinguishing an actual error from ambiguity, an unstated assumption, or an interpretation.
3. State the correct mathematical distinction and give a practical way to proceed, where one can responsibly be offered. Acknowledge multiple valid models or answers when appropriate.
4. Remain separate from the main teaching and neutral packet-reference strips. Place it near the affected instruction, without making criticism the lesson's organizing principle.

Label the box **“MVP clarification — Section …”** or **“Important mathematical clarification — …”** according to its scope; use stronger wording only when the evidence supports it. Retain readable text, a light-red background, a darker red left border, and print-visible styling, following the reference lessons' `.mvp-correction` and `.mvp-correction-title` styles. The label and explanation must communicate its purpose without relying on color alone.

An opening red notice is appropriate only when a serious recurring issue affects much of the section. Keep it concise, use focused local notes for the affected problems, and link a separate supplementary explanation if deeper discussion would overwhelm the daily lesson. The teacher's review may summarize the serious issue without repeating the full student-facing explanation.

## 6. Review Ready, Set, Go and use instructional judgment

Examine every problem in all three homework components to identify the mathematics students need. **Coverage means teaching relevant skills, not providing an answer key, treating every exercise equally, or reproducing every packet problem.**

- Teach genuinely new, worthwhile skills explicitly, including relevant skills that the main task does not introduce.
- Group repetitive exercises by skill. A brief explanation and a representative worked example may support many problems; do not expand the lesson merely to match the number of exercises.
- Give familiar prerequisite material a brief refresher when needed. An exercise's being routine, uninteresting, or tangential does not by itself justify omitting an important skill.
- If a question is ambiguous, explain the ambiguity and any reasonable interpretation or necessary assumption. Do not invent a uniquely intended answer when the packet does not establish one. If the intended skill cannot be determined, say so.
- If an exercise adds no worthwhile instructional topic, or cannot be interpreted responsibly from the available information, it may be omitted from detailed instruction. Identify its problem number or range and a brief reason in the coverage notes so the omission is visible to the human reviewer.
- Distinguish skills taught, skills already supported elsewhere in the lesson, assumed prior knowledge, ambiguous exercises, and deliberate omissions. Do not claim complete coverage when exceptions remain.

Ready often reviews prerequisites; Set often reinforces or extends the main ideas; Go may review loosely related skills. Judge the instructional value and needed depth rather than assigning importance solely by the component's name.

The goal is useful preparation for the day's meaningful mathematics. Provide enough examples to teach distinct procedures, without forcing lengthy treatment of repetitive or poorly specified homework.

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

### Publisher packet links

Place a prominent “Use this supplement with your MVP packet” box beneath the lesson header, linking directly to the corresponding module student-edition PDF on the publisher’s website. Identify the course, module, and numbered section. Include a smaller link to the official course materials for teacher notes and honors editions. Verify the URL and matching edition; never upload local packet PDFs. Use the site’s established publisher-materials styling. During ingestion, refresh these links with `python3 tools/update_publisher_links.py` after updating the navigation indexes.

### Mandatory connections to the original MVP packet

**Make the correspondence between the supplemental lesson and the original packet immediately clear to students.** Under each major student-facing instructional heading, include a compact, visually distinctive **“In your MVP packet”** reference strip. Add a smaller version below a subheading when it helps locate a more specific set of problems. Use the established reference-file style when one is provided: a restrained blue or blue-gray shaded background, subtle left border, and readable text, not an oversized callout.

Each reference strip should provide:

1. **An exact location:** MVP section number, main task or Ready/Set/Go, the **page number printed in the MVP packet** (not the PDF viewer's page index), and the relevant problem number or range.
2. **A brief explanation (usually one sentence)** of what those problems ask students to do and how the immediately following instruction helps.
3. **A precise scope:** List the problems that the nearby instruction actually addresses, not all problems belonging to a larger activity or topic.

**Example of a clean mapping for Secondary Math I, Section 3.1:**

- Under *A complete example: Sylvia's pool*: **In your MVP packet — Section 3.1 · Main task · p. 1 · Problems 1–2.** Explain that this material develops and describes the pool graph.
- Under *Why this water-height graph is a function*: **In your MVP packet — Section 3.1 · Main task · p. 1 · Problem 3.** Explain that this material addresses why water height is a function of time.

**Do not automatically label the first heading “Problems 1–3” and then separately label the function subsection “Problem 3.”** Some overlap is appropriate when one explanation genuinely supports multiple exercises, but overlap must be intentional and informative. Prefer a clear, specific mapping over repeated broad references; distinguish overview coverage from focused instruction when both are genuinely useful.

Additional rules:

- Keep the supplement's **logical, explicit-instruction sequence**. References are signposts, not instructions to reorganize the lesson into a problem-by-problem answer key.
- Use reference strips under **major headings** and selected subheadings, not after every paragraph, worked example, or minor concept. Avoid decorative repetition.
- Where a navigation menu exists, use helpful problem ranges such as **Ready (1–6)**, **Set (7–13)**, **Go (14–22)**, drawn from the actual packet.
- Distinguish these **neutral location/coverage guides** from **packet clarifications**, which address errors, ambiguities, or assumptions. Packet-reference strips should not criticize the packet or replace the mathematical teaching.
- Verify each cited title, page number, problem range, and explanation against the actual packet. If a page or problem reference cannot be verified, do not invent it.
- Preserve both directions of use: a student should be able to read the supplement in order **and** to find the instruction relevant to an exercise in the MVP packet quickly.

### Begin teaching mathematics promptly; avoid meta-instructions

**Do not add generic directions about how to read the supplement.** After the standard header, a concise learning goal (if useful), and navigation, begin the mathematical instruction. The structure and the “In your MVP packet” references should be self-explanatory. Do not explain the reference-strip colors, describe the document's organization in prose, or tell students to read explanations in order, work through examples, or follow other obvious textbook conventions.

- **Put qualifications where they matter.** If a worked example uses invented numbers, extra assumptions, or one possible interpretation of an underspecified packet problem, state that directly beside the relevant example, not in a general opening disclaimer.
- **Don't repeat packet-reference information in the following paragraph.** The reference strip already identifies the problems and their purpose. Begin the section with the mathematics, not a second announcement of what “Packet problems 1–6” ask students to do.
- **Keep directions that genuinely teach or guide mathematical work.** Specific explanations of how to plot a point, choose a scale, interpret a diagram, or avoid a common error are useful. Remove boilerplate, organizational narration, empty encouragement, and commentary about the supplement itself.
- **Do not remove needed instructional depth** just to shorten the document. Edit redundant prose while preserving prerequisite explanations, concepts, worked solutions, critical assumptions, and relevant packet clarifications.

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

The document should have four clearly identifiable kinds of content.

**Main instructional material:** The primary textbook-style explanation of the mathematics. It should be organized logically, independent of the packet's narrative, and free of unnecessary commentary about the curriculum.

**Packet-reference strips:** Brief, neutral student-facing signposts under major headings and selected subheadings that map the nearby instruction to exact MVP pages and problems. They describe correspondence, not curriculum defects, and are not substitutes for teaching.

**Packet clarifications:** Student-facing notes about specific exercises that require interpretation, qualification, or correction. They must be visibly distinguished from both the lesson and reference strips, and must identify the relevant problem numbers.

**Teacher's review:** A separate end section identifying only egregious problems in the packet.

Do not mix these four functions.

In particular, do not introduce a mathematical concept primarily through a criticism of the curriculum when it could be taught directly and clearly.

## 11. Quality control

Before delivering the document, review it carefully.

### Mathematical correctness

- Verify every worked example.
- Check all calculations and algebraic manipulations.
- Verify plotted coordinates and graph shapes.
- For each geometry diagram, record its defining constraints, construct its coordinates from those constraints, and validate the relevant relationships computationally before embedding it.
- Render and inspect every geometry diagram for correct labels, markings, intersections, clipping, and aspect ratio; verify that the final embedded diagram agrees with the surrounding explanation.
- Check vertices, intercepts, transformations, and other labeled features.
- Ensure that mathematical terminology is used correctly.
- Distinguish rigorous mathematical conclusions from assumptions or observations based on examples.

### Mandatory cross-document mathematical consistency gate — BLOCKING

**Every lesson must pass this gate on the actual final HTML file before delivery.** The gate applies to *all* mathematical claims and representations: geometry diagrams, function graphs, tables, algebraic solutions, examples, headings, figure labels, axis labels, legends, captions, and explanatory prose. It supplements—not replaces—the geometry construction tests and rendering checks elsewhere in this document.

1. **Establish a single source of truth for the construction.** Before generating each example or visualization, record the mathematical givens, parameters, units, transformations, claimed properties, and expected numerical results in a canonical specification (structured data when practical). Compute dependent coordinates and numeric annotations from those values rather than typing conflicting values independently. Keep the specification separate from presentation and label-placement choices.
2. **Verify the mathematics independently.** Use a mathematically independent calculation or test—not merely the same drawing function reporting its own inputs—to recompute every relevant constraint. For dilations, verify \(P'=O+k(P-O)\) and each applicable nonzero distance ratio; for other diagrams, check the actual claimed incidences, lengths, angles, parallelism, congruence, etc.; for graphs, test important plotted points, function values, intercepts, vertices, and graph labels. Record expected and observed values and numerical tolerances where applicable.
3. **Inventory and reconcile every related claim.** Check each example's narrative, displayed equations, worked steps, table entries, SVG text, figure heading, legend, and caption against the verified specification. Extract or inspect these items from the *finished HTML*, not just from the script or earlier assets. Treat mathematically equivalent expressions (such as \(3/2\) and \(1.5\)) as consistent; distinguish unlike quantities (such as a length factor of 2 and an area factor of 4). Flag any unexplained value, unit, label, or relationship mismatch.
4. **Inspect the final rendered output.** After embedding the graphics, render or rasterize every diagram and inspect labels and captions together with the nearby example. Check correspondence labels, overlaps, truncation, equal axis scales for geometry, responsiveness, and print legibility. When a full browser is available, inspect the *final HTML* in it; when unavailable, use the Section 11 fallback and explicitly disclose the missing browser check.
5. **Retest after corrections.** If a discrepancy is found, correct the canonical specification or affected prose/diagram as mathematically appropriate, regenerate the affected outputs, and rerun both numerical and cross-document checks on the revised *final deliverable*. Do not fix a true mathematical inconsistency by changing only a caption, suppressing a failed assertion, loosening the tolerance without justification, or adding a vague 'not to scale' disclaimer.
6. **Enforce failure conditions.** Mark the validation **FAIL** and **do not deliver as a completed/verified lesson** if a required geometric or numerical constraint fails; a diagram, formula, example, title, or caption contradicts another representation; a required check was not performed; or final-file content was not reconciled with its specification. Correct and rerun until all required mathematical checks pass. If browser rendering is unavailable but the permitted automated/rasterized fallback is complete, delivery may proceed with an explicit disclosure of that limitation; the unperformed browser test must never be marked PASS.
7. **Report only evidence-based outcomes.** Use **PASS**, **FAIL**, or **NOT CHECKED** for each test, with a meaningful actual observation (a calculated value, inspected label, parsed final-file text, or documented visual observation) and, where useful, the exact file/figure checked. A declaration that a diagram was 'verified' is not evidence by itself. Do not automatically fill report rows with PASS from the same values used to generate the illustration.

**Required internal verification report:** Create and inspect a concise, section-specific report *before* delivery. It is for quality control, not a student-facing section. Include each substantive visualization/example, its canonical parameters and relevant invariants, independent computational results, the actual title/caption/label values extracted or observed in the final file, visual-inspection status, and the final outcome. Retain the report as an internal audit artifact when practical; it need not accompany the student HTML unless requested.

For example, a dilation worked example with \(k=3/2\) requires independent checks of the corresponding point distances **and** agreement of the example statement, diagram coordinates, heading, labels, and caption:

| Test | Expected | Observed in final output or independent calculation | Status |
|---|---|---|---|
| Worked-example scale factor | \(3/2 = 1.5\) | Value extracted from the example | PASS / FAIL / NOT CHECKED |
| Point-distance ratios | \(OA'/OA = OB'/OB = OC'/OC = 1.5\) | Independently computed ratios | PASS / FAIL / NOT CHECKED |
| Figure heading | Scale factor 1.5 | Heading read from delivered HTML/SVG | PASS / FAIL / NOT CHECKED |
| Figure caption | Scale factor 1.5 | Caption read from delivered HTML | PASS / FAIL / NOT CHECKED |
| Visual inspection | Correct vertex labels and readable geometry | Inspected rendered final image, or noted limitation | PASS / FAIL / NOT CHECKED |

*This table is a reporting template, not evidence of completed checks.* A heading of 1.8 and a caption of 1.6 for an example with \(k=1.5\) are **two blocking failures**, even if the SVG coordinates happen to depict a valid dilation. Every finished lesson must have its own observed results, not a prefilled template.

**Final acceptance rule:** A lesson is ready only when its mathematical and cross-document checks **PASS**, its final-file HTML/math-syntax validation has been performed, and any browser-rendering limitation is disclosed accurately. The final delivered file—not an intermediate draft—is the object of verification.

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
- Today's main-task objectives and worthwhile Ready/Set/Go skills are taught within this section; any ambiguous exercises or deliberate omissions are identified under Section 6. Do not defer needed skills merely for narrative neatness.
- Concepts from later packet sections are not used to explain earlier lessons.
- The lesson is substantial enough to **teach** its content, not simply summarize it. Do not sacrifice the explanation, distinct transformations, graphs, and worked examples to fit an arbitrary page count or to generate a large module in one pass.
- A student can read this section directly after the previous day's lesson and work on the supported exercises without reading ahead; limitations caused by ambiguous or deliberately omitted exercises are stated honestly.

### Instructional coherence

**Read the document as a student would encounter it.** Check that:

- Each concept is introduced before it is used.
- The instructional sequence develops naturally.
- Examples follow logically from the explanations.
- Every additional graph, diagram, or table has a specific instructional justification; it does not merely duplicate a useful packet graphic or introduce irrelevant mathematical differences that obscure the point being taught.
- New terminology is defined when needed.
- Packet-specific clarifications do not interrupt the narrative.
- The level of detail is appropriate for the intended students.
- The lesson can be understood without consulting the original packet.
- The opening begins teaching promptly, and no generic usage instructions, redundant packet-number introductions, or unnecessary descriptions of visual conventions interrupt the lesson.
- Packet-specific assumptions are stated beside the worked example or problem they affect, not in a detached introductory disclaimer.

### Presentation quality

- Confirm that equations render correctly.
- Check that graphs are legible and accurate.
- Ensure that text is not clipped or overlapping.
- Check that the document displays well at ordinary browser widths.
- Verify that the print layout is readable.
- Confirm that all packet references are accurate, including printed MVP page numbers, task labels, problem ranges, and the link between the immediately following explanation and the referenced problems.
- Check that reference strips under headings and selected subheadings are concise, readable, and not misleadingly repetitive. Resolve unnecessary overlapping ranges and keep these strips visually distinct from packet-clarification boxes.
- Confirm that every supplemental illustration materially improves the lesson compared with referring to the original packet figure; remove accurate but redundant or conceptually confusing graphics.

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
- Where each skill is taught in the supplemental lesson, consistent with the section's **“In your MVP packet”** reference strips.

The purpose is to make instructional coverage and its limits clear, not to provide lengthy commentary on every exercise. Include concise rows or notes for ambiguous exercises and deliberate omissions, with problem numbers and reasons; do not present those entries as taught or verified.

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
6. Selective, clearly labeled packet clarifications referencing specific exercises, with light-red callouts reserved for serious mathematical or instructional problems.
7. Curated additional learning resources **for each section**, with specific links and explicit scope/skip guidance.
8. A concise teacher's review of serious problems.
9. A coverage table showing where worthwhile mathematical skills are taught and identifying any ambiguous exercises, assumed prior knowledge, or deliberate omissions.

Use the attached curriculum for determining content coverage and the previous supplement, if supplied, for maintaining visual consistency.

**Before providing the download link, complete the mandatory cross-document mathematical consistency gate in Section 11 against the exact HTML file being delivered. Do not substitute checks of generation scripts or intermediate SVGs for checks of the final document.**

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
