# Changelog

All changes are recorded here and reflected in README.md.
For new entries: date, iteration, reason, files, behavior,
validation, open items, and migrations (old → new, or "none").

## 2026-09-23: Iteration 013, flattened to Processing/ and translated to English

- Reason: the user asked to remove the double folder layer under `Processing/`,
  translate the tool's documentation from Spanish to English, and keep the
  repository's folder layout concise.
- Files: every file under `Processing/processing_notes/` (`.gitignore`, `.vscode/`,
  `README.md`, `CHANGELOG.md`, `course_context.md`, `process_notes.py`, `prompts/`,
  `references.bib`, `scripts/`, `tests/`, `figures/`, plus the gitignored `raw/`,
  `work/`, `.tools/`) moved up one level to `Processing/`; the now-empty
  `Processing/processing_notes/` was removed. Stale `__pycache__/` directories deleted.
- Translated `README.md`, `CHANGELOG.md`, `course_context.md`, and
  `prompts/01_transcribe.md`–`04_verify.md` from Spanish to English; no
  technical content, rules, or data changed, only language.
- README delivery links updated for the new depth: `../../Homework/...` and
  `../../Notes/...` → `../Homework/...` and `../Notes/...` (Processing/README.md
  is now one level from the repo root instead of two). Internal paths inside
  `Processing/` (raw/, work/, figures/, .tools/) are unchanged since they moved
  together as a unit.
- No changes to script behavior, tests, or LaTeX. `process_notes.py` and the
  scripts under `scripts/` have no hardcoded references to the old
  `processing_notes/` path name, so no code changes were needed.
- Validation: tests and compilation were not re-run, since no Python or LaTeX
  logic changed. Migrations: see "Files" above (old → new: drop the
  `processing_notes/` path segment).

## 2026-09-23: Iteration 012, deliveries moved to Homework/Notes at the root

- Reason: the user organized the repository into three top-level folders
  (`Homework/`, `Notes/`, `Processing/`); deliveries should no longer live
  inside the internal tool.
- Files: `final/assignments/assignment1/Lopez_Juan_Assignment_1_21092026.pdf`
  and `traceability.pdf` → `Homework/HW1/`; `final/notes/14_09_2026/notes.pdf`
  and `traceability.pdf` → `Notes/14_09_2026/`. `final/` was left empty and removed.
- README updated with the new relative links (`../../Homework/HW1/…`,
  `../../Notes/14_09_2026/…`) and a note explaining the convention.
- No changes to `raw/`, `work/`, scripts, or tests. `process_notes.py --deliver`
  still writes to `final/RELATIVE_PATH/` (it recreates it with
  `mkdir(parents=True, exist_ok=True)`); a future delivery must be moved again
  manually to `Homework/` or `Notes/` after it is verified.
- Validation: tests and compilation were not re-run, no LaTeX or script changed.
  Migrations: see "Files" above (old → new paths).

## 2026-09-21: Iteration 011, separated nutritional bounds

- Assignment notes.md: four double inequalities in exercise 2 become
  eight lines: minimums >= P_j N and maximums <= u_j N. No math changes.
- traceability.md, prompts 03/04 and their copies, README, and review updated.
- Previous sources in work/archive/iteration-010-assignment1/; previous
  deliveries archived automatically. Final paths unchanged.
- Both PDFs and LaTeX regenerated. Page and exercise-2-constraint verification.

## 2026-09-21: Iteration 010, presentation and exercise 6 provided

- Author Juan Lopez Olivan and date 9/21/2026 in metadata and heading. Titles
  with no em dashes; build_batch uses a colon and passes author to the renderer.
- render_notes supports ### headings, author, and paragraph spacing for assignments.
- notes.md: explicit variables in 1/2/5; demand table D and cost table CI with
  units in 5, storage, and stocks; correct math balances preserved.
- Incorporated the full text of exercise 6 received via chat. Metadata selection
  1/2/5/6, exclusions 3/4. Previous exclusion of 6 overridden by the new instruction.
- traceability records provenance of the text and notation; prompts 03/04 and their
  copies reflect presentation, costs, author/date, and the new selection. README and review updated.
- Previous sources/code/documentation archived in work/archive/iteration-009-assignment1/;
  previous PDFs archived automatically. No path migration.
- Initial builds failed due to missing cmmi6/cmmi7 fonts with no network access;
  the CI subscript was simplified and cmmi7 was downloaded with authorized access. Final delivery
  compiled: four main pages, one per exercise; both PDFs regenerated.
