# Homework

Folder: `Homework/HWn/`

| File | What |
|---|---|
| `handout.pdf` | the assignment sheet |
| `scan.pdf` | Luke's handwritten work |
| `main.tex` | what you write |
| `Luke Pepin - ISE 555 HWn.pdf` | the final PDF Luke submits (compiled and renamed by Luke) |
| `J-HWn.pdf`, `J-traceability.pdf` | Juan's version, if Juan sent one. File it only; never use it as a source for Luke's `main.tex`. |

## Rules

This is Luke's graded work. Your job is typesetting it.

- **Typeset what Luke wrote.** Tidy up wording and grammar, but keep Luke's method,
  variables, and answers.
- **Don't fix answers without saying so.** If a step or result looks wrong, keep it
  as written, add `% CHECK: <what looks off and why>` above it, and bring it up in
  the report. Luke decides what to change.
- **Don't solve problems Luke hasn't worked.** If the handout requires a problem that
  the scan doesn't cover, say so in the report and leave it out.
- Get the due date and the list of required problems from `handout.pdf`. Put the
  due date in `\date`. Number the questions the way the handout does.
- Mark uncertain readings with `\unclear{}`, the same as in notes.

## Style

Match `Homework/HW1/main.tex`:
- `\section*{Question N}` for each problem, with `Part (A)` and so on inside it
- one or two sentences defining the decision variables and what they mean
- a formulation block: `Maximize:` or `Minimize:`, then `Subject to:` followed by an
  `itemize` list with one constraint per item and a short label in parentheses
- supporting work (numerical checks, bounds, optimality arguments) under bold run-in headings
- don't restate the problem statement unless asked
