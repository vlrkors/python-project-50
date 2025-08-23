"""Тесты для модуля find_diff."""

from __future__ import annotations

from gendiff.scripts.find_diff import find_diff


def test_find_diff_flat_and_nested():
    data1 = {
        "a": 1,
        "b": 2,
        "nested": {"x": 1},
        "same": 10,
    }
    data2 = {
        "a": 1,  # unchanged
        "b": 3,  # modified
        "nested": {"x": 1, "y": 2},  # nested
        "added": True,  # added
        "same": 10,  # unchanged
    }

    diff = find_diff(data1, data2)

    # Ожидаемый список отсортирован по имени ключа
    expected = [
        {"action": "unchanged", "name": "a", "value": 1},
        {"action": "added", "name": "added", "new_value": True},
        {
            "action": "modified",
            "name": "b",
            "old_value": 2,
            "new_value": 3,
        },
        {
            "action": "nested",
            "name": "nested",
            "children": [
                {"action": "unchanged", "name": "x", "value": 1},
                {"action": "added", "name": "y", "new_value": 2},
            ],
        },
        {"action": "unchanged", "name": "same", "value": 10},
    ]

    assert diff == expected

