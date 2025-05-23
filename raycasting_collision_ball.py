import pygame
import random
import math

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
BALL_SIZE = 25


class Ball:
    """
    Class to keep track of a ball's location, velocity, and mass.
    """

    def __init__(self):
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.mass = 1.0  # Default mass, can be adjusted based on size


def make_ball():
    """
    Function to make a new, random ball.
    """
    ball = Ball()
    # Starting position of the ball.
    # Take into account the ball size so we don't spawn on the edge.
    ball.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
    ball.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
    # Speed and direction of the ball
    ball.change_x = random.randrange(-2, 3)
    ball.change_y = random.randrange(-2, 3)

    return ball


def raycast_collision(ball1, ball2, dt):
    """
    Uses a ray-casting approach to detect a collision between two balls
    during the time step dt. If a collision occurs, calculates the impact time.
    Returns True if collision happens, False otherwise, along with collision angle
    and point of collision (even if None in case of no collision).
    """
    # Relative position and velocity (ball1 relative to ball2)
    rx = ball1.x - ball2.x
    ry = ball1.y - ball2.y
    vx = ball1.change_x - ball2.change_x
    vy = ball1.change_y - ball2.change_y
    R_eff = ball1.mass + ball2.mass  # Effective radius for collision detection

    A = vx * vx + vy * vy
    B = 2 * (rx * vx + ry * vy)
    C = rx * rx + ry * ry - R_eff * R_eff  # Distance squared minus radii squared

    # Discriminant check for real roots (collision)
    discriminant = B * B - 4 * A * C
    if A == 0 or discriminant < 0:
        return False, None, None, None, None

    sqrt_disc = math.sqrt(discriminant)
    t1 = (-B - sqrt_disc) / (2 * A)
    t2 = (-B + sqrt_disc) / (2 * A)

    t_hit = None
    if 0 < t1 <= dt:
        t_hit = t1
    elif 0 < t2 <= dt:
        t_hit = t2

    if t_hit is None:
        return False, None, None, None, None

    # Collision point is computed along ball1's path
    collision_x = (ball1.x + ball1.change_x * t_hit)
    collision_y = (ball1.y + ball1.change_y * t_hit)

    # Calculate collision angle (direction of the collision vector)
    collision_angle = math.atan2(ry, rx)

    # Return True for collision and the calculated values
    return True, t_hit, collision_angle, collision_x, collision_y


def calculate_post_collision_velocities(m1, m2, v1, v2, collision_angle, restitution=1.0):
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

    pygame.display.set_caption("Ball Collision with Ray Casting")

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
            if ball.y > SCREEN_HEIGHT - BALL_SIZE or ball.y < BALL_SIZE:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - BALL_SIZE or ball.x < BALL_SIZE:
                ball.change_x *= -1

        # --- Collision Detection with Ray Casting
        dt = 1.0 / 60.0  # Time step, assuming 60 FPS
        for i in range(len(ball_list)):
            for j in range(i + 1, len(ball_list)):
                b1 = ball_list[i]
                b2 = ball_list[j]
                collided, t_hit, collision_angle, collision_x, collision_y = raycast_collision(b1, b2, dt)
                if collided:
                    # Update ball positions to avoid overlap
                    b1.x = collision_x
                    b1.y = collision_y
                    b2.x = collision_x
                    b2.y = collision_y

                    # Calculate new velocities after collision
                    v1 = (b1.change_x, b1.change_y)
                    v2 = (b2.change_x, b2.change_y)
                    v1_after, v2_after = calculate_post_collision_velocities(
                        b1.mass, b2.mass, v1, v2, collision_angle, restitution=1.0
                    )
                    b1.change_x, b1.change_y = v1_after
                    b2.change_x, b2.change_y = v2_after

        # --- Drawing
        screen.fill(BLACK)

        for ball in ball_list:
            pygame.draw.circle(screen, WHITE, [ball.x, ball.y], BALL_SIZE)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
