#!/usr/bin/python3
"""Function that checks inheritance only (not same class)."""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class.
    If obj is exactly an instance of a_class, return False.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
