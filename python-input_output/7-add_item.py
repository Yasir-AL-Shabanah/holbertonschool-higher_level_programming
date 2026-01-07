#!/usr/bin/python3
"""Add all arguments to a Python list, then save to add_item.json."""

from sys import argv
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def main():
    """Load list from file, extend with argv, then save it back."""
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
    items.extend(argv[1:])
    save_to_json_file(items, filename)


if __name__ == "__main__":
    main()
