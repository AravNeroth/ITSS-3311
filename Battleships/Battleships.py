# ITSS / OPRE 3311 – Introduction to Programming
# Project: Battleship Game
# Student Name: Arav Neroth
# Date Completed: 2/27/2025

# Import necessary modules
import random
# Display intro message
print("""
Welcome to the Battleship Game!    
Try to sink all the battleships by guessing their locations.
The board size is 5x5 and there are 3 ships to sink.
      """)
# Initialize the game board and ships
board_size = 5
num_ships = 3
board = [['O'] * board_size for _ in range(board_size)]
# Place the ships randomly on the board using a while loop and selection statement
ships = {}
# generate 2 numbers, check if the numbers exist in ships{}. If they dont, create a new ship with these coordinates
while len(ships) < 3:
    position = (random.randint(0, 4), random.randint(0, 4))
    if position not in ships:
        ships[position] = False
# store user guesses to later check against the ship locations
guesses = []
# Initialize counters for attempts and hits
attempts = 0
hits = 0
# Start main game loop
while hits < num_ships:
  # Print the game board after each guess using a for loop
 for row in board:
    print(" ".join(row))
 try:
    # Prompt user for their guess
    guess_row = int(input("\nGuess Row (1-5): ")) -1
    guess_col = int(input("Guess Col (1-5): ")) -1
 except ValueError:
    print("Invalid input. Please enter numbers between 1 and 5.")
    continue
 # Check if the guess is valid and not a duplicate
 if (guess_row, guess_col) in guesses:
    print("You already guessed that location. Try again.")
 elif 0 <= guess_row < board_size and 0 <= guess_col < board_size:
    attempts += 1
    guesses.append((guess_row, guess_col))
    # Check if the guess is a hit or miss
    if (guess_row, guess_col) in ships:
        print("Hit!")
        hits += 1
        ships[(guess_row, guess_col)] = True
        board[guess_row][guess_col] = 'X'
    else:
        print("Miss!")
        board[guess_row][guess_col] = '-'
 else:
    print("Invalid input. Please enter numbers between 0 and 4.")
 
 # End game and display results
print(f"Congratulations! You sunk all the battleships in {attempts} attempts.")
for row in board:
    print(" ".join(row))