#!/usr/bin/python3
def inherits_from(obj, a_class):
    """True if obj is an instance of subclass of a_class (not exact)."""
    return isinstance(obj, a_class) and type(obj) is not a_class
