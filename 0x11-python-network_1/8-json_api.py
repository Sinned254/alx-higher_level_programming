#!/usr/bin/python3
""" script that takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys


if __name__ == "__main__":
    # Get thelettefrom the command-line arguments or
    # set it to an empty string if not provided
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # URL for the search_user endpoint
    url = "http://0.0.0.0:5000/search_user"

    try:
        # Send a POST request with the letter parameter
        response = requests.post(url, data={'q': q})

        # Check if the response body is properly JSON formatted and not empty
        try:
            user_data = response.json()
            if user_data:
                print("[{}] {}".format(user_data['id'], user_data['name']))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.RequestException as e:
        print("Error accessing the API: {}".format(e))
    except Exception as e:
        print("An unexpected error occurred: {}".format(e))
