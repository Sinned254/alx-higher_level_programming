#!/usr/bin/python3
"""module contains defination of funtion ``read_file``"""


def read_file(filename=""):
    """funtion reads ile in UTF8 and prints to stdout"""
    with open(filename, encoding="utf-8") as f:
        for lines in f:
            print(lines, end="")
