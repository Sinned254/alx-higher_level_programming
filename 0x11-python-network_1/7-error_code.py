#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
    the body of the response
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Send a GET request
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        content = response.text

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))

        # Check if HTTP status code is greater than or equal to 400
        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))

    except requests.RequestException as e:
        print("Error accessing the URL: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))
