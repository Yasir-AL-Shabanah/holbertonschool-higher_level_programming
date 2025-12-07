#!/usr/bin/python3
"""Divide all elements of a matrix by a number."""

def matrix_divided(matrix, div):
    """Return a new matrix rounded to 2 decimals."""
    if (not isinstance(matrix, list) or
            any(not isinstance(r, list) for r in matrix) or
            any(not isinstance(x, (int, float)) for r in matrix for x in r)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )
    if len({len(r) for r in matrix}) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in r] for r in matrix]
