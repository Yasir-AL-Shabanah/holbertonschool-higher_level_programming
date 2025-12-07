#!/usr/bin/python3
"""Module: add two newlines after '.', '?' and ':'. """
def text_indentation(text):
    """Print text with two newlines after '.', '?' and ':'. """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    n = len(text)
    while i < n:
        ch = text[i]
        print(ch, end="")
        if ch in ".?:":
            print("\n")
            i += 1
            while i < n and text[i] == " ":
                i += 1
            continue
        i += 1
