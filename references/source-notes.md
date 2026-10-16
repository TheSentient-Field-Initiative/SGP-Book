# Source Notes

How to read the book's citations. Companion to the bibliography.

## Citation form

Institute records are cited as `path:line` relative to the source repository root (`github.com/urmt/sgp_core_v2` — the Institute working tree, consulted read-only October 2026). Example: `SGP_RESPONSE_VS_RELATION_AUDIT_001.md:412` means line 412 of that file.

## Status of cited records

- **Git-tracked records** (governance, glossary, methodology, paper trees, docs/audits): first-appearance dates verified via `git log --diff-filter=A`. See research-map 02-chronology.
- **Unpublished working files** (most audits, RD-001…RD-004, experiment engines): carry internal date headers but no git history (untracked at time of consultation). Cited with file:line precision and internal dates. They are primary records of the Institute's work, not peer-reviewed publications. The book never calls them publications.
- **Manuscripts** (Paper 3 submission text; Paper 4 v3): LaTeX sources. Reported as manuscript claims with verification scope; internal audits (R64/R65) reported as internal audits; peer review outstanding.

## Lines verified directly by the book's author

GOVERNANCE.md:13–38; paper3 abstract (submission text :36–48); paper_v3 abstract/theorem/proof/examples/remark (:15–97); Exp24 header + :69, :96, :319, :363, :390, :408, :412; Exp25 §25–§26 (:440–475); RD-001 :340–369; sgp_physics_cases_01.py :5–9, :219–244. All other Institute citations were located by targeted search with surrounding context read; items known only via secondary audit tables are marked "cited via" in Appendix D.

## External sources

DOIs verified live for Bell 1964, Anderson 1995 (BEC), Davis 1995 (sodium BEC), Hensen 2015 (loophole-free Bell). Remaining references are canonical citations (EPR 1935, CHSH 1969, Aspect 1982, Bose 1924, Einstein 1924/25, Pauli 1940, standard textbooks, PDG); the book asserts their standard content, which is textbook-stable, and invites correction on details.

## What was NOT used

- The book does not reproduce private credentials, personal data, or development artifacts. No such material was encountered in the consulted records.
- The book does not copy datasets, engines, or result JSONs; it cites their reported outputs with file paths so a reader with repository access can check them.
- Where the records are silent (Exp03–Exp11 IDs; Phases XVIII–XXV; any electron=proton doctrine), the book says so rather than filling the gap.
