# Makefile
.PHONY: install pytest lint format test test-coverage build clean gendiff package-install package-uninstall record

VENV := .venv
PY := $(VENV)/bin/python
PIP := $(VENV)/bin/pip
UVPIP := uv pip

$(VENV):
	uv venv $(VENV)

install: $(VENV)
	. $(VENV)/bin/activate && $(UVPIP) install -e ".[dev]"

build: 
	uv build

# Линтинг (ruff + проверка форматирования)
lint:
	uv run ruff check gendiff
	uv run black --check gendiff

# Автоформатирование кода
format:
	uv run ruff format gendiff
	uv run black gendiff

# Запуск тестов с подробным выводом
test:
	uv run pytest -v

# Покрытие кода с генерацией отчета
test-coverage:
	uv run pytest --cov=gendiff --cov-report=term-missing --cov-report xml

# Очистка артефактов
clean:
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .coverage coverage.xml
	rm -rf .ruff_cache


check: test lint

# Запуск CLI (пример с тестовыми файлами)
gendiff:
	uv run gendiff --format json gendiff/tests/test_data/file1.json gendiff/tests/test_data/file2.json
#	uv run gendiff --format plain gendiff/tests/test_data/file1.json gendiff/tests/test_data/file2.json
# 	uv run gendiff gendiff/tests/test_data/file1.json gendiff/tests/test_data/file2.json

# Установка пакета через uv tool
package-install:
	uv tool install dist/*.whl

# Удаление пакета
package-uninstall:
	uv tool uninstall hexlet-code || true

# Запись демонстрации
record:
	asciinema rec gendiff/recordings/gendiff.cast
