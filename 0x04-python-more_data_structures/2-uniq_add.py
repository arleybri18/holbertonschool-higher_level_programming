#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_list = list(set(my_list))
    for el in new_list:
        print(el)
        el = el + el
    return el
