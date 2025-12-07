#!/usr/bin/python3
"""
Module: 2-matrix_divided
Return a new matrix with each element divided by div.
"""

def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by div and return a NEW matrix.

    matrix: list of lists of ints/floats; all rows same length
    div: int/float and not zero
    """
    if (not isinstance(matrix, list) or
            any(not isinstance(r, list) for r in matrix) or
            any(not isinstance(x, (int, float)) for r in matrix for x in r)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    lengths = {len(r) for r in matrix}
    if len(lengths) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[x / div for x in r] for r in matrix]
