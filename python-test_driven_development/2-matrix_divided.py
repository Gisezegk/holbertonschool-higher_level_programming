#!/usr/bin/python3
def matrix_divided(matrix, div):
    """Check if matrix rows are same size"""
    if len(set(map(len, matrix))) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    for iterator in matrix:
        for elem in iterator:
            if type(elem) != int and type(elem) != float:
                raise TypeError("matrix must be a matrix (list of lists)\
                         of integers/floats")
    if type(div) != float and type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    divided_matrix = []

    for i in matrix:
        div_i = []
        for j in i:
            div_element = round(j / div, 2)
            div_i.append(div_element)
        divided_matrix.append(div_i)
    return divided_matrix
