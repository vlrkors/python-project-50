### Hexlet tests and linter status:
[![Actions Status](https://github.com/vlrkors/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/vlrkors/python-project-50/actions)

<!-- [![Coverage](https://sonarcloud.io/api/project_badges/measure?project=python-project-50&metric=coverage)](https://sonarcloud.io/project/overview?id=vlrkors_python-project-50) -->

[![sonar-quality-gate](https://sonarcloud.io/api/project_badges/measure?project=vlrkors_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=vlrkors_python-project-50)

## Проект: ВЫЧИСЛИТЕЛЬ ОТЛИЧИЙ

Gendiff позволяет сравнивать два JSON-файла (и в будущем другие форматы) и показывать различия между ними в читаемом формате. Инструмент можно использовать как из командной строки, так и как библиотеку в Python-скриптах.

### Сборка и тестирование

**Соберите пакет:**
    ```bash
    uv build
    ```
**Установите пакет в режиме разработки (если еще не установлено):**
    ```bash
    uv pip install -e .
    ```
**Тест CLI**
    ```bash
    uv run gendiff data/file1.json data/file2.json
    ```
    Должно вывести:
    ```
    {
        follow: false
        host: 'hexlet.io'
      - proxy: '123.234.53.22'
      - timeout: 50
      + timeout: 20
      + verbose: true
    }
    ```
**Тест библиотеки**
    Создайте тестовый файл: test_lib.py, а в нем:
    ```
    from gendiff import generate_diff

    diff = generate_diff('data/file1.json', 'data/file2.json')
    print(diff)
    ```
    Запустите его:
    ```bash
    uv run python test_lib.py
    ```

    Результат должен быть таким же, как и при вызове CLI.