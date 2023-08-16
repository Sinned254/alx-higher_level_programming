#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is not None:
        value = None
        key = None
        for i in a_dictionary.keys():
            if value is None or a_dictionary[i] > value:
                value = a_dictionary[i]
                key = i
        return key
