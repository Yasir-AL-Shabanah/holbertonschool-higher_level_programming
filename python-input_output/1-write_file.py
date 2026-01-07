#!/usr/bin/python3
"""Write a string to a UTF-8 text file and return characters written."""
def write_file(filename="", text=""):
    """Create/overwrite file and return number of written characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
