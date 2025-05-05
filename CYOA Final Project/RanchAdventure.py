# RanchAdventure.py
# Name: Arav Neroth
# Date: May 4 2025
# Description: The Re-Invention of Ranch Choose Your Own Adventure game.

import sys

# ending tracker
done_endings = set()


# gets name
def get_name():
    return input("Enter your name: ")

# welcome message
def print_welcome(name):

    print(f"\nWelcome, {name}, to the Re-Invention of Ranch!")
    print("How To Play: Enter the number of your choice to make decisions.")
    print("Your choices determine the path and ending you achieve.\n")

# starts game- "1" to Look or "2" to Recreate.
def start_game():

    print("It’s gone! One sorrowful morning, every trace of ranch has vanished from the world.")
    print("1. Look for any remaining ranch.")
    print("2. Try to recreate ranch.")
    return input_choice("Enter 1 or 2: ", ["1", "2"])

# returns the story text corresponding to the given path
def get_story(path):

    stories = {
        "choose_team": "\nDo you work alone or with other people?",
        "solo_ingredient": "\nYou gather ingredients you think you need to make up ranch. You need the final few elements.",
        "solo_secondary": "\nIt's coming together nicely! What else do you think it needs?",
        "balance_stage": "\nExcellent! It's almost done! How do you balance it out?",
        "dangerous_work": (
            "\nSomething's different about this ranch batch now...it has more...POTENTIAL!\n"
            "You can't let up now - even though the ranch is 'technically' complete, leaving it like this would be unjust...\n\n"
            "You push past your, and the recipe's limits. What experimental ingredient do you add?"
        ),
        "super_choice": "\nYou've finally done it! You've made Super Ranch! But now the final question- What do you do?"
    }
    return stories[path]

# list of (key, description) tuples for the given path
def get_choices(path):

    choices = {
        "choose_team": [("1", "Work with a team of specialists."), ("2", "Go solo.")],
        "solo_ingredient": [("1", "Butter"), ("2", "Sour Cream")],
        "solo_secondary": [("1", "Mayo"), ("2", "Pickle Juice")],
        "balance_stage": [("1", "Water"), ("2", "Sugar")],
        "dangerous_work": [("1", "Maple Syrup"), ("2", "Worcestershire Sauce")],
        "super_choice": [("1", "Everyone deserves super ranch (Share with the world)!"), ("2", "It's...TOO GOOD! (Keep it all to yourself).")]
    }
    return choices[path]

# prints story + choices, then checks for valid user input
def make_choice(path):

    print(get_story(path))
    options = get_choices(path)
    for key, desc in options:
        print(f"{key}. {desc}")
    valid = [v for v, _ in options]
    prompt = f"Enter {' or '.join(valid)}: "
    return input_choice(prompt, valid)

# keeps track of endings achieved. displays special message if all are found
def record_ending(label):
    done_endings.add(label)
    print(f"Endings achieved ({len(done_endings)}/{5}): {', '.join(sorted(done_endings))}")
    if len(done_endings) == 5:
        print("*** Astounding! You've discovered all possible endings! Thanks for exploring every path! ***\n")
        print("*** You've earned the title of RANCH REVOLUTIONARY ***")

# prompts for play again with error handinling
def play_again():
    return input_choice("\nPlay again? (Y/N): ", ["Y", "N", "y", "n"]).upper()

# ending message display
def print_end_message(name, ending):
    print(f"\nCongratulations, {name}! {ending}")
    print("Thank you for playing!\n")

# catches invalid input 
def input_choice(prompt, valid_choices):

    choice = input(prompt).strip()
    while choice not in valid_choices:
        choice = input("Invalid choice. " + prompt).strip()
    return choice


def main():
    name = get_name()
    print_welcome(name)

    while True:
        #  choose to recreate after any number of "look option"
        while True:
            choice = start_game()
            if choice == "1":
                print("\nYou don't find anything... it's really gone :( \n")
            else:
                break

        # team vs. solo branch
        choice = make_choice("choose_team")
        if choice == "1":
            ending_label = "Betrayal Ending"
            ending_text = (
                "After years of hard work, you and your team successfully recreate ranch! The world is saved! \nUnfortunately, your team got greedy and silenced you, monopolizing ranch as a delicacy for the elite. \nBetrayal Ending (1/5)"
            )
            print_end_message(name, ending_text)
            record_ending(ending_label)

        else:
            # solo Path ingredient 1
            while True:
                if make_choice("solo_ingredient") == "2":
                    break
                print("\nBad combination... It ruined the whole mixture! Try again.")

            # ingredient 2
            while True:
                sec = make_choice("solo_secondary")
                if sec == "2":
                    print("\nBad combination... It ruined the whole mixture! Try again.")
                    
                    # re-pick the ingredient 1
                    while True:
                        if make_choice("solo_ingredient") == "2":
                            break
                        print("\nBad combination... Try again.")
                else:
                    break

            # balance stage
            bal = make_choice("balance_stage")
            if bal == "1":
                ending_label = "Recreation Ending"
                ending_text = (
                    "YOU DID IT!! RANCH IS BACK! It’s so tasty!....but could one of the "
                    "ingridents have made it even better? \nRecreation Ending (2/5)"
                )
                print_end_message(name, ending_text)
                record_ending(ending_label)
            else:
                # experimental branch
                exp = make_choice("dangerous_work")
                if exp == "1":
                    ending_label = "Poisoned Ending"
                    ending_text = (
                        "The combination was so heinous you passed away, ruining the batch "
                        "of ranch and your soul. \nPoisoned Ending (3/5)"
                    )
                    print_end_message(name, ending_text)
                    record_ending(ending_label)
                else:
                    # Super Ranch endings
                    sup = make_choice("super_choice")
                    if sup == "1":
                         # selfless ending 
                        ending_label = "Super Ending"
                        ending_text = (
                            "Super Ranch for everyone! You are hailed as The Ranch Savior! "
                            "With your Super Ranch, you are unstoppable! \nYou set up mass "
                            "predictions factories and pay your employees in Ranch servings. "
                            "You make billions and there are dog parks and shrines named in your honor.\nEnding (5/5)"
                        )
                    else:
                        # selfish ending
                        ending_label = "Selfish Ending"
                        ending_text = (
                            "You keep Super Ranch all to yourself and live in ranch bliss! The world "
                            "slowly recovers from the loss of ranch. \nYou however, are living your "
                            "best Ranch life! \nSelfish Ending (4/5)"
                        )
                    # wrap up path
                    print_end_message(name, ending_text)
                    record_ending(ending_label)

        if play_again() != "Y":
            break

if __name__ == "__main__":
    main()
