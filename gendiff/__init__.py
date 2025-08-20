"""Пакет для сравнения конфигурационных файлов."""

from gendiff.gendiff import generate_diff

# gendiff/__init__.py
from .parsers.json_parser import parse_json
from .parsers.yaml_parser import parse_yaml

FORMATS = {
    'json': parse_json,
    'yml': parse_yaml,
    'yaml': parse_yaml,
}

__all__ = ["generate_diff"]
__version__ = "0.1.1"

