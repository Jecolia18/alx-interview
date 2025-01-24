#!/usr/bin/python3
"""2D matrix rotation module.
"""


def rotate_2d_matrix(matrix):
    """Rotates an m by n 2D matrix in place.
    """
    if not isinstance(matrix, list):
        return
    if len(matrix) <= 0:
        return
    if not all(map(lambda x: isinstance(x, list), matrix)):
        return
    r = len(matrix)
    columns = len(matrix[0])
    if not all(map(lambda x: len(x) == columns, matrix)):
        return
    c, j = 0, r - 1
    for i in range(columns * r):
        if i % r == 0:
            matrix.append([])
        if j == -1:
            j = r - 1
            c += 1
        matrix[-1].append(matrix[j][c])
        if c == columns - 1 and j >= -1:
            matrix.pop(j)
        j -= 1
