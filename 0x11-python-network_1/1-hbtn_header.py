#!/usr/bin/python3
"""script that takes in a URL, sends a request to the URL and displays the
    value of the X-Request-Id variable found in the header of the response
"""
import urllib.request
import sys


def get_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id is not None:
                print("{}".format(x_request_id))
            else:
                print("X-Request-Id not found in the response headers.")

    except urllib.error.URLError as e:
        print("Error accessing the URL: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
