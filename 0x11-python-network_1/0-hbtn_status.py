#!/usr/bin/python3
""" use urlib for make requests
"""
import urllib.request as req

url = "https://intranet.hbtn.io/status"
with req.urlopen(url) as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf-8 content: {}".format(html.decode('utf-8')))
