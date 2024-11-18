#!/usr/bin/python3

"""pascal riangle"""


def pascal_triangle(n):

    pasc = []

    if n <= 0:
        return pasc
    else:
        pasc.append([1])
        for i in range(1, n):
            r = [1]
            for j in range(1, i):
                r.append(pasc[i-1][j-1] + pasc[i-1][j])
            r.append(1)
            pasc.append(r)
    return pasc
