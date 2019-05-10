#!/usr/bin/python3
def uniq_add(my_list=[]):
    for el in set(my_list):
        print(el)
        el = el + el
    return el
