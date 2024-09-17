# Testing The Apple Park Adventure

#### Testing Step by Step

- Testing if the game goes step by step and shows the right content every step. 

##### Testing 1

- Testing age and name and they working as they should. 
- When I tested the functions call, I get help with my mentor. And my mentor told me that I invoked all the functions three times and to fix this I use while loop and break the condition if the user chooses right option and call the next function inside the while loop scope, otherwise call the game over function so the game exits and tells the user that he/she loose the game.
- I had also unstyled text and the output informations and input choices made the screen hard to read and find the right text so I fix this to add time between print outputs and clear function (Added time and os modules.) To use time when printing out informations and clear the informations before the user types in one of the options.
- The game over conditions works like string and to fix this I added exit method in the game over function.
- When it comes calling the functions I called them once from the functions and the main function.

 ##### Testing 2

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

