# Temperature converter by @panwarcodes/github
import sys
import time

# Neccesary functions
def c_to_f():
    try:
        c = float(input("Enter magnitude: "))
        f = (c * 9/5) + 32
        print(f"{f} F")
    except ValueError:
        print("Only integers are allowed!")

def f_to_c():
    try:
        f = float(input("Enter magnitude: "))
        c = (f - 32) * 5/9
        print(f"{c} C")
    except ValueError:
        print("Only integers are allowed!")

def k_to_f():
    try:
        k = float(input("Enter magnitude: "))
        f = (1.8 * k) -  459.67
        print(f"{f} F")
    except ValueError:
        print("Only integers are allowed!")

def f_to_k():
    try:
        f = float(input("Enter magnitude: "))
        k = (f + 459.67) * 5/9
        print(f"{k} K")
    except ValueError:
        print("Only integers are allowed!")

def c_to_k():
    try:
        c = float(input("Enter magnitude: "))
        k = c + 273.15
        print(f"{k} K")
    except ValueError:
        print("Only integers are allowed!")

def k_to_c():
    try:
        k = float(input("Enter magnitude: "))
        c = k - 273.15
        print(f"{c} C")
    except ValueError:
        print("Only integers are allowed!")

# Welcome design
print("-----Welcome to multi-functional Temperature Converter-----\n-----Pick and enter the index of the operation you---------\n------------------Want to perform. Eg: 1-------------------")
time.sleep(1)
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Kelvin to Fahrenhiet")
print("4. Fahrenheit to Kelvin")
print("5. Celsius to Kelvin")
print("6. Kelvin to Celsius")
time.sleep(1)
try:
    choice = int(input("Enter your choice (integer): "))
except ValueError:
    print("Only integer are allowed!")
    sys.exit()

# Choice logic
match choice:
    case 1:
        c_to_f()
    case 2:
        f_to_c()
    case 3:
        k_to_f()
    case 4:
        f_to_k()
    case 5:
        c_to_k()
    case 6:
        k_to_c()