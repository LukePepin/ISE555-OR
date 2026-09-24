# ISE555-OR

Coursework for ISE 555, Advanced Deterministic Systems Optimization (URI, Fall 2026).

## Workflow

1. **Write** notes or homework on paper.
2. **Scan** with Adobe Scan and put the PDF in `Inbox/`. For anything from Juan, start the filename with `J-` (e.g. `J-sep28.pdf`).
3. **Process:** run `/process` in Claude Code. It files each scan in its folder and
   writes the `.tex` file. Uncertain readings show up in **red** in the PDF, and
   Claude lists them so you can check them against the paper.
4. **Compile** the `.tex` in VS Code (LaTeX Workshop). For homework, rename
   `main.pdf` to `Luke Pepin - ISE 555 HWn.pdf` before submitting.

`/process Notes/Lectures/2026-09-23` (or any folder) redoes a single item.

## Layout

```
Inbox/                      drop new scans here (emptied by /process)
Notes/
  Lectures/2026-09-23/      scan.pdf · notes.tex · notes.pdf
  Lectures/2026-09-14/      J-notes.pdf · J-traceability.pdf   (Juan's)
  Reading/ch01/             reading notes, named by textbook chapter
Homework/
  HW1/                      handout.pdf · main.tex · Luke Pepin - ISE 555 HW1.pdf
                            J-HW1.pdf · J-traceability.pdf     (Juan's)
Bhunia-Sahoo-Shaikh-2019-Advanced-Optimization-and-OR.pdf   textbook; local only, not on GitHub
```

- Folder names: lectures use ISO dates (`2026-09-23`), readings use two-digit chapter numbers (`ch01`).
- Juan's files start with `J-` and sit next to yours in the same folder.
- `Homework/HW1/main.tex` and `Notes/Lectures/2026-09-14/J-notes.pdf` are the style examples.
- In the `.tex` files, `\unclear{...}` marks a reading to check against the paper, and
  the `aside` environment marks explanation that wasn't on the page.
- Course context and the textbook chapter map are in [CLAUDE.md](CLAUDE.md).
  Processing rules are in [.claude/skills/process/](.claude/skills/process/SKILL.md).
