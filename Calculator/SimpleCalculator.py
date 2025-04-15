# ITSS / OPRE 3311 – Introduction to Programming
# Project: Simple Calculator
# Student Name: Arav Neroth
# Date Completed: 4/14/2025

 # Import necessary modules
import tkinter as tk
from tkinter import messagebox

# initialize main window

root = tk.Tk()
root.title("Simple Calculator")

# intro message 
print("Welcome to the Simple Calculator!")

# StringVar stores and updates the display
display_text = tk.StringVar()

# create and place entry and buttons
entry = tk.Entry(root, textvariable=display_text, font = ("Times New Roman", 20), bd = 10, 
                 relief = tk.RIDGE, justify = 'right')
entry.grid(row = 0, column = 0, columnspan = 4, padx = 10, pady = 10)

# handle button clicks, perform calculations, and display functions.
def update_display(char):
    # add a number or action to the current user input
    current = display_text.get()
    display_text.set(current + str(char))

def clear_display():
    display_text.set("")

def evaluate_expression():
    # solve equation; if it's invalid, send an error message
    try:
        expression = display_text.get()
        # Evaluate using Python's eval function.
        result = eval(expression)
        display_text.set(str(result))

    except ZeroDivisionError:
        messagebox.showerror("Error", "Divided by Zero")

    except Exception:
        messagebox.showerror("Error", "Invalid Expression Entered")

# button layout 
#   Row 1: 7  8  9  /
#   Row 2: 4  5  6  *
#   Row 3: 1  2  3  -
#   Row 4: 0  .  =  +   
#   Row 5:  CLEAR (this is added at end after all the buttons are set up)

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3)
]

# Loop through each button (rows 1-4) configuration, set up its command, and place it.
for (text, row, column) in buttons:

    if text == '=':
        button = tk.Button(root, text=text, font = ("Times New Roman", 20), bd = 5,
                        padx = 20, pady = 20, command = evaluate_expression)
    else:
        # use lambda to pass the label to update_display.
        button = tk.Button(root, text=text, font = ("Times New Roman", 20), bd = 5,
                        padx = 20, pady = 20, command = lambda char = text: update_display(char))
        
    button.grid(row = row, column = column, padx = 5, pady = 5)

# clear button on row 5
clear = tk.Button(root, text='CLEAR', font = ("Times New Roman", 20), bd = 5,
                      padx = 20, pady = 20, command = clear_display)
clear.grid(row = 5, column = 0, columnspan = 4, sticky = "nsew", padx = 5, pady = 5)

# run the python file to start calculator
root.mainloop()
