#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if elem == search else elem for elem in my_list]
