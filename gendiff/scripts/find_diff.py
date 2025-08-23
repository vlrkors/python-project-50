def item_add(key, value):
    return {"action": "added", "name": key, "new_value": value}


def item_delete(key, value):
    return {"action": "deleted", "name": key, "old_value": value}


def items_unchanged(key, value):
    return {"action": "unchanged", "name": key, "value": value}


def items_modified(key, value1, value2):
    return {
        "action": "modified",
        "name": key,
        "new_value": value2,
        "old_value": value1,
    }


def items_nested(key, value1, value2):
    return {
        "action": "nested",
        "name": key,
        "children": find_diff(value1, value2),
    }


def find_diff(data1, data2):
    keys_union = data1.keys() | data2.keys()
    keys_added = data2.keys() - data1.keys()
    keys_deleted = data1.keys() - data2.keys()

    diff = []

    for key in keys_union:
        value1 = data1.get(key)
        value2 = data2.get(key)

        if key in keys_added:
            diff.append(item_add(key, value2))
        elif key in keys_deleted:
            diff.append(item_delete(key, value1))
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.append(items_nested(key, value1, value2))
        elif value1 != value2:
            diff.append(items_modified(key, value1, value2))
        else:
            diff.append(items_unchanged(key, value1))

    sorted_diff = sorted(diff, key=lambda x: x["name"])

    return sorted_diff


def build_diff(dict1, dict2):
    """Build internal representation of difference

    between two dictionaries."""
    diff = {}

    all_keys = set(dict1.keys()) | set(dict2.keys())

    for key in sorted(all_keys):
        if key not in dict1:
            diff[key] = {"type": "added", "value": dict2[key]}
        elif key not in dict2:
            diff[key] = {"type": "removed", "value": dict1[key]}
        elif dict1[key] == dict2[key]:
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                diff[key] = {
                    "type": "nested",
                    "children": build_diff(dict1[key], dict2[key]),
                }
            else:
                diff[key] = {"type": "unchanged", "value": dict1[key]}
        else:
            # Если оба значения - словари, создаем вложенную структуру
            if isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
                diff[key] = {
                    "type": "nested",
                    "children": build_diff(dict1[key], dict2[key]),
                }
            else:
                # Иначе это изменение значения
                diff[key] = {
                    "type": "changed",
                    "old_value": dict1[key],
                    "new_value": dict2[key],
                }

    return diff
