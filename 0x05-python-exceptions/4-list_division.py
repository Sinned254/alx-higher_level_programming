#!/usr/bin/python3

def safe_division(a, b):
    qtt = 0
    try:
        qtt = a / b
    except ZeroDivisionError:
        print("division by 0")
    except TypeError:
        print("wrong type")
    finally:
        return qtt


def list_division(list_1, list_2, list_len):
    result_li = []
    for i in range(list_len):
        try:
            result_li.append(safe_division(list_1[i], list_2[i]))
        except IndexError:
            print("out of range")
            result_li.append(0)

    return result_li
