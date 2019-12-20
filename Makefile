PROJECT_NAME := "algopro"

.PHONY: dep
dep: ## Install dependencies
	# TODO get req.txt from Pipfile.lock && install all pkgs;

.PHONY: lint
lint: ## Lint modules
	@pipenv run pylint src tests;

.PHONY: test
test: ## Run unit_tests /w coverage
	@pipenv run pytest -v;

.PHONY: help
help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
