#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
argc = len(argv)
if argc == 1:
    print('0')
else:
    sum = 0
    for i in range(1, argc):
        sum += int(argv[i])
    print("{:d}".format(sum))
