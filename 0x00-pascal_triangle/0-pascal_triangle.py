#!/usr/bin/python3
"""
returns a list of lists of integers
representing the pascals triangle of 'n'
"""


def pascal_triangle(n):
    """
    generate list of lists of ints in the form of pascals triangle
    """
    if n <= 0:
        return []

    pascal = [[1]]
    for i in range(1, n):
        b = [1]
        for j in range(1, i):
            b.append(pascal[i-1][j-1] + pascal[i-1][j])
        b.append(1)
        pascal.append(b)

    return pascal
