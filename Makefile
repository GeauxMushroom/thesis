FILE = thesis
BIBS = general.bib
DEFAULTBIB = karming.bib
REFDIR = ~/apssamp/references

default: pdf1

bib:
	touch $(BIBS)
	rm $(BIBS)
	find $(REFDIR) -name "*bib" -exec cat {} >> $(BIBS) \;
	cat ${DEFAULTBIB} >> $(BIBS)

pdf1: $(FILE).tex
	pdflatex $(FILE)
	bibtex $(FILE)
	pdflatex $(FILE)
	pdflatex $(FILE)

dvi2: $(FILE).tex
	latex $(FILE)
	bibtex $(FILE)
	latex $(FILE)
	latex $(FILE)

pdf2: dvi2
	dvipdf -p letter $(FILE).dvi $(FILE).pdf
	rm $(FILE)*dvi $(FILE)*pdf $(FILE)*log $(FILE)*aux $(FILE)*spl $(FILE)*blg $(FILE)*bbl $(FILE)*toc	

pdf3: $(FILE).tex
	pdflatex $(FILE).tex

clean:
	rm $(FILE)*dvi $(FILE)*pdf $(FILE)*log $(FILE)*aux $(FILE)*spl $(FILE)*blg $(FILE)*bbl $(FILE)*toc


