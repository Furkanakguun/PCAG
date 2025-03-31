# -*- coding: utf-8 -*-

import pygame

# Define some colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

pygame.init()

click_sound = pygame.mixer.Sound("boink.ogg")

# Set the height and width of the screen
size = [700, 500]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Bouncing Circle")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the circle
circle_size = 40
center_x = size[0] / 2
center_y = size[1] / 2

# Speed and direction of circle
center_change_x = 5
center_change_y = 5

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
    print(done)
    # Set the screen background
    screen.fill(black)

    # Draw a circle
    pygame.draw.circle(screen, yellow, [center_x, center_y], circle_size)
    pygame.draw.circle(screen, black, [center_x, center_y], circle_size - 10)

    # Move the rectangle starting point        
    center_x += center_change_x
    center_y += center_change_y

    # Bounce the ball if needed
    if center_y > size[1] - (circle_size) or center_y < circle_size:
        center_change_y = center_change_y * -1
        click_sound.play()
        pygame.draw.circle(screen, red, [center_x, center_y], circle_size - 10)

    if center_x > size[0] - (circle_size) or center_x < circle_size:
        center_change_x = center_change_x * -1
        click_sound.play()
        pygame.draw.circle(screen, blue, [center_x, center_y], circle_size - 10)

    # Limit to 30 frames per second
    clock.tick(30)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
