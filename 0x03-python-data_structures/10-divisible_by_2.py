#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    listdiv = []
    for n in my_list:
        if n % 2 == 0:
            listdiv.append(True)
        else:
            listdiv.append(False)
    return listdiv
