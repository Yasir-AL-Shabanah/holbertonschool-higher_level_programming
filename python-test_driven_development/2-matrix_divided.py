#!/usr/bin/python3
"""
Divide all elements of a matrix, returning a new matrix rounded to 2 decimals.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with each element divided by div (rounded to 2)."""
    import math
    msg_matrix = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or
            any(not isinstance(row, list) for row in matrix)):
        raise TypeError(msg_matrix)

    if len(matrix) == 0 or any(len(row) == 0 for row in matrix):
        raise TypeError(msg_matrix)

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)) or isinstance(x, bool):
                raise TypeError(msg_matrix)

    if isinstance(div, bool) or not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if isinstance(div, float) and not math.isfinite(div):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # new matrix; do not mutate input
    return [[round(x / div, 2) for x in row] for row in matrix]
