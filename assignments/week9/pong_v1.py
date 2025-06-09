# Assignment 9 - due 09.06.2025
# Pong game following tutorial from https://www.youtube.com/watch?v=Qf3-aDXG8q4&list=PL8ui5HK3oSiEk9HaKoVPxSZA03rmr9Z0k&index=1

import pygame, sys, random
from IPython.core.events import post_execute

# general setup
pygame.init()
clock = pygame.time.Clock()

# constants
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 800
BACKGROUND_COLOR = (255, 238, 187)
PLAYERS_COLOR = (221, 119, 170)
BALL_COLOR = (238, 68, 153)
GUI_COLOR = (255, 204, 153)
TIMER_COLOR = (255, 136, 136)

BALL_POS_X = DISPLAY_WIDTH / 2 - 10 # perfectly centers ball
BALL_POS_Y = DISPLAY_HEIGHT / 2 - 10

PLAYER_POS_X = 0
PLAYER_POS_Y = DISPLAY_HEIGHT / 2 - 70

OPPONENT_POS_X = DISPLAY_WIDTH - 20
OPPONENT_POS_Y = PLAYER_POS_Y

LINE_POS_START = (DISPLAY_WIDTH / 2, 0)
LINE_POS_END = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT)

BALL_SPEED_X = 7 * random.choice((1, -1))
BALL_SPEED_Y = 7 * random.choice((1, -1))
PLAYER_SPEED = 0
OPPONENT_SPEED = 0

# classes for games

def ball_animation():
    global BALL_SPEED_X, BALL_SPEED_Y, PLAYER_SCORE, OPPONENT_SCORE, SCORE_TIME

    ball.x += BALL_SPEED_X
    ball.y += BALL_SPEED_Y

    # ball hits top/bottom of screen and bounces
    if ball.top <= 0 or ball.bottom >= DISPLAY_HEIGHT:
        BALL_SPEED_Y *= -1

    # player scores
    if ball.left <= 0:
        PLAYER_SCORE += 1
        SCORE_TIME = pygame.time.get_ticks()

    # opponent scores
    if ball.right >= DISPLAY_WIDTH:
        OPPONENT_SCORE += 1
        SCORE_TIME = pygame.time.get_ticks()

    if ball.colliderect(player) and BALL_SPEED_X > 0: # check if collision occurred
        if abs(ball.right - player.left) < 10: # check what in what side has a collision occurred
            BALL_SPEED_X *= -1
        elif abs(ball.bottom - player.top) < 10 and  BALL_SPEED_Y > 0:
            BALL_SPEED_Y *= -1
        elif abs(ball.top - player.bottom) < 10 and  BALL_SPEED_X < 0:
            BALL_SPEED_Y *= -1
    if ball.colliderect(opponent) and BALL_SPEED_X > 0:
        if abs(ball.left - opponent.left) < 10:
            BALL_SPEED_X *= -1
        elif abs(ball.bottom - opponent.top) < 10 and  BALL_SPEED_Y > 0:
            BALL_SPEED_Y *= -1
        elif abs(ball.top - opponent.bottom) < 10 and  BALL_SPEED_X < 0:
            BALL_SPEED_Y *= -1

def ball_restart():
    global BALL_SPEED_X, BALL_SPEED_Y, SCORE_TIME

    current_time = pygame.time.get_ticks()
    ball.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)

    if current_time - SCORE_TIME < 700:
        number_three = timer_font.render("3", False, TIMER_COLOR)
        screen.blit(number_three, (DISPLAY_WIDTH / 2 - 20, DISPLAY_HEIGHT / 2 - 250))

    if 700 < current_time - SCORE_TIME < 1400:
        number_two = timer_font.render("2", False, TIMER_COLOR)
        screen.blit(number_two, (DISPLAY_WIDTH / 2 - 20, DISPLAY_HEIGHT / 2 - 250))

    if 1400 < current_time - SCORE_TIME < 2100:
        number_one = timer_font.render("1", False, TIMER_COLOR)
        screen.blit(number_one, (DISPLAY_WIDTH / 2 - 20, DISPLAY_HEIGHT / 2 - 250))

    if current_time - SCORE_TIME < 2100:
        BALL_SPEED_X, BALL_SPEED_Y = 0, 0
    else:
        BALL_SPEED_Y = 7 * random.choice((1, -1))
        BALL_SPEED_X = 7 * random.choice((1, -1))
        SCORE_TIME = None

def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= DISPLAY_HEIGHT:
        player.bottom = DISPLAY_HEIGHT

def opponent_animation():
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= DISPLAY_HEIGHT:
        opponent.bottom = DISPLAY_HEIGHT

# setting up our game window
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT)) # returns a display surface object stored in screen variable
pygame.display.set_caption('Pong')

# game rectangles
ball = pygame.Rect(BALL_POS_X, BALL_POS_Y, 20, 20)
player = pygame.Rect(PLAYER_POS_X, PLAYER_POS_Y, 20, 140)
opponent = pygame.Rect(OPPONENT_POS_X, OPPONENT_POS_Y, 20, 140)

# text variables
PLAYER_SCORE = 0
OPPONENT_SCORE = 0
game_font = pygame.font.Font("freesansbold.ttf", 32)
timer_font = pygame.font.Font("freesansbold.ttf", 64)

# score timer
SCORE_TIME = True

# game loop
while True:
    # handling input
    for event in pygame.event.get(): # checks for all user actions
        if event.type == pygame.QUIT: # check if user has closed window
            pygame.quit() # uninitializes the pygame module
            sys.exit() # closes entire program
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                PLAYER_SPEED += 9
            if event.key == pygame.K_w:
                PLAYER_SPEED -= 9

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                PLAYER_SPEED -= 9
            if event.key == pygame.K_w:
                PLAYER_SPEED += 9

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                OPPONENT_SPEED += 9
            if event.key == pygame.K_UP:
                OPPONENT_SPEED -= 9

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                OPPONENT_SPEED -= 9
            if event.key == pygame.K_UP:
                OPPONENT_SPEED += 9

    # game logic
    ball_animation()
    player.y += PLAYER_SPEED
    player_animation()
    opponent.y += OPPONENT_SPEED
    opponent_animation()

    # drawing game components
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PLAYERS_COLOR, player)
    pygame.draw.rect(screen, PLAYERS_COLOR, opponent)
    pygame.draw.ellipse(screen, BALL_COLOR, ball)
    pygame.draw.aaline(screen, GUI_COLOR, LINE_POS_START, LINE_POS_END)

    if SCORE_TIME:
        ball_restart()

    player_text = game_font.render(f"{PLAYER_SCORE}", False, GUI_COLOR)
    screen.blit(player_text, (520, 400))

    opponent_text = game_font.render(f"{OPPONENT_SCORE}", False, GUI_COLOR)
    screen.blit(opponent_text, (460, 400))

    # updating the window
    pygame.display.flip()
    clock.tick(60) # limits how fast the loop runs (60 fps)