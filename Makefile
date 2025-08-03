# Установка проекта в режиме разработки
install:
	uv pip install -e .

# Линтинг кода
lint:
	uv run ruff check gendiff

# Форматирование кода
format:
	uv run ruff format --check gendiff

# Запуск тестов
test:
    uv run pytest tests -v

# Запуск тестов с измерением покрытия
test-coverage:
    uv run pytest --cov=gendiff --cov-report=xml tests

# Сборка пакета
build:
    uv build

# Запуск CLI утилиты
gendiff:
    uv run gendiff

# Установка собранного .whl пакета как инструмента
package-install:
    uv tool install dist/*.whl

# Удаление установленного .whl пакета как инструмента
package-uninstall:
    uv tool uninstall dist/*.whl

# Запись asciinema
record:
    asciinema rec gendiff.cast