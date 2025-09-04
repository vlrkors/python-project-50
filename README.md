### Вычислитель отличий (gendiff)
[![CI](https://github.com/vlrkors/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/vlrkors/python-project-50/actions)
[![Hexlet Autocheck](https://github.com/vlrkors/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/vlrkors/python-project-50/actions/workflows/hexlet-check.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/quality_gate?project=vlrkors_python-project-50)](https://sonarcloud.io/summary/new_code?id=vlrkors_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=vlrkors_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=vlrkors_python-project-50)

CLI‑утилита для сравнения двух файлов конфигурации и отображения различий. Поддерживаются форматы входных данных JSON и YAML/YML. Результат можно вывести в одном из трех форматов: `stylish` (по умолчанию), `plain`, `json`.

### Требования
- Python 3.12+
- Утилита `uv` (рекомендуется для изоляции и установки); при желании можно использовать стандартные `venv`/`pip`.

### Установка

Установить проект в editable‑режиме с dev‑зависимостями:
```bash
uv pip install -e '.[dev]'


Сборка wheel‑пакета:
```bash
uv build
```

### Использование (CLI)

```bash
gendiff <первый_файл> <второй_файл> [--format stylish|plain|json]
```

Пример:
```bash
gendiff gendiff/tests/test_data/file1.json gendiff/tests/test_data/file2.json
```

Вывод формата `stylish` (по умолчанию):
```
{
  - a: 1
  + a: 2
    b: {
        x: 1
      - y: 2
      + z: 3
    }
  - c: true
  - d: null
  + e: str
}
```

Справка:
```bash
gendiff --help
```

### Использование как библиотеки

```python
from gendiff import generate_diff

print(generate_diff('file1.json', 'file2.json', formatter='stylish'))
```

### Форматы вывода
- `stylish`: древовидное представление с пометками добавленных/удаленных/измененных ключей.
- `plain`: плоские текстовые сообщения «Property 'a.b' was updated…».
- `json`: сериализованная внутренняя структура diff в JSON.

### Поддерживаемые входные форматы
- JSON
- YAML/YML

### Команды разработки
Через `make`:
- `make install`: установка зависимостей (через `uv`) в локальное окружение.
- `make test`: запуск тестов (`pytest`).
- `make test-coverage`: тесты с покрытием (формирует `coverage.xml`).
- `make lint`: статический анализ (ruff) и проверка форматирования (black --check).
- `make format`: автоформатирование (ruff format, black).
- `make build`: сборка wheel‑пакета.

Эквиваленты на `uv` напрямую:
```bash
uv run pytest -v
uv run pytest --cov=gendiff --cov-report=term-missing --cov-report xml
uv run ruff check gendiff
uv run ruff format gendiff && uv run black gendiff
```

### Установка/удаление CLI как инструмента uv
```bash
make build
uv tool install dist/*.whl   # устанавливает скрипт `gendiff`
uv tool uninstall hexlet-code
```

### Аксинема
- gendiff/recordings/gendiff_stage**.cast, где ** - номер стадии проекта
# Запись демонстрации
	asciinema rec gendiff/recordings/gendiff_stage**.cast
