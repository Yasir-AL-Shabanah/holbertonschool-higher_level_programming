#!/usr/bin/python3
"""Module that defines Square with a private size (no validation yet)."""

class Square:
    """Square storing a private size attribute."""

    def __init__(self, size):
        """Initialize a new Square with a raw size (task 1)."""
        self.__size = size
