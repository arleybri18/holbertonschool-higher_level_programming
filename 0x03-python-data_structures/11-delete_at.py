#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    else:
        new_list = []
        for index in range(len(my_list)):
            if index != idx:
                new_list.append(my_list[index])
        return new_list
