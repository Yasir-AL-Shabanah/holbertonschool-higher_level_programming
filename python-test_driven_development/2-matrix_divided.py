#!/usr/bin/python3
"""Matrix division with full validation and 2-decimal rounding."""


def matrix_divided(matrix, div):
    """Return new matrix where each element is rounded(x / div, 2).

    Constraints:
    - matrix: list of lists of ints/floats.
    - All rows must have same size.
    - div: number (int/float), non-zero.

    Examples:
    >>> matrix_divided([[1, 2, 3], [4, 5, 6]], 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided([[3, 9], [12, 15]], -3)
    [[-1.0, -3.0], [-4.0, -5.0]]
    """
    emsg = "matrix must be a matrix (list of lists) of integers/floats"
    if (not isinstance(matrix, list) or
            any(not isinstance(r, list) for r in matrix)):
        raise TypeError(emsg)
    if len(matrix) == 0 or any(len(r) == 0 for r in matrix):
        raise TypeError(emsg)
    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for item in row:
            if not isinstance(item, (int, float)):
                raise TypeError(emsg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
