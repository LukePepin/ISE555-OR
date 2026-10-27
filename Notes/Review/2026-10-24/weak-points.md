# ISE 555 midterm prep: weak points

From the cold diagnostic on 2026-10-24 (D1–D7, no notes). The midterm is on
2026-10-28, 4:00–5:15 PM. The final review is on 2026-10-27.

## Weak, ranked

| # | Topic | What went wrong | Fix | Drill |
|---|---|---|---|---|
| 1 | Simplex tableau mechanics | Couldn't continue after the first tableau; picked the wrong leaving row | The loop: enter = most negative in row 0; leave = smallest ratio RHS / (positive entry); divide pivot row by pivot; zero the rest of the column, row 0 included. Optimal when row 0 ≥ 0. Basic columns form an identity. | HW4 Q1–Q4, B2-1 |
| 2 | Artificials, Phase 1 / Big-M | Used +e on the ≥ row; no Phase 1 objective | ≤ → +s; ≥ → −e + a; = → +a. Phase 1: min w = Σa. Then subtract the artificial rows so row 0 is 0 under each artificial. | HW5 Q1, D6 |
| 3 | Feasible descent directions | Marked an inactive constraint as active; no inequalities written in p | Active g(x) ≥ 0 → ∇gᵀp ≥ 0 (= 0 for equalities); descent → cᵀp < 0; a p meeting all of them means the point isn't optimal | HW2 Q4, Q6; Unit 2 slides 18–22 |
| 4 | Variable substitutions | Left x ≤ 0 and free variables unsubstituted | x ≤ 0 → x = −x′; free → x = x′ − x″; x ≥ k → x = x′ + k | HW3 Q1–Q3 |
| 5 | Dual signs | Read a coefficient from a row instead of a column; left out "max" | Dual constraints come from primal columns; min primal ↔ max dual; = constraint → free y | HW5 Q2–Q4, D7 |
| 6 | Theorem names | Couldn't name it | Fundamental Theorem of LP: if an optimal solution exists, an optimal BFS exists (Unit 3, slide 19). Weak duality: min primal, bᵀy ≤ cᵀx. | — |
| 7 | Convex set test | Gave continuity as the reason | Segment test: (1,0) and (−1,0) in S, midpoint (0,0) not | D1 |
| 8 | Chain rule | Self-flagged | e^{x²}: f′ = 2x·e^{x²}, f″ = (2 + 4x²)·e^{x²} | HW2 Q3 |

## Solid

- Counting and enumerating basic solutions, picking the best BFS (D4)
- Equality constraint gives a free dual variable (D7)
- Convexity conclusions; convex f over convex S means a local min is global (D1)

## Review session 2026-10-26

- **#1 done (B2-1).** Answer: x₁ = 2, x₂ = 4, z = 20. Entering and leaving were right every time.
  Arithmetic slips to drill: dividing by 0.5 *doubles* a row (twice multiplied instead); relabel
  basic rows after each pivot; read z off row 0 directly for a max problem, don't negate it.
  Check at the end: at a BFS with both slacks nonbasic, every constraint is tight.
  One more practice tableau later.

## Review session 2026-10-27

Notes in `Notes/Review/2026-10-27/study-session.md`.

- Scope settled from `Notes/Slides/midterm-review.pdf`: "revised" means Big-M and "dual simplex"
  means building the dual plus complementary slackness. Sensitivity is not on the review slide.
- Quiz 1 (forms): 3 of 4 answered right. Missed x₃ ≤ 0 → x₃ = −x′ (picked writing it as a row with
  a slack, which with x₃ ≥ 0 forces x₃ = 0).

## Review session 2026-10-27 (evening)

- Blocks 1 (redone as a 3x3 jungle: standard → canonical → dual), 2, 3, 4 all covered;
  full bread/cake practice problem solved correctly (x=(40,20), z=200, y read straight
  off the optimal tableau). Three special-case tableaus (unbounded, infeasible, alternate
  optima) worked in full.
- New error pattern for **#1 Simplex arithmetic**: clearing a column, grabbed the pivot
  row's unrelated coefficient instead of the target row's own coefficient in the entering
  column (e.g. used 0.5 from the pivot row instead of 1 from the row being cleared), and
  used `+` instead of `−`. Self-diagnosed as "small dumb mistakes without the calculator,"
  not a conceptual gap — matches the existing fix for #1 (relabel/recheck each step).
- Dual conversion (#5) still has one recurring trap distinct from the sign-table one already
  listed: confusing a primal constraint row with a dual constraint. One primal row → one new
  dual *variable*, whose coefficients spread across the *existing* dual constraints (one per
  primal variable) plus one objective term — it does not become a new dual constraint on its own.

## Still open

- Finish the brewery bonus problem (3rd tableau onward — see 2026-10-27 notes).
- Phase 1 on the D6 tableau, starting from row 0 = (−2, −3, 1, 0, 0 | −10). Drill written out in
  the 2026-10-27 notes: min 2x₁ + 3x₂, x₁ + x₂ ≥ 4, x₁ + 2x₂ = 6. Not confirmed finished.
- Quiz 1 questions 5–8 (if not already covered elsewhere)
- Timed tableau speed/arithmetic drill before the exam
