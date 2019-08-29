#!/usr/bin/python3
import requests
import sys

try:
    if len(sys.argv) < 2:
        s = ""
    else:
        s = sys.argv[1]
    data = {'q': s}
    url = 'http://0.0.0.0:5000/search_user'
    res = requests.post(url, data)
    res = res.json()
    if res:
        print("[{}] {}".format(res.get('id'), res.get('name')))
    else:
        print("No result")
except Exception:
    print("Not a valid JSON")
