'''
    Assignmnet 8 - due 02.06.2025
    Animate an image of your choice using pygame
    Used tutorial https://www.geeksforgeeks.org/pygame-tutorial/ to learn how to use pygame library and 
    to learn about animations
'''
# import necessary library
import pygame, random

class Cat(pygame.sprite.Sprite): # inherit the properties from pygame's sprite class
    def __init__(self, pos_x, pos_y):
        super().__init__() #  call constructor for sprite class
        self.sprites = []
        for i in range (1, 9):
            self.sprites.append(pygame.image.load(f"catwalk/{i}.png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect() # this will allow us to move the sprites
        self.rect.center =  [pos_x, pos_y]

    def update(self, speed, pos_x):
        self.current_sprite += speed

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[int(self.current_sprite)]

        self.rect.center = [pos_x, 150]

# constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 300
BACKGROUND_COLOR = (255,255,255)
SPEED = 0.15

# initialize library - return a tuple with (successfully initialized modules, modules that failed to initialize)
pygame.init()
clock = pygame.time.Clock()

# check whether all the modules are initialized successfully or not - returns True if things worked
# pygame.get_init()

# initialize window to display sth with width and height from constants
screen = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# set title displayed on top of window 
pygame.display.set_caption('TechBasics1 - Assignment 8')

cat_x = 0
cat_y = 150

# creating the sprites for animation
cat_group = pygame.sprite.Group()
cat = Cat(cat_x, cat_y)
cat_group.add(cat)

# keep above defined window running until users clicks exit button
# creating a Boolean value to check if the game is running
running = True

# loop to keep animation running
while running:
    for event in pygame.event.get(): # check for event
        if event.type == pygame.QUIT: # event is user has closed window
            running = False

    if cat_x < DISPLAY_WIDTH:
        cat_x += 5
    else:
        cat_x = 0

    # drawing the cats
    screen.fill(BACKGROUND_COLOR)
    cat_group.draw(screen)
    cat_group.update(SPEED, cat_x)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
exit(0)
