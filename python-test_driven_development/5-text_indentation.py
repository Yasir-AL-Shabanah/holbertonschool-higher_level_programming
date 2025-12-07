#!/usr/bin/python3
"""
Print text with 2 new lines after '.', '?' and ':' with no edge spaces.
"""


def text_indentation(text):
    """Print text with two newlines after . ? : and trim spaces around lines."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i, n = 0, len(text)
    line = ""
    import sys

    while i < n:
        ch = text[i]
        if ch in ".?:":
            sys.stdout.write(line.rstrip() + ch + "\n\n")
            line = ""
            i += 1
            # skip spaces immediately following the punctuation
            while i < n and text[i] == ' ':
                i += 1
            continue
        line += ch
        i += 1

    if line.strip():
        sys.stdout.write(line.strip())
