from gendiff.formatters.plain import format_plain
from gendiff.formatters.stylish import format_stylish
from gendiff.scripts.find_diff import build_diff
from gendiff.scripts.parser import parse_data_from_file


def generate_diff(file_path1, file_path2, formatter="stylish"):
    # Чтение файлов и парсинг данных
    first_file = parse_data_from_file(file_path1)
    second_file = parse_data_from_file(file_path2)
    # Нахождение различий
    diff = build_diff(first_file, second_file)

    if formatter == "stylish":
        return format_stylish(diff)
    elif formatter == "plain":
        return format_plain(diff)

    raise ValueError(f"Unsupported formatter: {formatter}")
