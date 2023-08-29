#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return True
    except Exception as era:
        err = "exception: " + str(era) + "\n"
        sys.stderr.write(era)
        return False
