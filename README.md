### Статус
[![CI](https://github.com/vlrkors/python-project-50/actions/workflows/ci.yml/badge.svg)](https://github.com/vlrkors/python-project-50/actions)
[![Hexlet Autocheck](https://github.com/vlrkors/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/vlrkors/python-project-50/actions/workflows/hexlet-check.yml)
[![Quality Gate](https://sonarcloud.io/api/project_badges/quality_gate?project=vlrkors_python-project-50)](https://sonarcloud.io/summary/new_code?id=vlrkors_python-project-50)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=vlrkors_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=vlrkors_python-project-50)

## Генератор различий (gendiff)

CLI‑утилита и библиотека для сравнения двух конфигурационных файлов и вывода различий в удобочитаемом виде.

Поддерживаемые форматы входных данных: JSON и YAML/YML. Формат вывода по умолчанию — `stylish`.

### Требования
- Python 3.12+
- Рекомендуется менеджер `uv` (или используйте системный `pip`/`venv`).

### Установка

Установить в режиме разработки из исходников:
```bash
uv pip install -e '.[dev]'
# либо
python -m venv .venv && . .venv/bin/activate
pip install -e '.[dev]'
```

Сборка wheel‑пакета:
```bash
uv build
```

### Использование (CLI)

```bash
gendiff <первый_файл> <второй_файл> [--format stylish]
```

Пример:
```bash
gendiff gendiff/tests/test_data/file1.json gendiff/tests/test_data/file2.json
```

Пример вывода (`stylish`):
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

Подсказка по параметрам:
```bash
gendiff --help
```

### Использование как библиотеки

```python
from gendiff import generate_diff

print(generate_diff('file1.json', 'file2.json', formatter='stylish'))
```

### Разработка

Команды с `make`:
- `make install` — создание виртуального окружения и установка зависимостей.
- `make test` — запуск тестов.
- `make test-coverage` — тесты с покрытием, отчёт `coverage.xml`.
- `make lint` — проверка стиля (ruff, black --check).
- `make format` — автоформатирование (ruff format, black).

Те же действия напрямую через `uv`:
```bash
uv run pytest -v
uv run pytest --cov=gendiff --cov-report=term-missing --cov-report xml
uv run ruff check gendiff
uv run ruff format gendiff && uv run black gendiff
```

### Детали реализации
- Парсинг: строгий JSON; при ошибке парсинга JSON допускается резервный разбор как YAML для «нестрогих» входов (например, ключи без кавычек).
- Вывод `stylish`: древовидный вид с пометками добавленных/удалённых/изменённых/неизменённых значений.

### Планы
- Расширение поддерживаемых форматов вывода (plain, json).
