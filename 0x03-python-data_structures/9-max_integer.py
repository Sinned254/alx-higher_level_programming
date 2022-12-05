#!/usr/bin/python3
def max_integer(my_list=[]):
    big = 0
    if len(my_list) == 0:
        return None
    for i, n in enumerate(my_list):
        if i == 0 or n > big:
            big = n
    return big
