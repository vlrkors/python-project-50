def format_value(value):
    if isinstance(value, (dict, list)):
        return "[complex value]"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_plain(diff, parent_key: str = "") -> str:
    """Format difference as plain string."""
    lines: list[str] = []

    for key, node in diff.items():
        current_key = f"{parent_key}.{key}" if parent_key else key
        node_type = node["type"]

        if node_type == "added":
            value = format_value(node["value"])
            lines.append(
                f"Property '{current_key}' was added with value: {value}"
            )
        elif node_type == "removed":
            lines.append(f"Property '{current_key}' was removed")
        elif node_type == "changed":
            old_value = format_value(node["old_value"])
            new_value = format_value(node["new_value"])
            lines.append(
                f"Property '{current_key}' was updated. "
                f"From {old_value} to {new_value}"
            )
        elif node_type == "nested":
            nested = format_plain(node["children"], current_key)
            if nested:
                lines.extend(nested.split("\n"))
        # Для unchanged ничего не выводим в plain формате

    return "\n".join(lines)


def format_diff_plain(diff) -> str:
    return format_plain(diff)
