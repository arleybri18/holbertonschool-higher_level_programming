#!/usr/bin/python3
""" use urlib for make requests """

import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf-8 content: {}".format(html.decode('utf-8')))
