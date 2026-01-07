#!/usr/bin/python3
"""Generate Pascal's triangle up to n."""


def pascal_triangle(n):
    """Return list of lists representing Pascal's triangle of size n."""
    if n <= 0:
        return []
    tri = [[1]]
    while len(tri) < n:
        prev = tri[-1]
        row = [1]
        for i in range(1, len(prev)):
            row.append(prev[i - 1] + prev[i])
        row.append(1)
        tri.append(row)
    return tri
