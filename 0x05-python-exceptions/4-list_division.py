#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for idx in range(list_length):
        try:
            result.append(my_list_1[idx] / my_list_2[idx])
        except ZeroDivisionError:
            result.append(0)
            print("division by 0")
        except IndexError:
            result.append(0)
            print("out of range")
        except (TypeError, ValueError):
            result.append(0)
            print("wrong type")
    return result
