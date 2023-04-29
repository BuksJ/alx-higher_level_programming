#!/usr/bin/python3
"""
This module fetches https://alx-intranet.hbtn.io/status using urllib package
and displays the body of the response.
"""

from urllib import request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("- type: {}".format(type(html)))
        print("- content: {}".format(html))
        print("- utf8 content: {}".format(html.decode('utf-8')))
