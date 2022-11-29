#!/usr/bin/python3
def uppercase(str):
    ucs = ''
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            ucs = ucs + chr(ord(c) - 32)
        else:
            ucs = ucs + c
    print('{}'.format(ucs))