- Visual inspection of all four pages, text extraction with no em dashes,
  eight automated tests passing. No external submission.

## 2026-09-21 — Iteration 009: one exercise per page

- Request: remove the interpretation/verification sections and added solutions.
- assignment1 notes.md: removed repetitive labels, lengthy interpretations,
  optima, and the solution table; kept statements, variables, and formulations.
- metadata.json adds layout one_problem_per_page. scripts/render_notes.py generates
  exercises on separate pages with no cover page/index or double numbering;
  scripts/build_batch.py applies this format only to the main document.
- traceability.md records the review and keeps numeric evidence separately.
- Prompts 03/04 and the batch copies updated; README documents configuration,
  procedure, and delivery; review.md records verification for this iteration.
- Previous sources in work/archive/iteration-008-assignment1/; previous deliveries
  kept by the builder in work/archive/deliveries/.
- Both PDFs and LaTeX/logs/reports regenerated. Main: 3 pages (1, 2, 5),
  visually inspected and checked via text extraction; companion: 3 pages.
  Exercise 6 remains excluded. Successful build and 8 tests passing.
- No migrations: final/assignments/assignment1/ keeps the same PDF pair.

## 2026-09-21 — Iteration 008: Assignment 1 in LaTeX and PDF

- User requests reviewing the provided solutions against the statements, clarity within
  each exercise, no final theory section; explicitly excludes exercise 6.
- Visual inventory: IMG_7828/7829/7830 statements; IMG_7897/7898/7899 solutions
  for 1, 2, 5. That selection of three exercises is worked; solutions for 3/4 are not invented.
- New sources in work/batches/assignments/assignment1/: notes.md, traceability.md,
  metadata.json, manifest.json (six hashes), structured transcription.md,
  academic_review.md, numerical_check.json, review.md, and context/prompt copies.
- Exercise 1: forging capacity corrected to 90000 and the objective formalized; the check
  and solver confirm 45000 assemblies/year. Exercise 2: indices/units/bounds u_j
  made consistent, with explicit non-negativity. Exercise 5: complete inventory balances,
  non-negativity, I4=0; optimum 92750 validated both algebraically and by solver.
- Statements faithfully rewritten, not a literal transcription of the whole sheet. Exercise 6
  remains unwritten; required per the source but excluded by the user.
- scripts/build_batch.py: configurable title via document_title; the rest of the
  folder contract and document pair unchanged.
- Prompts 03/04: criteria for assignments, explanations within each exercise,
  no theory appendix, respecting the explicit selection and exclusions.
- README: links, command, scope, corrections, and the assignments rule.
- Deliveries final/assignments/assignment1/notes.pdf (4 pages) and traceability.pdf
  (3 pages); single self-contained LaTeX in build/notes.tex. No unnecessary figures.
- Validation: visual review of the 7 pages, build, and numeric checks.
  No submission to any teaching platform. Paths: no migration, new batch in the current structure.

## 2026-09-17 — Iteration 007: the folder defines the document

- Explicit instruction: all images in a folder must always go into a single
  LaTeX/PDF, even across multiple dates; keep the documentation companion.
  The user authorizes deleting lectures/ if unused and requires the rule in every prompt.
- The nine images in raw/notes/14_09_2026 reunified: complete notes.md and traceability.md
  in work/batches/notes/14_09_2026/. Dates only as internal sections.
  Metadata with the exact folder, nine images, dates, and display_date. Copies of
  the transcription, review, manifest, and confirmations kept as evidence.
- Current delivery: final/notes/14_09_2026/notes.pdf and traceability.pdf, 8 pages each.
  One complete notes.tex and one traceability.tex in the session's build/.
- scripts/build_daily.py → scripts/build_batch.py: identity by path relative to raw,
  validation of the full inventory with no per-day subsets, duplicate rejection,
  leaf-folder selection, outputs and archive keyed to the same path; descriptive dates.
- process_notes.py: preparation in work/batches/PATH; --deliver takes a folder,
  not a date; retired historical publish/cumulative functions and arguments.
- Removed the empty lectures/; main.tex and lectures.tex retired from the root with a
  historical copy kept. No active consumers of lectures/ remain.
- Four prompts updated: management/transcription, review, production, and
  documentation now require processing the whole folder, sources kept separate from
  the study material, and logging decisions/migrations. Current copies in the active session.
- course_context.md and its active copy: grouping by folder replaces the daily rule.
- .vscode/tasks.json: per-folder task. README rewritten with the contract, commands,
  single LaTeX, links, structure, migrations, dependencies, and validation.
