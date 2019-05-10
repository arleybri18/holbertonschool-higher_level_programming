#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for x, y in a_dictionary.items():
        new_dict[x] = y * 2
    return new_dict
