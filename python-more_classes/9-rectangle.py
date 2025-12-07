#!/usr/bin/python3
"""Module 9-rectangle: add classmethod square(cls, size)."""
class Rectangle:
    """Rectangle with a square() alternate constructor."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Init; track instances."""
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
        """Draw using print_symbol; empty string if width/height is 0."""
        if self.__width == 0 or self.__height == 0:
            return ""
        sym = str(self.print_symbol)
        row = sym * self.__width
        return "\n".join([row] * self.__height)

    def __repr__(self):
        """Return code-like string."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Farewell and decrement counter."""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the rectangle with bigger area, rect_1 if equal."""
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """Return a new Rectangle where width == height == size."""
        return cls(size, size)
