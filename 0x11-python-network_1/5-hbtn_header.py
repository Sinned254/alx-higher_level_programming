#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL and displays
    the value of the variable X-Request-Id in the response header
"""
import requests
import sys


def get_x_request_id(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id is not None:
            print("{}".format(x_request_id))
        else:
            print("X-Request-Id not found in the response headers.")

    except requests.RequestException as e:
        print("Error accessing the URL: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))


if __name__ == "__main__":
    url = sys.argv[1]
    get_x_request_id(url)
