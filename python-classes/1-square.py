#!/usr/bin/python3
"""Module 1-square: define Square with a private size."""
class Square:
    """Square with a private __size set at construction."""
    def __init__(self, size):
        """Init: store size privately without validation (next tasks validate).

        Args:
            size: intended length of a square side (any type accepted here).
        """
        self.__size = size
