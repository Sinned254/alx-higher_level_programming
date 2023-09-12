#!/usr/bin/python3
"""Module contains ``pascal_triangle`` defination
"""


def pascal_triangle(n):
    """Function returns a list of integers representin
    pascals triangele. Returns empty list if n is less than 1
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1]  # The first element in each row is always 1
        if triangle:
            prev_row = triangle[-1]
            for j in range(len(prev_row) - 1):
                row.append(prev_row[j] + prev_row[j + 1])
            row.append(1)  # The last element in each row is always 1
        triangle.append(row)

    return triangle
