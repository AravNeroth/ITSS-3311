# ITSS / OPRE 3311 – Object-Oriented Programming
# Assignment 4: 3-Dice Game Revisited
# Programmer: Arav Neroth
# Date: 3/6/2025
# Description: This program simulates the rolling of 3 dice and evaluates the dice roll to determine points scored based on the game's rules.

# imports
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

# get name
def get_name():
    while True:
        try:
            name = input("Enter your name (one word, no spaces): ").strip()
            # catch some common things
            if " " in name:
                raise ValueError("Error: Please enter only one name without spaces.")
            if not name.isalpha():
                raise ValueError("Error: Name must contain only letters.")
            if len(name) == 0:
                raise ValueError("Error: Name cannot be empty.")
            
            return name.capitalize()  # capitalize for fun
        
        except ValueError as e:
            print(e)

# welcome message + rules
def print_welcome(name):
    print(f"""
Welcome to the 3-Dice Game, {name}!
      
Rules: Roll 3 dice. If you roll a pair (Doublet), you get 5 bonus points. If you roll three-of-a-kind (Triplet), you get 20 bonus points. 
Your score is the sum of the dice plus any bonus points.
""")

# gets how many times user wants to play
def get_games():
    while True:
        try:
            games = int(input("Enter the number of games you would like to play: "))
            if games > 0:
                return games
            else:
                print("Please enter a positive number.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

# generate nums for dice that are put into a list, sorted, and then returned 
def roll_sort_die():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)
    return sorted([die1, die2, die3])  

# calculate bonus depending on how many dice are the same  
def calculate_bonus(die1, die2, die3):
    if die1 == die2 == die3:
        return 20
    elif die1 == die2 or die1 == die3 or die2 == die3:
        return 5
    
    return 0

# choose the type of bonus recieved after calculation (see above)
def get_result(bonus):
    if bonus == 20:
        return "Triplet"
    elif bonus == 5:
        return "Doublet"
    else:
        return "No Bonus"
    
# print the game stats
def print_game_stat(result, bonus, score, die1, die2, die3):
    print(f"""
        Today's Date: {date}
        Dice values: {die1}, {die2}, {die3}
        Result: {result}
        Bonus: {bonus}
        Score: {score}
        """)

# prompts play again loop once "games" has finished. 
def ask_play_again():
    return input('Would you like to play again? (Y/N): ').strip().upper() == 'Y'

# goodbye message
def print_end_message(name):
    print(f"Thank you for playing, {name}!")


def main():
    # get and store name, and welcome user
    name = get_name()  
    print_welcome(name)

    while True:
        # get and store num of games to loop through
        games = get_games()  
        for _ in range(games):
            input("Press 'Enter' to roll the dice...")  
            # call roll function and store sorted val in d1, d2, d3
            die1, die2, die3 = roll_sort_die() 
            # call respective functions with the sorted dice as parameters
            bonus = calculate_bonus(die1, die2, die3)
            score = die1 + die2 + die3 + bonus
            result = get_result(bonus)
            # print game results using updated variables as parameters
            print_game_stat(result, bonus, score, die1, die2, die3)

        # if user responded no, break and end game
        if not ask_play_again(): 
            break
    # goodbye message
    print_end_message(name)

if __name__ == "__main__":
    main()