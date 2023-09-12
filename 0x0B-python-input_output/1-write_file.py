#!/usr/bin/python3
"""Module contains ``write_file`` funtion
"""


def write_file(filename="", text=""):
    """Funtion writes content writes content to fileanme

    Args:
        filename: Name of the file
        text: text to be written
    Returns: Number of character written
    """
    with open(filename, 'w', encoding='utf-8') as f:
        nb = f.write(text)
    return nb
