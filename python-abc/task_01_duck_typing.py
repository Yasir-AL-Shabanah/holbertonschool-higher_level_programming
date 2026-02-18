#!/usr/bin/env python3
"""
Module for Shape abstract class and concrete classes Circle and Rectangle.
Also includes shape_info function.
"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class Shape."""
    @abstractmethod
    def area(self):
        """Abstract method for area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Abstract method for perimeter."""
        pass


class Circle(Shape):
    """Circle class inheriting from Shape."""
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter of the circle."""
        return 2 * math.pi * abs(self.radius)


class Rectangle(Shape):
    """Rectangle class inheriting from Shape."""
    def __init__(self, width, height):
        """Initialize Rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape using duck typing.
    Args:
        shape: An object that has area() and perimeter() methods.
    """
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
