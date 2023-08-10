#!/usr/bin/python3
if __name__ == "__main__"
import hidden_4 as toprint
names = dir(toprint)
for name in names:
    if not name.startwith("__"):
        print("{:s}".format(name))
