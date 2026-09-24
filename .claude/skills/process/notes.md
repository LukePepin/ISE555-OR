# Lecture and reading notes

The goal is clean study notes that stay faithful to the page. For the level of
polish (not the exact format), see Juan's `Notes/Lectures/2026-09-14/J-notes.pdf`.

## Header

- Lecture: `\title{ISE 555 Lecture Notes\\\large <main topic>}`, with the lecture date as `\date`.
- Reading: `\title{ISE 555 Reading Notes\\\large Chapter N: <book chapter title>}`,
  with the date written on the page as `\date`.
- `\author{Luke Pepin}`, or `Juan Lopez Olivan` for Juan's scans (which become `J-notes.tex`).

## Content

- **Keep everything on the page.** Every definition, example, table, question, and
  side note goes in. Keep the page order unless moving something clearly helps,
  for example putting a margin note next to the definition it explains.
- **Crossed-out text** was deleted by the writer. Leave it out.
- **Clean up wording, not meaning.** Fix spelling and grammar, expand abbreviations,
  and turn fragments into sentences where that helps. These are study notes, not a
  textbook, so keep them concise.
- **Illegible or uncertain text:** write `\unclear{best guess}` or
  `\unclear{illegible}`. Never guess silently.
- **Math:** typeset every equation properly and check each one. If the page has an
  error (a sign, an index, arithmetic), write the correct version and put
  `% CHANGED: page had <original>` on the line above it.
- **Your own additions** go in `\begin{aside}...\end{aside}`, so it's always clear
  what came from class and what was added. Keep them brief: an intuition, a missing
  step, a one-line answer to a question written on the page. Don't add whole topics.
- **Questions on the page** ("what's the difference between active and boundary?"):
  keep the question. Answer it in an `aside` if the material makes the answer clear.

## Structure and formatting

- Use `\section` for each major topic and `\subsection` only when needed. Put worked
  examples under `\subsection*{Example: ...}`.
- Bold a term the first time it is defined.
- Write tables with `tabular` and booktabs rules (`\toprule`, `\midrule`, `\bottomrule`).
- Redraw sketches that carry meaning (feasible regions, function shapes, networks,
  graphs) with TikZ or pgfplots. Keep them simple and label the axes and key points.
  Skip doodles.
- Follow the notation used in class (see `CLAUDE.md`), e.g. the feasible set is $S$,
  with equality constraints for $i \in \mathcal{E}$ and inequality constraints for $i \in \mathcal{J}$.

## Reading notes and the textbook

You may check the textbook to resolve an `\unclear` reading or to confirm a
definition. Page ranges are in `CLAUDE.md`. Extract only the pages you need into
the scratchpad, then Read that file:

```python
from pypdf import PdfReader, PdfWriter
r = PdfReader("Bhunia-Sahoo-Shaikh-2019-Advanced-Optimization-and-OR.pdf")
w = PdfWriter()
for p in range(START - 1, END):  # 1-based PDF page numbers
    w.add_page(r.pages[p])
w.write(f"{SCRATCH}/chapter.pdf")
```

Don't pad the notes with book content that isn't on the scan. If something from
the book really helps, put it in an `aside`.
