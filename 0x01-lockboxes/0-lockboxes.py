#!/usr/bin/python3
"""method that determines if all boxes can be opened
"""


def canUnlockAll(boxes):
    """method to check if boxes cann be open"""

    for k in range(1, len(boxes)):
        f = False
        for box in range(len(boxes)):
            if k in boxes[box] and box != k:
                f = True
                break
        if not f:
            return False
    return True
