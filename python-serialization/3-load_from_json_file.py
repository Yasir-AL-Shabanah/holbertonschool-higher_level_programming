#!/usr/bin/python3
"""Create an object from a JSON file."""

import json


def load_from_json_file(filename):
    """Read filename and return the deserialized Python object."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)


if __name__ == "__main__":
    pass
