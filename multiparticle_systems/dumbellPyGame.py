# -*- coding: utf-8 -*-
from pylab import *
import pygame

def dumbellMass(mA, mB, k, b, y0, g, dt, t):
    n = int(round(time/dt))
    t = zeros(n, float)
    yA = zeros(n, float)
    vA = zeros(n, float)
    yB = zeros(n, float)
    vB = zeros(n, float)
    yA[0] = y0 + b
    vA[1] = 0.0
    yB[0] = y0
    vB[1] = 0.0

    for i in range(n-1):
        f = k*(yA[i] - yB[i] - b)
        fA = -f - mA*g
        fB = f - mB*g
        aA = fA/mA
        vA[i+1] = vA[i] + aA*dt
        yA[i+1] = yA[i] + vA[i+1]*dt
        aB = fB/mB
        vB[i+1] = vB[i] + aB*dt
        yB[i+1] = yB[i] + vB[i+1]*dt
        t[i+1] = t[i] + dt
        if (yB[i+1] < 0.0) and (yB[i] >= 0.0):
            vB[i+1] = abs(vB[i+1])
    return t, yA, yB

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
# screen = pygame.display.set_mode([1280, 800])
background_image_ground = 600
player_image = pygame.image.load("red_sprite_small.png")
player_image_width, player_image_height = player_image.get_rect().size
player_image = player_image.convert()

m1 = 0.9
m2 = 0.9
k = 2.0
b = 200
g = 9.8
time = 60
dt = 0.01

done = False
simulation = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            _, rA, rB = dumbellMass(m1, m2, k, b, background_image_ground - (b + y), g, dt, time)
            simulation = True

    # Copy image to screen:
    screen.blit(background_image, background_position)
    # Get the current mouse position. This returns the position
    # as a list of two numbers.
    if not simulation:
        player_position = pygame.mouse.get_pos()
        x = player_position[0] - player_image_width/2
        y = player_position[1] - player_image_height/2
        if y > background_image_ground:
            y = background_image_ground
        # Copy image to screen:
        screen.blit(player_image, [x, y])
        screen.blit(player_image, [x, y + b])
    else:
        pygame.mouse.set_visible(False)
        for i in range(len(rA)):
            screen.blit(background_image, background_position)
            xsimA = x
            ysimA = background_image_ground - rA[i]
            ysimB = background_image_ground - rB[i]
            # Copy image to screen:
            screen.blit(player_image, [xsimA, ysimA])
            screen.blit(player_image, [xsimA, ysimB])
            pygame.mouse.set_pos(xsimA + 45, ysimA + 45)
            pygame.display.flip()
        pygame.mouse.set_visible(True)
        simulation = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit ()