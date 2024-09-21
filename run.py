# importing math, os and time modules
import os
import math
import time

# Global variable to store and access the player's name,
# used throughout the functions.
global PLAYER_NAME


def clear():
    """
    Clear function to clean-up the terminal so things don't get messy.
    """
    os.system("cls" if os.name == "nt" else "clear")


def start_adventure():
    """
    Introduction for the adventure game, telling the user where he/she is,
    the main goal, advice to choose wisely and asking to start with their age.
    """
    global PLAYER_NAME
    print("\nWelcome to the Apple Park Adventure!")
    time.sleep(0.25)

    print(
        "As a tech enthusiast, you have decided to explore"
        "the heart of innovation at Apple Park."
    )
    time.sleep(0.25)

    print(
        "However, as you wander through the"
        "sprawling campus, you realize you're lost."
    )
    time.sleep(0.25)

    print(
        "You will need to choose your path wisely to"
        "make it to the highest office.\n"
    )
    time.sleep(0.25)

    print(
        "To play the game alone you must be at least 18 or older."
        "If you are less than 18 and want to"
        "play alone please type in (security)"
    )
    time.sleep(0.25)

    while True:
        player_age = input("\nLet's start with your age: ")
        clear()
        if validate_player_age(player_age):
            break
        else:
            print("Please try again")

    # Asking for the name only after age has been
    # validated so player doesn't enter a
    # name if they're not allowed to continue.

    while True:
        PLAYER_NAME = input("What's your name: ").strip()
        clear()
        if validate_player_name(PLAYER_NAME):
            print(
                f"\nWelcome {PLAYER_NAME}! You are ready to embark on the"
                "Apple Park Adventure."
            )
            print(
                "As you step into the sprawling campus of innovation, you'll"
                "face choices that could either guide you to greatness or"
                "leave you wandering."
                )
            print(
                "Trust your instincts, think wisely, and"
                "remember, every decision shapes your journey."
                )
            print("\nGood luck, adventurer! Let the journey begin...\n")
            return PLAYER_NAME
        else:
            print(
                "Name cannot be empty, Please"
                " enter a valid name (Alphabetic) \n"
                )


def validate_player_age(age_input):
    """
    Makes sure that the user types in number,
    valid age and has security clearance.
    """

    try:
        player_age = int(age_input)
        if player_age < 18:
            print(
                f"You are {player_age} years old,"
                "you need Security House permission to"
                "play the game alone."
                )
            return False
        else:
            return True
    except ValueError:
        if age_input.lower() == 'security':
            return True
        else:
            print(
                "Invalid input. Please enter a"
                "number for age or 'security'.\n"
                )
            return False


def validate_player_name(name):
    """
    Validated that the player's name is
    not empty and contains only letters and spaces
    """
    global PLAYER_NAME
    if not name:
        return False
    else:
        # Check if name contains only
        # alphabetic characters and spaces
        return all(part.isalpha() or part.isspace() for part in name)


def game_over():
    """
    Ends the game and displaying a thankz message.
    """
    global PLAYER_NAME
    print(
        f"\nThank you {PLAYER_NAME} for playing the journey to the"
        "highest office at Apple Park!"
        )
    exit()


def adventure_choices():
    """
    Giving the user the important choice of the
    adventure and calling the main building
    if user takes the right path.
    Calling the game over function if
    user want to stay in the visit center.
    """

    while True:
        choise = input(
            "You start at the Apple Park Visitor Center."
            "Do you explore the store or head straight to"
            "the main building? (explore/head) "
            ).lower()
        clear()

        if choise == 'explore':
            print(
                    "You spend some time exploring the Visitor Center,"
                    "admiring the Apple products and grabbing a coffee."
                    )
            choise = input(
                        "Do you now want to head to the main building"
                        "or stay longer? (head/stay) "
                        ).lower()
            clear()

            while True:
                if choise == 'stay':
                    print(
                        "You stayed too long, and the"
                        "offices closed. Game over."
                        )
                    game_over()

                elif choise == 'head':
                    print(
                        "You decide to"
                        "head towards the main building."
                        )
                    break

                else:
                    print("Invalid option. Please choose 'stay' or 'head'. \n")
                    time.sleep(0.25)

                    print(
                        f"{PLAYER_NAME} you typed {choise}, and it's"
                        " invalid option. Please choose"
                        " 'stay' or 'head' next time. \n"
                        )
                    time.sleep(0.25)

                    print("Let's start again \n")
                    time.sleep(0.25)
                    break

        elif choise == 'head':
            break

        else:
            print("Invalid option. Please choose 'explore' or 'head'. \n")

    main_building()


