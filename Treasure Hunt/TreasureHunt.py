# ITSS / OPRE 3311 – Introduction to Programming
# Project: Word Search
# Student Name: Arav Neroth
# Date Completed: 4/6/2025

import random

GRID_SIZE = 3
NUM_TREASURES = 1
treasure_counter = 0

# new empty grid
def create_empty_grid(grid_size):
    return [["empty" for _ in range(grid_size)] for _ in range(grid_size)]


# randomly place treasure
def place_treasures(grid, num_treasures):

    grid_size = len(grid)
    # edge case handling to account for avoiding placing treasure at start
    available_positions = [(i, j) for i in range(grid_size) for j in range(grid_size) if (i, j) != (0, 0)]
    treasure_positions = random.sample(available_positions, num_treasures)

    for row, col in treasure_positions:
        grid[row][col] = "treasure"


# create the grid with randomized treasure 
def create_grid_with_treasures():

    grid = create_empty_grid(GRID_SIZE)
    place_treasures(grid, NUM_TREASURES)
    return grid


# start the game
def initialize_game():

    grid = create_grid_with_treasures()
    player_position = (0, 0)
    return grid, player_position

# change current position
def update_player_position(player_position, move):

    row, col = player_position

    if move == "up":
        new_position = (row - 1, col)

    elif move == "down":
        new_position = (row + 1, col)

    elif move == "left":
        new_position = (row, col - 1)

    elif move == "right":
        new_position = (row, col + 1)

    else:
        raise ValueError("Invalid move direction")
    
    return new_position

# out of bounds assertion
def validate_game_state(player_position, grid_size):

    row, col = player_position
    if not (0 <= row < grid_size and 0 <= col < grid_size):
        print("Player position is out of bounds. Try a move within bounds.")
        return False
    return True


# does current position have treasure
def check_for_treasure(grid, player_position):

    row, col = player_position
    if grid[row][col] == "treasure":
        grid[row][col] = "empty"
        print("You found a treasure!")

        return True
    
    return False

# checks to see if there is any treasuer left
def all_treasures_found(grid):

    for row in grid:
        if "treasure" in row:
            return False
    return True


def main():
    
    print("Welcome to the Treasure Hunt Game!")
    print("Navigate the grid to find hidden treasures.")
    grid, player_position = initialize_game()
    
    while not all_treasures_found(grid):

        move = input("\nEnter your move (up, down, left, right): ").lower().strip()

        try:
            new_position = update_player_position(player_position, move)
            if not validate_game_state(new_position, GRID_SIZE):
                continue  # skip this move and prompt again
            
            # if the move is valid, update it
            player_position = new_position

        except ValueError:
            print("Input not recognized. Please enter a valid move.")
            continue

        else:
            player_position = new_position
            check_for_treasure(grid, player_position)
            
        finally:
            print("\nCurrent Position: ", player_position)
            print("Teasure Found: ", treasure_counter)
            print("Teasure Left: ", NUM_TREASURES - treasure_counter)

    # final statement
    print("\nCongratulations! You found all the treasures.")
    print("Teasure Found: ", NUM_TREASURES)
    print("Teasure Left: 0")

if __name__ == "__main__":
    main()
