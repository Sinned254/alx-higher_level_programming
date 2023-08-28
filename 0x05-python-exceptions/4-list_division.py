#!/usr/bin/python3
def divide_safe(a, b):
    res = 0
    try:
        res = a / b
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    finally:
        return res

def list_division(my_list_1, my_list_2, list_length):
    res_list = []
    for i in range(list_length):
        try:
            res_list.append(divide_safe(my_list_1[i], my_list_2[i]))
        except IndexError:
            print("out of range")
            res_list.append(0)
    return res_list
