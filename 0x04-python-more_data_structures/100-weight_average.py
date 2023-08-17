#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) > 0:
        sumprod = 0
        addi = 0
        for i in my_list:
            sumprod += i[0] * i[1]
            addi += i[1]
        return sumprod/addi
    return 0
