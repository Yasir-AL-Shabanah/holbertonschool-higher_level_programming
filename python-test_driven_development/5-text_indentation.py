#!/usr/bin/python3
"""Module that provides a function to print text with indentation."""


def text_indentation(text):
    """Print text with two newlines after '.', '?' and ':'.

    There will be no spaces at the beginning or at the end of each line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    while i < length:
        ch = text[i]
        print(ch, end="")
        if ch in ".?:":
            print("\n")
            i += 1
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1
