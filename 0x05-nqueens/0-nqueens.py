#!/usr/bin/python3
"""queen"""
import sys


solu = []
"""Possible solutsions to nqueens problem"""
i = 0
position = None


def get_input():
    """validate argument of this program

    Returns:
    int: size of the board
    """
    global i
    i = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        i = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if i < 4:
        print("N must be at least 4")
        sys.exit(1)
    return i
def is_attacking(pos0, pos1):
    """checks if the positions are in an attack mod"""

    if (pos0[0] == pos1[0]) or (pos0[1] == pos1[1]):
        return True
    return abs(pos0[0] - pos1[0]) == abs(pos0[1] - pos1[1])

def group_exists(group):
    """checks if a group exists"""
    global solu
