#!/usr/bin/python3

def safe_print_division(a, b):
    qtt = 0

    try:
        qtt = a / b
    except ZeroDivisionError:
        qtt = None
    except TypeError:
        qtt = None
    finally:
        print('Inside result: {}'.format(qtt))

    return qtt
