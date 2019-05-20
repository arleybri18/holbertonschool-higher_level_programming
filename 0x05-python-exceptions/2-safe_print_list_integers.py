#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    y = 0
# print exception only if my_list[el] is out of range
    for el in range(x):
        try:
            print("{:d}".format(my_list[el]), end="")
            y += 1
        except (TypeError, ValueError):
            pass
    print()
    return y
