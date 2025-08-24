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




import pygame, sys, random

global ball_speed_x, ball_speed_y, player_score, opponent_score, score_time

def ball_start():
	current_time = pygame.time.get_ticks()
	ball.center = (WIDTH/2, HEIGHT/2)

	if current_time - score_time < 700:
		number_three = game_font.render("3", False, light_grey)
		screen.blit(number_three, (WIDTH/2 - 10, HEIGHT/2 + 20))
	if current_time - score_time < 700:
		number_two = game_font.render("2",False, light_grey)
		screen.blit(number_two, (WIDTH/2 - 10, HEIGHT/2 + 20))
		
	if current_time - score_time < 2100:
		ball_speed_x, ball_speed_y = 0, 0
	else:
		ball_speed_y = 7 * random_choice((1, -1))
		ball_speed_x = 7 * random_choice((1, -1))
		score_time = None

pygame.init()
clock = pygame.time.Clock()

WIDTH, HEIGHT = 1280, 960
screen = pygame.display.set__mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")

ball = pygame.Rect(WIDTH/2 - 15, HEIGHT/2 - 15, 30, 30)
player = pygame.Rect(WIDTH - 20, HEIGHT/2 - 70, 10, 140)
opponent = pygame.Rect(20, HEIGHT/2 - 70, 10, 140)

bg_color = pygame.Color("grey12")
light_grey = (200, 200, 200)

ball_speed_x = 7 * random_choice((1, -1))
ball_speed_y = 7 * random_choice((1, -1))
player_speed = 0
opponent_speed = 7

# Text Variables
player.score = 0
opponent.score = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)

# Score timer
score_time = None

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				player_speed += 7
			if event.key == pygame.K_UP:
				player_speed -= 7
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_DOWN:
				player_speed -= 7
			if event.key == pygame.K_UP:
				player_speed += 7


	# ball_animation()
	ball.x += ball_speed_x
	ball.y = ball_speed_y

	if ball.top <= 0 or ball.bottom >= HEIGHT:
		ball_speed_y *= -1
	if ball.left <= 0:
		player_score += 1
		score_time = pygame.time.get_ticks()	
	if ball.right >= WIDTH:
		opponent_score += 1
		score_time = pygame.time.get_ticks()

	if ball.colliderect(player) or ball.colliderect(opponent):
		ball_speed_x *= -1
		
	# player_animation()
	player.y += player_speed
	if player.top <= 0:
		player.top = 0
	if player.bottom >= HEIGHT:
		player.bottom = HEIGHT

	# opponent_ai()
	if opponent.top < ball.y: 
		opponent.top += opponent_speed
	if opponent.bottom > ball.y:
		opponent.bottom -= opponent_speed
	if opponent.top <= 0:
		opponent.top = 0
	if opponent.bottom >= HEIGHT:
		opponent.bottom = HEIGHT

	screen.fill(bg_color)
	pygame.draw.rect(screen, light_grey, player)
	pygame.draw.rect(screen, light_grey, opponent)
	pygame.draw.ellipse(screen, light_grey, ball)
	pygame.draw.aaline(screen, light_grey, (WIDTH/2, 0), (WIDTH/2, HEIGHT))

	if score_time:
		ball_start()

	player_text = game_font.render(f"{player_score}", False, light_grey)
	screen.blit(player_text, (660, 470))
	opponent_text = game_font.render(f"(opponent_score)", False, light_grey)
	screen.blit(opponent_text, (600,470))

	pygame.display.flip()
	clock.tick(60)









