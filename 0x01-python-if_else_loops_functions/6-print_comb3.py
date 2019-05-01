#!/usr/bin/python3
for i in range(9):
    for j in range(1, 10):
        if (i == 8 and j == 9):
            print("{}{}".format(i, j))
        elif (j != i and i < j):
            print("{}{}".format(i, j), end=", ")
