import os
import time

OS = os.name
cmd_cleaner = 'cls' if OS == 'nt' else 'clear'


def Calculator(x, y, op):
    match op:
        case '+':
            return x + y
        case '-':
            return x - y
        case '*':
            return x * y
        case '/':
            return x / y
        case _:
            print("invalid operator!!")


print("Welcome!!!")
for i in range(1, 6):
    print('*' * i)
    time.sleep(1)
while True:
    os.system(cmd_cleaner)
    first_int = int(input("Enter first integer :"))
    while True:
        op = input("select an op in (+, -, *, /): ")
        if op not in ['+', '-', '*', '/']:
            print("wrong op!!!")
            print()
        else:
            break
    second_int = int(input("Enter second integer: "))
    Calculator(first_int, second_int, op)
