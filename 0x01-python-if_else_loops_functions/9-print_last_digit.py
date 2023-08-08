#!/usr/bin/python3
def print_last_digit(number):
    lastdigit = 0
    if number >= 0:
        lastdigit = number % 10
    else:
        lastdigit = 10 - (number % 10)

    print('{:d}'.format(lastdigit), end="")
    return lastdigit
