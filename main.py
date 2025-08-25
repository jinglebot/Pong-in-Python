"""
Pong pseudo code 

Create classes
    ⁃   Ball
    ⁃   Paddle
    ⁃   Court
    ⁃   Players
    ⁃   Scoreboard 
    ⁃   Game

Ball
    ⁃   Form: circle 
    ⁃   Initial position: in front of serving player
    ⁃   Attributes: x, y, speed
    ⁃   Methods: move (random)
    ⁃   Movements: serve to start movement, from one paddle area to the other, will bounce when wall/paddle is hit, the speed of the paddle move will determine the speed of the ball, will initialize when player scores 
    ⁃   Limitations: can only move within the wall boundary

Paddle
    ⁃   Form: rectangle
    ⁃   Initial position: middle of movement line ( left/right side of the screen)
    ⁃   Attributes: center x, center y, width, height, line position, speed of reaction 
    ⁃   Methods: slide (user input)
    ⁃   Movements: maneuvered by player, the degree of the movement will determine the speed of movement, will initialize with a new game
    ⁃   Limitations: only moves up/down within a line segment

Court
    ⁃   Form: rectangle 
    ⁃   Initial position: center of screen 
    ⁃   Attributes: left wall x, left wall y, right wall x, right wall y, length, width, background color, background image
    ⁃   Methods: change background image, change background color 
    ⁃   Limitations: wall length is distance between paddle line segments, wall width is length of paddle line segment

Players
    ⁃   Form: none 
    ⁃   Initial position: new paddle, new score
    ⁃   Attributes: score
    ⁃   Movements: user input, user movement will determine score, moves their own paddle, accumulates scores, serves the ball

Scoreboard 
    ⁃   Form: rectangle
    ⁃   Initial position: top of screen
    ⁃   Attributes: Player1 score, Player2 score, timer, set
    ⁃   Methods: add to player score, start timer, end timer
    ⁃   Movements: keeps track of scores/sets/time

Game
    ⁃   Form: none
    ⁃   Initial position: none
    ⁃   Attributes:
    ⁃   Methods: initialize game, reset game
    ⁃   Movements: initializes new Ball, Paddle, Court, Players and Scoreboard 



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
"""



import pygame, sys, random

class Block(pygame.sprite.Sprite):
    def __init__(self,path,pos_x,pos_y):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (pos_x,pos_y))

class Player(Block):
    def __init__(self, path, pos_x, pos_y, speed):
        super().__init__(path, pos_x, pos_y)
        self.speed = speed
        self.movement = 0

    def screen_limit(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

    def update(self, ball_group):
        self.rect.y += self.movement
        self.screen_limit()

class Ball(Block):
    def __init__(self,path,pos_x,pos_y,speed_x,speed_y,paddles):
        super().__init__(path,pos_x,pos_y)
        self.speed_x = speed_x * random.choice((1, -1))
        self.speed_y = speed_y * random.choice((1, -1))
        self.paddles = paddles
        self.active = False
        self.score_time = 0

    def collisions(self):
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            pygame.mixer.Sound.play(pong_sound)
            self.speed_y *= -1

        if pygame.sprite.spritecollide(self,self.paddles,False):
            pygame.mixer.Sound.play(pong_sound)
            collision_paddle = pygame.sprite.spritecollide(self,self.paddles,False)[0].rect
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_y > 0: 
                self.speed_x *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_y < 0: 
                self.speed_x *= -1
            if abs(self.rect.top - collision_paddle.bottom) < 10 and self.speed_y < 0:
                self.rect.top = collision_paddle.bottom
                self.speed_y *= -1
            if abs(self.rect.bottom - collision_paddle.top) < 10 and self.speed_y > 0:
                self.rect.bottom = collision_paddle.top
                self.speed_y *= -1

    def reset_ball(self):
            self.active = False
            self.speed_x *= random.choice((1, -1))
            self.speed_y *= random.choice((1, -1))
            self.score_time =  pygame.time.get_ticks()
            self.rect.center = (WIDTH/2, HEIGHT/2)
            pygame.mixer.Sound.play(score_sound)
    
    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart_counter()

    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown = 3

        if current_time - self.score_time <= 700:
            countdown = 3
        if 700 < current_time - self.score_time <= 1400:
            countdown = 2
        if 1400 < current_time - self.score_time <= 2100:
            countdown = 1
        if current_time - self.score_time >= 2100:
            self.active = True

        time_counter = game_font.render(str(countdown),True,light_grey)
        time_counter_rect = time_counter.get_rect(center = (WIDTH/2, HEIGHT/2 + 50))
        pygame.draw.rect(screen,bg_color,time_counter_rect)
        screen.blit(time_counter, time_counter_rect)

class Opponent(Block):
    def __init__(self, path, pos_x, pos_y, speed):
        super().__init__(path, pos_x, pos_y)
        self.speed = speed

    def update(self, ball_group):
        if self.rect.top < ball_group.sprite.rect.y: 
            self.rect.y += self.speed
        if self.rect.bottom > ball_group.sprite.rect.y:
            self.rect.y -= self.speed
        self.screen_limit()

    def screen_limit(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= HEIGHT:
            self.rect.bottom = HEIGHT

class Game_Manager:
    def __init__(self,ball_group,paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group

    def run_game(self):
        # draw objects
        self.paddle_group.draw(screen)
        self.ball_group.draw(screen)

        # update
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= WIDTH:
            self.opponent_score += 1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self):
        player_score = game_font.render(str(self.player_score), True, accent_color)
        opponent_score = game_font.render(str(self.opponent_score), True, accent_color)

        player_score_rect = player_score.get_rect(midleft = (WIDTH/2 + 40, HEIGHT/2))
        opponent_score_rect = opponent_score.get_rect(midright = (WIDTH/2 -40, HEIGHT/2))

        screen.blit(player_score,player_score_rect)
        screen.blit(opponent_score,opponent_score_rect)

pygame.mixer.pre_init(44100, -16, 2, 512)       
pygame.init()
clock = pygame.time.Clock()

# Main window
WIDTH, HEIGHT = 1280, 960
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG GAME")

# Game Variables
bg_color = pygame.Color("grey12")
accent_color = (127, 135, 143)
light_grey = (200, 200, 200)
game_font = pygame.font.Font("freesansbold.ttf", 32)
pong_sound = pygame.mixer.Sound("pong.ogg")
score_sound = pygame.mixer.Sound("score.ogg")
middle_strip = pygame.Rect(WIDTH/2 - 2, 0, 4, HEIGHT)

# Game Objects
player = Player('Paddle.png', WIDTH - 20, HEIGHT/2, 20)
opponent = Opponent('Paddle.png', 20, WIDTH/2,5)
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

ball = Ball('Ball.png',WIDTH/2, HEIGHT/2,4,4,paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = Game_Manager(ball_sprite,paddle_group)

while True:

    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.movement += player.speed
            if event.key == pygame.K_UP:
                player.movement -= player.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.movement -= player.speed
            if event.key == pygame.K_UP:
                player.movement += player.speed

    # Background
    screen.fill(bg_color)
    pygame.draw.rect(screen, accent_color, middle_strip)

    # Run game
    game_manager.run_game()

    # Rendering
    pygame.display.flip()
    clock.tick(60)





