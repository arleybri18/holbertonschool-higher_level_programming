#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    lines = 0
    with open(filename, 'r') as f:
        if nb_lines <= 0:
            for line in f:
                print(line, end='')
        else:
            for i in range(nb_lines):
                line_data = f.readline()
                if (line_data != ''):
                    print(line_data, end='')
