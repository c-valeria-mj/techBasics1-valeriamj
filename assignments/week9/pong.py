# Assignment 9 - due 09.06.2025
# Pong game following tutorial from https://www.youtube.com/watch?v=Qf3-aDXG8q4&list=PL8ui5HK3oSiEk9HaKoVPxSZA03rmr9Z0k&index=1

'''
GAME INSTRUCTIONS:

USE W KEY TO MOVE OPPONENT (LEFT SIDE) UP
USE S KEY TO MOVE OPPONENT (LEFT SIDE) DOWN

USE UP ARROW KEY TO MOVE OPPONENT (RIGHT SIDE) UP
USE DOWN KEY TO MOVE OPPONENT (RIGHT SIDE) DOWN
'''

import pygame, sys, random

# general setup
pygame.init()
clock = pygame.time.Clock()

# for displaying window
DISPLAY_WIDTH = 1000
DISPLAY_HEIGHT = 800

# setting up our game window
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT)) # returns a display surface object stored in screen variable
pygame.display.set_caption('Pong')

# colors
BACKGROUND_COLOR = (0, 0, 0)
GUI_COLOR = (255, 255, 255)

# text
game_font = pygame.font.Font("freesansbold.ttf", 32)
timer_font = pygame.font.Font("freesansbold.ttf", 64)

# line in the middle
middle_line = pygame.Rect(DISPLAY_WIDTH / 2 - 2, 0, 4, DISPLAY_HEIGHT)

# classes for game
class GameComponent(pygame.sprite.Sprite):
    def __init__(self, path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(path)
        self.rect = self.image.get_rect(center = (pos_x, pos_y))

class Player(GameComponent):
    def __init__(self, path, pos_x, pos_y, speed):
        super().__init__(path, pos_x, pos_y)
        self.speed = speed
        self.movement = 0

    def screen_constraint(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= DISPLAY_HEIGHT:
            self.rect.bottom = DISPLAY_HEIGHT

    def update(self, ball_group):
        self.rect.y += self.movement
        self.screen_constraint()

class Ball(GameComponent):
    def __init__(self, path, pos_x, pos_y, speed_x, speed_y, paddles):
        super().__init__(path, pos_x, pos_y)
        # ball goes in random direction when game starts
        self.speed_x = speed_x * random.choice((1, -1))
        self.speed_y = speed_y * random.choice((1, -1))
        # ball knows where paddles are and can collide with them
        self.paddles = paddles
        # if ball is moving or not
        self.active = False
        # so ball can wait a bit if point is scored
        self.score_time = 0

    def update(self):
        if self.active:
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y
            self.collisions()
        else:
            self.restart_counter()

    def collisions(self):
        # check for a collision with top or bottom of screen
        if self.rect.top <= 0 or self.rect.bottom >= DISPLAY_HEIGHT:
            self.speed_y *= -1

        # check for collision with player/opponent paddles
        if pygame.sprite.spritecollide(self, self.paddles, False):
            collision_paddle = pygame.sprite.spritecollide(self, self.paddles, False)[0].rect
            if abs(self.rect.right - collision_paddle.left) < 10 and self.speed_x > 0:
                self.speed_x *= -1
            if abs(self.rect.left - collision_paddle.right) < 10 and self.speed_x < 0:
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
        self.score_time = pygame.time.get_ticks()
        self.rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)

    def restart_counter(self):
        current_time = pygame.time.get_ticks()
        countdown_num = 3

        if current_time - self.score_time <= 700:
            countdown_num = 3
        if 700 < current_time - self.score_time <= 1400:
            countdown_num = 2
        if 1400 < current_time - self.score_time <= 2100:
            countdown_num = 1
        if current_time - self.score_time >= 2100:
            self.active = True

        time_counter = timer_font.render(str(countdown_num), True, GUI_COLOR)
        time_counter_rect = time_counter.get_rect(center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2 - 250))
        pygame.draw.rect(screen, BACKGROUND_COLOR, time_counter_rect)
        screen.blit(time_counter, time_counter_rect)

class GameManager():
    def __init__(self, ball_group, paddle_group):
        self.player_score = 0
        self.opponent_score = 0
        self.ball_group = ball_group
        self.paddle_group = paddle_group

    def run_game(self):
        # drawing game objects
        self.paddle_group.draw(screen)
        self.ball_group.draw(screen)

        # updating game objects
        self.paddle_group.update(self.ball_group)
        self.ball_group.update()
        self.reset_ball()
        self.draw_score()

    def reset_ball(self):
        if self.ball_group.sprite.rect.right >= DISPLAY_WIDTH:
            self.opponent_score +=1
            self.ball_group.sprite.reset_ball()
        if self.ball_group.sprite.rect.left <= 0:
            self.player_score += 1
            self.ball_group.sprite.reset_ball()

    def draw_score(self):
        player_score = game_font.render(str(int(self.player_score)), True, GUI_COLOR)
        opponent_score = game_font.render(str(int(self.opponent_score)), True, GUI_COLOR)

        player_score_rect = player_score.get_rect(midleft = (DISPLAY_WIDTH / 2 + 40, DISPLAY_HEIGHT / 2))
        opponent_score_rect = opponent_score.get_rect(midright = (DISPLAY_WIDTH / 2 - 40, DISPLAY_HEIGHT / 2))

        screen.blit(player_score, player_score_rect)
        screen.blit(opponent_score, opponent_score_rect)

# create game objects
player = Player('player.png', DISPLAY_WIDTH - 20, DISPLAY_HEIGHT / 2, 8)
opponent = Player('opponent.png', 20, DISPLAY_HEIGHT / 2, 8)
# group so img can "move"
paddle_group = pygame.sprite.Group()
paddle_group.add(player)
paddle_group.add(opponent)

ball = Ball('riz.png', DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2, 6, 6, paddle_group)
ball_sprite = pygame.sprite.GroupSingle()
ball_sprite.add(ball)

game_manager = GameManager(ball_sprite, paddle_group)

# game loop
while True:
    # handling input
    for event in pygame.event.get(): # checks for all user actions
        if event.type == pygame.QUIT: # check if user has closed window
            pygame.quit() # uninitializes the pygame module
            sys.exit() # closes entire program

        '''if game_manager.opponent_score == 5:
            pygame.quit()  # uninitializes the pygame module
            sys.exit()  # closes entire program

        if game_manager.player_score == 5:
            pygame.quit()  # uninitializes the pygame module
            sys.exit()  # closes entire program'''

        # opponent is controlled wit W (up) and S (down)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                opponent.movement -= opponent.speed
            if event.key == pygame.K_s:
                opponent.movement += opponent.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                opponent.movement += opponent.speed
            if event.key == pygame.K_s:
                opponent.movement -= opponent.speed

        # player is controlled with arrow keys up and down
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.movement -= player.speed
            if event.key == pygame.K_DOWN:
                player.movement += player.speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.movement += player.speed
            if event.key == pygame.K_DOWN:
                player.movement -= player.speed

    # GUI stuff
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, GUI_COLOR, middle_line)

    # running game (all the game logic is here)
    game_manager.run_game()

    # updating the window
    pygame.display.flip()
    clock.tick(60) # limits how fast the loop runs (60 fps)