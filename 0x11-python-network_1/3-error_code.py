#!/usr/bin/python3
'''send request and decode utf-8, capture HTTPError
'''
import urllib.request as url
import urllib.error as urlerr
import sys

try:
    req = url.Request(sys.argv[1])
    try:
        with url.urlopen(req) as response:
            print(response.read().decode('utf-8'))
    except urlerr.HTTPError as e:
        print("Error code:", e.code)
except BaseException:
    pass
