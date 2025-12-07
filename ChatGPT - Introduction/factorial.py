#!/usr/bin/python3
"""Factorial debugging exercise."""


def factorial(n):
    """Return factorial of n (non-negative int).

    Args:
        n (int): Non-negative integer.

    Returns:
        int: n! (1 * 2 * ... * n), or 1 if n is 0.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be >= 0")

    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result


def main():
    """Entry point when run as a script."""
    import sys

    if len(sys.argv) != 2:
        print("Usage: ./factorial.py <n>")
        return

    try:
        number = int(sys.argv[1])
    except ValueError:
        print("n must be an integer")
        return

    try:
        print(factorial(number))
    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
