#!/usr/bin/python3
def safe_print_division(a, b):
    # use finally clause
    try:
        result = a / b
    except:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result
