#!/usr/bin/python3
"""Return the dictionary description for JSON serialization of an object."""


def class_to_json(obj):
    """Return a dict of serializable attributes of obj."""
    if hasattr(obj, "__dict__"):
        return obj.__dict__.copy()
    return {}


if __name__ == "__main__":
    pass
