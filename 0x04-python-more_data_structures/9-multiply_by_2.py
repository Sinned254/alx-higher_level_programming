#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is not None:
        new_dictionary = dict(a_dictionary)
        for i, j in new_dictionary.items():
            new_dictionary[i] = j * 2

        return new_dictionary
