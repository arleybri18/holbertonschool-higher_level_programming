#!/usr/bin/python3
def safe_print_integer(value):
# capture exception if type is not integer
    try:
        print("{:d}".format(value))
    except ValueError:
        return False
    return True
