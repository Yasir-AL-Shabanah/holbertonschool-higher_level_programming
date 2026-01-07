#!/usr/bin/python3
"""Insert a line after each line containing a given string."""


def append_after(filename="", search_string="", new_string=""):
    """Insert new_string after lines that contain search_string."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    out = []
    for line in lines:
        out.append(line)
        if search_string in line:
            out.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(out)
