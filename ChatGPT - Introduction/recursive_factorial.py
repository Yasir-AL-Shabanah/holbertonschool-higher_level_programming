#!/usr/bin/python3
"""Recursive factorial module."""


def factorial(n):
    """Return n! (factorial of n).

    Parameters:
        n (int): Non-negative integer whose factorial is desired.

    Returns:
        int: The factorial value (1 * 2 * ... * n) for n >= 1,
        or 1 if n is 0.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be >= 0")
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def main():
    """Small test when run as a script."""
    import sys

    if len(sys.argv) == 2:
        try:
            number = int(sys.argv[1])
        except ValueError:
            print("n must be an integer")
            return
        print(factorial(number))


if __name__ == "__main__":
    main()
