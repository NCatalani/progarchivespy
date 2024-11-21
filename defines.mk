NAME := "progarchivespy"
VENV ?= .env
BIN := $(VENV)/bin

PYTHON := $(BIN)/python
PIP := $(BIN)/pip
PIP-UPGRADE := $(BIN)/pip-upgrade
PIP-COMPILE := $(BIN)/pip-compile
PIP-SYNC := $(BIN)/pip-sync
PYTEST := $(BIN)/pytest
COVERAGE-LCOV := $(BIN)/coverage-lcov
MYPY := $(BIN)/mypy
RUFF := $(BIN)/ruff
ACTIVATE := $(BIN)/activate

PYPROJECT := pyproject.toml
REQUIREMENTS := requirements.txt
REQUIREMENTS-DEV := requirements-dev.txt
COVERAGE_FILE := .coverage
LCOV_FILE := lcov.info

define run_python
	@echo Activating virtual environment...
	@. $(ACTIVATE); \
	echo Running: $(PYTHON) $(1); \
	$(PYTHON) $(1)
endef
