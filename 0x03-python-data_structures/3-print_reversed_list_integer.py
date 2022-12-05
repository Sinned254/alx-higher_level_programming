#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(my_list)):
        newlist = my_list[::-1]
        print("{:d}".format(newlist[i]))
