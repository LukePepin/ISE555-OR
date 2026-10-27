# ISE 555 midterm study session, 2026-10-27

Midterm is 2026-10-28, 4:00–5:15 PM. Plan for the 90-minute session: definitions →
weak points (no chain rule) → Blocks 1–4, each with a short MC/TF quiz → full practice
problems. This session got through definitions, weak points, Block 1 and half of Quiz 1.

## Exam scope

From `Notes/Slides/midterm-review.pdf`: formulation; feasibility, basic solutions and
extreme points; descent and optimality; standard, canonical and dual forms; graphical and
algebraic solutions; simplex with tableaus, Phase 1 / Big-M, special cases; duality and
complementary slackness.

In Dr. Houghton's slides, "revised" means Big-M and "dual simplex" means building the dual
and using complementary slackness. Sensitivity analysis is not on the review slide.

## Definitions

- **Feasible point:** meets every constraint, bounds included. **Feasible region S:** the set of them.
- **Active (binding):** the constraint holds with equality at the point. Equality constraints are always active.
- **Standard form:** min cᵀx, Ax = b, x ≥ 0, b ≥ 0.
- **Canonical primal form:** min cᵀx, Ax ≥ b, x ≥ 0 (b can be negative).
- **Dual form:** max bᵀy, Aᵀy ≤ c, y ≥ 0.
- **Slack / excess / artificial:** ≤ row gets +s; ≥ row gets −e; artificial a goes on ≥ and = rows only to get a starting basis, and must end at 0.
- **Basic solution:** with m rows and n variables, pick m basic variables with linearly independent columns, set the other n − m to 0, solve. At most C(n, m).
- **BFS:** basic solution with x ≥ 0. Same thing as an **extreme point** (corner).
- **Degenerate BFS:** a basic variable equals 0.
- **Feasible direction p:** x + αp stays in S for small α > 0. **Descent direction:** cᵀp < 0.
- **Convex set:** the segment between any two points stays in the set. LP feasible regions are always convex.
- **Row 0 (min form):** reduced costs; basic columns show 0. Optimal when all ≥ 0. Enter = most negative; leave = smallest rhs ÷ (positive entry).
- **Special cases:** unbounded = entering column has no positive entry; alternate optima = a nonbasic variable has 0 in row 0 at the optimum; infeasible = Phase 1 ends with w > 0.
- **Dual variable yᵢ:** marginal value of resource i (shadow price, imputed cost).
- **Houghton's tableau:** row 0 is labeled −z, so the row-0 rhs is −z.

## Weak points review

**#1 Simplex arithmetic.** Dividing by 0.5 multiplies by 2. Relabel each row's basic
variable after every pivot. For a max converted to min, z_max is the row-0 rhs as it stands.

**#2 Phase 1 / Big-M.** ≤ → +s; ≥ → −e + a; = → +a. Phase 1: min w = Σa, then subtract
each artificial row from row 0 (row 0 = −(sum of a-rows)). w = 0 at the end: drop the a
columns, put the original c back, zero out the basic columns. w > 0: infeasible. Big-M: row 0
is c with M under each a, then subtract M × each a-row.

Drill (probably D6): min z = 2x₁ + 3x₂ s.t. x₁ + x₂ ≥ 4, x₁ + 2x₂ = 6, x ≥ 0.

```
      x1  x2  e1  a1  a2 | rhs
-w    -2  -3   1   0   0 | -10
a1     1   1  -1   1   0 |   4
a2     1   2   0   0   1 |   6
```

Check: x₂ in, a₂ out (ratio 3 < 4); x₁ in, a₁ out (ratio 2 < 6); w = 0 at (2, 2).
Phase 2 row 0 = (0, 0, 1 | −10): optimal, z = 10 at (2, 2). **Not yet worked by Luke.**

**#3 Feasible descent directions.** Only active constraints: active g ≥ 0 → ∇gᵀp ≥ 0;
equality → ∇gᵀp = 0; descent → cᵀp < 0. Step α from a ratio test on the inactive ones.
Example: min −x₁ − 2x₂, x₁ ≥ 0, x₂ ≥ 0, 4 − x₁ − x₂ ≥ 0. At (0,0), p = (0,1) is a feasible
descent direction, α = 4 → (0,4). At (0,4), p₁ ≥ 0 and −p₁ − p₂ ≥ 0 give cᵀp ≥ p₁ ≥ 0, so
there is no descent: optimal, z = −8.

