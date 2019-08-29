#!/usr/bin/python3
'''Search API
'''
import requests
import sys
from requests.auth import HTTPBasicAuth as aut

try:
    data = {'username': sys.argv[1], 'password': sys.argv[2]}
    url = 'https://api.github.com/user'
    res = requests.get(url, auth=aut(
            sys.argv[1],
            sys.argv[2]))
    res = res.json()
    print(res.get('id'))

except Exception as e:
    print(e)
