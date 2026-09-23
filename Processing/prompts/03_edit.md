# 3. Drafting and production: one folder, one complete document

CURRENT RULE: all images in a single input folder ALWAYS form a single
notes document, a single LaTeX file, and a single study PDF. Never
split deliveries by date, page, or topic. Different dates may be organized
as internal sections. The folder, not the date, identifies the batch.

Read the transcription, review, context, manifest, and user confirmations.
For raw/RELATIVE_PATH, create in work/batches/RELATIVE_PATH/:

1. notes.md: final, complete notes, in plain English, with integrated explanations
   and correct formulas. No photo file names, Source, Documented Correction,
   Additional Explanation/Information, or editorial history. Do not remove useful
   explanations when stripping labels. Keep relevant assumptions and mathematical limits.
2. traceability.md: ONE companion for the WHOLE batch, with section→photo
   correspondence, additions/reasons, original/correction/justification, confirmations,
   dates, figures, verification, and administrative material excluded from the study text.
3. metadata.json: source_batch (full raw/... path), course, images (ALL
   images in that folder, each listed once), optional display_date, optional
   image_dates. Dates inform the content, they never split the delivery.

Build with: python3 process_notes.py --deliver raw/RELATIVE_PATH
Delivery: final/RELATIVE_PATH/notes.pdf and traceability.pdf.
LaTeX: work/batches/RELATIVE_PATH/build/notes.tex and traceability.tex.
A single notes.tex must contain ALL the content of the folder. The second tex/pdf
is only the separate traceability document authorized by the user, not another
academic split of the batch. Do not use preview.pdf, work/days, main.tex, or lectures/.

Formulation basis: scope → data/units → variables/domain → objective →
justified constraints → assumptions → validation and interpretation. Distinguish
quantities, fractions, and binary variables. When essential data is uncertain, ask
in chat; do not invent it. Keep open items and decisions in the traceability document.

Figures only when they explain geometry, objective, constraints, or model structure.
Reproducible code, vector PDF, and PNG for Markdown. Clean academic captions;
source and any added detail go in traceability.md. No decorative figures or
uncalculated solutions. Resolve relative paths from the effective working folder.

Record every change, iteration, and migration in CHANGELOG.md and update README.md.
Archive previous deliveries without moving originals or leaving old outputs as current.


For assignments: work only the selected/authorized exercises and check the
solutions provided against their statements. Include the statement, variables, and
formulation directly. Each exercise occupies its own page within the SAME
LaTeX/PDF for the folder, with no cover page or separate index. Use
metadata.layout="one_problem_per_page" and verify that no exercise overflows
its page. Do not include labels such as "Interpretation of the constraints" or
"Check and interpretation", numeric solutions, or verification blocks. Keep only
short, essential clarifications; checks and solver results belong in the separate
traceability document. Do not add a final theory section, topic background, or
general explanations unrelated to the exercises. Respect explicit exclusions even
if the printed statement asks to solve them. Record photos of unselected exercises
in traceability without inventing solutions.
Assignment 1: exercises 1, 2, and 5, plus the text of exercise 6 provided later by
the user. Authorization of exercise 6's text supersedes its earlier exclusion.
Do not use em dashes in the clean delivery. Include the author and date given in
the metadata; visually separate statement and formulation with short subheadings.
Explicitly define decision variables and distinguish them from data and parameters.
Show all costs, demands, and units; preserve manuscript notation when it is clear.
Do not replace correct balances with incomplete inequalities.

For the assignment's nutritional bounds, show each minimum P_j N and maximum
u_j N on separate lines; do not use chained inequalities.
