#!/usr/bin/python3
"""Text indentation: 2 newlines after '.', '?', ':' and trim spaces."""


def text_indentation(text):
    """Print text with 2 newlines after '.', '?', ':' and no edge spaces.

    The final output does not add a trailing newline after the last line.

    Examples:
    >>> text_indentation("Holberton School")
    Holberton School
    >>> text_indentation("Holberton. School? How are you: John")
    Holberton.

    School?

    How are you:

    John
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    parts = []
    buf = ""
    for ch in text:
        if ch in ".?:":
            parts.append((buf + ch).strip())
            buf = ""
        else:
            buf += ch
    if buf.strip():
        parts.append(buf.strip())

    # Print without adding an extra newline at the end
    out = "\n\n".join(parts)
    import sys
    sys.stdout.write(out)
