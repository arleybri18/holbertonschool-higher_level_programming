#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for nlist in matrix:
        i = 1
        if len(nlist) == 0:
            print("")
        else:
            for el in nlist:
                if i < len(nlist):
                    print("{:d}".format(el), end=" ")
                else:
                    print("{:d}".format(el), end="\n")
                i += 1
