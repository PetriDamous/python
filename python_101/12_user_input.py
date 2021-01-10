#Input box

# name = input("Enter Name ")

# print(f"my name is {name}")

#practice
num1 = float(input("enter a number: "))
num2 = float(input("enter another number: "))
operation = input("enter operation: ")

def add (num1, num2):
    return num1 + num2

def subtract (num1, num2):
    return num1 - num2

def multiply (num1, num2):
    return num1 * num2

def divide (num1, num2):
    return num1 / num2

if operation == "add":
    print(add(num1, num2))
elif operation == "subtract":
    print(subtract(num1, num2))
elif operation == "multiply":
    print(multiply(num1, num2))
elif operation == "divide":
    print(divide(num1, num2))
else:
    print("enter valid operation")



