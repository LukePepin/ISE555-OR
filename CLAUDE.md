# ISE 555 coursework

Luke Pepin's coursework for ISE 555, Advanced Deterministic Systems Optimization
(University of Rhode Island, Fall 2026, Dr. James Houghton). Class meets Monday and
Wednesday. Course software is mainly Julia and Excel.

## Workflow

Luke writes notes on paper, scans them (Adobe Scan, which makes a PDF), and drops
them in `Inbox/`. Juan's files go there too, with names starting `J-`. The `/process` skill
(`.claude/skills/process/`) files each scan and writes its `.tex` file. **Luke
compiles the PDFs.** When you test-compile, send the output to the scratchpad so
no PDFs or build files are left in the repo.

## Layout

```
Inbox/                      new scans, emptied by /process
Notes/
  Lectures/YYYY-MM-DD/      scan.pdf, notes.tex, notes.pdf  (+ J-notes.pdf etc.)
  Reading/chNN/             same files, named by textbook chapter
Homework/HWn/               handout.pdf, scan.pdf, main.tex, "Luke Pepin - ISE 555 HWn.pdf"  (+ J-HWn.pdf)
Bhunia-Sahoo-Shaikh-2019-Advanced-Optimization-and-OR.pdf   the textbook, gitignored
```

- **Juan's files carry a `J-` prefix** and sit in the same folder as Luke's:
  `J-scan.pdf`, `J-notes.tex`, `J-notes.pdf`, `J-traceability.pdf`, `J-HWn.pdf`.
  There is no separate Juan folder.
- Dates are always ISO (`2026-09-23`). Chapters are always two digits (`ch01`).
- `Homework/HW1/main.tex` is the style example for homework, and
  `Notes/Lectures/2026-09-14/J-notes.pdf` (Juan's, covering 9/14 and 9/16) for notes.
- Each `.tex` file stands alone. There is no shared preamble.

## Rules

- **This GitHub repo is public.** Never commit the textbook PDF, which is copyrighted.
  It's in `.gitignore`; don't work around that.
- Don't commit or push unless Luke asks.
- To read a scan PDF, call Read without `pages`, because poppler isn't installed.
  For textbook pages, extract a range with pypdf into the scratchpad first.

## Notation used in class

- Decision vector $x \in \mathbb{R}^N$ (or $\mathbb{Z}^N$); objective $f(x)$, also written $Z$ or $z$.
- Feasible set $S$. Equality constraints $g_i(x) = 0$ for $i \in \mathcal{E}$;
  inequality constraints $g_i(x) \ge 0$ for $i \in \mathcal{J}$.
- A point can be feasible or infeasible. A constraint is active at a point if it
  holds with equality there.

## Textbook

Bhunia, Sahoo, Shaikh, *Advanced Optimization and Operations Research*, Springer, 2019.
The syllabus lists it as optional/supplementary.
File: `Bhunia-Sahoo-Shaikh-2019-Advanced-Optimization-and-OR.pdf` in the repo root.
Page numbers below are PDF pages, not printed page numbers.

| Ch | Title | PDF pages |
|---|---|---|
| 1 | Introduction to Operations Research | 17–27 |
| 2 | Convex and Concave Functions | 28–42 |
| 3 | Simplex Method | 43–92 |
| 4 | Revised Simplex Method | 93–122 |
| 5 | Dual Simplex Method | 123–139 |
| 6 | Bounded Variable Technique | 140–149 |
| 7 | Post-optimality Analysis in LPPs | 150–182 |
| 8 | Integer Programming | 183–207 |
| 9 | Basics of Unconstrained Optimization | 208–221 |
| 10 | Constrained Optimization with Equality Constraints | 222–258 |
| 11 | Constrained Optimization with Inequality Constraints | 259–277 |
| 12 | Quadratic Programming | 278–311 |
| 13 | Game Theory | 312–375 |
| 14 | Project Management | 376–411 |
| 15 | Queueing Theory | 412–495 |
| 16 | Flow in Networks | 496–528 |
| 17 | Inventory Control Theory | 529–587 |
| 18 | Mathematical Preliminaries | 588–620 |

Tentative course topics (from the syllabus): introduction; feasibility and
optimality; linear programming; simplex; revised and dual simplex; post-optimality;
networks; transportation and assignment; job shop; knapsack and dynamic programming.
