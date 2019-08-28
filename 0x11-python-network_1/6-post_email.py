#!/usr/bin/python3
import requests
import sys

try:
    data = {'email': sys.argv[2]}
    res = requests.post(sys.argv[1], data)
    print(res.text)
except BaseException:
    pass
