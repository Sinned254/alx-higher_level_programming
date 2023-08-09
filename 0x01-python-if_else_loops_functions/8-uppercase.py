#!/usr/bin/python3
def uppercase(str):
    c = ''
    for s in str:
        if ord(s) > 96 and ord(s) < 123:
            c = c + chr(ord(s) - 32)
        else:
            c = c + s
    print("{:s}".format(c))
