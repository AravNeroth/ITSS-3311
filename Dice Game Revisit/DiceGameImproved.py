# ITSS / OPRE 3311 – Object-Oriented Programming
# Assignment 4: 3-Dice Game Revisited
# Programmer: Arav Neroth
# Date: 3/6/2025
# Description: This program simulates the rolling of 3 dice and evaluates the dice roll to determine points scored based on the game's rules.

import datetime
import random

# variables
name = ""
result = ""
die1 = 0
die2 = 0
die3 = 0
bonus = 0
sum = 0
score = 0
games = 0   
play_again = False
date = datetime.date.today()

'''
2. Define Functions
•	Define a function to prompt for and return the user's name.
•	Define a function to print the welcome message and game rules.
•	Define a function to prompt for and return the number of games.
•	Define a function to simulate rolling a die and return the value.
•	Define a function to calculate the bonus based on the dice values.
•	Define a function to return the descriptive result based on the bonus.
•	Define a function to prompt for and return if the player wants to play again.   
•	Define a function to print the end-of-game message.'
'''

def get_name():
    name = input("Enter your name please: ")
    return name

def print_welcome(name):
    print(f"""
Welcome to the 3-Dice Game, {name}!
      
Rules: Roll 3 dice. If you roll a pair (Doublet), you get 5 bonus points. If you roll three-of-akind (Triplet), you get 20 bonus points. 
Your score is the sum of the dice plus any bonus points.
""")
    
def get_games():
    games = input("Enter the number of games you would like to play: ")
    return games

def roll_sort_die(die1, die2, die3):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    
    die1, die2, die3 = sorted([die1, die2, die3])

def calculate_bonus(die1, die2, die3):
    if((die1 == die2) and (die1 == die3)):
        bonus = 20
    elif((die1 == die2) or (die1 == die3) or (die2 == die3)):
        bonus = 5
    else:
        return 0

def get_result(bonus):
    if bonus == 20:
        return "Triplet"
    elif bonus == 5:
        return "Doublet"
    else:
        return "No Bonus"

def play_again():
    play_again = input('Would you like to play again? (Y/N): ').upper().strip() == 'Y'
    return play_again

def print_end_message(name):
    print(f"Thank you for playing, {name}!")

def main():
    get_name()
    print_welcome(name)
    while True:
        get_games()
        for _ in range(games):
            input("Press 'Enter' to roll the dice...")            
            roll_sort_die(die1, die2, die3)
            calculate_bonus(die1, die2, die3)
            score = die1 + die2 + die3 + bonus
            get_result(bonus)
            print(f"""
            Today's Date: {date}
            Dice values: {die1}, {die2}, {die3}
            Result (Doublet or Triplet bonus): {bonus}
            Score: {score}
            """)
        if play_again():
            break
    print_end_message(name)

if __name__ == "__main__":
    main()