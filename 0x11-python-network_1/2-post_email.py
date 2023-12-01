#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    try:
        # Encode the email parameter
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')

        # Send a POST request
        with urllib.request.urlopen(url, data) as response:
            html_content = response.read().decode('utf-8')

            print("Body response:")
            print("\t- type: {}".format(type(html_content)))
            print("\t- content: {}".format(html_content))

    except urllib.error.URLError as e:
        print("Error accessing the URL: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
