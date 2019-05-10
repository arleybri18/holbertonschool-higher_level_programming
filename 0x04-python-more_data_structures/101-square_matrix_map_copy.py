#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    square = lambda num: num**2
    list_item = lambda item: list(map(square, item))
    return list(map(list_item, matrix))
