#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer (standard subtractive rules).
    Return 0 if input is None or not a str.
    """
    if not isinstance(roman_string, str) or roman_string == "":
        return 0
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
    total = 0
    i = 0
    s = roman_string.upper()
    n = len(s)
    while i < n:
        v = vals.get(s[i])
        if v is None:
            return 0
        if i + 1 < n:
            nxt = vals.get(s[i + 1])
            if nxt is None:
                return 0
            if v < nxt:
                total += (nxt - v)
                i += 2
                continue
        total += v
        i += 1
    return total
