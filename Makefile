# Makefile
.PHONY: install pytest lint format test test-coverage build clean gendiff package-install package-uninstall record

# Установка для разработки (с тестами и линтерами)
install:
	uv pip install -e ".[dev]"

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
	uv run pytest --cov=hexlet_python_package --cov-report xml

# Очистка артефактов
clean:
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .coverage coverage.xml
	rm -rf .ruff_cache


check: test lint

# Запуск CLI (пример с тестовыми файлами)
gendiff:
	uv run gendiff tests/fixtures/file1.json tests/fixtures/file2.json

# Установка пакета через uv tool
package-install:
	uv tool install dist/*.whl

# Удаление пакета
package-uninstall:
	uv tool uninstall hexlet-code || true

# Запись демонстрации
record:
	asciinema rec recordings/gendiff.cast
