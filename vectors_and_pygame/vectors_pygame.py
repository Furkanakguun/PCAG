import math
import pygame

#initialize the game engine
pygame.init()

# Define the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

#Set the height and width of the screen
size = [400,300]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Vectors in PYGAME")

#Loop until exit
done = False
clock = pygame.time.Clock()
angle = 0
mag = 10

# control how held keys are repeated
pygame.key.set_repeat(1, 50)
x, y = pygame.mouse.get_pos()

while not done:
    for event in pygame.event.get(): #User did something
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so adjust speed.
            if event.key == pygame.K_DOWN:
                angle += 5
            elif event.key == pygame.K_UP:
                angle -= 5
            elif event.key == pygame.K_RIGHT:
                mag += 5
            elif event.key == pygame.K_LEFT:
                mag -= 5
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User press mouse button down")
            x , y = pygame.mouse.get_pos()
    # Clear the screen and set the screen background
    screen.fill(white)
    # Draw on the screen a line from (x1,y1) to (x2, y2)
    pygame.draw.aaline(screen, red, [x, y], [x + mag * math.cos(math.radians(angle)), \
                                             y + mag * math.sin(math.radians(angle))], True)
    # This MUST happen after all the other drawing commands
    pygame.display.flip()
    clock.tick(60)  # the program will never run at more than 60 frames per second.
    # Be IDLE friendly
pygame.quit()