#!/bin/env python

#LEVEL 4 ; basic level calculator to dp basic maths with 2 numbers :)

import time

#colors
red = "\033[1;91m"
cyan = "\033[1;36m"
default = "\033[0m"

def menu():
    print("""\n\n
    1) Addition
    2) Subtraction
    3) Multiplication
    4) Division
    5) Floor Division
    6) quit\n\n
    """)

def variables():
    var1 = int(input("\nEnter a number: "))
    var2 = int(input("Enter next number: "))
    return [var1,var2]

def addition(var1,var2):
    sum = var1 + var2
    print(f"{cyan}The Sum of {var1} + {var2} = {sum}{default}")

def subtraction(var1,var2):
    difference = var1 - var2
    print(f"{cyan}The difference of {var1} - {var2} = {difference}{default}")

def multiplication(var1,var2):
    product = var1 * var2
    print(f"{cyan}Product of {var1} / {var2} = {product}{default}")

def division(var1,var2):
    quotient = var1 / var2
    print(f"{cyan}The Quotient of {var1} / {var2} = {quotient}{default}")

def floor_division(var1,var2):
    quotient = var1 // var2
    print(f"{cyan}The quotient of {var1} // {var2} = {quotient}{default}")

while 1 != 0 :
    menu()
    var = int(input("Enter your choice : "))
    if var == 1 :
        print(f"\n\n\t{red}Addition{default}\n")
        var1,var2 = variables()
        addition(var1,var2)
        time.sleep(2)
    elif var == 2 :
        print(f"\n\n\t{red}Suntraction{default}\n")
        var1,var2 = variables()
        subtraction(var1,var2)
        time.sleep(1)
    elif var == 3 :
        print(f"\n\n\t{red}Multiplication{default}\n")
        var1,var2 = variables()
        multiplication(var1,var2)
        time.sleep(1)
    elif var == 4 :
        print(f"\n\n\t{red}Division{default}\n")
        var1,var2 = variables()
        division(var1,var2)
        time.sleep(1)
    elif var == 5 :
        print(f"\n\n\t{red}Floor Division{default}\n")
        var1,var2 = variables()
        floor_division(var1,var2)
        time.sleep(1)
    elif var == 6 :
        print(f"\n\n\t{cyan}[{default} ! {cyan}]  {red}QUITTING{default}\n")
        quit()
    else :
        print(f"\n\n\t{cyan}[{default} ! {cyan}]  {red}INVALID OPTION {default}\n")

