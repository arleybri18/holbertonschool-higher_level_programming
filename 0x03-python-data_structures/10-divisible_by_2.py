#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for num in my_list:
        new_list.append(True) if num % 2 == 0 else new_list.append(False)
    return new_list
