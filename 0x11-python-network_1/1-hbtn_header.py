#!/usr/bin/python3
''' get a url from shell retrieve value of header
'''
import urllib.request as ur
import sys

try:
    req = ur.Request(sys.argv[1])
    with ur.urlopen(req) as response:
        print(response.getheader('X-Request-Id'))
except BaseException:
    pass
