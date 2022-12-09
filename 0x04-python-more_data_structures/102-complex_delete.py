#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newdic = dict(a_dictionary)
    for k, v in newdic.items():
        if v == value:
            a_dictionary.pop(k)
    return a_dictionary
