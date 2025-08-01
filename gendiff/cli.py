"""Точка входа для CLI утилиты gendiff."""

import argparse

from gendiff.gendiff import generate_diff


def main():
    """Главная функция CLI."""
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file", help="Path to the first file")
    parser.add_argument("second_file", help="Path to the second file")
    parser.add_argument(
        "-f", "--format", help="set format of output", default="stylish"
    )

    args = parser.parse_args()

    # Вызов основной функции сравнения
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == "__main__":
    main()
