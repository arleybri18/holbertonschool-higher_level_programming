#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None and len(my_list) is not 0:
        denominator = 0
        numerator = 0
        for elem in my_list:
            denominator += elem[0] * elem[1]
            numerator += elem[1]
        return denominator / numerator
    else:
        return 0
