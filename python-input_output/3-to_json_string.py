#!/usr/bin/python3
"""Return JSON representation (string) of a Python object."""
import json
def to_json_string(my_obj):
    """Return a JSON string representing my_obj."""
    return json.dumps(my_obj)
