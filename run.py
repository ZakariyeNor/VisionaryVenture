#importing math module
import math 

def start_adventure():
    """
    Introduction for the adventure game, telling the user where he/she is, the main goal, advice to choose wisely and asking to start with their name.
    """
    while True:

        print("\nWelcome to the Apple Park Adventure!")
        print("As a tech enthusiast, you have decided to explore the heart of innovation at Apple Park.")
        print("However, as you wander through the sprawling campus, you realize you're lost.")
        print("You will need to choose your path wisely to make it to the highest office.\n")
        print("To play the game alone you must be at least 18 or older. If you are less than 18 and want to play alone please type in (security)")
        
        player_age = input("\nLet's start with your age: ")

        if validate_player_age(player_age):
            #Asking for the name only after age has been validated so player doesn't enter a name if they're not allowed to continue. 
            player_name = input("What's your name: ").strip()
            if validate_player_name(player_name):

                print(f"\nWelcome {player_name}! You are ready to embark on the Apple Park Adventure.")
                print("As you step into the sprawling campus of innovation, you'll face choices that could either guide you to greatness or leave you wandering.")
                print("Trust your instincts, think wisely, and remember, every decision shapes your journey.")
                print("\nGood luck, adventurer! Let the journey begin...\n")
                break

            else:
                print("Name cannot be empty. Please enter a valid name.\n")
            
        else:
            print("Please try again")

def validate_player_age(age_input):
    """
    Makes sure that the user types in number, valid age and has security clearance.
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

def validate_player_name(name):
    """
    Validated that the player's name is not empty and contains only letters and spaces
    """
    if not name: 
        return False
    else:
        #Check if name contains only alphabetic characters and spaces
        return all(part.isalpha() or part.isspace() for part in name)

def adventure_choices():
    choise = input("You start at the Apple Park Visitor Center. Do you explore the store or head straight to the main building? (explore/head) ").lower()
    
    if choise == 'explore':
        print("You spend some time exploring the Visitor Center, admiring the Apple products and grabbing a coffee.")
        choise = input("Do you now want to head to the main building or stay longer? (head/stay) ").lower()
        if choise == 'stay':
            print("You stayed too long, and the offices closed. Game over.")
            
        else:
            print("You decide to head towards the main building.")
            main_building()
    elif choise == 'head':
        main_building()
    else:
        print("Invalid option. Game over.")





























































def main():
    """
    Main function to controll the flow of the game and call all the program from one function
    """

    start_adventure()
    adventure_choices()


#Calling the main function
main()
