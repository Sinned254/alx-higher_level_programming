#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL and displays
    the body of the response (decoded in utf-8)
"""
import urllib.request
import urllib.error
import sys


def fetch_and_display_body(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read().decode('utf-8')

            print("Body response:")
            print("\t- type: {}".format(type(html_content)))
            print("\t- content: {}".format(html_content))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
    except urllib.error.URLError as e:
        print("Error accessing the URL: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)


    url = sys.argv[1]
    fetch_and_display_body(url)
