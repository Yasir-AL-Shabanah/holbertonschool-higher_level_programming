#!/usr/bin/python3
"""Module for text_indentation function."""


def text_indentation(text):
    """Print text with 2 new lines after '.', '?' and ':'.

    Text must be a string. Each printed line will not start
    or end with a space.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    i = 0
    n = len(text)

    # تخطي المسافات في بداية النص
    while i < n and text[i] == " ":
        i += 1

    result = ""

    while i < n:
        ch = text[i]
        result += ch

        if ch in separators:
            # إضافة سطرين جديدين بعد علامة الترقيم
            result += "\n\n"
            i += 1
            # تخطي المسافات بعد علامة الترقيم
            while i < n and text[i] == " ":
                i += 1
            continue

        i += 1

    # عدم طباعة سطر جديد إضافي في النهاية
    print(result, end="")
