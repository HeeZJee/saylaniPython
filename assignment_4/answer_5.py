"""Guess the number game
Write a program which randomly generate a number between 1 to 30 and ask the user in input field to guess the correct number. Give three chances to user guess the number and also give hint to user if hidden number is greater or smaller than the number he given to input field.
"""

import random
 
hidden_number = random.randrange(1,30)
chances = 3

for chance in range(chances):
    guess = int(input("Can you guess a hidden number? \nTake guess: "))
    if hidden_number == guess:
        print("You guessed it! The number was",hidden_number)
        break
    elif hidden_number > guess:
        print("Higher")
    elif hidden_number < guess:
        print("Lower")

if guess != hidden_number:
    print()
    print('Sorry you reached the maximum number of tries')
    print('The secret number was', hidden_number)
    
