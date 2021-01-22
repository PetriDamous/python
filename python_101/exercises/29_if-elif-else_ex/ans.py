# print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

# My solution

mode = input('Please select mode (temp conversion or math): ')

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def math():
    operator = input('Enter +,-,*,/: ')
    num_1 =  input('Enter a number: ')
    num_2 = input('Enter another number: ')

    num_1 = float(num_1)
    num_2 = float(num_2)

    if operator == "+":
        print(add(num_1, num_2))
    elif operator == "-":
        print(subtract(num_1, num_2))
    elif operator == "*":
        print(multiply(num_1, num_2))
    elif operator == "/":
        print(divide(num_1, num_2))

def temp_conversion():
    celsius = input('Enter celsius (number) to convert to fahrenheit: ')
    C = float(celsius)
    print(C*(9/5) + 32)

def mode_select(mode):
    mode = mode.lower()
    if mode == 'temp conversion' or mode == 'math':
        if mode == 'math':            
            math()
            return
        else:
            temp_conversion()
            return

    print("Please enter valid mode!!")

mode_select(mode)

# Instructors Solution
mode = input('Enter math operation(+,-,*,/) or f for Celsius to Fahrenheit conversion: ')
num1 = float(input('Enter first number: '))
if mode.lower() == 'f':
    print(f'{num1} Celsius is equivalent to {(num1*9/5)+32 } fahrenheit')
else:
    num2 = float(input('Enter second number: '))

    if mode == '+':
        print(f'Answer is: {num1 + num2}')
    elif mode == '-':
        print(f'Answer is: {num1 - num2}')
    elif mode == '*':
        print(f'Answer is: {num1 * num2}')
    elif mode == '/':
        print(f'Answer is: {num1 / num2}')
    else: