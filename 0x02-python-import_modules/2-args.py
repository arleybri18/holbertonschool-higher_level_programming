#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    argument = len(sys.argv)
    if argument == 1:
        print("0 arguments.")
    elif argument == 2:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argument - 1))
        for i in range(1, argument):
            print("{}: {}".format(i, sys.argv[i]))
