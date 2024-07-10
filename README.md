## Pong Game
This is a simple implementation of the classic Pong game using Python and the Turtle graphics library. The game features two paddles controlled by the players, a ball that bounces off the walls and paddles, and a scoring system.

##Table of Contents
Installation
How to Play
Controls
Code Structure
Features
License

## Installation
To run this game, you need to have Python installed on your system. You can download Python from the official website.

Clone this repository to your local machine:

sh
Copy code
git clone https://github.com/your-username/pong-game.git
Navigate to the project directory:

sh
Copy code
cd pong-game
Install the required libraries (if not already installed):

sh
Copy code
pip install turtle


## How to Play
Run the main.py script to start the game:

sh
Copy code
python main.py
The game starts with the ball moving towards the right paddle. Use the keyboard controls to move the paddles and prevent the ball from going out of bounds. The game keeps track of the score, and the first player to miss the ball loses a point.

## Controls
Right Paddle:

Move Up: Up Arrow Key
Move Down: Down Arrow Key
Left Paddle:

Move Up: W Key
Move Down: S Key
Code Structure
main.py: This is the main game loop and setup for the screen and objects.
paddle.py: Contains the Paddle class which handles the paddle behavior.
ball.py: Contains the Ball class which manages the ball movement and collisions.
scoreboard.py: Contains the Scoreboard class which keeps track of the scores and displays them on the screen.
main.py
Sets up the screen, initializes the paddles, ball, and scoreboard, and contains the main game loop.

paddle.py
Defines the Paddle class with methods to move the paddle up and down.

ball.py
Defines the Ball class with methods to move the ball, detect collisions with walls and paddles, and reset the ball position.

scoreboard.py
Defines the Scoreboard class with methods to update and display the score, and show the game over message.

## Features
Two-player paddle control
Ball that bounces off paddles and walls
Scoring system that keeps track of points
Game over detection and reset functionality
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
