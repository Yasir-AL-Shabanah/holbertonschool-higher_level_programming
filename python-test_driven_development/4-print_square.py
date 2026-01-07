#!/usr/bin/python3
"""Module that provides a function to print a square."""


def print_square(size):
    """Print a square made of '#' characters.

    size must be an integer >= 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
