#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq = lambda x: x**2
    square = []
    for row in matrix:
        for i in range(len(row)):
            square.append(sq(row[i]))
    return square
