#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    request = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode(encoding='utf-8'))
    except URLError as error:
        print('Error code: {}'.format(error.getcode()))
