# Variables
PYTHON = python3
PELICANCONF = pelicanconf.py
OUTPUTDIR = output

# Default pelican build
PELICAN = pelican
PELICANOPTS =

# Targets
.PHONY: install generate build serve clean preview

install:
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -r requirements.txt

# Generates a new weekly post into content/
generate:
	$(PYTHON) post_generator.py

# Build static site into ./output using Pelican
build:
	$(PELICAN) content -o $(OUTPUTDIR) -s $(PELICANCONF) $(PELICANOPTS)

# Quick local preview: http://localhost:8000
serve: build
	cd $(OUTPUTDIR) && python3 -m http.server 8000

# Clean output dir
clean:
	rm -rf $(OUTPUTDIR)

# Shortcut: build + serve (dev mode)
preview: clean build serve
