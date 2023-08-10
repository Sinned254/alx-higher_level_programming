#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    import sys
count = len(sys.argv)
if count != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
elif sys.argv[2] not in ['+', '-', '*', '/']:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
else:
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == '+':
        res = calc.add(a, b)
    elif op == '-':
        res = calc.sub(a, b)
    elif op == '*':
        res = calc.mul(a, b)
    else:
        res = calc.div(a, b)
    print("{:d} {:s} {:d} = {:d}".format(a, op, b, res))
