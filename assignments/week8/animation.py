'''
    Assignmnet 8 - due 02.06.2025
    Animate an image of your choice using pygame
    Used tutorial https://www.geeksforgeeks.org/pygame-tutorial/ to learn how to use pygame library
'''
# import necessary library
import pygame

# constants
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600

# initialize library - return a tuple with (successfully initialized modules, modules that failed to initialize)
pygame.init()

# check whether all the modules are initialized successfully or not - returns True if things worked
pygame.get_init()

# initialize window to display sth with width and height from constants
pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# keep above defined window running until users clicks exit button
# creating a Boolean value to check if the game is running
running = True

# loop to keep game running
while running:
    for event in pygame.event.get(): # check for event
        if event.type == pygame.QUIT:
            pass

