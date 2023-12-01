#!/usr/bin/python3
""" script fetches https://intranet.hbtn.io/status"""
import urllib.request


def fetch_and_display_status(url):
    try:
        with urllib.request.urlopen(url) as response:
            html_content = response.read()
            decoded_content = html_content.decode('utf-8')

            print("Body response:")
            print("\t- type: {}".format(type(html_content)))
            print("\t- content: {}".format(html_content))
            print("\t- utf8 content: {}".format(decoded_content))

    except urllib.error.URLError as e:
        print("Error accessing the URL: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))


if __name__ == "__main__":
    status_url = "https://alx-intranet.hbtn.io/status"
    fetch_and_display_status(status_url)
