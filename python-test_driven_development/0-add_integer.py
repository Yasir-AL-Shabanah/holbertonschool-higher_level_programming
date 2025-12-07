#!/usr/bin/python3
"""Addition of two integers with strict type validation.

This module exposes add_integer(a, b=98) and its doc examples are
verified by doctest.
"""


def add_integer(a, b=98):
    """Return int(a) + int(b).

    Rules:
    - a, b must be int or float, else TypeError with precise message.
    - If float, they are cast to int before the addition.

    Examples:
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    >>> add_integer(2)
    100
    >>> add_integer(100.3, -2)
    98
    >>> add_integer(4, "School")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer
    >>> add_integer(None)
    Traceback (most recent call last):
    ...
    TypeError: a must be an integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # int() will raise OverflowError for inf and ValueError for NaN (by design).
    return int(a) + int(b)
