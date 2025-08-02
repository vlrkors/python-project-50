install:
    uv pip install -e .

lint:
    uv run ruff check gendiff
    uv run ruff format --check gendiff

format:
    uv run ruff format gendiff

test:
    uv run pytest tests -v

test-coverage:
    uv run pytest --cov=gendiff --cov-report=xml tests

.PHONY: install lint format test test-coverage

install:
	uv sync

install_project:
	uv pip install -e 

build: 
	uv build

gendiff:
	uv run gendiff

package-install:
	uv tool install dist/*.whl

package-uninstall:
	uv tool uninstall dist/*.whl

uninstall:
	uv tool uninstall .

record:
	asciinema rec gendiff.cast