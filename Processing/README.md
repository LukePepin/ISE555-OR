# ISE 555 — One folder, one complete document

**Current rule (iteration 007): everything in the same input folder always
goes into the same notes LaTeX and PDF.** Dates or topics may be internal
sections; they never automatically split a delivery.

The requested separation between study material and evidence is preserved: for
each folder, one clean `notes.pdf` and one complementary `traceability.pdf`,
each with a single LaTeX file that covers the whole batch. This replaces the
earlier "per day" rule.

## Current delivery

Original folder: `raw/notes/14_09_2026/`, with **all nine photographs**,
including the ones from 9/16. No photo has been moved or renamed.

- [Complete notes — 8 pages](../Notes/14_09_2026/notes.pdf)
- [Complete traceability — 8 pages](../Notes/14_09_2026/traceability.pdf)
- [Single notes LaTeX](work/batches/notes/14_09_2026/build/notes.tex)
- [Single traceability LaTeX](work/batches/notes/14_09_2026/build/traceability.tex)

**Note (iteration 012):** delivered PDFs no longer stay in `final/`; after each
delivery they are moved to the `Notes/` folder at the repository root (one
subfolder per batch, using the same path relative to `raw/`). `final/` stays
empty between deliveries; `process_notes.py --deliver` recreates it
automatically on every build.

## Content contract

`notes.pdf` contains correct theory, definitions, problem formulation,
integrated explanations, examples, tables, and figures. It shows no photo file
names, Source, Documented Correction, Additional Explanation/Information, or
editorial history. It teaches the correct formulas directly. Necessary
assumptions and mathematical limits do stay in the text.

`traceability.pdf` covers every image in the same batch: sources per section,
original/correction/reason, additions, confirmations, dates, figures,
verification, excluded reminders, and open questions. Cleaning up the notes
does not mean removing useful explanations or losing evidence. Essential
uncertainties are communicated through chat; no data is invented and no human
review is presented as having happened when it has not.

The shared pedagogical basis is: scope → data/units → variables/domain →
objective → justified constraints → assumptions → check and interpretation.

## Structure and batch identity

The path relative to `raw/` is kept intact. This prevents collisions between
notes, assignments, and syllabus folders, or similarly named folders. Folder
names are never normalized as if they were dates: `14_09_2026` and
`2026-09-14` are different folders.

```text
raw/notes/14_09_2026/                all original photos in the batch
work/batches/notes/14_09_2026/
  manifest.json                     inventory and hashes at prep time
  transcription.md                  internal faithful transcription
  academic_review.md                internal review
  notes.md                          editable clean content for the whole batch
  traceability.md                    editable evidence for the whole batch
  metadata.json                     exact path and complete inventory
  course_context.md                 reference context
  build/
    notes.tex                       single complete study LaTeX
    traceability.tex                 single complete traceability LaTeX
    figures/                        local assets needed to compile
    inputs/                         copy of inputs from the last build
    *.log                           logs
  build_report.json                 hashes of inputs, originals, and PDFs
  review.md                         visual/editorial review
final/notes/14_09_2026/
  notes.pdf                         study delivery
  traceability.pdf                  documentation delivery
figures/                            reproducible charts (PDF and PNG)
work/archive/                       previous versions
```

The same mapping applies to `raw/assignments/assignment1/` and
`raw/syllabus/`. Different folders are never mixed. Pick a leaf folder: the
system rejects folders that contain other folders, to avoid omissions from
implicit recursion.

## How to use it

Drop in the photos and ask the assistant to "process this folder." The
assistant does the transcription, review, drafting of both documents, and
verification. The script organizes and compiles; **it does not call an API or
transcribe images on its own**.

To prepare a new folder:

```bash
python3 process_notes.py raw/notes/OTHER_BATCH
```

JPG/JPEG, PNG, and WebP are accepted. Convert HEIC/HEIF or PDF first. Sort
file names to reflect the desired order; EXIF data is not used. Preparation
refuses to overwrite an existing session. Assignments and syllabus material
get a separate material review; exercises are not solved automatically.

To regenerate the current full batch:

```bash
python3 process_notes.py --deliver raw/notes/14_09_2026
```

Equivalent: `python3 scripts/build_batch.py raw/notes/14_09_2026`.
In VS Code, the **Build complete folder PDFs** task prompts for the folder, not a date.

## Stages and responsibilities

1. **01_transcribe.md:** all images in the folder, one internal transcription;
   preserve order, dates, languages, formulas, and `[UNCLEAR]` without guessing.
2. **02_review.md:** review the whole batch; record additions and corrections
   with source and reason. Do not overwrite the original or split by date.
3. **03_edit.md:** produce a clean `notes.md` and a complete `traceability.md`
   in the same session. Integrate explanations, teach correct formulations,
   keep evidence out of the study text. Create metadata listing every image.
4. **04_verify.md:** cross-check both documents and the full inventory, verify
   math/figures, compile and review every page. Save review.md, update
   README/CHANGELOG, and deliver both links.

The grouping rule is stated explicitly in all four prompts, including
drafting, production, and documentation. Copies of the current prompts are in
the active session.

Example `metadata.json` (list every real image, not a subset):

```json
{
  "source_batch": "raw/notes/MY_BATCH",
  "course": "ISE 555: Advanced Deterministic Systems Optimization",
  "images": ["001.jpg", "002.jpg"],
  "display_date": "September 14 and 16, 2026",
  "image_dates": {"001.jpg": "2026-09-14", "002.jpg": "2026-09-16"}
}
```

`display_date` and `image_dates` are descriptive information; they do not
determine splits or paths. The compiler rejects omitting/duplicating an image
even if it corresponds to a different day.

