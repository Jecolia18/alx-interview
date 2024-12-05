#!/usr/bin/python3

"""demo of function that calculates operations
"""


def minOperations(n):
    """method to calculate the fewest
    number of operations"""

    if n <= 1:
        return 0
    op = 0
    div = 2

    while n > 1:
        while n % div == 0:
            op += div
            n //= div
        div += 1
    return op