- tests/test_daily.py → tests/test_batches.py; tests/test_workflow.py adapted to the
  new contract, obsolete behavior removed. 8 tests passing, including
  a folder with two dates producing a single pair, and rejection of an omitted photo.
- Archive work/archive/iteration-006/: previous README/code/tests/prompts/templates,
  work/days sources, and the two per-date final folders retired from the current delivery.
  work/2026-09-14/DELIVERY_MOVED.md now points to the unified batch.
- Validation: local build of both PDFs with no warnings, text extraction confirms
  both models and the absence of editorial labels; visual inspection of 16 pages.
- Migrations: final/DATE → final/notes/14_09_2026; work/days → work/batches/PATH;
  build_daily → build_batch; --deliver DATE → --deliver raw/PATH. Originals untouched.
- Previous open items kept in traceability; P4=19 and the 9/16 dates resolved.

## 2026-09-17 — Iteration 006: two final PDFs per day

- Explicit preference: correct, integrated study notes, with no sources,
  addition/correction labels, or original errors; a separate second PDF
  keeps all the traceability. Deliveries per date, no mixed preview.pdf.
- `work/days/2026-09-14/` and `work/days/2026-09-16/`: new clean notes.md,
  complete traceability.md, and metadata.json with dates and sources per day; a copy
  of the current context. Day 14: IMG_7831–7834; day 16: IMG_7835–7839.
- Semantic cleanup: additions are integrated; only corrected formulas are taught;
  original/correction comparisons, image references, open questions, and
  administrative reminders move to traceability. Assumptions are kept.
  The production/fractions comparison sits on day 16, after both models.
- `final/2026-09-14/notes.pdf` (5 pages) and traceability.pdf (4 pages).
  `final/2026-09-16/notes.pdf` (4 pages) and traceability.pdf (4 pages).
  Exactly two delivery files per day; sources/logs kept outside final/.
- `scripts/render_notes.py`: refactored into a library with no fixed date, a daily
  template with cover page/index, no visible editorial environments; adjustable
  code paths, relative figures, and left-aligned traceability to avoid
  justification issues with long paths.
- `scripts/build_daily.py`: date validation and a mandatory companion, rejection
  of source/illegible markers in the study material, hashes of originals/inputs/outputs,
  temporary build of both PDFs before replacing deliveries, archiving of previous
  versions with build sources when available. Limitation: no concurrency
  lock or crash-resistant transaction.
- Adjustments during the build: downloaded the lmr12.pfb font to the local cache
  after a network restriction; copied figures to staging to resolve portable paths;
  path and alignment fixes removed overflow/warnings from the supplements.
- `process_notes.py`: new --deliver DATE; --preview and --publish removed from the CLI
  with a note on the replacement. Historical functions and cumulative --build kept
  as legacy; they do not sync daily deliveries. raw preparation remains compatible.
- `.vscode/tasks.json`: Build both daily PDFs task, prompting for a date.
- Prompts 03/04 and the batch copies: two-document contract, no labels in the
  study material, evidence/corrections in the companion, review of both, and the
  existing authorization being sufficient to generate them. Daily course/context reflects the preference.
- `README.md`: guide rewritten with the current rules, paths, commands, regeneration,
  limitations, dependencies, backups, migrations, and four links.
- `tests/test_daily.py`: four new tests (date/math, labels and companion,
  second-PDF failure, archiving of previous sources). 14 total passing.
- `review.md` per day: visual review of all 17 pages, no warnings in the logs.
  Text extraction confirms the absence of IMG_/Source/Documented Correction/
  Additional Explanation/Information in both clean PDFs. Hashes checked.
- `build_report.json` per day: build results, hashes, and pages.
- Archived previous README/renderer/prompts in work/archive/iteration-005/.
  The preview PDF/TeX/log moved there; the work/2026-09-14 batch kept as
  evidence and flagged via DELIVERY_MOVED.md. Rebuilds from this iteration
  archived automatically in work/archive/deliveries/DATE/TIMESTAMP/.
- Migrations: root preview.pdf/preview.tex → work/archive/iteration-005/;
  mixed study output → final/DATE/{notes,traceability}.pdf;
  active drafting sources → work/days/DATE/{notes,traceability}.md.
  No original photo was moved or modified. No notes were uploaded to any service.
- Open items: HW1 reminder, abbreviations, trimmed introduction, and unspecified
  units; detailed in traceability. Date and coefficient 19 resolved.

