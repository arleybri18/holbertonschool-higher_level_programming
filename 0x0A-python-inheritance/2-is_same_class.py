#!/usr/bin/python3
def is_same_class(obj, a_class):
    '''Method that validate if object is the same a_class
    don't review the inherit'''
    return type(obj) == a_class
