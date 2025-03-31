# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 20:45:30 2024

@author: SA-Lenovo
"""

import math 
import pygame

pygame.init() 

clock = pygame.time.Clock() 

FrameHeight = 810
FrameWidth = 1200

# Pygame Screen 
pygame.display.set_caption("Endless Scrolling in pygame")
screen = pygame.display.set_mode((FrameWidth, FrameHeight)) 

# Load and set up graphics
bg = pygame.image.load("endlessBG_3.png").convert()

# Variable for scrolling 
scroll = 0

tiles = math.ceil(FrameWidth / bg.get_width()) + 10 # 10 pixels buffer

# Main Loop 
done = False

while not done:
    
	# Appending the image to the back of the background image 
    i = 0
    while(i < tiles): 
        screen.blit(bg, (bg.get_width()*i + scroll, 0)) 
        i += 1

	# Frame for scrolling 
    scroll -= 3

	# Reset Scroll Frame 
    if abs(scroll) > bg.get_width(): 
        scroll = 0

	# CLOSINF THE FRAME OF SCROLLING 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            done = True

    clock.tick(33)
    pygame.display.update() 

pygame.quit() 