## 2026-09-17 — Iteration 005: PDF, confirmations, and formulation basics

- User confirms worker 4's coefficient P = 19 and dates IMG_7835–7838 =
  9/16/2026; requests an actual PDF and figures only when they help understand the model.
- Archived previous notes/review/context/preview in
  `work/archive/2026-09-14/iteration-004/`; originals untouched.
- `notes.md` and `draft.tex`: dates and coefficient corrected; a seven-step
  expansion for formulating problems, units and domains, constraint direction,
  production vs. fractions, model validation, and common mistakes.
- `transcription.md` and `academic_review.md`: addendum with confirmations, keeping
  the original historical readings. `user_confirmations.json`: structured evidence.
  `manifest.json`: per-photo dates with no change to origin or hashes.
- Root and session contexts updated with dates, data, and pedagogical criteria.
- `scripts/generate_figures.py`: two reproducible Matplotlib/NumPy figures.
  `figures/2026-09-14-feasible-region.{pdf,png}`: region and objective lines.
  `figures/2026-09-16-workload-model.{pdf,png}`: tasks, workloads, and bound t.
- `scripts/render_notes.py`: renderer for the pilot's Markdown, previously temporary;
  figure support, existence checks, numbering, and quote fixes.
  Generates a draft.tex fragment and a preview.tex document; not a general converter.
- `main.tex`/`preview.tex`: inputenc conditioned on the engine; paragraph-spacing
  adjustment to remove a 10pt overflow. Format visually reviewed.
- `process_notes.py`: --preview; build shared with --build; falls back to a local
  Tectonic/PATH if latexmk is missing; cache kept inside the project.
- sudo install not performed: requires a password. Downloaded Tectonic 0.17.0
  from the official repository to `.tools/`; the first build downloaded packages and
  fonts, later builds use the local cache. No notes were uploaded.
- `.gitignore`: .tools/ excluded. `.vscode/tasks.json`: task for the study PDF.
- Prompts 03/04 and their session copies: formulation method and figure criteria,
  math validation, and visual review of the PDF.
- `verification.md/json`, `numerical_check.json`: status updated; P4 and date
  questions resolved; incomplete reminders, a trimmed introduction, and an unspecified
  time unit remain. No full human approval is implied.
- `build_report.json`: compiler, command, hash, and PDF validation.
- `README.md`: links, current status, regeneration commands, dependencies,
  renderer limits, previous archive, and pedagogical criteria.
- Validation: 10 tests passing; `python3 process_notes.py --preview` produces
  preview.pdf (8 pages), final build with no warnings/overflow. All 8 pages and both
  figures rendered and visually reviewed. Cache rebuild successful.
- Paths: no migration; the photos and mixed batch stay in their locations.

## 2026-09-17 — Iteration 004: first real notes

- Request: deliver the actual notes, not just prepare folders.
- Visual inspection of the 9 note photos and the 4 syllabus photos; no
  photo edited, moved, or renamed. The assignment is out of scope for this delivery.
- `work/2026-09-14/transcription.md`: transcription with per-photo blocks,
  original formulas, drawing descriptions, illegible/cut-off fragments.
- `academic_review.md` in that session: sign corrections, binary domain,
  minimum definitions, and model explanation; no silent corrections.
- `notes.md`: first readable English version, nine sections, tables,
  examples, added demonstrations labeled, and explicit open items.
- `draft.tex`: LaTeX version; `preview.tex`: separate entry point to preview the
  draft without publishing it. One-off local conversion; escaping of
  replacements and quote handling fixed during generation, before delivery.
- `verification.md` and `verification.json`: AI review (not independent or
  human), current hash, discrepancies, and a false approval flag. Not published.
- `numerical_check.json`: SciPy/HiGHS confirms a furniture optimum of 62500 at
  (375, 0, 0, 62.5); substitution and the dual bound also verified. Insurance left unsolved:
  coefficient P4 ambiguous between 15/19, kept as a4 in the derivation.
- `work/syllabus/material_review.md`: selective extraction with sources and limits;
  no claim of a full transcription or human verification of the syllabus.
- `course_context.md`: identified ISE 555, the professor, and the photographed textbook;
  withdrew the provisional Hillier & Lieberman suggestion. Textbook and web not consulted.
- Archived previous context in `work/archive/context/iteration-004/` and explicitly
  updated context copies in the notes and syllabus sessions. Assignment copy
  unchanged, documented for future processing.
