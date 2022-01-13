#!/bin/env python 
import random

#LEVEL 2 ; A program in which python will guess the number , the actual opposite of the first project 

def c_guess(high) :
    low = 1
    high = high
    user_input = ""
    while user_input != "c" :
        c_guess = random.randint(low,high)
        user_input = input(f"Is {c_guess} a correct guess(C), guess something greater (G), guess something lesser (L):\n~> ").upper()
        if user_input == "C" :
            print("Seems i\'m luckier than u ;)")
            quit()
        elif user_input == "G" :
            low = c_guess + 1
        elif user_input == "L" :
            high = c_guess - 1
        else :
            print("Invalid option")

c_guess(10) #u can change the parameter to make python struggle a little bit ;)
