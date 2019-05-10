#!/usr/bin/python3
def search_replace(my_list, search, replace):
    rep = lambda elem, search, replace: replace if search == elem else elem
    return [rep(elem, search, replace) for elem in my_list]
    
