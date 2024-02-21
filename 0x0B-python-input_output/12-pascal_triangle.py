#!/usr/bin/python3

"""Defines a function that represents pascals triangle."""


def pascal_triangle(n):
    """Return a list of ints representing Pascals triangle of n.
    Args:
        n (int): the extent of pascals triangle
    """
    new = [[]]
    if n == 0:
        return ([])
    for i in range(0, n + 1):
        for j in range(i):
    return (new)
