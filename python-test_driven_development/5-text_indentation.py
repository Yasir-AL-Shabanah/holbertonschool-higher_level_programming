#!/usr/bin/python3
"""Print text with two new lines after . ? :"""


def text_indentation(text):
    """Split on . ? : and print each chunk trimmed, plus a blank line."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    buf = []
    for ch in text:
        if ch in ".?:":
            line = "".join(buf).strip()
            print(line)
            print()
            buf = []
        else:
            buf.append(ch)
    tail = "".join(buf).strip()
    if tail:
        print(tail)
