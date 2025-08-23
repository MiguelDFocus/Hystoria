local_setup:
	@echo "Setting up local environment"
	./setup.sh

create_post:
	python post_generator.py

update_content:
	pelican content -s local_pelicanconf.py

run:
	pelican --listen -s local_pelicanconf.py