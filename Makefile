include defines.mk

all:
	@echo "Usage: make <target>"
	@echo "Targets:"
	@echo "  setup: Sync dependencies"
	@echo "  compile-deps: Compile dependencies"
	@echo "  test: Run tests"
	@echo "  coverage: Run tests with coverage"
	@echo "  clean: Remove virtualenv and cache files"

clean:
	rm -rf $(VENV) .pytest_cache/ .coverage dist/ build/ .ruff_cache/ $(LCOV_FILE) $(COVERAGE_FILE)

env:
	python -m venv $(VENV) && $(PIP) install poetry==2.1.1

setup: env
	. "$(VENV)/bin/activate" && $(POETRY) sync --with dev

lock: env
	$(POETRY) lock

static-analysis:
	$(MYPY) src/

lint:
	$(RUFF) check .

install: setup
	$(POETRY) install

coverage:
	$(PYTEST) --cov=src/$(NAME) --cov-report=term-missing --cov-report=xml --verbose

coverage-lcov: coverage
	$(COVERAGE-LCOV) --data_file_path $(COVERAGE_FILE) --output_file_path $(LCOV_FILE)

