#!/bin/env python

import random

def GuessMe(high):
    random_number = random.randint(1,high)
    guess = 0
    input(f"guess a number between 1 & {high}, press ENTER to continue")
    while random_number != guess :
        guess = int(input("\nEnter your guess: "))
        if random_number > guess :
            print(f"guess something higher than {guess}")
        elif random_number < guess:
            print(f"guess something lower than {guess}")
        else :
            print("Nize !!, Correct guess")
            quit()

GuessMe(10) # you can change the parameter
