Pong pseudo code 

"""
Create classes
	⁃	Ball
	⁃	Paddle
	⁃	Court
	⁃	Players
	⁃	Scoreboard 
	⁃	Game

Ball
	⁃	Form: circle 
	⁃	Initial position: in front of serving player
	⁃	Attributes: x, y, speed
	⁃	Methods: move (random)
	⁃	Movements: serve to start movement, from one paddle area to the other, will bounce when wall/paddle is hit, the speed of the paddle move will determine the speed of the ball, will initialize when player scores 
	⁃	Limitations: can only move within the wall boundary

Paddle
	⁃	Form: rectangle
	⁃	Initial position: middle of movement line ( left/right side of the screen)
	⁃	Attributes: center x, center y, width, height, line position, speed of reaction 
	⁃	Methods: slide (user input)
	⁃	Movements: maneuvered by player, the degree of the movement will determine the speed of movement, will initialize with a new game
	⁃	Limitations: only moves up/down within a line segment

Court
	⁃	Form: rectangle 
	⁃	Initial position: center of screen 
	⁃	Attributes: left wall x, left wall y, right wall x, right wall y, length, width, background color, background image
	⁃	Methods: change background image, change background color 
	⁃	Limitations: wall length is distance between paddle line segments, wall width is length of paddle line segment

Players
	⁃	Form: none 
	⁃	Initial position: new paddle, new score
	⁃	Attributes: score
	⁃	Movements: user input, user movement will determine score, moves their own paddle, accumulates scores, serves the ball

Scoreboard 
	⁃	Form: rectangle
	⁃	Initial position: top of screen
	⁃	Attributes: Player1 score, Player2 score, timer, set
	⁃	Methods: add to player score, start timer, end timer
	⁃	Movements: keeps track of scores/sets/time

Game
	⁃	Form: none
	⁃	Initial position: none
	⁃	Attributes:
	⁃	Methods: initialize game, reset game
	⁃	Movements: initializes new Ball, Paddle, Court, Players and Scoreboard 

"""

class Game (object) :
    def __init__(self, Ball, Player1, Player2, Court, Scoreboard) :
        self.Ball = Ball
        self.Player1 = Player1
        self.Player2 = Player2
        self.Court = Court
        self.Scoreboard = Scoreboard

class Court (object) :
    def __init__(self, LwallX, LwallY, RwallX, RwallY, length, width, BGcolor, BGimage) :
        self.Rectangle = (LwallX, LwallY, RwallX, RwallY, length, width, BGcolor=black, BGimage)

class Scoreboard (object) :
    def __init__(self, Player1score, Player2score) :
        self.Player1score = Player1score
        self.Player2score = Player2score
        self.timer = 0

    def display (self) :
        print ("Player 1" + "         " + "Player 2")
        print ("\n")
        print ("   " + Player1score + "          " + Player2score)





newgame = Game()


