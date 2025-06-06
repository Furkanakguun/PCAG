# -*- coding: utf-8 -*-
import sys
import pygame
from pygame.locals import *
import pymunk #1

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Joints. Just wait and the L will tip over")
    clock = pygame.time.Clock()
    space = pymunk.Space() #2
    space.gravity = (0.0, 980.0)

    try:
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    sys.exit(0)
                    
            screen.fill((127,127,255))
            space.step(1/50.0) #3 
            pygame.display.flip()
            clock.tick(50)
    finally:    
        pygame.quit()
        sys.exit()

if __name__ == '__main__':
    main()

