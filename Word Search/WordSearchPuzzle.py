# ITSS / OPRE 3311 – Introduction to Programming
# Project: Word Search
# Student Name: Arav Neroth
# Date Completed: 3/27/2025

import random
import re
import os

def read_words(file_name):
    """Reads words from a file in the 'Word Search' folder and returns a list."""
    base_dir = os.path.join(os.getcwd(), "Word Search")
    file_path = os.path.join(base_dir, file_name)
    try:
        with open(file_path, "r") as f:
            return [x.strip().upper() for x in f.readlines()]
    except FileNotFoundError:
        print(f"File not found in {base_dir}. Please check the file name and try again.")
        return []

def write_results(file_name, results):
    """Writes the game results to a file in the 'Word Search' folder."""
    base_dir = os.path.join(os.getcwd(), "Word Search")
    file_path = os.path.join(base_dir, file_name)
    try:
        with open(file_path, "w") as f:
            f.write(results)
        print(f"Results have been written to {file_path}")
    except Exception as e:
        print(f"Error writing to file: {e}")

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
    
    for i in range(size):
        for j in range(size):
            if grid[i][j] == ' ':
                grid[i][j] = chr(random.randint(65, 90))
    
    return grid

def print_grid(grid):
    """Prints the word search grid."""
    for row in grid:
        print(" ".join(row))
    print("\n")

def find_word(grid, word):
    """Finds the word in the grid and returns its coordinates."""
    size = len(grid)
    for row in range(size):
        for col in range(size):
            if grid[row][col] == word[0]:
                if col + len(word) <= size and all(grid[row][col + i] == word[i] for i in range(len(word))):
                    return [(row, col + i) for i in range(len(word))]
                if row + len(word) <= size and all(grid[row + i][col] == word[i] for i in range(len(word))):
                    return [(row + i, col) for i in range(len(word))]
    return []

def interact_and_locate_words(grid, words):
    """Allows the user to find words in the grid by inputting coordinates."""
    found_words = []
    for word in words:
        print(f"Find the word: {word}")
        print("Your input should look like this: 4,3 4,4 4,5 4,6")
        user_input = input("Enter the coordinates: ")
        try:
            coordinates = [tuple(map(int, coord.split(','))) for coord in user_input.split()]
        except ValueError:
            print("Invalid input format. Please enter row,col pairs.")
            continue

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
    file_name = input("Enter the input file name containing the words: ")
    words = read_words(file_name)
    if not words:
        return
    
    grid = generate_grid(words)
    print("\nWord Search Grid:")
    print_grid(grid)
    
    found_words = interact_and_locate_words(grid, words)
    
    results = f"Words found: {', '.join(found_words)}\nTotal: {len(found_words)}/{len(words)}\nPercentage: {(len(found_words) / len(words)) * 100:.2f}%"
    print("\nGame Over!", results)
    
    output_file = "game_results.txt"
    write_results(output_file, results)
    print(f"Results have been written to {output_file}")

if __name__ == "__main__":
    main()
