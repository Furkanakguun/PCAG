# -*- coding: utf-8 -*-
import pygame
import numpy as np
from pygame.locals import *
 
pygame.init()
#pygame.key.set_repeat(1, 0)
#event = pygame.event.get
#rect = pygame.draw.rect

scrx = 800
scry = 600
scrcolor = Color('white')

scr_toggle = 0

screen = pygame.display.set_mode((scrx, scry), 0, 32)
pygame.display.set_caption('Pygame Rotation')
polycolor = Color('green')
polyv = [[100, 100], [200, 100], [200, 200], [100, 200]]
polym = [150, 150]

def rotate(pointlist, angle):
    theta = np.radians(angle)
    c, s = np.cos(theta), np.sin(theta)
    R = np.matrix('{} {}; {} {}'.format(c, -s, s, c))
    a = R.dot(np.asarray(pointlist).T).T
    return a

def translate(pointlist, translation):
    polyvM = np.matrix(pointlist)
    return np.hstack((polyvM[:,0] + translation[0], polyvM[:,1] + translation[1])).tolist()       
    
done = False
pos_y = 0
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(scrcolor, (0, 0, scrx, scry))
    polyv= translate(polyv, [-150, -150])
    polyv = rotate(polyv, 0.1).tolist()
    polyv= translate(polyv, [150+ pos_y, 150 + pos_y])
    pos_y += .001
    pygame.draw.polygon(screen, polycolor, polyv, 0)
    pygame.display.update()

pygame.quit()