**#4 Substitutions.** x ≥ k → x = x′ + k (shifts every rhs and the objective constant);
x ≤ 0 → x = −x′; free → x = x′ − x″; upper bound x ≤ u → keep as a row x + s = u.
Example: min 3x₁ − x₂ + 2x₃, x₁ + x₂ + x₃ ≤ 6, x₁ ≥ 1, x₂ ≤ 0, x₃ free →
min 3x₁′ + x₂′ + 2x₃′ − 2x₃″ (drop +3), x₁′ − x₂′ + x₃′ − x₃″ + s₁ = 5.

**#5 Dual signs.** Canonical first (min, all rows ≥, split = rows), then max bᵀy,
Aᵀy ≤ c, y ≥ 0. One y per primal row; one dual constraint per primal column.
Example: max 3x₁ + 2x₂, x₁ + x₂ ≤ 4, x₁ + 3x₂ ≤ 6 → canonical min −3x₁ − 2x₂,
−x₁ − x₂ ≥ −4, −x₁ − 3x₂ ≥ −6 → dual max −4y₁ − 6y₂, −y₁ − y₂ ≤ −3, −y₁ − 3y₂ ≤ −2, y ≥ 0.
Complementary slackness: primal optimum (4, 0), z = 12; row 2 slack → y₂ = 0; x₁ > 0 →
y₁ + y₂ = 3 → y₁ = 3; w = 12 ✓.

**#6 Theorem names.** Fundamental Theorem of LP (an optimum exists → an optimal BFS exists).
Weak duality (bᵀy ≤ cᵀx). Strong duality (equal at the optimum). Complementary slackness
(xᵀ(c − Aᵀy) = 0). Primal unbounded → dual infeasible.

**#7 Convex set.** Segment test: {x₁² + x₂² ≥ 1} contains (±1, 0) but not the midpoint (0, 0).

## Block 1: Formulation and forms

Bread x₁, cake x₂. Flour 2 and 1 kg (100 kg); oven 1 and 2 hr (80 hr); profit $3 and $4;
at least 10 cakes.

- LP: max 3x₁ + 4x₂ | 2x₁ + x₂ ≤ 100 | x₁ + 2x₂ ≤ 80 | x₂ ≥ 10 | x ≥ 0
- Standard (x₂ = x₂′ + 10): min −3x₁ − 4x₂′ (−40 dropped) | 2x₁ + x₂′ + s₁ = 90 | x₁ + 2x₂′ + s₂ = 60
- Canonical: min −3x₁ − 4x₂ | −2x₁ − x₂ ≥ −100 | −x₁ − 2x₂ ≥ −80 | x₂ ≥ 10 | x ≥ 0
- Counts: canonical with n variables and m rows → dual with m variables and n rows.

### Quiz 1

1. T/F: In standard form, b can have negative entries.
2. T/F: In canonical form, b can have negative entries.
3. x₃ ≤ 0 becomes: (a) x′ − x″ (b) x₃ = −x′ (c) x₃ + s = 0 (d) leave it
4. 2x₁ − x₂ ≥ −5 fully in standard form (b ≥ 0): (a) 2x₁ − x₂ − e = −5 (b) −2x₁ + x₂ + s = 5 (c) 2x₁ − x₂ + s = −5 (d) −2x₁ + x₂ − e = 5
5. T/F: With the same constraints, max 5x₁ − x₂ + 7 and min −5x₁ + x₂ have the same optimal x.
6. A canonical primal with 3 variables and 2 constraints has a dual with: (a) 3 vars, 2 cons (b) 2 vars, 3 cons (c) 5 vars (d) 6 vars
7. In canonical form, x₁ + x₂ = 5 becomes: (a) x₁ + x₂ ≥ 5 and −x₁ − x₂ ≥ −5 (b) +s (c) −e (d) x₁ + x₂ ≥ 5 only
8. T/F: For 0 ≤ x₁ ≤ 7, handle the 7 by substituting x₁ = x′ + 7.

Luke's answers: 1F ✓, 2T ✓, 3c ✗ (answer b), 4b ✓. Questions 5–8 not answered.

Q3: x₃ ≤ 0 is a sign restriction, so substitute x₃ = −x′ with x′ ≥ 0. Writing it as a row
x₃ + s = 0 leaves x₃ in the problem, and standard form then also requires x₃ ≥ 0, which
forces x₃ = 0.

Answer key for 5–8: 5T, 6b, 7a, 8F (the upper bound stays a row, x₁ + s = 7).

## Next session

1. Finish Quiz 1 (5–8).
2. Block 2: basic solutions, extreme points, graphical solutions + quiz.
3. Block 3: tableau, special cases, Phase 1 / Big-M (work the #2 drill) + quiz.
4. Block 4: duality and complementary slackness + quiz.
5. Full practice problems. Ready-made one: solve the bread/cake LP (answer x = (40, 20),
   z = 200), write its dual and get y by complementary slackness (y = (2/3, 5/3, 0)).
