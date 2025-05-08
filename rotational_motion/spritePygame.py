# -*- coding: utf-8 -*-
import pygame

def rot_center(image, angle):
    """rotate an image while keeping its center and size"""
    """ It *only* works with square images """
    orig_rect = image.get_rect()
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = orig_rect.copy()
    rot_rect.center = rot_image.get_rect().center
    rot_image = rot_image.subsurface(rot_rect).copy()
    return rot_image


def rot_center_rect(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


# Call this function so the Pygame library can initialize itself
pygame.init()
# Create an 1280x800 sized screen
screen = pygame.display.set_mode([1280, 800])
# This sets the name of the window
pygame.display.set_caption('Pygame is cool')
clock = pygame.time.Clock()
# Before the loop, load the sounds:
# Set positions of graphics
background_position = [0, 0]
# Load and set up graphics.
background_image = pygame.image.load("background.png").convert()
player_image = pygame.image.load("rightArrow200.png").convert()
angle = 0
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            angle += 3
            if angle >= 360: angle = 0
            #player_image = rot_center(player_image, 3)
            # player_image, rotRect = rot_center_rect(player_image, player_image.get_rect(), 5)
            # click_sound.play()
    # Copy image to screen:
    screen.blit(background_image, background_position)
    # Get the current mouse position. This returns the positiong
    # as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0] - 100
    y = player_position[1] - 100
    # Copy image to screen:
    screen.blit(rot_center(player_image, angle), [x, y])
    #screen.blit(player_image,  [x, y])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
