# Olivia Riley 
# Game One, Part 2
# September 12, 2022

import random

# Creating Function 

def play():
    '''Determines if user imput number is correct or incorrect'''
    number = random.randint(1,100)
    print("I have chosen a number between 1 and 100. What is it?")
    guess_number = int(input("Enter Guess here: "))

# Using while loop to determine if user entered number is incorrect

    while guess_number != number:

        if guess_number < number:
            print("My number is higher than that.")

        else:
            print("My number is lower than that.")

        guess_number = int(input("Please try again:"))

    print("Yay! You guessed my number! The secret number was:", number)

play()