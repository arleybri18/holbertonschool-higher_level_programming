#!/usr/bin/python3
'''Search API
'''
import requests
import sys

try:
    list_commits = []
    owner = sys.argv[1]
    repo = sys.argv[2]
    url = 'https://api.github.com/repos/'+owner+"/"+repo+"/commits"
    res = requests.get(url)
    res = res.json()
    for el in res:
        commit = el.get('commit')
        sha = el.get('sha')
        author = commit.get('author').get('name')
        date = commit.get('author').get('date')
        tupla = sha, author, date
        list_commits.append(tupla)
        tupla = ()
        list_commits.sort(key=lambda k: k[2])
    for i in range(10):
        print(list_commits[i][0] + ': ' + list_commits[i][1])
except Exception as e:
    print(e)
