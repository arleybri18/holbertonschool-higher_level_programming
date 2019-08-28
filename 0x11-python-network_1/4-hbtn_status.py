#!/usr/bin/python3
""" use requests for make requests
"""

if __name__ == "__main__":
    import requests as req
    r = req.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", type(r.text))
    print("\t- content:", r.text)
