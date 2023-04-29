#!/usr/bin/python3
"""
This script takes a URL, sends a request to the URL,
and displays the body of the response
If the HTTP status code is greater than or equal to 400,
it will print an error message with the status code.
"""

import requests
from sys import argv


if __name__ == "__main__":
    request = requests.get(argv[1])
    if request.status_code >= 400:
        print("Error code: {}".format(request.status_code))
    else:
        print(request.text)
