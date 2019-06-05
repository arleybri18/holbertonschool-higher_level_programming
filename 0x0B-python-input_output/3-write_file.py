#!/usr/bin/python3
def write_file(filename="", text=""):
    lines = 0
    with open(filename, 'w') as f:
        lines = f.write(text)
    return lines
