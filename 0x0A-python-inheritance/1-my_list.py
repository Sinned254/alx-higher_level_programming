#!/usr/bin/python3
"""Module contains classes ``MyList`` that inherits from
class list
"""


class MyList(list):
    """``MyList`` class defination."""
    def print_sorted(self):
        """ Prints sorted list
        """
        my_list = sorted(self)
        print(my_list)
