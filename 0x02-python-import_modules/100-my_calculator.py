#!/usr/bin/python3

if __name__ == '__main__':
    """handle basic arithematic operations"""
    import sys
    from calculator_1 import add, subtract, multiply, divide

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    if operator == '+':
        result = add(a, b)

    elif operator == '-':
        result = subtract(a, b)

    elif operator == '*':
        result = multiply(a, b)

    elif operator == '/':
        result = divide(a, b)

    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    print("{} {} {} = {}".format(a, operator, b, result))
