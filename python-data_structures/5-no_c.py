#!/usr/bin/python3
def no_c(my_string):
    """Remove all characters 'c' and 'C' from a string."""
    if my_string is None:
        return None
    return "".join(ch for ch in my_string if ch != 'c' and ch != 'C')
