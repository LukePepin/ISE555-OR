# 4. Verification and documentation of the complete batch

CURRENT RULE: one input folder = one single notes LaTeX/PDF covering ALL its
images, plus one single traceability LaTeX/PDF for that same set.
Different dates within the folder do NOT generate separate deliveries.

Compare the complete list of images in the folder against the manifest, transcription,
review, confirmations, notes.md, traceability.md, and metadata.json.
Verify exact coverage: no photo omitted, duplicated, or excluded by date.
Preserve path identity (notes/batch, assignments/batch, syllabus) without collisions.

Check equations, numbers, variables, indices, inequalities, units, matrices,
and tables against the photos. The clean text teaches correct formulations without
editorial labels, photo file names, or comparisons with inherited errors. Relevant
assumptions remain. Every source, addition, original correction/reason, and open
question is documented in the batch's single traceability companion.

Check figures: coordinates, signs, labels, captions, and provenance in traceability.
Compile both documents with --deliver raw/PATH. Visually review all
pages, tables, and figures. Confirm that build/notes.tex is the single source for the
complete study PDF and that final/PATH contains only notes.pdf and traceability.pdf.
Record the result and hashes in the internal work; do not insert reports into the study material.

Do not fake human or independent review. The existing authorization allows generating
the deliverables; communicate essential open questions in chat without presenting them as facts.
Update README and CHANGELOG: what changed, why, files, validation, open items,
and any old→new path. Archive replaced outputs and remove active references
to the obsolete workflow. Do not use lectures/, main.tex, --build, --publish, or --preview.


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
