import json


def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read()


def parse_data(data_string, file_format="JSON"):
    """Парсим строку данных в словарь."""
    if file_format.upper() == 'JSON':
        return json.loads(data_string)
    # Здесь можно добавить поддержку других форматов
    else:
        return json.loads(data_string) # По умолчанию пробуем JSON


def build_diff_plain(data1, data2):
    """
    Сравниваем два плоских словаря и возвращает строку с различиями.
    Ключи выводятся в алфавитном порядке.
    """
    diff_lines = ["{"]
    
    # Получаем все ключи из обоих словарей и сортируем их
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))

    for key in all_keys:
        if key not in data1:
            # Ключ есть только во втором файле
            diff_lines.append(f"  + {key}: {repr(data2[key])}")
        elif key not in data2:
            # Ключ есть только в первом файле
            diff_lines.append(f"  - {key}: {repr(data1[key])}")
        elif data1[key] != data2[key]:
            # Ключ есть в обоих, но значения различаются
            diff_lines.append(f"  - {key}: {repr(data1[key])}")
            diff_lines.append(f"  + {key}: {repr(data2[key])}")
        else:
            # Ключ есть в обоих и значения совпадают
            diff_lines.append(f"    {key}: {repr(data1[key])}")

    diff_lines.append("}")
    return "\n".join(diff_lines)


def generate_diff(file_path1, file_path2):
    """
    Сравниваем два конфигурационных файла и возвращаем строку с различиями.
    
    Args:
        file_path1 (str): Путь к первому файлу.
        file_path2 (str): Путь ко второму файлу.
        
    Returns:
        str: Строка с различиями в формате stylish.
    """
    # Чтение файлов
    content1 = read_file(file_path1)
    content2 = read_file(file_path2)

    # Парсинг данных
    data1 = parse_data(content1)
    data2 = parse_data(content2)

    # Генерация различий
    diff_result = build_diff_plain(data1, data2)
    
    return diff_result
