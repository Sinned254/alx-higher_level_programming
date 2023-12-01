#!/usr/bin/python3
""" script that takes in a URL and an email address, sends a POST request
    to the passed URL
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    try:
        # Send a POST request with the email parameter
        response = requests.post(url, data={'email': email})
        response.raise_for_status()  # Raise an HTTPError for bad responses

        content = response.text

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))

    except requests.RequestException as e:
        print("Error accessing the URL: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))
