#!/usr/bin/python3
"""module conatins funtion ``append_write``
"""


def append_write(filename="", text=""):
    """Funtion appends charatcers to a file
    Args:
        filename: filename to append
        text: text charatcer to append
    Returns: nuber of character appended
    """
    with open(filename, 'a', encoding="utf-8") as f:
        nb = f.write(text)
    return nb
