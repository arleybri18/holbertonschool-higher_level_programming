#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    sum = 0
    argument = len(sys.argv)
    if argument == 1:
        print(0)
    elif argument >= 2:
        for i in range(1, argument):
            sum = sum + int(sys.argv[i])
        print("{:d}".format(sum))
