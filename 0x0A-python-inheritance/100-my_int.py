#!/usr/bin/python3
class MyInt(int):
    '''class MyInt inherit from int'''
    def __init__(self, num):
        '''init method'''
        self.num = num

    def __eq__(self, other):
        '''overwrite eq method'''
        return (self.num != other.num)

    def __ne__(self, other):
        '''overwrite ne method'''
        return (self.num == self.num)
