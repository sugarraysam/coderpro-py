PROJECT_NAME := "algopro"

.PHONY: deps
deps: ## Install dependencies
	@./maketools/algopro.sh deps;

.PHONY: lint
lint: ## Lint modules
	@./maketools/algopro.sh lint;

.PHONY: test
test: ## Run unit_tests /w coverage
	@./maketools/algopro.sh test;

.PHONY: help
help: ## Display this help screen
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
