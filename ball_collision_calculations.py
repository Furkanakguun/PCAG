import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500


class Ball:
    """
    Class to keep track of a ball's location, velocity, mass, size, and color.
    """

    def __init__(self):
        self.radius = random.randint(10, 30)  # Random size for each ball (between 10 and 30 pixels)
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.mass = self.radius * 0.1  # Mass is proportional to the radius
        self.color = (
            random.randint(100, 255),  # Random color for each ball
            random.randint(100, 255),
            random.randint(100, 255)
        )


def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(ball.radius, SCREEN_WIDTH - ball.radius)
    ball.y = random.randrange(ball.radius, SCREEN_HEIGHT - ball.radius)
    # Speed and direction of the ball
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)

    return ball


def normal_collision_detection(ball1, ball2):
    """
    Uses normal collision detection for elastic collisions.
    Checks if the balls' centers are within their radii distance.
    """
    # Calculate the distance between the two balls' centers
    dx = ball2.x - ball1.x
    dy = ball2.y - ball1.y
    distance = math.hypot(dx, dy)

    # If the distance between the centers is less than the sum of the radii, a collision occurs
    if distance <= ball1.radius + ball2.radius:
        # Normalize the direction vector
        collision_angle = math.atan2(dy, dx)  # Angle of collision
        return True, collision_angle, (ball1.x + ball2.x) / 2, (ball1.y + ball2.y) / 2
    return False, None, None, None


def calculate_post_collision_velocities(m1, m2, v1, v2, collision_angle, restitution=0.9):
    """
    After a collision, this function calculates the post-collision velocities.
    Applies the formula for elastic collision.
    """
    v1x_rot = v1[0] * math.cos(collision_angle) + v1[1] * math.sin(collision_angle)
    v1y_rot = -v1[0] * math.sin(collision_angle) + v1[1] * math.cos(collision_angle)

    v2x_rot = v2[0] * math.cos(collision_angle) + v2[1] * math.sin(collision_angle)
    v2y_rot = -v2[0] * math.sin(collision_angle) + v2[1] * math.cos(collision_angle)

    # Calculate the new velocities after collision
    v1x_rot_after = (v1x_rot * (m1 - restitution * m2) + (1 + restitution) * m2 * v2x_rot) / (m1 + m2)
    v2x_rot_after = (v2x_rot * (m2 - restitution * m1) + (1 + restitution) * m1 * v1x_rot) / (m1 + m2)

    v1y_rot_after = v1y_rot  # Tangential velocity doesn't change
    v2y_rot_after = v2y_rot

    # Convert the velocities back to Cartesian coordinates
    v1x = v1x_rot_after * math.cos(collision_angle) - v1y_rot_after * math.sin(collision_angle)
    v1y = v1x_rot_after * math.sin(collision_angle) + v1y_rot_after * math.cos(collision_angle)

    v2x = v2x_rot_after * math.cos(collision_angle) - v2y_rot_after * math.sin(collision_angle)
    v2y = v2x_rot_after * math.sin(collision_angle) + v2y_rot_after * math.cos(collision_angle)

    return (v1x, v1y), (v2x, v2y)


def main():
    """
    This is our main program.
    """
    pygame.init()

    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Ball Collision with Normal Detection")

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    ball_list = []

    ball = make_ball()
    ball_list.append(ball)

    # -------- Main Program Loop -----------
    while not done:
        # --- Event Processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball = make_ball()
                    ball_list.append(ball)

        # --- Logic
        for ball in ball_list:
            # Move the ball's center
            ball.x += ball.change_x
            ball.y += ball.change_y

            # Bounce the ball if needed
            if ball.y > SCREEN_HEIGHT - ball.radius or ball.y < ball.radius:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - ball.radius or ball.x < ball.radius:
                ball.change_x *= -1

        # --- Collision Detection with Normal Elastic Collision
        for i in range(len(ball_list)):
            for j in range(i + 1, len(ball_list)):
                b1 = ball_list[i]
                b2 = ball_list[j]

                # Normal collision detection method
                collided, collision_angle, collision_x, collision_y = normal_collision_detection(b1, b2)

                if collided:
                    # Adjust ball positions to avoid overlap
                    overlap_distance = (b1.radius + b2.radius) - math.hypot(b1.x - b2.x, b1.y - b2.y)
                    b1.x -= overlap_distance * math.cos(collision_angle) / 2
                    b1.y -= overlap_distance * math.sin(collision_angle) / 2
                    b2.x += overlap_distance * math.cos(collision_angle) / 2
                    b2.y += overlap_distance * math.sin(collision_angle) / 2

                    # Calculate new velocities after collision
                    v1 = (b1.change_x, b1.change_y)
                    v2 = (b2.change_x, b2.change_y)
                    v1_after, v2_after = calculate_post_collision_velocities(
                        b1.mass, b2.mass, v1, v2, collision_angle, restitution=0.9
                    )
                    b1.change_x, b1.change_y = v1_after
                    b2.change_x, b2.change_y = v2_after

        # --- Drawing
        screen.fill(BLACK)

        for ball in ball_list:
            pygame.draw.circle(screen, ball.color, [ball.x, ball.y], ball.radius)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
