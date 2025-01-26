#!/usr/bin/python3
"""Island perimeter"""


def island_perimeter(grid):
    """computes the perimeter"""
    pe = 0
    if type(grid) != list:
        return 0
    length = len(grid)
    for i, row in enumerate(grid):
        m = len(row)
        for j, cell in enumerate(row):
            if cell == 0:
                continue
            edges = (
                    i == 0 or (len(grid[i - 1]) > j and grid[i - 1][j] == 0),
                    j == m - 1 or (m > j + 1 and row[j + 1] == 0),
                    j == 0 or row[j - 1] == 0,
                    )
            pe += sum(edges)
    return pe