## Build, figures, and versions

`scripts/build_batch.py` validates the exact folder, coverage of all its
images, existence of both documents, and the absence of known editorial
labels in the study material. It generates each complete LaTeX file with
`scripts/render_notes.py` and compiles both in staging. It only replaces the
current PDFs once both builds succeed.

Before replacing them, it archives previous PDFs, previously available
inputs, and a report under
`work/archive/deliveries/RELATIVE_PATH/TIMESTAMP/`. There is no concurrency
lock or power-loss-resistant transaction: run one delivery at a time.
Automated checks do not replace a semantic comparison against the photos.

The renderer supports the project's Markdown subset (headings, simple lists,
tables, math, and figures); it is not a general converter. Edit the Markdown
files, not the generated LaTeX. `build/` includes relative figures so the
LaTeX can be compiled from that folder. Markdown references depend on their
location; here `../../../../figures/NAME.png` is used from the active session.

Figures only when they clarify geometry, objectives, constraints, or model
structure. Reproducible code, vector PDF for LaTeX, and PNG for Markdown;
clean caption and provenance in traceability. For the two existing figures:

```bash
python3 scripts/generate_figures.py
```

That generator is specific to the current examples; it does not interpret new photos.

Dependencies: Python 3.10+ and Tectonic or latexmk/LaTeX; Matplotlib/NumPy to
regenerate figures. This project uses `.tools/tectonic` 0.17.0 and
`.tools/cache`. The builder prioritizes a local Tectonic, then PATH, then
latexmk, without enabling shell escape. New packages may need network access;
current ones are cached. No notes have been uploaded to any external service.

`raw/`, `work/`, and `.tools/` are excluded from Git: they need an independent
backup. `final/` and `figures/` are not excluded.

## Migration and retirement of the previous workflow

| Before | Now |
|---|---|
| `final/2026-09-14/` and `final/2026-09-16/` | Unified into `final/notes/14_09_2026/`; old outputs archived |
| `work/days/DATE/` | `work/batches/notes/14_09_2026/`; previous sources archived |
| `scripts/build_daily.py` | `scripts/build_batch.py` |
| `--deliver DATE` | `--deliver raw/RELATIVE_PATH` |
| `lectures/` | Removed: it was empty and is no longer used |
| `main.tex`, `lectures.tex`, old publish/build functions | Retired; historical files kept in the archive |

Archive of this migration: `work/archive/iteration-006/`, with README,
prompts, code, tests, and previous deliveries. `preview.pdf` remains archived
in iteration-005. Old intermediate documents are kept as evidence, not as
current sources. The --build/--preview/--publish commands no longer exist.
No originals were moved. No active code generates or uses lectures/.

**After every change or iteration:** update the CHANGELOG with the reason,
files, validations, open items, and old→new paths; update the README with the
current procedure. Archive replaced outputs so `final/` only shows what is current.

## Current validation

8 tests focused on the current contract, all passing: full coverage even with
mixed dates, folder identity, mandatory companion document, label cleanup,
preservation of the previous pair on failure, source archiving, and
preparation.

```bash
python3 -m unittest discover -s tests -v
```

Compilation of the two unified PDFs: 8 pages each, 16 pages visually
inspected, logs with no warnings/overflow. The study material covers both days
and both figures with no traceability labels. P4=19 and confirmed dates are
preserved. Administrative/contextual open items remain in the companion PDF.


## Assignment 1: iteration 011, 2026-09-21

- [PDF for exercises 1, 2, 5, and 6](../Homework/HW1/Lopez_Juan_Assignment_1_21092026.pdf)
- [Complete LaTeX](work/batches/assignments/assignment1/build/notes.tex)
- [Traceability](../Homework/HW1/traceability.pdf)

See the iteration 012 note above: the delivery lives in `Homework/HW1/` at the
repository root, not in `final/assignments/assignment1/`.

One exercise per page, four pages in the same PDF/LaTeX. Author:
Juan Lopez Olivan; date: 9/21/2026. No em dashes or
interpretation/verification sections, no final theory. The user provided the
full text of exercise 6 and authorized including it: this supersedes the
earlier exclusion. Exercises 3 and 4 remain out of scope. The six original
photos stay in raw, and the received text is kept in notes.md with provenance
noted in traceability.

Explicit variables and a clear separation between statement and formulation
via `###` headings. In exercise 5, a table of demands D1..D4 and production
costs CI1..CI4, units, inventory cost, opening/closing stock, and
production/stock variables. Full corrected balances are kept. The text of
exercise 6 is kept exactly as the user provided it. Numeric checks appear only
in the documentation companion.

```bash
python3 process_notes.py --deliver raw/assignments/assignment1
```

metadata.json supports document_title, author, display_date, and
`layout: "one_problem_per_page"`. This format only affects notes: each `##`
starts an exercise on its own page, with no cover page/index; each `###`
separates data/variables from the statement. Visually check that nothing
overflows. The LaTeX is self-contained. Keep the prompts and their batch
copies up to date. Tectonic downloads any fonts missing from the cache; this
iteration required cmmi7.pfb. If the build fails, the previous pair is kept.
Nothing is sent to any platform.

Previous sources: work/archive/iteration-009-assignment1/; previous
deliveries are archived automatically in work/archive/deliveries/. Current
paths unchanged. Validation of this delivery: four main pages inspected, both
PDFs compiled, no em dashes in the extracted text; eight tests passing.

Iteration 011: exercise 2 with eight explicit nutritional constraints, one
line per minimum and one per maximum, keeping one page per exercise. Model
and data unchanged. Previous sources in work/archive/iteration-010-assignment1/.
