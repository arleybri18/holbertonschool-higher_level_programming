#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string.translate({'c': None, 'C': None})
    return new_str
