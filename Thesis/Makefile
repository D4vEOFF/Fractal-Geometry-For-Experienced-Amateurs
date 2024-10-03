FILE=diploma-thesis

all: pdf clean

pdf:
	"pdflatex.exe" $(FILE).tex
	"pdflatex.exe" $(FILE).tex
	"bibtex.exe" $(FILE)
	"pdflatex.exe" $(FILE).tex

clean:
	for /r %%i in (*.aux *.log *.bbl *.blg *.toc *.lof *.lot *.out *.gz) do del "%%i"