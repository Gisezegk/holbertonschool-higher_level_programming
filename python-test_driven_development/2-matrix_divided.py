#!/usr/bin/python3
"""Function that divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix"""
    error = "matrix must be a matrix (list of lists) of integers/floats"
    size_error = "Each row of the matrix must have the same size"

    if (not isinstance(matrix, list) or
            not all(isinstance(element, list) for element in matrix)):
        raise TypeError(error)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    my_matrix = []
    bc = []
    len_r = len(matrix[0])

    for row in matrix:
        if len_r != len(row):
            raise TypeError(size_error)
        for element in row:
            if isinstance(element, (int, float)):
                bc.append(round(element / div, 2))
            else:
                raise TypeError(error)
        my_matrix.append(bc)
        bc = []
    return my_matrix
