#!/usr/bin/python3
class MyList(list):
    '''Class Mylist inherit from list class'''
    def print_sorted(self):
        '''print_sorted use the sort method of the super class'''
        new_list = self[:]
        new_list.sort()
        print(new_list)