def main_building():
    """
    Inform that the user arrived The Spaceship, give options and
    if he takes the right path call the executive corridor function
    otherwise error message and game over.
    """
    while True:

        choise = input(
            "You arrive at the entrance of the Apple Park main"
            "building, also known as 'The Spaceship.' The circular"
            "glass structure is impressive. Do you enter through the"
            "main lobby or take the side entrance near the Steve Jobs"
            "Theater? (lobby/side) "
            ).lower()
        clear()

        if choise == 'lobby':
            print(
                "You enter through the sleek main lobby,"
                "greeted by natural light and a massive"
                "open space."
                )
            break

        elif choise == 'side':
            print(
                "You enter through a smaller side door"
                "near the Steve Jobs Theater. It's quieter"
                "but feels exclusive."
                )
            break

        else:
            print(
                "Invalid option. Please choose"
                "'lobby' or 'side'. \n"
            )

    executive_corridor()


def executive_corridor():
    """
    Function to give the user two options, go to the
    highest office or go high secret area, and depends
    on the users choise to keep playin or being escorted
    out by security and loose the game
    """

    while True:
        choise = input(
            "Inside the building, you spot two elevators."
            "One says 'Executive Floors,' and the other"
            "'R&D Labs.' Which one do you take? (executive/labs) "
            ).lower()
        clear()

        if choise == 'executive':
            print(
                "You take the executive elevator up"
                "towards the highest office."
            )
            break

        elif choise == 'labs':
            print(
                "You ended up in the Research and"
                "Development Labs, where everything is top"
                "secret. You are escorted out by security."
                "Game over."
            )
            game_over()
        else:
            print(
                "Invalid option. Please choose"
                "'executive' or 'labs'. \n"
            )

    top_office()


def top_office():
    """
    Function for going either to design team or top office.
    And calling the ceo office function if the user chooses
    the right path
    """
    while True:
        choise = input(
            "You exit the elevator and walk down the executive"
            "corridor. Do you want to visit the design team offices"
            "on this floor or go straight to the top"
            "office? (design/top) "
            ).lower()
        clear()

        if choise == 'design':
            print(
                "You meet the design team, but the office"
                "you're looking for isn't here. You lose the game."
            )
            game_over()

        elif choise == 'top':
            print("You head towards the top office of Apple.")
            break
        else:
            print(
                "Invalid option. Please"
                "choose 'design' or 'top'. \n"
            )

    ceo_office()


def ceo_office():
    """
    Gives the player a polite choice to
    either wait for the Apple CEO to invite
    him/her in, or enter the office and ask what he/she wants.
    """

    while True:
        choise = input(
            "You arrive at Tim Cook's office."
            "The door is slightly open. Do you"
            "enter or wait? (enter/wait) "
            ).lower()
        clear()

        if choise == 'enter':
            print(
                "You meet Tim Cook, and he greets you"
                "warmly. You’ve reached the highest"
                "office in Apple Park!"
                )
            break

        elif choise == 'wait':
            print(
                "You wait too long, and the"
                "office closes. Game over."
                )
            game_over()
        else:
            print(
                "Invalid option. Please"
                "choose 'enter' or 'wait'. \n"
                )

    final_decision()


def final_decision():
    """
    Function for the final step to win
    or loose the adventure game.
    """

    while True:
        choise = input(
            "Do you ask Tim Cook for advice on your next"
            "move, or just leave the office? (ask/leave) "
            ).lower()
        clear()

        if choise == 'leave':
            print(
                "You left without talking to Tim Cook."
                "You missed your chance. Game over."
                )
            game_over()

        elif choise == 'ask':
            print(
                "Tim Cook shares valuable"
                "insights with you. You win the game!"
            )
            break
        else:
            print(
                "Invalid option."
                "Please choose 'leave' or 'ask'. \n"
            )

    exit_options()


def exit_options():
    """
    Options to exit the Park
    """
    global PLAYER_NAME

    while True:
        print(
            f"Adventurer {PLAYER_NAME}"
            "you have 5 options to exit Apple Park:\n"
            )

        exit_options_list = [
            "1. Exit through the main gate and head to the Visitor Center",
            "2. Leave by the side gate near the Steve Jobs Theater.",
            "3. Exit using the underground parking near the R&D Labs.",
            "4. Take the rooftop helicopter if you're feeling adventurous.",
            "5. Walk out through the beautifully landscaped garden paths."
        ]

        for option in exit_options_list:
            print(option)

        choise = input(
            f"\n Choose which path you want take to exit the Apple Park: "
            )
        clear()

        if choise in ["1", "2", "3", "4", "5"]:
            if choise == "1":
                print("\nYou exited through the main gate.\n")
                break
            elif choise == "2":
                print(
                    "\nYou exited the side gate"
                    "near the Steve Jobs Theater.\n"
                    )
                break
            elif choise == "3":
                print(
                    "\nYou exited using the underground"
                    "parking near the R&D Labs.\n"
                )
                break
            elif choise == "4":
                print("\nYou took helicoter from the rooftop.\n")
                break
            elif choise == "5":
                print(
                    "\nYou exited out through the"
                    "beautifully landscaped garden paths.\n"
                    )
                break
        else:
            print(f"{choise} Invalid. Please enter 1 - 5\n")

    game_over()


# Calling the main function
if __name__ == "__main__":
    """
    Main function to controll the flow of the game and
    call all the program from one function
    """

    clear()
    start_adventure()
    adventure_choices()
