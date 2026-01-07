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
    saw_punct = False

    while i < length:
        ch = text[i]
        print(ch, end="")
        if ch in ".?:":
            saw_punct = True
            # سطر جديد واحد بعد علامة الترقيم
            print()
            i += 1
            # تخطي المسافات بعد علامة الترقيم
            while i < length and text[i] == " ":
                i += 1
            continue
        i += 1

    # newline أخير فقط إذا كان في النص علامة ترقيم
    if saw_punct:
        print()
