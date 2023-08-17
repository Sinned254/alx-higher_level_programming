#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    dictcopy = dict(a_dictionary)
    for k, v in dictcopy.items():
        if v == value:
            a_dictionary.pop(k)
    return a_dictionary
