# ISE555-OR

Coursework for ISE 555 (Advanced Deterministic Systems Optimization), Fall 2026.

## Layout

- `Homework/` — graded assignment deliverables, one subfolder per assignment
  (`HW1`, `HW2`, ...). Each contains the finished PDF plus its traceability PDF.
- `Notes/` — cleaned-up lecture notes, one subfolder per batch (named after the
  source photo folder). Each contains `notes.pdf` plus `traceability.pdf`.
- `Processing/processing_notes/` — the internal tool that turns raw lecture/assignment
  photos into the PDFs above. See its own [README](Processing/processing_notes/README.md)
  for how to run it. Deliverables are moved out of its `final/` folder into
  `Homework/` or `Notes/` after each build; `final/` itself is regenerated on demand
  and not meant to hold the current copy.
