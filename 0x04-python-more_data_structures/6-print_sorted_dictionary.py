#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is not None:
        s_dict = sorted(a_dictionary.keys())
        for keys in s_dict:
            print("{:s}: {}".format(keys, a_dictionary[keys]))
