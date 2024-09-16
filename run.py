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
                return player_name

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
    """
    Giving the user the important choice of the adventure and calling the main building if user takes the right path.
    Returns the result of the user's decision.
    """

    while True:
        choise = input("You start at the Apple Park Visitor Center. Do you explore the store or head straight to the main building? (explore/head) ").lower()
            
        if choise == 'explore':
                print("You spend some time exploring the Visitor Center, admiring the Apple products and grabbing a coffee.")
                choise = input("Do you now want to head to the main building or stay longer? (head/stay) ").lower()

                if choise == 'stay':
                    print("You stayed too long, and the offices closed. Game over.")
                    return 'game_over'

                elif choise == 'head':
                    print("You decide to head towards the main building.")
                    return 'main_building'
                   
                else:
                    print("Invalid option. Please choose 'stay' or 'head'. \n")

        elif choise == 'head':
            return 'main_building'
                
        else:
            print("Invalid option. Please choose 'explore' or 'head'. \n")

def game_loop(player_name):
    while True:
        result = adventure_choices()
        building = main_building()
        higher_office = top_office()
        ceo = ceo_office()
        exits = exit_options(player_name)

        if result == 'main_building':
            main_building()
        elif result == 'game_over':
            print("Game Over. You can try again!")
            break
        elif result == 'invalid_choice':
            print("You made an invalid choice. Please follow the instructions next time.")
            break
        elif building == 'executive_corridor':
            executive_corridor()

        elif higher_office == 'top_office':
            top_office()

        elif ceo == 'ceo_office':
            ceo_office()

        elif final == 'final_decision':
            final_decision()

        elif exits == 'exit_options':
            exit_options(player_name)

        else:
            print(F"An unexpected error occurred.")
            break 

def main_building():
    """
    Inform that the user arrived The Spaceship, give options and if he takes the right path call the executive corridor function otherwise error message and game over from the executive corridor function
    """
    while True:

        choise = input("You arrive at the entrance of the Apple Park main building, also known as 'The Spaceship.' The circular glass structure is impressive. Do you enter through the main lobby or take the side entrance near the Steve Jobs Theater? (lobby/side) ").lower()
        
        
        if choise == 'lobby':
            print("You enter through the sleek main lobby, greeted by natural light and a massive open space.")
            return 'executive_corridor'
        
        elif choise == 'side':
            print("You enter through a smaller side door near the Steve Jobs Theater. It's quieter but feels exclusive.")
            return 'executive_corridor'

        else:
            print("Invalid option. Please choose 'lobby' or 'side'. \n")

def executive_corridor():
    """
    Function to give the user two options, go to the highest office or go high secret area, and depends the choise either keep playin or being escorted out by security and loose the game
    """
    choise = input("Inside the building, you spot two elevators. One says 'Executive Floors,' and the other 'R&D Labs.' Which one do you take? (executive/labs) ").lower()

    if choise == 'executive':
        print("You take the executive elevator up towards the highest office.")
        return 'top_office'

    elif choise == 'labs':
        print("You ended up in the Research and Development Labs, where everything is top secret. You are escorted out by security. Game over.")
        return 'game_over'
    else:
        print("Invalid option. Please choose 'executive' or 'labs'. \n")

def top_office():
    """
    Function for going either to design team or top office. And calling the ceo office function if the user chooses the right path
    """

    choise = input("You exit the elevator and walk down the executive corridor. Do you want to visit the design team offices on this floor or go straight to the top office? (design/top) ").lower()

    if choise == 'design':
        print("You meet the design team, but the office you're looking for isn't here. You lose the game.")
        return 'game_over'

    elif choise == 'top':
        print("You head towards the top office of Apple.")
        return 'ceo_office'
    else:
       print("Invalid option. Please choose 'design' or 'top'. \n")

def ceo_office():
    """
    Function to give the user to be bolite and wait the Apple CEO or go in his office and ask your question
    """

    choise = input("You arrive at Tim Cook's office. The door is slightly open. Do you enter or wait? (enter/wait) ").lower()

    if choise == 'enter':
        print("You meet Tim Cook, and he greets you warmly. You’ve reached the highest office in Apple Park!")
        return 'final_decision'

    elif choise == 'wait':
        print("You wait too long, and the office closes. Game over.")
        return 'game_over'
    else:
        print("Invalid option. Please choose 'enter' or 'wait'. \n")

def final_decision():
    """
    Function for the final step to win or loose the adventure game
    """
    choise = input("Do you ask Tim Cook for advice on your next move, or just leave the office? (ask/leave) ")

    if choise == 'leave':
        print("You left without talking to Tim Cook. You missed your chance. Game over.")
        return 'game_over'

    elif choise == 'ask':
        print("Tim Cook shares valuable insights with you. You win the game!")
        return 'final_decision'
    else:
        print("Invalid option. Please choose 'leave' or 'ask'. \n")

def exit_options(player_name):
    """
    Options to exit the Park
    """
    print(f"Adventurer {player_name} you have 5 options to exit Apple Park:")

    exit_options_list = [
        "1. Exit through the main gate and head to the Visitor Center",
        "2. Leave by the side gate near the Steve Jobs Theater.",
        "3. Exit using the underground parking near the R&D Labs.",
        "4. Take the rooftop helicopter if you're feeling adventurous.",
        "5. Walk out through the beautifully landscaped garden paths."
    ]

    for option in exit_options_list:
        return option

    print(f"Thank you {player_name} for playing the journey to the highest office at Apple Park!")

def main():
    """
    Main function to controll the flow of the game and call all the program from one function
    """

    start_adventure()
    player_name = start_adventure()
    game_loop(player_name)
    adventure_choices()
    main_building()
    executive_corridor()
    top_office()
    ceo_office()
    final_decision()
    exit_options(option)


#Calling the main function
main()


