#!/usr/bin/python3
def append_write(filename="", text=""):
    lines = 0
    with open(filename, 'a') as f:
        lines = f.write(text)
    return lines
