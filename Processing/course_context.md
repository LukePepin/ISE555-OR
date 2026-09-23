# Course context — ISE 555

Updated in iteration 004 via AI visual reading of the local syllabus.
Sources: `raw/syllabus/IMG_7842.jpeg` and `IMG_7843.jpeg`; extraction in
`work/syllabus/material_review.md`. Pending human review; the textbook was not consulted.

- Course: ISE 555 — Advanced Deterministic Systems Optimization.
- Institution: University of Rhode Island. Semester: Fall 2026; 3 credits.
- Professor: Dr. James Houghton.
- Listed textbook: Bhunia, Sahoo, Shaikh, Advanced Optimization and Operations
  Research, Springer, 2019; optional and supplementary per the syllabus.
- Course software: mainly Julia and Excel; software of choice permitted.
- Tentative calendar topics: introduction; feasibility and optimality;
  linear programming; simplex; revised/dual simplex; post-optimality;
  networks; transportation/assignment; job shop; knapsack/dynamic programming.
- Final language: plain academic English. Transcription: original languages.
- Notation observed: x_i, f(x), Z/z; x∈R^N or Z^N; feasible set S;
  g_i(x)=0 for i∈E, g_i(x)≥0 for i∈J; P_i, Q_i, R_i and t for workloads.
- Preferences: preserve order and sources; flag additions, corrections, and illegible text.

## Provenance and dates

- `raw/notes/14_09_2026/`: batch of 9 images; IMG_7831–7834 show 9/14;
  IMG_7839 shows 9/16/2026; IMG_7835–7838 are from 9/16/2026, confirmed by the user in iteration 005.
  Do not attribute the whole batch to the 14th. The original path is kept as-is.
- `raw/assignments/assignment1/`: separate material, not transcribed or solved.
- `raw/syllabus/`: 4 images inspected to extract context; not a full transcription.

This context does not authorize filling in illegible words or attributing additions
to the professor. The original template suggested Hillier & Lieberman without verification;
that suggestion was withdrawn once the actual textbook was identified. Prior copies are
archived in `work/archive/context/iteration-004/`.

## Confirmations and pedagogical criteria — iteration 005

- Worker 4, task P: coefficient 19, confirmed by the user.
- Formulation basis: data/units → variables/domain → objective → constraints → assumptions → validation and interpretation.
- Figures only when they explain the model; generated with code and clearly labeled.


## Final format — iteration 007 (replaces the daily rule)

One input folder always maps to a single, complete study document:
one notes.tex and one notes.pdf with ALL the images, even across different dates.
Dates may be internal sections; they never split a delivery. The companion
traceability.tex/pdf keeps sources, additions, corrections, dates, and review
for the whole batch. Clean study material, integrated explanations, no editorial labels.
Paths: work/batches/RELATIVE_PATH/ and final/RELATIVE_PATH/ mirror raw/RELATIVE_PATH/.
Do not use lectures/ or old cumulative documents. All migrations are recorded
in CHANGELOG and README. Confirmed data: P4=19 and photos 7835–7838 from 9/16.
