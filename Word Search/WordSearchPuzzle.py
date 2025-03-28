# ITSS / OPRE 3311 – Introduction to Programming
# Project: Word Search
# Student Name: Arav Neroth
# Date Completed: 3/27/2025

import random
import re

word_list = []
word_list_path = r"C:\Users\reach\OneDrive\Documents\GitHub\ITSS-3311\Word Search\GameWords.txt"

def read_words(file_name):
    try:
        with open(word_list_path, "r") as f:
            for x in f:
                word_list.append(x.strip())
    except FileNotFoundError:
        print("File not found. Path may be incorrect, or file may not exist")

def write_results(file_name, results):
    with open(f"{file_name}", "w") as f:
        f.write(f"{results}")

"""
Generates a word search grid with the given words placed in random
positions.
"""
def generate_grid(words, size=10):

    grid = [[' ' for _ in range(size)] for _ in range(size)]

    for word in words:
        placed = False
        while not placed:
            direction = random.choice(['horizontal', 'vertical'])
            if direction == 'horizontal':
                row = random.randint(0, size - 1)
                col = random.randint(0, size - len(word))
                if all(grid[row][col + i] in [' ', word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row][col + i] = word[i]
                        placed = True
            else:
                row = random.randint(0, size - len(word))
                col = random.randint(0, size - 1)
                if all(grid[row + i][col] in [' ', word[i]] for i in range(len(word))):
                    for i in range(len(word)):
                        grid[row + i][col] = word[i]
                    placed = True

    # Fill the remaining empty spaces with random letters
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = chr(random.randint(65, 90))

    return grid

def print_grid(grid):
    """
    Prints the word search grid with borders.
    """
    size = len(grid)
    print(" " + " ".join([str(i) for i in range(size)]))
    print(" +" + "---" * size + "+")
    for i, row in enumerate(grid):
        print(f"{i}| " + " ".join(row) + " |") 
    print(" +" + "---" * size + "+") 

def find_word(grid, word):
    """
    Finds the word in the grid and returns its coordinates.
    """
    size = len(grid)
    coordinates = []
    for row in range(size):
        for col in range(size):
            if grid[row][col] == word[0]:
                # Check horizontal
                if col + len(word) <= size and all(grid[row][col + i] == word[i] for i in range(len(word))):
                    coordinates = [(row, col + i) for i in range(len(word))]
                    return coordinates
                # Check vertical
                if row + len(word) <= size and all(grid[row + i][col] ==
                    word[i] for i in range(len(word))):
                    coordinates = [(row + i, col) for i in range(len(word))]
                    return coordinates
    return coordinates

def interact_and_locate_words(grid, words):
    """
    Allows the user to interact and locate words in the grid.
    """
    found_words = []
    for word in words:
        print(f"Find the word: {word}")
        user_input = input("Enter the coordinates (row,col) separated by spaces: ")
        coordinates = [tuple(map(int, coord.split(','))) for coord in user_input.split()]

        actual_coordinates = find_word(grid, word)

        if coordinates == actual_coordinates:
            found_words.append(word)
            print(f"Found {word} at {coordinates}")
            # Highlight found word in the grid
            for (row, col) in coordinates:
                grid[row][col] = grid[row][col].lower()
        else:
            print(f"{word} not found. Actual coordinates: {actual_coordinates}")

    return found_words



def main():
    read_words("GameWords.txt")
    print(word_list)
'''
 PRINT intro message
 PROMPT user for input file name
 READ words from input file
IF words is None:
 RETURN
 GENERATE word search grid
 PRINT word search grid
 INITIALIZE list for found words
FOR each word in words:
 PRINT prompt to find word
 FIND word in grid
IF found:
 ADD word to found words
 PRINT found message
ELSE:
 PRINT not found message
 PREPARE results summary
 WRITE results to output file
 PRINT completion message
'''
if __name__ == "__main__":
    main()