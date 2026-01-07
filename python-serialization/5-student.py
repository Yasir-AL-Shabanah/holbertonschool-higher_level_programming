#!/usr/bin/python3
"""Define a Student class with JSON serialization."""


class Student:
    """Student with first_name, last_name, age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return dict for JSON serialization."""
        return self.__dict__.copy()


if __name__ == "__main__":
    pass
