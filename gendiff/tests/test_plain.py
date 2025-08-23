"""Тесты для форматтера plain."""

from __future__ import annotations

from gendiff.formatters.plain import format_diff_plain, format_plain
from gendiff.scripts.find_diff import build_diff


def test_plain_outputs_expected_for_nested_changes():
    d1 = {
        "a": 1,
        "b": {"x": 1, "y": 2},
        "c": True,
        "d": None,
    }
    d2 = {
        "a": 2,  # changed
        "b": {"x": 1, "z": 3},  # nested: y removed, z added
        "e": "str",  # added
    }

    diff = build_diff(d1, d2)
    out = format_diff_plain(diff)

    expected = "\n".join(
        [
            "Property 'a' was updated. From 1 to 2",
            "Property 'b.y' was removed",
            "Property 'b.z' was added with value: 3",
            "Property 'c' was removed",
            "Property 'd' was removed",
            "Property 'e' was added with value: 'str'",
        ]
    )
    assert out == expected


def test_plain_formats_various_value_types():
    d1 = {
        "num": 1,
        "flag": True,
        "none": None,
        "obj": {"k": "v"},
        "arr": [1, 2, 3],
        "str": "hello",
    }
    d2 = {
        "num": 2,  # changed (number)
        "flag": False,  # changed (bool)
        # none removed
        # obj removed (complex value)
        # arr removed (complex value)
        "str": "world",  # changed (string)
        "added": {"x": 1},  # added (complex value)
    }

    diff = build_diff(d1, d2)
    out = format_plain(diff)

    expected_lines = [
        "Property 'added' was added with value: [complex value]",
        "Property 'arr' was removed",
        "Property 'flag' was updated. From true to false",
        "Property 'none' was removed",
        "Property 'num' was updated. From 1 to 2",
        "Property 'obj' was removed",
        "Property 'str' was updated. From 'hello' to 'world'",
    ]
    # Порядок строк должен соответствовать сортировке ключей
    assert out == "\n".join(expected_lines)
