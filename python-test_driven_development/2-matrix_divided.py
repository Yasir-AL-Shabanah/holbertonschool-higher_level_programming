#!/usr/bin/python3
"""Module: divide each element of a matrix by a number."""
def matrix_divided(matrix, div):
    """Return new matrix with elements divided by div, rounded to 2."""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or
            any(not isinstance(r, list) for r in matrix) or
            any(not isinstance(x, (int, float)) for r in matrix for x in r)):
        raise TypeError(msg)
    if len(matrix) == 0 or any(len(r) == 0 for r in matrix):
        raise TypeError(msg)
    row_len = len(matrix[0])
    if any(len(r) != row_len for r in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(x / div, 2) for x in r] for r in matrix]
