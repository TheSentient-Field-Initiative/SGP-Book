# BUILD — Assembling and Verifying the Manuscript

## Single-file LaTeX + PDF (the deliverable)

```bash
bash build/build.sh   # -> manuscript.tex (single file) + manuscript.pdf
```

Pipeline: `build/assemble.py` concatenates chapters/appendices in order and
injects the nine figures (`figures/*.pdf`, converted from SVG by
rsvg-convert) at their mapped positions → `build/manuscript.md` →
pandoc (book class, TOC, TeX Gyre Termes + TeX Gyre DejaVu Math) →
`manuscript.tex` → XeLaTeX ×2 → `manuscript.pdf`. `build/preamble.tex`
holds glyph fallbacks and line-breaking tolerance. Requirements:
python3, pandoc, xelatex, rsvg-convert. Expected: 0 errors, 0 missing
glyphs, all 9 figures included.

## Plain-text concatenation (reading order)

```bash
cat chapters/prologue.md chapters/ch01.md chapters/ch02.md chapters/ch03.md \
  chapters/ch04.md chapters/ch05.md chapters/ch06.md chapters/ch07.md \
  chapters/ch08.md chapters/ch09.md chapters/ch10.md chapters/ch11.md \
  chapters/ch12.md chapters/ch13.md chapters/ch14.md chapters/ch15.md \
  chapters/ch16.md chapters/ch17.md chapters/ch18.md chapters/ch19.md \
  chapters/ch20.md chapters/ch21.md chapters/epilogue.md > MANUSCRIPT.md
```

Appendices, references, research-map, and figures are standalone; they are not concatenated.

## Verify

1. **File inventory** — expect: README.md, BOOK.md, BUILD.md, LICENSE, 23 chapter files, 13 appendix files, 2 reference files, 8 research-map files, 9 SVGs. No other files belong here.
2. **SVG well-formedness** — `python3 -c "import xml.dom.minidom,glob; [xml.dom.minidom.parse(f) for f in glob.glob('figures/*.svg')]; print('SVG OK')"`.
3. **Citation spot-check** — pick any `path:line` citation; confirm the file and line in the source working tree (`github.com/urmt/sgp_core_v2`, consulted read-only). Key verified lines are listed in `references/source-notes.md`.
4. **Checklist** — mission §19 (reproduced below) before any commit.

## Review checklist (mission §19)

- [x] Original theory faithfully represented (C1–C5 verbatim; both sentience wordings).
- [x] Historical definitions and revisions distinguished (App. A/B; Ch. 2).
- [x] Each rung follows from the previous question (Ch. 7→13 transitions).
- [x] Mathematical claims traceable (App. D; research-map 04).
- [x] Negatives fairly presented (Ch. 19; App. E; "not established ≠ disproved").
- [x] Entanglement/BEC/identical-particle physics accurate (Ch. 15–17; bibliography DOIs verified).
- [x] Electrons/protons never conflated (Ch. 17; fig7; checklist enforced).
- [x] Interpretations not presented as physics (labels; Ch. 13 four-way split).
- [x] Ambition distinguished from results (Ch. 20; App. H).
- [x] Readable without advanced training (App. I; worked examples).
- [x] Payoffs without overstatement (Ch. 14; Epilogue).
- [x] Appendices auditable (A–M complete).
- [x] Citations/links checked (source-notes; DOI verification noted).
- [ ] Only book-related files staged (verify at commit time).
- [ ] Source records unaltered (read-only discipline; verify `git status` in source tree shows no book-mission modifications).
- [ ] Destination has no unrelated files/secrets (verify staged list).
- [ ] Commit + push verified (or obstacle reported).
