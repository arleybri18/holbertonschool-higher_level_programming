#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0 and idx >= len(my_list):
        return my_list
    else:
        return (my_list[0 : idx] + my_list[idx + 1 :])
