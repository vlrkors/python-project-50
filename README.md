### Вычислитель отличий (gendiff)
[![CI](https://github.com/vlrkors/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/vlrkors/python-project-50/actions)
[![Hexlet Autocheck](https://github.com/vlrkors/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/vlrkors/python-project-50/actions/workflows/hexlet-check.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/quality_gate?project=vlrkors_python-project-50)](https://sonarcloud.io/summary/new_code?id=vlrkors_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=vlrkors_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=vlrkors_python-project-50)

CLI‑утилита для сравнения двух файлов конфигурации и отображения различий. Поддерживаются форматы входных данных JSON и YAML/YML. Результат можно вывести в одном из трех форматов: `stylish` (по умолчанию), `plain`, `json`.

### Требования
- Python 3.12+
- Утилита `uv`

### Установка
 - git clone git@github.com:vlrkors/python-project-50.git
 - cd python-project-50
 - uv build
 - uv tool install dist/*.whl


Сборка wheel‑пакета:
```bash
uv build
```

### Использование (CLI)

```bash
gendiff <первый_файл> <второй_файл> [--format stylish|plain|json]
```

### Пример вывода инструмента при использовании разных форматтеров

Default (stylish) formatter:
uv run gendiff tests/test_data/<file1> tests/test_data/<file1>
Using the JSON formatter:
uv run gendiff -f stylish tests/test_data/<file1> tests/test_data/<file1>
Using the Plain formatter:
uv run gendiff -f plain tests/test_data/<file1> tests/test_data/<file1>


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
- https://asciinema.org/a/DI3fQ45lId0Y4kNKPBt4T2wfT - запись работы команды gendiff --h
- https://asciinema.org/a/8WcX5bf0pP9Xl75jFipe9qlcH - запись работы команды gendiff tests/test_data/file1.json tests/test_data/file2.json
- https://asciinema.org/a/7vaMZjKBt6Vh1hizKldNf14Mm - запись работы команды gendiff tests/test_data/file1.yml tests/test_data/file2.yml
- https://asciinema.org/a/ODlG6o4fBBlfllKULxU8ydbkj - запись работы команды gendiff tests/test_data/filepath1.json tests/test_data/filepath2.json
- https://asciinema.org/a/NCNEynYss770hBmNKuSWoA5KB - запись работы команды gendiff --format plain tests/test_data/filepath1.json tests/test_data/filepath2.json
- https://asciinema.org/a/ps7er3pN1Qzzws1Y5A3Behgk5 - запись работы команды gendiff --format json tests/test_data/filepath1.json tests/test_data/filepath2.json
