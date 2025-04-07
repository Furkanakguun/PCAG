import pygame
import numpy as np

CIRCLERADIUS = 20 
alpha = 0               # Initial angle in degrees
v0 =0.0

# Integration loop
def dropBall(x, y, v0, g, time, dt):
    
    # Numerical initialization
    n = int(np.ceil(time/dt))
    a = np.zeros((n), float)
    v = np.zeros((n), float)
    r = np.zeros((n), float)
    t = np.zeros((n), float)
    
    # Set initial values
    # Set initial values
    r[0] = y   # meters 
    v[0] = v0    # initial velocity
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
background_image = pygame.image.load("background.png")
# Create an 884x804 sized screen
background_image_width, background_image_height = background_image.get_rect().size
screen = pygame.display.set_mode((background_image_width, background_image_height), pygame.DOUBLEBUF)
background_image = background_image.convert()       
background_image_ground = background_image_height
 
pygame.display.set_caption("BCO611 is cool")
 
#Loop until the user clicks the close button.
done = False
simulation = False 
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
                _, r, _ = dropBall(circle_x, background_image_height - circle_y, 0, 20, 9.81, 1/60)
                print('dropBall')
                simulation = True
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
        #print(circle_x, circle_y)
        if circle_y > background_image_height - CIRCLERADIUS:
            circle_y = background_image_height - CIRCLERADIUS
        if circle_y < 0 + CIRCLERADIUS:
            circle_y = CIRCLERADIUS
        if circle_x > background_image_width - CIRCLERADIUS:
            circle_x = background_image_width - CIRCLERADIUS
        if circle_x < 0 + CIRCLERADIUS:
            circle_x = CIRCLERADIUS    
            
    # ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT    

    # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
    # Copy image to screen:
    # First, clear the screen to Background. Don't put other drawing commands
    # above this, or they will be erased with this command.   
    screen.blit(background_image, background_position)
    pygame.draw.aaline(screen, BLACK, [circle_x, circle_y], [circle_x+v0*np.cos(np.radians(alpha)),\
                                                      circle_y+v0*np.sin(np.radians(alpha))], True)    
    
    if simulation:
        for i in range(len(r)):
            circle_y = background_image_height - r[i]
            screen.blit(background_image, background_position)
            pygame.draw.circle(screen, RED, (circle_x, circle_y), CIRCLERADIUS, CIRCLERADIUS-2)
            pygame.display.flip()
            #clock.tick(60)
            if circle_y > background_image_height - CIRCLERADIUS:  break     
        simulation = False
    else:    
        # Draw the circle
        pygame.draw.circle(screen, RED, (circle_x, circle_y), CIRCLERADIUS, CIRCLERADIUS-2)
  
    # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT    

    pygame.display.flip()
    # # pygame.display.update()
    clock.tick(30)
    
pygame.quit()
