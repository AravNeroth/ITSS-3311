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


def generate_grid(words, size=10):
 """
 Generates a word search grid with the given words placed in random
positions.
 """
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