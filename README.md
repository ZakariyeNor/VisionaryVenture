# Apple Park Adventure

Apple Park Adventure is a text-based adventure game that takes place in the iconic Apple Park campus. In this game, the player navigates through various choices to reach the highest office in the building and ultimately meet Tim Cook. Along the way, the player must make careful decisions, as the wrong path may lead to failure!. The adventure is for people intersted to go the highest office of Apple and have chance to ask Tim Cook what they want.

![The App](/documentation/respon.png)

## Features 

The adventure starts welcoming and informing the user the game and the main goal they are playing this adventure game. 
The first rule is to varify the age of the player, if it is allowed age it goes to the next step where the user must input his/her name and if it is valid, the game starts and the user has one of the two options to choose, if its the right option it goes to the next questions otherwise it asks same question until user gets the right one. The player is getting information if the question is right, wrong and if the win or loose. And that why this Appl Park adventure is the best app for playing adventure game to meet Tim Cook. 

### Existing Features

- Informing if user wins or looses the game.
- Interactive text-based adventure.
  - Making the information text show up 0.25 seconds after one another.

- Age validation to ensure the player is eligible to play.
  - Input number, valid age or security house clearance

![Player Validation](/documentation/player_validation.png) ![Cleanup](/documentation/clear.png)

- Custom player name input to personalize the experience.
  - Input only alphabetic name and spaces
  - Name input can't be empty

- Dynamic screen cleanup for smooth transitions betwenn game events.
  - Clear other texts to make the next question and information texts readable

- Multiple decision points that determine the outcome of the game.
  - User can only choose one of the two options otherwise it goes in loop. 

### Future Features

- Allow player to see visual images of Apple Park.
- Digital timer 
  - Limit the time a player can play the game

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![Gitpod](https://img.shields.io/badge/Gitpod-grey?logo=gitpod&logoColor=FFAE33)](https://gitpod.io) used as a cloud-based IDE for development.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language. 
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.


## Testing


## Bugs

Solved Bugs

- Too long lines and White spaces
- Hash tag for the comments 
- Over indented and visual indented lines 
- Exit options was printing only the text
- Added while loop to the next question
- In Testing part 4, I noticed that if the user inputs something else rather then 'stay' or 'head' it runs the prints statement and never stops. I solved this to break the loop add another print statement to start over and choose the right one next time. And the game starts from the base while loop because of these two questions are connected to each other, user must choose 'explore ' to come to the next question where user must choose either 'stay' or 'head'. To find more about this solution, please visit [Testing 4](TESTING.md)

Remaining Bugs

- No bugs remaining

Validator Testing 

- PEP8 
  - Over 80 errors were retuned from PEP8online.com
  - To know about the PEP8 errors and their solutions [TESTING.md](TESTING.md)

## Deployment

- This project were deployed using Code Institute mock terminal for Heroku.
  - The live deployed application can be found deployed on [Heroku](https://apple-park-eedfc5a2a619.herokuapp.com/).

#### Heroku Deployment

- Steps for deployment: 

  - Select **New** in the top-right corner of your Heroku Dashboard, and select **Create new app** from the dropdown menu.
  - Choose app name and it must be unique, then choose a region (EU or USA), and finally, select **Create App**.
  - Further down, to support dependencies, select **Add Buildpack**.
  - Connect to Github, and then search the repository.
  - Deployed manually

#### Cloning

- Setting Up the Project Locally

To work on this project locally, you need to create a local copy of the repository on your computer. This process, called cloning, allows you to view, edit, and experiment with the codebase independently.

  1. Go to the [GitHub repository](https://github.com/ZakariyeNor/VisionaryVenture) 
  2. Locate the Code button above the list of files and click it 
  3. Select if you prefer to clone using HTTPS, SSH, or GitHub CLI and click the copy button to copy the URL to your clipboard
  4. Open Git Bash or Terminal
  5. Change the current working directory to the one where you want the cloned directory
  6. In your IDE Terminal, type the following command to clone my repository:
    - `git clone https://github.com/ZakariyeNor/VisionaryVenture.git`
  7. Press Enter to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/ZakariyeNor/VisionaryVenture)

Please note that in order to directly open the project in Gitpod, you need to have the browser extension installed.
A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

- You can fork this repository by using the following steps:

  1. Log in to GitHub and locate the [GitHub Repository](https://github.com/ZakariyeNor/VisionaryVenture)
  2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
  3. Once clicked, you should now have a copy of the original repository in your own GitHub account!.

## Credits 

| [Markdown Builder](https://tim.2bn.dev/markdown-builder) | README and TESTING | Tool to help generate the Markdown files |

| [Youtube Tutorial](https://www.youtube.com/watch?v=th4OBktqK1I) | Funtions and Conditions | Tutorial I watched to learn more and practise functions and conditions |

### Media 

| [Chatgpt](https://chatgpt.com/) | Questions | Different paths | Options | Chatgpt generated fictional Apple Park adventure game, their options and different paths but I choose which one of these two options is the right one |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://github.com/TravelTimN) for his support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) tutor team for their assistance with troubleshooting and debugging some project issues.
- Educators and Mentors: Thank you to all the teachers and my personal mentor [Tim Nelson](https://github.com/TravelTimN) who provided guidance and inspiration. Your passion for sharing knowledge ignited my interest in this project.
- Developers of Tools and Resources and Content Creators: Thanks to the creator of Markdown Builder [Tim Nelson](https://github.com/TravelTimN) and youtuber [Tech with Tim](https://www.youtube.com/@TechWithTim) whose tutorials and insights shaped my understanding of coding and game development. Your willingness to share knowledge made a difference.