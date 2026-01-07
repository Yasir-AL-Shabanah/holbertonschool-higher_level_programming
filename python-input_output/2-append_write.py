#!/usr/bin/python3
"""Append a string to a UTF-8 text file and return characters added."""


def append_write(filename="", text=""):
    """Append to file (create if missing) and return number of chars added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
