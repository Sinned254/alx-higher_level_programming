#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is not None:
        b_dictionary = a_dictionary
        b_dictionary[key] = value
        return b_dictionary
