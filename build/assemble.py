#!/usr/bin/env python3
"""Assemble the single-file manuscript source from chapters/appendices.

Reads the ordered chapter files, appends figure inclusions at the mapped
positions, and writes build/manuscript.md for pandoc.
"""
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAPTERS = [
    "chapters/prologue.md",
    "chapters/ch01.md", "chapters/ch02.md", "chapters/ch03.md",
    "chapters/ch04.md", "chapters/ch05.md", "chapters/ch06.md",
    "chapters/ch07.md", "chapters/ch08.md", "chapters/ch09.md",
    "chapters/ch10.md", "chapters/ch11.md", "chapters/ch12.md",
    "chapters/ch13.md", "chapters/ch14.md", "chapters/ch15.md",
    "chapters/ch16.md", "chapters/ch17.md", "chapters/ch18.md",
    "chapters/ch19.md", "chapters/ch20.md", "chapters/ch21.md",
    "chapters/epilogue.md",
]
APPENDICES = [f"appendices/{n}.md" for n in
              ["A-vocabulary", "B-provenance", "C-ladder", "D-theorems",
               "E-negatives", "F-physics", "G-chronology", "H-closure",
               "I-glossary", "J-bibliography", "K-reproducibility",
               "L-open-questions", "M-evidence-key"]]
# chapter file -> (figure pdf, caption)
FIGURES = {
    "chapters/ch03.md": ("figures/fig1-sequence.pdf",
        "The raw SGP conceptual sequence (illustration; dashed = unresolved transition)"),
    "chapters/ch06.md": ("figures/fig2-possibility-actualization.pdf",
        "Possibility is cheap; actuality needs a selector (illustration)"),
    "chapters/ch09.md": ("figures/fig4-relation-closure.pdf",
        "Many wirings, one consequence-structure (illustration; schematic)"),
    "chapters/ch14.md": ("figures/fig3-ladder.pdf",
        "The ladder: question per rung, status per audit (illustration)"),
    "chapters/ch15.md": ("figures/fig5-entanglement.pdf",
        "Correlated outcomes, no message (illustration)"),
    "chapters/ch16.md": ("figures/fig6-bec.pdf",
        "One rung crowded, the rest thin (illustration; not to scale)"),
    "chapters/ch17.md": ("figures/fig7-particles.pdf",
        "Indistinguishability stops at the species boundary (illustration)"),
    "chapters/ch19.md": ("figures/fig8-timeline.pdf",
        "From first formulations to portfolio decision (illustration)"),
    "chapters/epilogue.md": ("figures/fig9-synthesis.pdf",
        "What the program leaves behind (illustration)"),
}


def main():
    out = []
    for rel in CHAPTERS + APPENDICES:
        text = (ROOT / rel).read_text(encoding="utf-8").rstrip() + "\n"
        out.append(text)
        if rel in FIGURES:
            path, cap = FIGURES[rel]
            out.append(f"\n![{cap}]({path}){{width=100%}}\n")
    build = ROOT / "build"
    build.mkdir(exist_ok=True)
    (build / "manuscript.md").write_text("\n\\newpage\n".join(out), encoding="utf-8")
    print(f"assembled {len(CHAPTERS) + len(APPENDICES)} files -> build/manuscript.md")


if __name__ == "__main__":
    main()
