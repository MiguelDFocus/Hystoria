local_setup:
	@echo "Setting up local environment"
	./setup.sh

create_post:
	python post_generator.py

update_content:
	pelican content -s local_pelicanconf.py

run:
	pelican --listen -s local_pelicanconf.py

# Production commands
.PHONY: install generate build serve clean

PYTHON=python3

install:
	$(PYTHON) -m pip install -U pip
	$(PYTHON) -m pip install -r requirements.txt

# Generates a new weekly post into content/
generate:
	$(PYTHON) post_generator.py

# Build static site into ./output using Pelican
build:
	pelican content -o output -s pelicanconf.py

# Quick local preview: http://localhost:8000
serve:
	pelican --listen --autoreload -s pelicanconf.py

clean:
	rm -rf output