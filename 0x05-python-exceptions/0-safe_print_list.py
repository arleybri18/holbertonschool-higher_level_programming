#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    y = 0
    try:
        for el in range(x):
            print(my_list[el], end="")
            y += 1
        print()
    except:
        print()
    return y
