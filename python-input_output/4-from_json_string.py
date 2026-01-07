#!/usr/bin/python3
"""Return a Python object represented by a JSON string."""
import json
def from_json_string(my_str):
    """Convert JSON string to its Python data structure."""
    return json.loads(my_str)
