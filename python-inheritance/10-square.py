#!/usr/bin/python3
"""Define Square that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class."""

    def __init__(self, size):
        """Initialize square with validated size."""
        super().__init__(size, size)
