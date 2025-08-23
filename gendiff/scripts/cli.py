"""Точка входа для CLI утилиты gendiff."""

import argparse

from gendiff.scripts.generate_diff import generate_diff


def main():
    """Главная функция CLI."""
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )

    parser.add_argument("first_file", help="Path to the first file")
    parser.add_argument("second_file", help="Path to the second file")
    parser.add_argument(
        "-f",
        "--format",
        default="stylish",
        choices=["stylish", "plain"],
        help="Output format (default: stylish)",
    )

    args = parser.parse_args()

    # Вызов основной функции сравнения
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
