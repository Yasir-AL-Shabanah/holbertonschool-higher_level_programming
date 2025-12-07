#!/usr/bin/python3
"""Print a square using '#'."""


def print_square(size):
    """Print a size x size square."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
