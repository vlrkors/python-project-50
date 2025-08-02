import argparse
import json


def read_file(filepath):
    """
    Читает файл и возвращает его содержимое.
    Для этого проекта предполагаем, что файл всегда существует и читается успешно.
    """
    with open(filepath, 'r') as file:
        return file.read()


def parse_data(data_string, file_format):
    """
    Парсит строку данных в Python-словарь.
    На данном этапе поддерживается только JSON.
    """
    # В будущем здесь можно добавить определение формата по расширению файла
    # или содержимому, если file_format не предоставлен.
    if file_format.upper() == 'JSON':
        return json.loads(data_string)
    # Здесь можно добавить поддержку других форматов (YAML и т.д.)
    else:
        # По умолчанию пробуем JSON
        return json.loads(data_string)

def read_file(filepath):
    """
    Читает файл и возвращает его содержимое.
    Для этого проекта предполагаем, что файл всегда существует и читается успешно.
    """
    with open(filepath, 'r') as file:
        return file.read()


def parse_data(data_string, file_format):
    """
    Пока только только JSON.
    """
    # В будущем здесь можно добавить определение формата по расширению файла
    # или содержимому, если file_format не предоставлен.
    if file_format.upper() == 'JSON':
        return json.loads(data_string)
    # Здесь можно добавить поддержку других форматов (YAML и т.д.)
    else:
        # По умолчанию пробуем JSON
        return json.loads(data_string)


def generate_diff(first_data, second_data):
    """
    Сравнивает два словаря и возвращает различия.
    Пока это заглушка, которая просто возвращает входные данные.
    Реальная логика будет реализована позже.
    """
    diff = {
        'first_file_data': first_data,
        'second_file_data': second_data
    }
    return diff


def format_diff(diff, format_type):
    """
    Форматирует различия в заданный формат.
    Пока это заглушка.
    """
    if format_type == 'json':
        return json.dumps(diff, indent=2)
    else:  # 'stylish' or default
        result_lines = []
        result_lines.append("First file data:")
        for key, value in diff['first_file_data'].items():
            result_lines.append(f"  {key}: {value}")
        result_lines.append("Second file data:")
        for key, value in diff['second_file_data'].items():
            result_lines.append(f"  {key}: {value}")
        return '\n'.join(result_lines)


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )

    parser.add_argument('first_file', help='Path to the first file')
    parser.add_argument('second_file', help='Path to the second file')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish'
    )

    args = parser.parse_args()

    # Чтение файлов
    first_file_content = read_file(args.first_file)
    second_file_content = read_file(args.second_file)

    # Парсинг данных (предполагаем JSON для простоты)
    # Потом можно будет определять формат по расширению файла
    first_data = parse_data(first_file_content, 'JSON')
    second_data = parse_data(second_file_content, 'JSON')

    # Генерация различий
    diff = generate_diff(first_data, second_data)

    # Форматирование и вывод
    result = format_diff(diff, args.format)
    print(result)


if __name__ == '__main__':
    main()
    )
    
    args = parser.parse_args()
    # Пока просто заглушка - логика сравнения - потом
    print(f"Comparing {args.first_file} and {args.second_file}")
    print(f"Format: {args.format}")


if __name__ == '__main__':
    main()