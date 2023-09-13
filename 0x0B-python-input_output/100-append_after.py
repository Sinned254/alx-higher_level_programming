#!/usr/bin/python3
"""Module contain defination of ``append_after`` funtion
"""


def append_after(filename="", search_string="", new_string=""):
    """Funtion inserts a line of text to a file after a
    line containg specific string
    Args:
        filename: file to work on
        search_string: a string to determine where to insert string
        new_string: String to be inserted
    """
    if not filename or not search_string or not new_string:
        return

    with open(filename, 'r') as f:
        lines = f.readlines()
    with open(filename, 'w') as f:
        for line in lines:
            f.write(line)
            if search_string in line:
                f.write(new_string)
