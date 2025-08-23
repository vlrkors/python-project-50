def format_stylish(diff, depth=0):
    """Format difference as stylish string."""
    indent = "    " * depth
    lines = ["{"]

    for key, node in diff.items():
        node_type = node["type"]

        if node_type == "added":
            lines.append(
                f"{indent}  + {key}: {format_value(node['value'], depth + 1)}"
            )
        elif node_type == "removed":
            lines.append(
                f"{indent}  - {key}: {format_value(node['value'], depth + 1)}"
            )
        elif node_type == "changed":
            lines.append(
                f"{indent}  - {key}: "
                f"{format_value(node['old_value'], depth + 1)}"
            )
            lines.append(
                f"{indent}  + {key}: "
                f"{format_value(node['new_value'], depth + 1)}"
            )
        elif node_type == "unchanged":
            lines.append(
                f"{indent}    {key}: {format_value(node['value'], depth + 1)}"
            )
        elif node_type == "nested":
            lines.append(
                f"{indent}    {key}: "
                f"{format_stylish(node['children'], depth + 1)}"
            )

    lines.append(f"{indent}" + "}")
    return "\n".join(lines)


def format_value(value, depth):
    """Format value for display."""
    if isinstance(value, dict):
        indent = "    " * depth
        lines = ["{"]
        for key, val in value.items():
            lines.append(f"{indent}    {key}: {format_value(val, depth + 1)}")
        lines.append(f"{indent}" + "}")
        return "\n".join(lines)
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    elif isinstance(value, str):
        return value
    else:
        return str(value)
