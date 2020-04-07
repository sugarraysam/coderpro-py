export PIPENV_VENV_IN_PROJECT=1

.PHONY: deps
deps: ## Install dependencies
	@pip3 install --user -U pipenv pip
	@if [ ! -d "$(PWD)/.venv" ]; then \
		pipenv install --dev; \
	else \
		pipenv update && pipenv clean; \
	fi

.PHONY: lint
lint: ## Lint modules
	@pipenv run flake8 --exclude=.venv/ --statistics --show-source --max-line-length=80 .
	@pipenv run pylint src tests

.PHONY: test
test: ## Run unit_tests /w coverage
	@pipenv run coverage run --include="src/*" -m pytest -v
	@pipenv run coverage report

.PHONY: help
help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
