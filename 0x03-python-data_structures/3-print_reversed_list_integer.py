#!/usr/bin/pythoni3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        my_list.reverse()
        listlen = len(my_list)
        for i in range(listlen):
            print("{:d}".format(my_list[i]))
