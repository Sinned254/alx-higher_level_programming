#!/usr/bin/python3
""" script that takes in a URL and an email address, sends a POST request
    to the passed URL
"""
import requests
import sys


if __name__ == "__main__":
    payload = {'email': sys.argv[2]}
    response = requests.post(sys.argv[1], data=payload)
    print(response.text)
