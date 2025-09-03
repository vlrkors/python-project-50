"""Тесты для JSON-форматтера."""

import json

from gendiff.formatters.json_formatter import format_diff_json
from gendiff.scripts.find_diff import build_diff


def test_format_diff_json_roundtrip():
    d1 = {"a": 1, "b": {"x": 1}, "c": True, "d": None}
    d2 = {"a": 2, "b": {"x": 1, "y": 2}, "e": "str"}

    diff = build_diff(d1, d2)
    out = format_diff_json(diff)

    # Парсим обратно и сверяем структуру
    parsed = json.loads(out)
    assert parsed == diff


def test_format_diff_json_is_pretty_indented():
    d1 = {"k": 1}
    d2 = {"k": 2}
    diff = build_diff(d1, d2)
    out = format_diff_json(diff)

    assert "\n" in out
    assert "    " in out  # 4 пробела

