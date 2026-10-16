#!/usr/bin/env bash
# Build the single-file LaTeX manuscript and the compiled PDF.
# Requirements: python3, pandoc, xelatex, rsvg-convert (figures already
# converted to figures/*.pdf and committed).
set -euo pipefail
cd "$(dirname "$0")/.."

python3 build/assemble.py

pandoc build/manuscript.md \
  --standalone --top-level-division=chapter \
  --metadata title="The Sentience Question" \
  --metadata subtitle="From the Foundations of SGP to the Mathematics of Reality" \
  --metadata author="TheSentient-Field-Initiative" \
  --metadata date="October 2026 (draft for review)" \
  -V documentclass=book -V fontsize=11pt -V geometry:margin=1in \
  -V mainfont="TeX Gyre Termes" \
  -V mathfont="TeX Gyre DejaVu Math" \
  -H build/preamble.tex \
  --toc -o manuscript.tex

xelatex -interaction=nonstopmode manuscript.tex
xelatex -interaction=nonstopmode manuscript.tex
echo "BUILD OK: manuscript.tex + manuscript.pdf"
