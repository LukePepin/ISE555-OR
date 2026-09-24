---
name: process
description: Turn scanned handwritten ISE 555 pages (lecture notes, textbook reading notes, homework) into LaTeX, and file anything from Juan. Use when the user asks to process their notes, scans, homework, or inbox, or mentions new files in Inbox/.
argument-hint: "[file or folder, defaults to everything in Inbox/]"
---

# Process scans into LaTeX

Target: `$ARGUMENTS`. If empty, process everything in `Inbox/` (ignore `.gitkeep`).
A target can also be an already-filed folder such as `Notes/Lectures/2026-09-23`,
meaning write or redo the `.tex` from the scan there (`scan.pdf` becomes `notes.tex`,
`J-scan.pdf` becomes `J-notes.tex`).

The user compiles the PDFs themselves. Your output is the `.tex` file.

## 1. Read and sort every item

Read each file in full before deciding anything. For a PDF, call Read with no
`pages` argument (poppler isn't installed, so `pages` fails). Images can be read directly.

| What it is | File it at | Then |
|---|---|---|
| Luke's lecture notes | `Notes/Lectures/YYYY-MM-DD/scan.pdf` | write `notes.tex`, see [notes.md](notes.md) |
| Luke's textbook reading notes | `Notes/Reading/chNN/scan.pdf` | write `notes.tex`, see [notes.md](notes.md) |
| Assignment handout | `Homework/HWn/handout.pdf` | nothing more on its own |
| Luke's handwritten homework | `Homework/HWn/scan.pdf` | write `main.tex`, see [homework.md](homework.md) |
| Juan: typeset notes PDF | `Notes/Lectures/YYYY-MM-DD/J-notes.pdf` (plus `J-traceability.pdf` if Juan sent one) | file only |
| Juan: typeset homework PDF | `Homework/HWn/J-HWn.pdf` (plus `J-traceability.pdf` if Juan sent one) | file only |
| Juan: handwritten notes | `Notes/Lectures/YYYY-MM-DD/J-scan.pdf` | write `J-notes.tex` with author Juan Lopez Olivan |
| Juan: handwritten homework | `Homework/HWn/J-scan.pdf` | file only, unless the user asks for more |

**Juan's files start with `J-`.** Luke adds the prefix when dropping them in
`Inbox/`. A typeset PDF with Juan Lopez Olivan as author is Juan's even without
the prefix. Everything of Juan's that you file or create keeps the `J-` prefix,
so Luke's and Juan's versions of the same lecture sit in one folder without
clashing. There is no separate Juan folder.

**Dates.** Use the date written on the page first, then the filename. The scan's
creation date (`mdls -name kMDItemContentCreationDate`) only tells you when it was
scanned. Class meets Monday and Wednesday, so a lecture date should fall on one of
those days. Ask the user if the date is still unclear. If one scan covers two
lectures, name the folder after the first date and give both dates in the title.

**Chapters.** Reading notes use two-digit textbook chapter numbers (`ch01`, `ch02`).
The chapter list is in `CLAUDE.md`.

**Several files for one item.** Combine them into a single `scan.pdf` in page order.
Convert images first with `sips -s format pdf IN.jpg --out OUT.pdf` (this also
handles HEIC), then merge with pypdf (`PdfWriter().append(...)`).

**The folder already exists.** New pages of the same lecture go at the end of
that author's scan (`scan.pdf` for Luke, `J-scan.pdf` for Juan). Extend the existing `.tex` file; don't rewrite it from scratch.
Never overwrite a PDF the user compiled.

Before moving anything, print the plan with one line per file: source, destination,
and what kind of item it is. Then go ahead. Stop and ask only if the kind, the date,
or the HW number is actually unclear. Move files with `mv`; don't copy them. When
you're done, `Inbox/` should hold only `.gitkeep`.

## 2. Write the LaTeX

Copy `templates/notes.tex` or `templates/homework.tex` from this skill's folder into
the item's folder, then follow [notes.md](notes.md) or [homework.md](homework.md).
Each `.tex` file stands alone (no shared preamble), so it also works on Overleaf.

## 3. Check that it compiles

Compile into the scratchpad so no build files end up in the repo:

```bash
latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir="$SCRATCH" notes.tex
```

Run it from the item's folder. Fix every error and every `Overfull \hbox` warning
in the log. Don't leave a PDF in the repo; the user builds that step.

## 4. Report back

Keep it short:
- where each file went
- every `\unclear{}` spot, with the scan page number, so the user can check the paper
- every math correction you made (shown as original, then corrected)
- anything you added in an `aside`, in one line each
