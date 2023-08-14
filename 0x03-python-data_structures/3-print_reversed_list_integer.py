#!/usr/bin/pythoni3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        newlist = my_list[::-1]
        listlen = len(newlist)
        for i in range(listlen):
            print("{:d}".format(newlist[i]))
