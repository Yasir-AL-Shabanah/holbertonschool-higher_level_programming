#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Return a new dict with values doubled."""
    return {k: v * 2 for (k, v) in a_dictionary.items()}
