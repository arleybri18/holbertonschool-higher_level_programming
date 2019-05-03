#!/usr/bin/python3.4
if __name__ == '__main__':
    import hidden_4
    import sys
    for x in dir(hidden_4):
        if (x[0:2] != "__"):
            print("{}".format(x))
