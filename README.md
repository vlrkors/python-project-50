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
 - asciinema rec gendiff.cast

### Результат записи
{"version": 2, "width": 168, "height": 26, "timestamp": 1756900102, "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"}}
[0.012353, "o", "\u001b[?2004h\u001b]0;vlrkors@DRG-124: ~/python-project-50\u0007\u001b[01;32mvlrkors@DRG-124\u001b[00m:\u001b[01;34m~/python-project-50\u001b[00m$ "]
[1.330241, "o", "gendiff gendiff/tests/test_data/file1.json gendiff/tests/test_data/file2.json"]
[4.22002, "o", "\r\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C-h\u001b[K"]
[6.008984, "o", "\b\b\b\b\b\b\b\b\b\b\u001b[4Pcode ."]
[6.36232, "o", "\b\b\b\b\bd ./python-project-50"]
[6.879842, "o", "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\u001b[7Pping github.com"]
[7.311783, "o", "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\bgit remote set-url origin git@github.com:vlrkors/python-project-50.git"]
[8.129856, "o", "\r\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[Cping github.com\u001b[K"]
[8.737676, "o", "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\bcd ./python-project-50"]
[9.243599, "o", "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\bode .\u001b[K"]
[9.274144, "o", "\b\b\b\b\b\bgendiff -h"]
[9.306314, "o", "\b\bgendiff/tests/test_data/file1.json gendiff/tests/test_data/file2.json"]
[9.336138, "o", "\r\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[K"]
[9.38298, "o", "\u0007"]
[9.414598, "o", "\u0007"]
[10.988191, "o", "\u001b[7mgendiff gendiff/tests/test_data/file1.yml gendiff/tests/test_data/file2.yml\u001b[27m"]
[12.156205, "o", "\r\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[C\u001b[Cgendiff gendiff/tests/test_data/file1.yml gendiff/tests/test_data/file2.yml\r\n\u001b[?2004l\r"]
[12.177197, "o", "{\r\n  - follow: false\r\n    host: hexlet.io\r\n  - proxy: 123.234.53.22\r\n  - timeout: 50\r\n  + timeout: 20\r\n  + verbose: true\r\n}\r\n"]
[12.180572, "o", "\u001b[?2004h\u001b]0;vlrkors@DRG-124: ~/python-project-50\u0007\u001b[01;32mvlrkors@DRG-124\u001b[00m:\u001b[01;34m~/python-project-50\u001b[00m$ "]
[15.920788, "o", "\u001b[?2004l\r\r\nexit\r\n"]

