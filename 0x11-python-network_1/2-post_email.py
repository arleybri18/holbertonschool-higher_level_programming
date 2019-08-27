#!/usr/bin/python3
'''send post request
'''
import urllib.request as url
import urllib.parse as parse
import sys

try:
    values = {'email': sys.argv[2]}
    data = parse.urlencode(values)
    data = data.encode('ascii')
    req = url.Request(sys.argv[1], data)
    with url.urlopen(req) as response:
        print(response.read().decode('utf-8'))
except BaseException as e:
    print(e)
