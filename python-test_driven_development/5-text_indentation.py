#!/usr/bin/python3
"""
Module: 5-text_indentation
Print text, adding a blank line after '.', '?' or ':'.
"""

def text_indentation(text):
    """
    Print text with two newlines after '.', '?' and ':'.

    Raises:
        TypeError: if text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cur = []
    for ch in text:
        cur.append(ch)
        if ch in ".?:":
            print("".join(cur).strip())
            print()
            cur = []
    if cur:
        print("".join(cur).strip())
