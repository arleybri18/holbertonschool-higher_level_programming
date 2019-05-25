#!/usr/bin/python3
"""Module for matrix_divided
"""


def matrix_divided(matrix, div):
    """Function to divide a matrix by a number.

    Args:
        matrix (int, float): is a matrxi with numbers.
        div (int, float): is number for div the matrix.

    Returns:
        matrix int, floats: New matrix with the values of div matrix in div
        or Error message if the data entry not are numbers.
    """
    new_matrix = []
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    cur_row, prev_row = len(matrix[0]), len(matrix[0])
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    for row in matrix:
        cur_row = len(row)
        if (cur_row != prev_row):
            raise TypeError("Each row of the matrix must have the same size")
        new_row = []
        for elem in row:
            if type(elem) is not int and type(elem) is not float:
                raise TypeError(msg)
            else:
                new_row.append(round((elem / div), 2))
        new_matrix.append(new_row)
        prev_row = len(row)
    return new_matrix
