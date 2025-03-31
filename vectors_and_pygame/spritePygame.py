# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 18:48:40 2016

@author: SA
"""
import pygame


# Call this function so the Pygame library can initialize itself
pygame.init()
# Create an 1280x800 sized screen
screen = pygame.display.set_mode([1280, 800])
# This sets the name of the window
pygame.display.set_caption('Pygame is cool')
clock = pygame.time.Clock()
# Before the loop, load the sounds:
click_sound = pygame.mixer.Sound("boink.ogg")
# Set positions of graphics
background_position = [0, 0]
# Load and set up graphics.
background_image = pygame.image.load("background.png").convert()
player_image = pygame.image.load("red_sprite_small.png").convert()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click_sound.play() 
            
    # Copy image to screen:
    screen.blit(background_image, background_position)

    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0] - 45
    y = player_position[1] - 45
    
    # Copy image to screen:
    screen.blit(player_image, [x, y])    
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
