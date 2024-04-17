from art import logo
print(logo)
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {'+': add, '-': subtract, '*': multiply, '/': divide}

def calculator():
    num1 = float(input('Enter first number: '))
    for operator in operations:
        print(operator)

    should_continue = True
    while should_continue:
        num2 = float(input('Enter second number: '))
        operation_symbol = input('Enter operator +, -, *, /): ')
        if operation_symbol in operations:
            opera = (num1, num2)
            print(operations[operation_symbol](*opera))
        else:
            print('Invalid operator')


        if input(f"Type {operation_symbol} again? (y/n): ").lower() == 'y':
            num1 = operations[operation_symbol](num1, num2)
        else:
            should_continue = False
            calculator() # call the function again

calculator() # call the function