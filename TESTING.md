# Testing The Apple Park Adventure

In this section, we aim to demonstrate that comprehensive testing has been conducted on the project to ensure it functions as expected and provides a smooth user experience. Each feature of the project has been meticulously tested to validate its proper functioning, ensuring that the user can achieve their goals without any hindrance. The focus is on presenting a well-structured testing process, covering various scenarios and outcomes to prove the reliability and usability of the project.

## Testing Step by Step

Testing if the game goes step by step and shows the right content every step. 

    The following sections detail the tests performed on "The Apple Park Adventure" game, including functional checks, error handling, and compliance with coding standards. Each test case describes the steps taken, the expected outcomes, and any issues encountered along the way, along with their resolutions. This thorough testing ensures that the game behaves as intended and provides a seamless experience for the users.

##### Testing 1

- Testing introduction text, age and name and they working as they should. 
  - When user enter age older than 18 or have security clearence from the Security House, then the user can go to the next step where user must type in only name (alphabetic) then he/she can start the adventure. Otherwise user can't go to the next step, it'll be loop asking same question only: if user don't have security clearence, younger then 18 or types alphabetic in age input or number in name input or empty in name input. The introductions and information of the adventure works also as they should, the text prints out 0.25 seconds after one another.
  - User will be informed that he/she must enter valid name, age, security clearence from the Security House or that the name input can't be empty.
- Here is screenshots of the testing name and age:

![Adventure Intro and Age](documentation/intro.png) ![Security Clearence](documentation/age_valid.png) ![Name Check](documentation/name_clear.png) ![Name Loop](documentation/loop.png)

- When I tested the functions call, I get help with my mentor. And my mentor told me that I invoked all the functions three times and to fix this I use while loop and break the condition if the user chooses right option and call the next function inside the while loop scope, otherwise call the game over function so the game exits and tells the user that he/she loose the game.
- I had also unstyled text and the output informations and input choices made the screen hard to read and find the right text so I fix this to add time between print outputs and clear function (Added time and os modules.) To use time when printing out informations and clear the informations before the user types in one of the options.
- The game over conditions works like string and to fix this I added exit method in the game over function.
- When it comes calling the functions I called them once from the functions and the main function.

 ##### Testing 2

This is direct path to win the Apple Park Adventure. User have one of the options to choose and if the user chhose right one it goes the direct path until the exit options, and user can choose which he/she want to exit and no matter which one it prints out the one that the user chooses and calls the game over function. If user chooses the wrong one it can go to the another path that can be end to the win path or the loose path. If user enters something else it informs to choose only one of these two options. 

- Direct win path
  - Age: 24
  - Name: Daiel
  - choice 1: explore
  - choice 2: head
  - choice 3: side
  - choice 4: executive
  - choice 5: top
  - choice 6: enter
  - choice 7: ask
  - exit option
- Result = no error

The Testing 2 screenshots:

![Win Path 1](documentation/first_win_option.png)
![Win Path 2](documentation/second_win.png)
![Win Path 3](documentation/win_3.png)
![Win Path 4](documentation/win_4.png)
![Win Path 5](documentation/win_5.png)
![Win Path 6](documentation/win_6.png)
![Win Path 7](documentation/win_7.png)
![Win Path 8](documentation/win_8.png)
![Exit Options](documentation/exit_option.png)
![Winner Way Out](documentation/winner_exit.png)

 ##### Testing 3 

- Direct game over path
  - Age: security
  - Name: Alex
  - choice 1: head
  - choice 2: lobby
  - choice 3: executive
  - choice 4: design
  - game over
- Result = no error

The Testing 2 screenshots:

![Loose Path 1](documentation/loose_1.png)
![Win Path 2](documentation/second_win.png)
![Loose Path 3](documentation/loose_3.png)
![Loose Path 4](documentation/loose_4.png)
![Loose Path 5](documentation/loose_5.png)
![Loose Path 6](documentation/loose_6.png)
![Looser Way Out](documentation/game_over.png)

##### Testing 3 

- Fast game over path
  - Age: 40
  - Name: Linda
  - choice 1: explore
  - choice 1: stay
  - game over
- Result = no error

##### Testing 4

- Testing the output informations, clear function, game over function and main function.
  - They are working as they should.
  - Time.sleep method also working.
  - The exit function works also.
- Result = no error

##### Testing on pep8 

- These are (Total 86 errors) the errors I solved when I did test the source code on pep8

- No space between hashtag and importing modules
- Line too long and expected 2 blank lines, found 1
- Whitespaces, trailing whitespace and over-indented
- Blank lines contains whitespaces and block comment should start with '# 
- Blank line at end of file
