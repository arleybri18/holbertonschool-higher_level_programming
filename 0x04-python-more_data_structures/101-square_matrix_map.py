#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda intern_list:
                list(map(lambda num: num**2, intern_list)), matrix))
