TEXCOMPILER = pdflatex
BIBCOMPILER = bibtex

DOCNAME = diploma_thesis

.PHONY: all compile clean compile-no-bibtex

all: compile clean

all-no-bibtex: compile-no-bibtex clean

compile: ${DOCNAME}.tex
	${TEXCOMPILER} ${DOCNAME}.tex
	${BIBCOMPILER} ./components/literature/literature
	${TEXCOMPILER} ${DOCNAME}.tex
	${TEXCOMPILER} ${DOCNAME}.tex

compile-no-bibtex:
	${TEXCOMPILER} ${DOCNAME}.tex
	${TEXCOMPILER} ${DOCNAME}.tex

clean:
	find . -type f -name '*.(aux|dvi|aux|toc|lof|lot|out|bbl|blg|xmpi|synctex.gz)' -delete