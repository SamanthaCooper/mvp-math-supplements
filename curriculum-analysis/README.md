# Curriculum comparison and packet practice records

This project compares the regular Khan Integrated Math I–III courses with the **full MVP honors packets**, not merely our published supplements. Snapshot: October 13, 2026. Khan's separate Illustrative Mathematics-aligned courses are not part of this first comparison.

## Topic inventory

`topic-catalog.json` is the maintained vocabulary: 99 existing MVP map topics plus 27 finer topics/methods and one contextual background entry, for 127 entries in the initial snapshot. Source review added whole-number division and factors on October 14, bringing the maintained vocabulary to 128 entries. `topic-catalog.md` is a readable initial snapshot. The vocabulary groups related skills while retaining finer distinctions where they affect comparison. The separate Khan map preserves the full captured course sequence and activity links. Update the snapshot when changing the catalog.

Each entry has a stable ID, scope, optional parent, MVP evidence/status, and Khan course/unit references. For the working comparison, treat the current MVP map as correct. Normalize names and consider broader entries before marking an unlisted mathematical skill provisionally missing. A match does not establish equal depth. Packet-level verification is deferred until the ongoing inventory develops.

Seven skills are provisionally missing after this first alignment: expected value, binomial probability, combinations, permutations, finite geometric sums, the angle-bisector length theorem, and proofs about irrationality. These are map-based inferences, not confirmed packet omissions. Finer skills judged to fit a broader map entry are retained with a broader-match label, so that judgment can be revisited later.

## Khan curriculum map

[Khan curriculum map](../khan-curriculum-map.html) provides topic and full-course-sequence views. `khan_curriculum_map.xlsx` is the matching Excel snapshot, with Topic map, Lesson coverage, and Activity references sheets. Its maintained inputs are `khan-course-outline.json` (captured public course/lesson/activity links) and `khan-lesson-alignment.json` (reviewed mapping to shared topic IDs). Rebuild with `python3 tools/build_khan_curriculum_map.py`; it also writes `khan-curriculum-map.json`.

The regular Integrated Math courses contain 44 units, 253 lesson groups, 820 videos, 164 articles, 444 listed practice skills, and 148 distinct quizzes/tests/course challenges in this snapshot. Footers and navigation links are excluded. Individual practice questions and video contents have not been comprehensively audited.

First listed explanation is the earliest matched lesson group containing video/article links in course order I–III; a prerequisite-only group is excluded from a broader topic’s first/further explanation fields. Further explanation groups come later; practice and assessments remain separate. These inferred inventory roles are not claims about what students previously learned. Topic counts refer to entire matched lesson groups, can overlap, and must not be summed as independent totals. They measure listed content, not instructional time or the number of generated questions.

Every captured lesson group has a reviewed topic alignment. Course totals include every captured teaching/practice item; raw source metadata preserves names and links. A missing Khan match for an MVP topic means no match was identified in these regular-course outlines, not that the topic is absent everywhere on Khan Academy.

## Side-by-side comparison

[Curriculum comparison](../curriculum-comparison.html) shows each shared topic with MVP and Khan in adjacent columns. MVP introduction, development, and review/practice references come from the maintained workbook; Khan first/further explanations and practice locations come from the captured course map. Search, course, and coverage filters are shared across both columns. The default view includes broad MVP topics and provisional gaps; finer subskills can be included explicitly. A finer topic matched under a broader MVP entry is labeled accordingly, and its MVP references cover the broader entry rather than only that subskill.

Rebuild with `python3 tools/build_curriculum_comparison.py`. It writes `curriculum-comparison.html` and `curriculum-comparison.json`, while preserving the independent Khan map. Counts identify map locations and listed practice skills, not comparable quantities of questions or time.

## Four-component coverage ledger

`packet-coverage.json` contains Main, Ready, Set, and Go records for all 236 mapped lessons (944 component records). Initial summaries are inherited from the workbook; source-checked records are identified by their verification status and `last_checked` date. Preserve unknown values as `null`.

Maintain these records as part of analyzing each packet section. Use `topic-catalog.json` as the shared topic vocabulary, adding finer skills when needed. Keep source verification distinct from the MVP map’s provisional comparison assumptions: the map guides comparisons, while actual packet evidence determines activity records and counts. Updating this ledger neither requires more student-facing explanation nor changes a supplement’s human-review status.

For each packet reviewed going forward:

1. Read all four components in the active honors PDF. Record exact printed/PDF pages and actual problem numbers, including duplicate numbers if any.
2. Give each component stable topic IDs and a concise summary. Preserve its role: supplied instruction/example, discovery, student practice, or review. Do not infer instruction from an exercise heading.
3. Add an `activities` record per independently requested response: problem number, subpart letter, kind, role, skill tags, required or optional method, representation, demand, printed/PDF page, and whether it is honors-only. For duplicate problem numbers, add a stable distinguishing suffix (e.g. `5-upper`).
4. Count numbered problems, explicitly lettered subparts, and independently requested response units separately. A problem with four lettered parts is one numbered problem, four subparts, and usually four response units. An unsplit problem is one numbered problem, zero lettered subparts, and one response unit. Do not split routine steps of a single solution into extra practice units. Record optional prompts separately and exclude them from required-practice totals.
5. Supplied worked examples are a separate count and never student practice. Tag algebraic systems by method: equating output rules, substitution, elimination, matrix row reduction, or inverse matrices. Also tag the algebraic family when applicable. Graphing, interpreting, and checking a proposed solution are distinct skills. Record whether a method is required or merely possible.
6. Deduplicate counts by course, section, component, problem, and subpart. Multiple skill tags do not make a problem count twice for the same query. Parent-topic totals must union activities rather than add child totals.
7. Set `packet_verified` only when the entire component's activity records and counts have been checked. Use `partially_verified` for incomplete records; keep uncounted fields null. Record the date and qualifications. This is source verification, not the supplement's human-review status.

The pilot shows **four independent algebraic-intersection exercises** and one supplied worked example in Math I 3.6 Ready (printed p.30 / PDF p.33). They equate two linear output rules; the packet labels this substitution. They are not four general-form substitution examples.

## Queries

Run:

```sh
python3 tools/query_packet_coverage.py --topic systems-linear-algebraic
python3 tools/query_packet_coverage.py --topic systems-linear-elimination --course 1
python3 tools/query_packet_coverage.py --topic solving-systems-of-linear-equations --search systems
```

Queries report deduplicated verified practice and the extent of unchecked coverage. Until source counting is complete, totals are lower bounds, not answers for the full curriculum. Inherited summaries can locate candidates, but are never included as invented numerical practice counts. Number of exercises is not a measure of instructional time or difficulty.
