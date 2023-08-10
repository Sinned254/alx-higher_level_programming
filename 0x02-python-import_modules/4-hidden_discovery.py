#!/usr/bin/python3
import hidden_4 as toprint
names = dir(toprint)
for name in names:
    if not name.startwith("__"):
        print("{:s}".format(name))
