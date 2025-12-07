#!/usr/bin/python3
"""Print a square using '#' character."""


def print_square(size):
    """Print a size x size square of '#'.

    Examples:
    >>> print_square(2)
    ##
    ##
    >>> print_square(0)
    >>> print_square(1)
    #
    >>> print_square(-1)
    Traceback (most recent call last):
    ...
    ValueError: size must be >= 0
    >>> print_square(3.5)
    Traceback (most recent call last):
    ...
    TypeError: size must be an integer
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
