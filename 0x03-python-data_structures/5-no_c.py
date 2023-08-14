#!/usr/bin/python3
def no_c(my_string):
    mylist = list(my_string)
    new_str = ''
    for i in mylist:
        if i != 'c' and i != 'C':
            new_str = new_str + i
    return new_str
