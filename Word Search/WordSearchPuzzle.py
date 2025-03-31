# ITSS / OPRE 3311 – Introduction to Programming
# Project: Word Search
# Student Name: Arav Neroth
# Date Completed: 3/27/2025

import random
import re
import os


# used google eamples to use OS package to find how to specify where I wanted the program to search for the files
# I have my python files organized through GitHub, so this is how I got it to accuratly write and read files on my machine
def read_words(file_name):
    base_dir = os.path.join(os.getcwd(), "Word Search")
    file_path = os.path.join(base_dir, file_name)
    
    try:
        with open(file_path, "r") as f:
            return [x.strip().upper() for x in f.readlines()]
    except FileNotFoundError:
        print(f"File not found in {base_dir}. Please check the file name and try again.")
        return []

def write_results(file_name, results):
    # used OS import to specify where I wanted the file to be created
    base_dir = os.path.join(os.getcwd(), "Word Search")
    file_path = os.path.join(base_dir, file_name)
    try:
        with open(file_path, "w") as f:
            f.write(results)
        print(f"Results have been written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

# sample code that iterates throughout the word list to place them randomly horizonatally or vertically
def generate_grid(words, size=10):
    """Generates a word search grid with given words randomly placed."""
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

    # after placing the words, fill in the blanks with random letters of the alphabet
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = chr(random.randint(65, 90))
    
    return grid

# decided to print it differently from the sample code by adding a space inbetween each letter and moving to the next line
def print_grid(grid):
    for row in grid:
        print(" ".join(row))
    print("\n")

# sample code that works by checking if entered coordinates matches the word cord by using regex
def find_word(grid, word):

    size = len(grid)

    # look horizontally for matches
    for row in range(size):
        # didn't know how to seach entire rows/col with re so i googled how to do it
        row_str = "".join(grid[row])
        match = re.search(word, row_str)
        if match:
            return [(row, match.start() + i) for i in range(len(word))]
        
    # look vertically for matches    
    for col in range(size):
        col_str = "".join(grid[row][col] for row in range(size))
        match = re.search(word, col_str)
        if match:
            return [(match.start() + i, col) for i in range(len(word))]
                
    # no horizontal or verticle matches, it returns empty
    return []


# takes user coords, finds the actual coords of word, then checks if they match. if they do, add to found_words 
def interact_and_locate_words(grid, words):
    found_words = []
    for word in words:
        print(f"Find the word: {word}")
        print("Your input should look like this: 1,3 1,4 1,5")
        user_input = input("Enter the coordinates: ")

        # using re for incorrect user formatting (googled the expression i needed)
        if not re.match(r'^(\d+,\d+)( \d+,\d+)*$', user_input):
            print("Invalid input format. Please enter row,col pairs separated by spaces.")
            continue
        
        coordinates = [tuple(map(int, coord.split(','))) for coord in user_input.split()]
        actual_coordinates = find_word(grid, word)

        if coordinates == actual_coordinates:
            found_words.append(word)
            print(f"Found {word} at {coordinates}")
            for (row, col) in coordinates:
                grid[row][col] = grid[row][col].lower()
        else:
            print(f"{word} not found. Actual coordinates: {actual_coordinates}")

    return found_words

def main():
    print("Welcome to the Word Search Puzzle Game!")
    file_name = input("Enter the input file name containing the words (your_file.txt): ")

    words = read_words(file_name)
    if not words:
        return
    
    grid = generate_grid(words)
    print("\nWord Search Grid:")
    print_grid(grid)
    
    found_words = interact_and_locate_words(grid, words)
    
    # I used ChatGPT for output file bc I wanted my results file was nicely formatted, and I knew it was possible but i didn't know how to do it optimally 
    # dictionary 'results', line 1 is all the words found by user, line 2 is how many words found out of total words, line 3 is the found percentage
    results = f"Words found: {', '.join(found_words)}\nTotal: {len(found_words)}/{len(words)}\nPercentage: {(len(found_words) / len(words)) * 100:.2f}%"
    
    print("\nGame Finished!", results)
    output_file = "game_results.txt"
    write_results(output_file, results)
    print(f"Results have been written to {output_file}")

if __name__ == "__main__":
    main()
