#!/usr/bin/env python3

import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.'
    )
    
    parser.add_argument('first_file', help='')
    parser.add_argument('second_file', help='')
    parser.add_argument(
        '-f', '--format',
        help='set format of output',
        default='stylish'
    )
    
    args = parser.parse_args()
    # Пока просто заглушка - логика сравнения - потом
    print(f"Comparing {args.first_file} and {args.second_file}")
    print(f"Format: {args.format}")


if __name__ == '__main__':
    main()