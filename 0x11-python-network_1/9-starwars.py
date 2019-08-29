#!/usr/bin/python3
import requests
import sys

try:
    values = {'search': sys.argv[1]}
    url = 'https://swapi.co/api/people/'
    res = requests.get(url, params=values)
    res = res.json()
    results = res.get('results')
    print('Number of results:', len(results))
    for result in results:
        print(result.get('name'))
except Exception:
    pass
