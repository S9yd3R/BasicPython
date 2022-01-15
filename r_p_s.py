#!/bin/env python

import random

#LEVEL 3 > This is a rock paper scissors game which will count your scores 

def play(total):
    print("\n\n\n\nThis is a rock, paper, scissors game !!")
    print("Enter your choice and press enter ")
    score = 0
    c_score = 0
    options = [ "Rock", "Paper", "Scissors" ]
    for i in range(total) :
        UsersChoice = input("\n(R)ock, (P)aper, (S)cissors : ").upper()
        c_Choice = random.choice(options)

        if UsersChoice == "R" and c_Choice == "Scissors" or UsersChoice == "S" and c_Choice == "Paper" or UsersChoice == "P" and c_Choice == "Rock" :
            score += 1
            print(f"You\'ve scored !")

        elif c_Choice == "Rock" and UsersChoice == "S" or c_Choice == "Scissors" and UsersChoice == "P" or c_Choice == "Paper" and UsersChoice == "R" :
            c_score += 1
            print("I\'ve scored !")

        elif UsersChoice == c_Choice :
            print("no points awarded !")
        else :
            print("invalid choice")
        print(f"My choice was {c_Choice} ")
    
    print(f"You\'ve scored {score}/{total}\nI\'ve scored {c_score}/{total}")

play(5) # change the parameter to extend the game !
