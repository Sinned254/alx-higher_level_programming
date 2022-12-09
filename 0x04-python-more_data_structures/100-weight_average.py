#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is not None and len(my_list) > 0:
        d1 = 0
        d2 = 0
        for tupl in my_list:
            d1 += tupl[0] * tupl[1]
            d2 += tupl[1]

        return d1/d2

    return 0
