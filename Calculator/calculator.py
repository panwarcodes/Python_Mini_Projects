# Simple calculator
import sys

print("""
This is a simple calculator.
Supported operators are as follows:
->Addition/Subtraction
->Division usage = /
->Multiplication usage = *
->Find modulo/remainder, use: %
->Find any number's power
->raise to specific number, use: **

""")

# Important Variables
try:
    num1 = float(input("Enter first integer: "))
    num2 = float(input("Enter second integer: "))
except ValueError:
    print("Please enter integers only!")
    sys.exit()
choosing_operator = input("Enter the operator you want to use: ")

# Defining operators:
# 1) Addition
def sum_operator(num1, num2):
    answer = num1 + num2
    printer = print(f"Sum of {num1} and {num2} is {answer}")
    return printer

# 2) Subtraction
def subtraction_operator(num1, num2):
    answer = num1 - num2
    printer = print(f"Subtraction of {num1} and {num2} is {answer}")
    return printer

# 3) Division
def division_operator(num1, num2):
    answer = num1 / num2
    printer = print(f"Division of {num1} and {num2} is {answer}")
    return printer

# 4) Multiplication
def multiplication_operator(num1, num2):
    answer = num1 * num2
    printer = print(f"Multiplication of {num1} and {num2} is {answer}")
    return printer

# 5) Modulo/Remainder
def modulo_operator(num1, num2):
    answer = num1 % num2
    printer = print(f"Remainder of {num1} and {num2} is {answer}")
    return printer

# 6) Exponential
def exponential_operator(num1, num2):
    answer = num1 ** num2
    printer = print(f"{num1} to the power of {num2} is {answer}")
    return printer

# Operator logic
if (choosing_operator == "+"):
    sum_operator(num1,num2)
elif (choosing_operator == "-"):
    subtraction_operator(num1,num2)
elif (choosing_operator == "/"):
    division_operator(num1,num2)
elif (choosing_operator == "*"):
    multiplication_operator(num1,num2)
elif (choosing_operator == "%"):
    modulo_operator(num1,num2)
elif (choosing_operator == "**"):
    exponential_operator(num1,num2)
else:
    print("Operator not supported!")
