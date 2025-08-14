# Makefile
.PHONY: install lint format test test-coverage build clean gendiff package-install package-uninstall record

# Установка в editable-режиме с dev-зависимостями
install:
	uv pip install -e ".[dev]"

# Линтинг (ruff + проверка форматирования)
lint:
	uv run ruff check gendiff/ tests/
	uv run black --check gendiff/ tests/

# Автоформатирование кода
format:
	uv run ruff format gendiff/ tests/
	uv run black gendiff/ tests/

# Запуск тестов с подробным выводом
test:
	uv run pytest tests/ -v

# Покрытие кода с генерацией отчета
test-coverage:
	uv run pytest --cov=gendiff --cov-report=term-missing --cov-report=xml tests/

# Сборка пакета (wheel и sdist)
build:
	uv run python -m build

# Очистка артефактов
clean:
	rm -rf dist/
	rm -rf build/
	rm -rf *.egg-info
	rm -rf .coverage coverage.xml
	rm -rf .ruff_cache

# Запуск CLI (пример с тестовыми файлами)
gendiff:
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

# Установка пакета через uv tool
package-install: build
	uv tool install dist/*.whl

# Удаление пакета
package-uninstall:
	uv tool uninstall hexlet-code || true

# Запись демонстрации
record:
	asciinema rec recordings/gendiff.cast