#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status using requests """
import requests


def fetch_and_display_status(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        content = response.text

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))

    except requests.RequestException as e:
        print("Error accessing the URL: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))


if __name__ == "__main__":
    status_url = "https://alx-intranet.hbtn.io/status"
    fetch_and_display_status(status_url)
