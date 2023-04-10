#!/bin/bash
PELICAN?=pelican
PELICANOPTS=

BASEDIR=$(PWD)
INPUTDIR=$(BASEDIR)/content
OUTPUTDIR=$(BASEDIR)/output
OLD_CONTENT=$(BASEDIR)/old_content
CONFFILE=$(BASEDIR)/pelicanconf.py
PUBLISHCONF=$(BASEDIR)/publishconf.py

help:
	@echo 'Makefile for a pelican Web site                                        '
	@echo '                                                                       '
	@echo 'Usage:                                                                 '
	@echo '   make html                        (re)generate the web site          '
	@echo '   make clean                       remove the generated files         '
	@echo '   make publish                     generate using production settings '
	@echo '   make devserver                   start/restart develop_server.sh    '
	@echo '                                                                       '


html: pre1 clean index.html post1
	@echo 'Done'

pre1:
	mv "$(OUTPUTDIR)/README.md" "$(BASEDIR)/README_bkp.md"

post1:
	mv "$(BASEDIR)/README_bkp.md" "$(OUTPUTDIR)/README.md"

index.html:
	cp -r "$(OLD_CONTENT)" "$(OUTPUTDIR)/"
	poetry run $(PELICAN) -o "$(OUTPUTDIR)" -s "$(CONFFILE)" $(PELICANOPTS) "$(INPUTDIR)"
	rm -r "$(OUTPUTDIR)/category" "$(OUTPUTDIR)/author"

clean:
	find "$(OUTPUTDIR)" -mindepth 1 -delete

devserver:
	"$(BASEDIR)/develop_server.sh"

publish:
	poetry run $(PELICAN) "$(INPUTDIR)" --output "$(OUTPUTDIR)" --settings "$(PUBLISHCONF)" $(PELICANOPTS)

.PHONY: html help clean serve devserver publish
