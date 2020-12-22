TARGETS := "deps test help"
.PHONY: $(TARGETS)

SHELL := /bin/bash

export PIPENV_VENV_IN_PROJECT=1

deps:
	@[[ "$(CI)" == "1" ]] && pip3 install -U pipenv pip || pip3 install --user -U pipenv pip
	@pipenv install --dev

test:
	@pipenv run coverage run --include="./core/src/*" -m pytest -v ./core
	@pipenv run coverage report

help:
	@echo "make [ $(TARGETS) ]"
