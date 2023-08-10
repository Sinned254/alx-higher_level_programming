#!/usr/bin/python3
if __name__ == "__main__":
    import sys
count = len(sys.argv)
res = 0
if len == 1:
    print(res)
else:
    for i in range(1, count):
        res = res + (int(sys.argv[i]))
    print(res)
