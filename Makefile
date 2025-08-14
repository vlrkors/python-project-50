# Установка проекта в editable-режиме (разработка)
install:
	uv pip install -e .

# Линтинг кода (ruff)
lint:
    uv run ruff check gendiff/ tests/

# Форматирование кода (ruff, только проверка)
format:
	uv run ruff format --check gendiff

# Запуск тестов
test:
    uv run pytest tests/ -v

# Запуск тестов с измерением покрытия
test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml tests

# Сборка wheel-пакета
build:
	uv build

# Запуск CLI утилиты
gendiff:
	uv run gendiff

# Установка wheel-пакета как инструмента (uv tool)
package-install:
	uv tool install dist/*.whl

# Удаление wheel-пакета как инструмента (uv tool)
package-uninstall:
	uv tool uninstall dist/*.whl

# Запись asciinema-сессии
record:
	asciinema rec gendiff.cast

