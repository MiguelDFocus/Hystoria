local_setup:
	@echo "Setting up local environment"
	./setup.sh

create_post:
	python post_generator.py