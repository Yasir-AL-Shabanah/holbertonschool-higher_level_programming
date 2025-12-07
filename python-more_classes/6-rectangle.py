#!/usr/bin/python3
"""Module 6-rectangle: track number_of_instances."""
class Rectangle:
    """Rectangle counting live instances."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Init and increment instance counter."""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        """Get width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width (int >= 0)."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height (int >= 0)."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return area."""
        return self.__width * self.__height

    def perimeter(self):
        """Return perimeter or 0 if empty."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Return rows of '#' or empty string if width/height is 0."""
        if self.__width == 0 or self.__height == 0:
            return ""
        row = "#" * self.__width
        return "\n".join([row] * self.__height)

    def __repr__(self):
        """Return code-like string."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print farewell and decrement counter."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1
