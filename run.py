#importing math module
import math 

def start_adventure():
    """
    Introduction for the adventure game, telling the user where he/she is, the main goal, advise to choose wisely and asking to star with their name.
    """
    while True:

        print("\nWelcome to the Apple Park Adventure!")
        print("As a tech enthusiast, you have decided to explore the heart of innovation at Apple Park.")
        print("However, as you wander through the sprawling campus, you realize you're lost.")
        print("You will need to choose your path wisely to make it to the highest office.\n")
        print("To play the game alone you must be minimum 18 or older. If you are less than 18 and want to play alone please type in (security)")
        
        player_age = input("\nLet's start with your age: ")
        player_name = input("What's your name: \n").strip()

        if validate_player_age(player_age):
            if player_name:
                print(f"Welcome {player_name}! to the Apple Park Adventure.")
                break

            else:
                print("Name cannot be empty. Please enter a valid name.\n")
            
        else:
            print("Please try again")

def validate_player_age(age_input):
    """
    Makes sure that the user types in number, valid age and have security clearency.
    """

    try:
        player_age = int(age_input)
        if player_age < 18:
            print(f"You are {player_age} years old, you need Security House permission to play the game alone.")
            return False
        else:
            return True
    except ValueError:
        if age_input.lower() == 'security':
            return True
        else:
            print("Invalid input. Please enter a number for age or 'security'.\n")
            return False



start_adventure()