- `main.tex`: the course's real title. `lectures.tex` remains empty.
- `.gitignore`: added preview.pdf exclusion. README updated with links,
  direct usage, optional build, actual status, and a list of all artifacts.
- Dates: 9/16/2026 detected in IMG_7839 within the nominal batch for the 14th;
  dates for IMG_7835–7838 pending. Draft labeled September 14–16.
- Validation: original hashes match; coverage of 9 photos confirmed; balanced
  LaTeX delimiters. No pdflatex/latexmk/tectonic engine: PDF not generated nor
  the build validated. Workflow Python code unchanged; tests not re-run.
- Paths: no migration; new draft outputs and archive documented above.

## 2026-09-17 — Iteration 003: classification by provenance

- Reason: the user organized originals into notes, assignments, and syllabus; the
  previous script rejected these paths and DD_MM_YYYY dates.
- Inventory: 9 images in `raw/notes/14_09_2026/`, 3 in
  `raw/assignments/assignment1/`, and 4 in `raw/syllabus/`.
- `process_notes.py`: source classification, date normalization,
  manifest with source_type and the real path; publication now verifies that path instead
  of reconstructing it from the date. Compatible with previous inputs and manifests.
  Non-lecture materials get two prompts and are not published.
- Material-review prompt generated by the script: keep statements
  without solving them, and extract syllabus data without inventing it or changing context.
- `course_context.md`: provenance of the three material types and academic data pending
  confirmation; photo content not yet reviewed.
- `tests/test_workflow.py`: three new tests for nested structure/publication,
  material separation, and rejection of invalid dates/paths outside raw.
- `README.md`: tree, commands, inventory, outputs, material review,
  context copies, compatibility, and version archive updated.
- Convention change: `raw/DATE/` → `raw/notes/DATE/`; no original was moved or
  renamed. `14_09_2026` → `2026-09-14` only in internal dates and outputs.
  Notes outputs remain in `work/ISO_DATE/` and `lectures/`.
- New working paths: `work/assignments/ID/` and `work/syllabus/`.
- Prepared the three real sessions with manifests, hashes, context, and prompts;
  the notes session includes an initially false approval flag. No transcription,
  solution, published lecture, or PDF was generated in this iteration.
- Validation: 9 tests passing and correct preparation of the 16 images.
  Build not re-run: no LaTeX changes, and latexmk installation still pending.

## 2026-09-17 — Iteration 001: initial implementation

- Starting point: empty folder, no existing code or notes.
- Decision: manual pilot for 3–4 classes before automating model calls.
- `process_notes.py`: session preparation, ISO dates, sorted image listing,
  hashes of originals, copy of prompts/context, human approval tied to the
  draft's hash, rejection of open questions and discrepancies, publication
  with no overwriting, chronological index, receipt, and build with latexmk.
- `prompts/01_transcribe.md`: faithful transcription with sources and `[UNCLEAR]`.
- `prompts/02_review.md`: separate review with traceable additions and corrections.
- `prompts/03_edit.md`: English and LaTeX, preserving order and origin.
- `prompts/04_verify.md`: independent comparison of the math against the photos.
- `course_context.md`: editable provisional context, no invented references.
- `main.tex`: stable template, definition/example/remark/correction environments.
- `lectures.tex`: initially empty index; `references.bib`: empty bibliography.
- `raw/`, `work/`, `lectures/`, `figures/`, `prompts/`, `tests/` directories:
  separation between originals, evidence, publication, and resources.
- `.vscode/tasks.json`: build task; `.gitignore`: exclusion of originals,
  local intermediates, Python caches, and build products.
- `README.md`: installation, paths, the four passes, approval, publication,
  build, review, version archive, and evolution plan.
- Paths: no migration. Adds `work/` for evidence and `lectures.tex` as a
  generated index instead of editing main.tex after every class.
- Open item: real photos, confirming context, and evaluating the first four classes.

## 2026-09-17 — Iteration 002: local validation

- `tests/test_workflow.py`: isolated tests for preparation/publication, chronological
  index, rejection of a stale hash, modified photos, incomplete approval,
  illegible content, and overwriting.
- `README.md`: test command, validation limits, pilot log.
- Paths: no migration.
- Result: `python3 -m unittest discover -s tests -v`, 6 tests passing.
- Build attempted with `python3 process_notes.py --build`: blocked by
  missing `latexmk`; no PDF generated and the template not validated with a
  LaTeX engine. No system dependencies installed.
- Close-out: README updated with the result and the limitation; pending validation
  of the PDF once LaTeX is installed, and visual quality once real photos exist.
