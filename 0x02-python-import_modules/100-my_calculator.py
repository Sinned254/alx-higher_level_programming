#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    from sys import argv

argc = len(argv)
if argc != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    a = int(argv[1])
    operator = argv[2]
    b = int(argv[3])
    if operator not in ['+', '-', '*', '/']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    if operator == '+':
        res = calc.add(a, b)
    elif operator == '-':
        res = calc.sub(a, b)
    elif operator == '*':
        res = calc.mul(a, b)
    else:
        res = calc.div(a, b)

    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, res))
