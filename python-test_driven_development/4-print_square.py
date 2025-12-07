#!/usr/bin/python3
"""
Module: 4-print_square
Print a square with the character '#'.
"""

def print_square(size):
    """
    Print a square of 'size' using '#'.

    Raises:
        TypeError: if size is not an integer
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
