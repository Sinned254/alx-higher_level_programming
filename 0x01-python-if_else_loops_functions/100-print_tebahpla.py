#!/usr/bin/python3
for i in range(122, 96, -1):
    c = ""
    if i % 2 == 0:
        c = c + chr(i)
    else:
        c = c + chr(i - 32)
    print("{:s}".format(c), end="")
