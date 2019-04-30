#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    print("Last digit of {0} is {1} and is less than 6 and not 0".format
          (number, -(-number % 10)))
else:
    if (number % 10) > 5:
        print("Last digit of {0} is {1} and is greater than 5".format
              (number, (number % 10)))
    elif (number % 10) == 0:
        print("Last digit of {0} is {1} and is 0".format
              (number, (number % 10)))
    elif (number % 10) < 6:
        print("Last digit of {0} is {1} and is less than 6 and not 0".format
              (number, (number % 10)))
