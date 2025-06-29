# Assignment 12 - due 30.06.2025
# Following tutorial from https://www.youtube.com/watch?v=UZg49z76cLw
# Using game assets from https://opengameart.org/content/flappy-beans

"""
    This is a Flappy Bird like game but with coffe beans :)
    Use the SPACE key to make the coffee bean 'flap/fly'
"""

import pygame, sys, random

pygame.init()

# global variables
DISPLAY_WIDTH = 290
DISPLAY_HEIGHT = 515

FLOOR_POS_X = 0

INITIAL_PIPE_POS = 300

GRAVITY = 0.1
BEAN_MOVEMENT = 0

GAME_ACTIVE = True

SCORE = 0
HIGH_SCORE = 0

GAME_FONT = pygame.font.Font('04B_19.ttf', 25)

# functions
def draw_floor():
    screen.blit(floor_surface, (FLOOR_POS_X, DISPLAY_HEIGHT - 50))
    screen.blit(floor_surface, (FLOOR_POS_X + 336, DISPLAY_HEIGHT - 50)) # second surface with floor image so the floor never 'leaves' the screen and moves fluidly

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop =  (INITIAL_PIPE_POS, random_pipe_pos))
    top_pipe = pipe_surface_top.get_rect(midbottom = (INITIAL_PIPE_POS, random_pipe_pos - 130))

    return bottom_pipe, top_pipe

def move_pipes(pipes: list): # takes all pipes and moves them to the left by a number (5)
    for pipe in pipes:
        pipe.centerx -= 2.5
    return pipes

def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= DISPLAY_HEIGHT:
            screen.blit(pipe_surface, pipe)
        else:
            screen.blit(pipe_surface_top, pipe)

def check_collisions(pipes):
    for pipe in pipes:
        if bean_rect.colliderect(pipe):
            return False

        if bean_rect.top <= -100 or bean_rect.bottom >= 400:
            return False

    return True

def rotate_bean(bean):
    new_bean = pygame.transform.rotate(bean, - BEAN_MOVEMENT * 3)

    return new_bean

def bean_animation():
    new_bean = bean_frames[bean_index]
    new_bean_rect = new_bean.get_rect(center = (100, bean_rect.centery))

    return new_bean, new_bean_rect

def score_display(game_state):
    if game_state == 'game':
        score_surface = GAME_FONT.render(str(int(SCORE)), True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (DISPLAY_WIDTH / 2, 50))
        screen.blit(score_surface, score_rect)

    if game_state == 'game over':
        score_surface = GAME_FONT.render(f'Score: {int(SCORE)}', True, (255, 255, 255))
        score_rect = score_surface.get_rect(center = (DISPLAY_WIDTH / 2, 50))
        screen.blit(score_surface, score_rect)

        high_score_surface = GAME_FONT.render(f'High Score: {int(HIGH_SCORE)}', True, (255, 255, 255))
        high_score_rect = high_score_surface.get_rect(center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT - 80))
        screen.blit(high_score_surface, high_score_rect)

def update_score(score, high_score):
    if score > high_score:
        high_score = score
    return high_score

# things needed for game logic
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT)) # convert improves game speed so pygame can load images more efficiently
clock = pygame.time.Clock()

# surfaces
bg_surface = pygame.image.load('game_assets/background.png')

floor_surface = pygame.image.load('game_assets/floor.png')

bean_down = pygame.transform.scale(pygame.image.load('game_assets/bean1.png'), (32, 32))
bean_middle = pygame.transform.scale(pygame.image.load('game_assets/bean2.png'), (32, 32))
bean_up = pygame.transform.scale(pygame.image.load('game_assets/bean2.png'), (32, 32))
bean_frames = [bean_up, bean_middle, bean_down]
bean_index = 0
bean_surface = bean_frames[bean_index]
bean_rect = bean_surface.get_rect(center = (100, DISPLAY_HEIGHT/2))

BEANFLAP = pygame.USEREVENT + 1
pygame.time.set_timer(BEANFLAP, 200)

pipe_surface = pygame.image.load('game_assets/pipe_bottom.png')
pipe_surface_top = pygame.image.load('game_assets/pipe_top.png')
pipe_list = []
SPAWNPIPE = pygame.USEREVENT # event triggered by a timer
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [250, 325, 400]

game_over_surface = pygame.image.load('game_assets/game_over.png')
game_over_rect = game_over_surface.get_rect(center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2))

# game loop
while True:
    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and GAME_ACTIVE:
                BEAN_MOVEMENT = 0
                BEAN_MOVEMENT -= 3.5
            if event.key == pygame.K_SPACE and GAME_ACTIVE == False:
                GAME_ACTIVE = True
                pipe_list.clear()
                bean_rect.center = (100, DISPLAY_HEIGHT/2)
                BEAN_MOVEMENT = 0
                SCORE = 0

        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

        if event.type == BEANFLAP:
            if bean_index < 2:
                bean_index += 1
            else:
                bean_index = 0

            bean_surface, bean_rect = bean_animation()

    # display
    screen.blit(bg_surface,(0, 0)) # draws the surface with our background image

    if GAME_ACTIVE:
        # bean
        BEAN_MOVEMENT += GRAVITY
        rotated_bean = rotate_bean(bean_surface)
        bean_rect.centery += BEAN_MOVEMENT # change the y position of the bean to simulate falling
        screen.blit(rotated_bean, bean_rect) # draw surface with bean on display

        # check collision
        GAME_ACTIVE = check_collisions(pipe_list)

        # pipes
        pipe_list = move_pipes(pipe_list)
        draw_pipes(pipe_list)

        # scores
        SCORE += 0.01
        score_display('game')
    else:
        screen.blit(game_over_surface, game_over_rect)
        HIGH_SCORE = update_score(SCORE, HIGH_SCORE)
        score_display('game over')

    # floor
    FLOOR_POS_X -= 1 # the floor will change it's x position by a small amount to simulate movement
    draw_floor() # call function to draw the continuous floor
    if FLOOR_POS_X <= -DISPLAY_WIDTH: # move floor across display until it hits an edge and reset x position
        FLOOR_POS_X = 0

    pygame.display.update()
    clock.tick(120) # game runs at 120 FPS and never faster