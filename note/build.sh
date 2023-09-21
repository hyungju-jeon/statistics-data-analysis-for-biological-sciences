#!/bin/sh

# compiles the LaTeX source to produce output PDF using latexmk
# it tags the PDF with the current git version tag



VER=$(git describe --tags --dirty)
echo $VER

# Loop through files matching the format lecture**_note.tex
for FILE in lecture[0-9][0-9]_note.tex; do
    TARGET="${FILE%.tex}"  # Remove the .tex extension
    echo "Compiling $TARGET"
    latexmk -pdf $TARGET
    mv $TARGET.pdf $TARGET-${VER}.pdf
done