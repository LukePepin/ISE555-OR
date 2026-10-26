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

## Still open

- B2-1: max z = 4x₁ + 3x₂, s.t. 2x₁ + x₂ ≤ 8, x₁ + x₂ ≤ 6
- Phase 1 on the D6 tableau, starting from row 0 = (−2, −3, 1, 0, 0 | −10)
- Block 3 (Ch 4–5, 7): check which of revised simplex, dual simplex and sensitivity were covered in class
