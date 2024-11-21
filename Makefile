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
	rm -rf $(VENV) .pytest_cache/ .coverage

env:
	python -m venv $(VENV) && $(PIP) install pip-tools

setup: env
	$(PIP-SYNC) $(REQUIREMENTS-DEV)

compile-deps: env
	$(PIP-COMPILE) $(PYPROJECT) --extra=all -o $(REQUIREMENTS)	--verbose
	$(PIP-COMPILE) $(PYPROJECT) --extra=dev -o $(REQUIREMENTS-DEV)

static-analysis:
	$(MYPY) src/

lint:
	$(RUFF) check .

test:
	$(PYTEST) --verbose

install:
	$(PIP) install -e .

coverage:
	$(PYTEST) --cov=src/$(NAME) --cov-report=term-missing --cov-report html --verbose

