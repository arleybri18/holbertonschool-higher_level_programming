#!/usr/bin/python3
import requests
import sys

res = requests.get(sys.argv[1])
head = res.headers['X-Request-Id']
print(head)
