#!/usr/bin/python3
"""Read a UTF-8 text file and print its content to stdout."""
def read_file(filename=""):
    """Print file content to stdout (no exceptions handling required)."""
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
