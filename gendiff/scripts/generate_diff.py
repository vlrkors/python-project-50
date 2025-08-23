from gendiff.scripts.find_diff import find_diff
from gendiff.scripts.parser import parse_data_from_file


def _format_value(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return str(value)
    return str(value)


def _format_stylish(diff):
    lines = ["{"]
    for item in diff:
        action = item["action"]
        name = item["name"]
        if action == "added":
            lines.append(f"  + {name}: {_format_value(item['new_value'])}")
        elif action == "deleted":
            lines.append(f"  - {name}: {_format_value(item['old_value'])}")
        elif action == "unchanged":
            lines.append(f"    {name}: {_format_value(item['value'])}")
        elif action == "modified":
            lines.append(f"  - {name}: {_format_value(item['old_value'])}")
            lines.append(f"  + {name}: {_format_value(item['new_value'])}")
        elif action == "nested":
            # Базовая заглушка для вложенных структур
            lines.append(f"    {name}: {{...}}")
    lines.append("}")
    return "\n".join(lines)


def generate_diff(file_path1, file_path2, formatter="stylish"):
    # Чтение файлов и парсинг данных
    first_file = parse_data_from_file(file_path1)
    second_file = parse_data_from_file(file_path2)
    # Нахождение различий
    diff = find_diff(first_file, second_file)

    if formatter == "stylish":
        return _format_stylish(diff)

    raise ValueError(f"Unsupported formatter: {formatter}")
