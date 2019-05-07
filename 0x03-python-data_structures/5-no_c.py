#!/usr/bin/python3
def no_c(my_string):
    new_str = my_string.translate({ord('c'): None, ord('C'): None})
    return new_str
