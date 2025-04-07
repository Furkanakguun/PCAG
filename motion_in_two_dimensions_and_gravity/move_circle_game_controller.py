import pygame
import numpy as np

# Integration loop
def dropBall(x, y, g, time, dt):
    
    # Numerical initialization
    n = int(np.ceil(time/dt))
    a = np.zeros((n), float)
    v = np.zeros((n), float)
    r = np.zeros((n), float)
    t = np.zeros((n), float)
    
    # Set initial values
    # Set initial values
    r[0] = y   # meters 
    v[0] = 0    # initial velocity
    a[:] = -g   # constant acceleretion

    # Integration loop
    for i in range(n-1):
        v[i+1] = v[i] + a[i]*dt
        r[i+1] = r[i] + v[i+1]*dt
        t[i+1] = t[i] + dt
        
    return t, r, v

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)

pygame.init()
# Count the joysticks the computer has
joystick_count = pygame.joystick.get_count()
if joystick_count == 0:
    # No joysticks!
    print ("Error, I didn't find any joysticks.")
    pygame.quit()
else:
    # Use joystick #0 and initialize it
    my_joystick = pygame.joystick.Joystick(0)
    my_joystick.init()
  
# Set the width and height of the screen [width,height]
# Set positions of graphics
background_position = [0, 0]
# Load and set up graphics.
background_image = pygame.image.load("pizzaTower.png")
# Create an 884x804 sized screen
background_image_width, background_image_height = background_image.get_rect().size
screen = pygame.display.set_mode((background_image_width, background_image_height))
background_image = background_image.convert()       
background_image_ground = background_image_height
 
pygame.display.set_caption("BCO611 is cool")
 
#Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of the circle
circle_x = background_image_width/2
circle_y = background_image_height/2

while not done:

    # ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        if event.type == pygame.JOYBUTTONDOWN:
            print("Joystick button pressed.")
            if my_joystick.get_button(5):
                _, r, _ = dropBall(circle_x, circle_y, 9.81, 5, 1/60)
    # ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT

    # ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT
            
    # As long as there is a joystick
    if joystick_count != 0:
    
        # This gets the position of the axis on the game controller
        # It returns a number between -1.0 and +1.0
        horiz_axis_pos = my_joystick.get_axis(0)
        vert_axis_pos = my_joystick.get_axis(1)   
        
        # Move x according to the axis. We multiply by 10 to speed up the movement.
        circle_x = circle_x + int(horiz_axis_pos * 10)
        circle_y = circle_y + int(vert_axis_pos * 10)
        print(circle_x, circle_y)
    
    screen.blit(background_image, background_position)
    # Draw the circle
    pygame.draw.circle(screen, RED, (circle_x, circle_y), 20, 18)

    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()
