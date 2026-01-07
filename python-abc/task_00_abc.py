#!/usr/bin/env python3
"""Task 00: Abstract Animal class and subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        raise NotImplementedError


class Dog(Animal):
    """Dog class implementing Animal."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat class implementing Animal."""

    def sound(self):
        """Return cat sound."""
        return "Meow"
