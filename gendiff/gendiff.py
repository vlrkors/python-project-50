import json


def read_file(filepath):
    with open(filepath, "r") as file:
        return file.read()


def parse_data(data_string, file_format="JSON"):
    """Парсим строку данных в словарь."""
    if file_format.upper() == "JSON":
        return json.loads(data_string)
    # Здесь можно добавить поддержку других форматов
    else:
        return json.loads(data_string)  # По умолчанию пробуем JSON


def build_diff_plain(data1, data2):
    """
    Сравниваем два плоских словаря и возвращает строку с различиями.
    Ключи выводятся в алфавитном порядке.
    """
    diff_lines = ["{"]
    all_keys = sorted(set(data1.keys()).union(set(data2.keys())))

    for key in all_keys:
        val1 = data1.get(key)
        val2 = data2.get(key)

        # Приводим boolean к lowercase
        if isinstance(val1, bool):
            val1 = str(val1).lower()
        if isinstance(val2, bool):
            val2 = str(val2).lower()

        if key not in data1:
            diff_lines.append(
                f"  + {key}: {
                    repr(val2).replace('True', 
                                       'true').replace('False', 'false')
                }"
            )
        elif key not in data2:
            diff_lines.append(
                f"  - {key}: {
                    repr(val1).replace('True', 
                                       'true').replace('False', 'false')
                }"
            )
        elif val1 != val2:
            diff_lines.append(
                f"  - {key}: {
                    repr(val1).replace('True', 
                                       'true').replace('False', 'false')
                }"
            )
            diff_lines.append(
                f"  + {key}: {
                    repr(val2).replace('True', 
                                       'true').replace('False', 'false')
                }"
            )
        else:
            diff_lines.append(
                f"    {key}: {
                    repr(val1).replace('True', 'true').replace('False', 'false')
                }"
            )

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
