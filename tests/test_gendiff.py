"""Тесты для модуля gendiff."""

import os
from gendiff import generate_diff

# Определяем путь к директории с фикстурами относительно местоположения этого файла тестов
FIXTURES_PATH = os.path.join(os.path.dirname(__file__), 'fixtures')


def get_fixture_path(filename: str) -> str:
    """Возвращает полный путь к файлу фикстуры."""
    return os.path.join(FIXTURES_PATH, filename)


def read_fixture(filename: str) -> str:
    """Читает содержимое файла фикстуры."""
    with open(get_fixture_path(filename), 'r') as f:
        return f.read()


def test_generate_diff():
    """Тест сравнения плоских JSON файлов."""
    # Пути к тестовым файлам
    file1_path = get_fixture_path('file1.json')
    file2_path = get_fixture_path('file2.json')
    
    # Ожидаемый результат
    expected_result = read_fixture('result_stylish.txt')
    
    # Получаем фактический результат
    actual_result = generate_diff(file1_path, file2_path)
    
    # Сравниваем
    assert actual_result == expected_result

# Добавьте больше тестов для других сценариев:
# - Файлы идентичны
# - Один файл пустой
# - Ключи есть только в первом файле
# - Ключи есть только во втором файле
# - Вложенные структуры (когда они будут реализованы)