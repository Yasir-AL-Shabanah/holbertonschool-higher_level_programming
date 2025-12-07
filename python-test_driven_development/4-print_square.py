#!/usr/bin/python3
"""Module: print a square of '#'. """
def print_square(size):
    """Print a square of side 'size' using '#'. """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
