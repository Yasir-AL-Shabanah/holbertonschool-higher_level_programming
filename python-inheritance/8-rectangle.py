#!/usr/bin/python3
"""Define a class Rectangle that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class that uses BaseGeometry's integer validation."""

    def __init__(self, width, height):
        """Initialize a new Rectangle with validated width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
