#!/usr/bin/python3
'''Search API
'''
import requests
import sys

try:
    owner = sys.argv[2]
    repo = sys.argv[1]
    url = 'https://api.github.com/repos/'+owner+"/"+repo+"/commits"
    res = requests.get(url)
    res = res.json()
    cont = 1
    for el in res:
        commit = el.get('commit')
        sha = el.get('sha')
        author = commit.get('author').get('name')
        print("{}: {}".format(sha, author))
        if cont == 10:
            break
        cont += 1
except Exception as e:
    print(e)
