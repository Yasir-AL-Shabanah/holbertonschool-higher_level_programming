#!/usr/bin/python3
"""Define a Student class with selective JSON serialization."""


class Student:
    """Student with first_name, last_name, age."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dict; if attrs is list of strings, filter keys."""
        data = self.__dict__
        if isinstance(attrs, list) and all(isinstance(a, str) for a in attrs):
            return {k: data[k] for k in attrs if k in data}
        return data.copy()
