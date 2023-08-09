#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
value = abs(number)
if number < 0:
    lastdigit = -1 * (value % 10)
else:
    lastdigit = value % 10

if lastdigit == 0:
    print(f"Last digit of {number:d} is {lastdigit:d} and is 0")
elif lastdigit < 6 and lastdigit != 0:
    m = "less than 6 and not 0"
    print(f"Last digit of {number:d} is {lastdigit:d} and is {m:s}")
else:
    print(f"Last digit of {number:d} is {lastdigit:d} and is greater than 5")
