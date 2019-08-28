#!/usr/bin/python3
""" use urlib for make requests
"""

if __name__ == "__main__":
    import urllib.request as url
    req = url.Request('https://intranet.hbtn.io/status')
    with url.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type:{}".format(type(html)))
        print("\t- content:{}".format(html))
        print("\t- utf-8 content:{}".format(html.decode('utf-8')))
