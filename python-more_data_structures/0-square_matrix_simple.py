#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Return a new matrix with squares of input values (no in-place change)."""
    if matrix is None:
        return None
    return [[n * n for n in row] for row in matrix]
