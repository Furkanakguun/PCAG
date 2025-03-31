import pygame
import math
import numpy as np

# -------------------------------- #

def draw_line_dashed(surface, color, start_pos, end_pos, width = 1, dash_length = 2, exclude_corners = True):

    # convert tuples to numpy arrays
    start_pos = np.array(start_pos)
    end_pos   = np.array(end_pos)

    # get euclidian distance between start_pos and end_pos
    length = np.linalg.norm(end_pos - start_pos)

    # get amount of pieces that line will be split up in (half of it are amount of dashes)
    dash_amount = int(length / dash_length)

    # x-y-value-pairs of where dashes start (and on next, will end)
    dash_knots = np.array([np.linspace(start_pos[i], end_pos[i], dash_amount) for i in range(2)]).transpose()

    return [pygame.draw.line(surface, color, tuple(dash_knots[n]), tuple(dash_knots[n+1]), width)
            for n in range(int(exclude_corners), dash_amount - int(exclude_corners), 2)]

# -------------------------------- #

# Initialize the game engine
pygame.init()
 
# Define the colors we will use in RGB format
black = (  0,  0,    0)
white = (255, 255, 255)
blue =  (  0,   0, 255)
green = (  0, 255,   0)
red =   (255,   0,   0)
 
# Set the height and width of the screen
size = [400, 300]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("BCO611 Bilgisayar Animasyonu ve Oyun Teknolojilerinde Fizik")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

x, y, angle, mag = 0, 0, 0, 0
vectors = []

# control how held keys are repeated
#pygame.key.set_repeat(1, 50)

while not done:    
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        if event.type == pygame.KEYDOWN:
            # Figure out if it was an arrow key. If so adjust speed.
            if event.key == pygame.K_DOWN: angle+= 10                
            elif event.key == pygame.K_UP: angle-= 10
            elif event.key == pygame.K_RIGHT: mag+= 5
            elif event.key == pygame.K_LEFT: mag-= 5
            
            elif event.key == pygame.K_KP_PLUS:
                print("User pressed NumPad <+>")
                vectors.append((x, y, angle, mag))
                is_are = 'is' if len(vectors) < 2 else 'are'
                plural = 's' if len(vectors) > 1 else ''
                print(f'There {is_are} {len(vectors)} vector{plural}')
                print(vectors)
                print('[{:.2f}, {:.2f}] - [{:.2f}, {:.2f}]'.format(x, y, (x + mag*math.cos(math.radians(angle))), (y + mag*math.sin(math.radians(angle)))))
                
            elif event.key == pygame.K_KP_ENTER:
                print("User pressed <ENTER>")
                # Sum all restored vectors
                sumX = sum([vectors[i][0] - (vectors[i][0] + vectors[i][3]*math.cos(math.radians(vectors[i][2]))) for i in range(len(vectors))])
                #sumX = sum([vectors[i][0] for i in range(len(vectors))])
                sumY = sum([vectors[i][1] - (vectors[i][1] + vectors[i][3]*math.sin(math.radians(vectors[i][2]))) for i in range(len(vectors))])
                #sumY = sum([vectors[i][1] for i in range(len(vectors))])
                sumMag = int(np.sqrt(sumX**2 + sumY**2))
                sumAngle = int(np.degrees(np.arctan2(sumY, sumX))) -180
    
                vectors = []
                vectors.append((x, y, sumAngle, sumMag))
                print(f'Resultant Vector -> x:{sumX:.2f} y:{sumY:.2f} Magnitude:{sumMag:.2f} Angle:{sumAngle}')
                    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button") 
            x, y = pygame.mouse.get_pos()
            angle, mag = -45, 10
            
    # Clear the screen and set the screen background
    screen.fill(white)
    
    # Draw on the screen a  line from (x1,y1) to (x2, y2)    
    pygame.draw.aaline(screen, black, [x, y], [x+mag*math.cos(math.radians(angle)),\
                                     y+mag*math.sin(math.radians(angle))], True)    
    # horizontal component
    draw_line_dashed(screen, red, (x, y), (x+mag*math.cos(math.radians(angle)), y)) 
    #pygame.draw.aaline(screen, red, [x, y], [x+mag*math.cos(math.radians(angle)), y], True)    
    # vertical component
    draw_line_dashed(screen, blue, (x, y), (x, y+mag*math.sin(math.radians(angle))))
    #pygame.draw.aaline(screen, blue, [x, y], [x, y+mag*math.sin(math.radians(angle))], True)

    
    # Draw all restored vectors
    if vectors:
        for vec in vectors:
            #print(vec)
            # Draw on the screen a  line from (x1,y1) to angle, magtitude    
            pygame.draw.aaline(screen, black, [vec[0], vec[1]], [vec[0]+vec[3]*math.cos(math.radians(vec[2])),\
                                             vec[1]+vec[3]*math.sin(math.radians(vec[2]))], True)    
                # # horizontal component
                # pygame.draw.aaline(screen, red, [x, y], [x+mag*math.cos(math.radians(angle)), y], True)    
                # # vertical component
                # pygame.draw.aaline(screen, blue, [x, y], [x, y+mag*math.sin(math.radians(angle))], True)
    
                
    # Go ahead and update the screen with what we've drawn.
    # This MUST happen after all the other drawing commands.
    pygame.display.flip()
    
    clock.tick(60) # program will never run at more than 60 frames per second
# Be IDLE friendly
pygame.quit()
