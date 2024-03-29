# Google Project Challenge: Breakout Clone

Play my version of the famous Arkanoid/Breakout game!

![Gameplay](images/breakout_running.png)

# Features
- Paddle and a ball where the ball can destroy the bricks in a wall

- Simple level and scoring system
- Dynamic level settings which change based on the current level

- 5 lives and 1 life is lost when the ball touches the bottom of the screen
- Game ends when lives reach 0 and player has the option to restart

# Requirements
- Created on Python 3.8
- Created using Python library - PyGame
- Developed on Windows 10, so presumably the game should run on any Windows system

## Installing instructions for Windows 10
### Python 3.8
1) Locate the appropriate version of Python here:
- https://www.python.org/downloads/

2) Add the file to a known directory of your choice and execute the file. ((C:) drive most accessible)

3) Run the command prompt and access the directory you chose in the previous step.

4) Type ```python``` in to the terminal to check your version.

### PyGame
PyGame is notoriously difficult to install! I will do my best at trying to explain how to install PyGame:


1) Locate the appropriate version of PyGame here:
- https://bitbucket.org/pygame/pygame/downloads/

or here if you can't find the correct version in the previous link:

- https://www.lfd.uci.edu/~gohlke/pythonlibs/#pygame

2) Copy the PyGame file into the same directory as the Breakout game and access this directory in the command prompt, then enter:
```
python -m pip install pygame
```

# Usage
## Running the game
Access the directory of the breakout file through the command prompt and simply execute by typing:
```
python main.py
```

## Exiting the game
You can exit the game by clicking the 'X' button at the top right, or you can press 'Q' at anytime.

# Running tests
I am going to be honest here and say that I was not really sure how to run unit tests for a program made with PyGame and thus I have no way of proving the robustness of my code. I understand the importance of testing and debugging your code, but my current programming knowledge has not stretched this far as of yet in terms of testing with PyGame.

However, I have run the game many times and any bugs that I ran into, I attempted to fix - see "Limitations".

# Components
See the relevant files for more detailed annotations. My project is made up of many parts:

- main.py - Executable code to run the game is located here
- /images - Contains the images used as the paddle and bricks. Sourced from: https://opengameart.org/

# Limitations
- The game only works for the specified screen dimensions. If changed, there will be large spaces without bricks.
- Only one type of brick.
- No sounds.
- Level difficulty increases very rapidly - may get too difficult from level 5 onwards.
- High score does not save in between executions of the game. In other words, the high score is the highest score of the current instance of the game running and not the highest score of all of the instances of the game that have run. (I hope that makes sense!)
### This is now fixed (10/03/2020): 
- Game over message is shown when all lives are lost but the game does not reset the statistics if the player attempts to have another go; Nor does the game end, the player must exit manually - see "Exiting the game". (currently trying to fix this for 11/03/2020 - I will commit my changes in time for my the interview tomorrow)! 
