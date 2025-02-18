"""
Developer: Arav Neroth 
Date: February 18, 2025
Descript: System that generates flash cards for basic math
Class: ITSS 3311.003
"""
# import necessary modules
import random
# intro message
name = input("Please enter your name, one word only: ")
# welcome message
print(f"Hi, {name}. Welcome to the 3311 Flashcard system!")
# loop for play again
while True:
# prompt user for the type of problem
    problem_type = input("""
Choose the problem type.
Enter "A" for addition, "S" for subtraction, "M" for multiplication, and "D" for division: """).upper()
    
    low = int(input("""
Set the range (lowest & highest) for the values in your problems.
                
Enter the lowest value for the problem numbers: """))
    
    high = int(input("Enter the highest value for the problem numbers: "))
    number_of_problems = int(input("Enter the number of problems you wish to work: "))

    # intialize other vars for later stats & answer comparison
    attempted = 0
    correct = 0
    answer = 0
    user_answer = 0

    # loop for number of problems
    for _ in range(number_of_problems):
        # generate random factors within the specified range
        factor1 = random.randint(low, high)
        factor2 = random.randint(low, high)

        # addition
        if problem_type == 'A':
            # solve, then prompt for user answer. if they match, add point
            # add point to attempted once problem is answered
            # same functionality & logic for other cases
            answer = factor1 + factor2 
            user_answer = int(input(f"{factor1} + {factor2} = "))
            if (user_answer == answer):
                print("Correct. Great job!")
                correct += 1
            else:
                print(f"Incorrect. Correct answer is {answer}.")

            attempted += 1

        # subtraction      
        elif problem_type == 'S':
            answer = factor1 - factor2 
            user_answer = int(input(f"{factor1} - {factor2} = "))
            if (user_answer == answer):
                print("Correct. Great job!")
                correct += 1
            else:
                print(f"Incorrect. Correct answer is {answer}.")
            attempted += 1

        # multiplication      
        elif problem_type == 'M':
            answer = factor1 * factor2 
            user_answer = int(input(f"{factor1} * {factor2} = "))
            if (user_answer == answer):
                print("Correct. Great job!")
                correct += 1
            else:
                print(f"Incorrect. Correct answer is {answer}.")
            attempted += 1

        # division      
        elif problem_type == 'D':
            print("(Round to the nearest tenth)")
            # catch zero division 
            if(factor2 == 0):
                factor2 = random.randint(1, high)
            # convert to float and round to nearest tenth since answer may be a decimal
            answer = round(float(factor1 / factor2), 1) 
            user_answer = float(input(f"{factor1} / {factor2} = "))
            if (user_answer == answer):
                print("Correct. Great job!")
                correct += 1
            else:
                print(f"Incorrect. Correct answer is {answer}.")
            attempted += 1
        
    # final stats 
    percent_correct = float(correct/attempted)
    print(f"""
Problems correct: {correct}
Problems attempted: {attempted}
Percentage correct: {percent_correct:.2%}
          """)
    
    # if user is done, break loop
    if (input("Would you like to play again? Enter Y/N: ").upper() == "N"):
        break
# exit message
print(f"Thank you, {name}, for using the 3311 Flashcard system!")