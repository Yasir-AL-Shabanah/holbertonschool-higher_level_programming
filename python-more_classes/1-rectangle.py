#!/usr/bin/python3
"""Module 1-rectangle: define Rectangle with width/height properties."""
class Rectangle:
    """Rectangle with validated width and height (int >= 0)."""

    def __init__(self, width=0, height=0):
        """Init with property setters to validate input."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get current width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width ensuring it is int >= 0."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get current height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height ensuring it is int >= 0."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
