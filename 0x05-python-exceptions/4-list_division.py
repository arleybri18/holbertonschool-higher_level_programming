#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for idx in range(list_length):
        res = 0
        try:
            res = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        except (TypeError, ValueError):
            print("wrong type")
        finally:
            result.append(res)
    return result
