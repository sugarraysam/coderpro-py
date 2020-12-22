TARGETS := "deps test help"
.PHONY: $(TARGETS)

export PIPENV_VENV_IN_PROJECT=1

deps:
	@pip3 install --user -U pipenv pip
	@pipenv install --dev

test:
	@pipenv run coverage run --include="./core/src/*" -m pytest -v ./core
	@pipenv run coverage report

help:
	@echo "make [ $(TARGETS) ]"
