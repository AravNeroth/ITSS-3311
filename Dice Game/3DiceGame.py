"""
Developer: Arav Neroth 
Date: February 11, 2025
Descript: System that rolls 3 dice and generates a score based on the values of the dice.
Class: ITSS 3311.003
"""
import datetime
import random

# variables
name = ""
result = ""
bonus = 0
die1 = 0
die2 = 0
die3 = 0
temp_die = 0
sum = 0
score = 0
keep_playing = True

# Instantiate objects
date = datetime.date.today()

# Prompt for and read-in user name
name = input("Enter your name please: ")

# Print welcome message and rules of the game
print(f"""
Welcome to the 3-Dice Game, {name}!
      
Rules: Roll 3 dice. If you roll a pair (Doublet), you get 5 bonus points. If you roll three-of-akind (Triplet), you get 20 bonus points. 
Your score is the sum of the dice plus any bonus points.
""")

# Prompt for any key to be entered to start the game
input("Press any key or 'Enter' to roll the dice...")

# Start of loop
while(keep_playing):

    # Roll dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    die3 = random.randint(1, 6)

    # Sort the dice lowest to highest (d1 lowest, temp_die always has the highest dice roll)
    if(die2 < die1):
        temp_die = die1
        die1 = die2
        die2 = temp_die

    if(die3 < die2):
        temp_die = die2
        die2 = die3
        die3 = temp_die

    if(die2 < die1):
        temp_die = die1
        die1 = die2
        die2 = temp_die

    # Reset bonus in case of 'No Bonus' value in the last loop that will cause error adding the score
    bonus = 0

    # Dice evaluation
    if((die1 == die2) and (die1 == die3)):
        bonus = 20
    elif((die1 == die2) or (die1 == die3) or (die2 == die3)):
        bonus = 5

    # Determine score
    score = die1 + die2 + die3 + bonus

    # If there is no bonus, then change to string for output
    if bonus == 0:
        bonus = "No bonus"

    # Final output
    print(f"""
    Today's Date: {date}
    Dice values: {die1}, {die2}, {die3}
    Result (Doublet or Triplet bonus): {bonus}
    Score: {score}
        """)
    
    keep_playing = input('Keep Playing? (yes/no): ').lower().strip() == 'yes'
    # End of loop
# Goodbye message
print(f"\n Thank you for playing the 3-Dice Game {name}! \n")