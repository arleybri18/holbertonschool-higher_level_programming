#!/usr/bin/python3
def remove_char_at(str, n):
    if n >= 0:
        string = str[:n] + str[n + 1:]
    else:
        string = str
    return (string)
