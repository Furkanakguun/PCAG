import pygame
import random
import math

# Screen configuration
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500

# Define colors
BLACK = (0, 0, 0)


# --- Ball Class ---
class Ball:
    """
    Stores a ball's position, velocity, radius, mass, and color.
    """

    def __init__(self):
        self.radius = random.randint(10, 30)  # Random radius: 10 to 30 pixels
        self.x = 0
        self.y = 0
        self.change_x = 0
        self.change_y = 0
        self.mass = self.radius * 0.1  # Mass proportional to radius
        self.color = (
            random.randint(100, 255),
            random.randint(100, 255),
            random.randint(100, 255)
        )


def make_ball(ball_list):
    """
    Creates a new ball with random attributes, ensuring it does not overlap any ball in ball_list.
    """
    max_attempts = 100
    for _ in range(max_attempts):
        ball = Ball()
        ball.x = random.randrange(ball.radius, SCREEN_WIDTH - ball.radius)
        ball.y = random.randrange(ball.radius, SCREEN_HEIGHT - ball.radius)
        ball.change_x = random.randrange(-2, 3)
        ball.change_y = random.randrange(-2, 3)
        overlap = False
        for other in ball_list:
            dx = ball.x - other.x
            dy = ball.y - other.y
            distance = math.hypot(dx, dy)
            if distance < (ball.radius + other.radius):
                overlap = True
                break
        if not overlap:
            return ball
    # If no valid position found, return the last candidate (rare case)
    return ball


# --- Ray-Casting Collision Detection ---
def raycast_collision(ball1, ball2, dt):
    """
    Determines if ball1 (moving along its velocity vector) will collide with ball2 within time dt using ray casting.
    Returns:
        (True, t_hit, collision_angle, collision_x, collision_y) if collision occurs in dt,
        Otherwise: (False, None, None, None, None).
    """
    rx = ball1.x - ball2.x
    ry = ball1.y - ball2.y
    vx = ball1.change_x - ball2.change_x
    vy = ball1.change_y - ball2.change_y
    R_eff = ball1.radius + ball2.radius

    A = vx * vx + vy * vy
    B = 2 * (rx * vx + ry * vy)
    C = rx * rx + ry * ry - R_eff * R_eff

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

    collision_x = ball1.x + ball1.change_x * t_hit
    collision_y = ball1.y + ball1.change_y * t_hit
    collision_angle = math.atan2(ball2.y - ball1.y, ball2.x - ball1.x)

    return True, t_hit, collision_angle, collision_x, collision_y


# --- Normal Collision Detection ---
def detect_collision_normal(ball1, ball2):
    """
    Detects a collision based on distance between centers. Returns collision angle and midpoint.
    """
    dx = ball2.x - ball1.x
    dy = ball2.y - ball1.y
    distance = math.hypot(dx, dy)
    if distance <= ball1.radius + ball2.radius:
        collision_angle = math.atan2(dy, dx)
        collision_point = ((ball1.x + ball2.x) / 2, (ball1.y + ball2.y) / 2)
        return True, collision_angle, collision_point[0], collision_point[1]
    return False, None, None, None


# --- Post-Collision Velocity Calculation ---
def compute_post_collision_velocities(v1, v2, collision_angle, m1, m2, restitution=0.9):
    """
    Calculates post-collision velocities based on conservation of momentum and restitution.
    """
    v1_normal = v1[0] * math.cos(collision_angle) + v1[1] * math.sin(collision_angle)
    v1_tangent = -v1[0] * math.sin(collision_angle) + v1[1] * math.cos(collision_angle)
    v2_normal = v2[0] * math.cos(collision_angle) + v2[1] * math.sin(collision_angle)
    v2_tangent = -v2[0] * math.sin(collision_angle) + v2[1] * math.cos(collision_angle)

    v1_normal_after = ((v1_normal * (m1 - restitution * m2)) + (1 + restitution) * m2 * v2_normal) / (m1 + m2)
    v2_normal_after = ((v2_normal * (m2 - restitution * m1)) + (1 + restitution) * m1 * v1_normal) / (m1 + m2)

    v1_tangent_after = v1_tangent
    v2_tangent_after = v2_tangent

    new_v1_x = v1_normal_after * math.cos(collision_angle) - v1_tangent_after * math.sin(collision_angle)
    new_v1_y = v1_normal_after * math.sin(collision_angle) + v1_tangent_after * math.cos(collision_angle)
    new_v2_x = v2_normal_after * math.cos(collision_angle) - v2_tangent_after * math.sin(collision_angle)
    new_v2_y = v2_normal_after * math.sin(collision_angle) + v2_tangent_after * math.cos(collision_angle)

    return (new_v1_x, new_v1_y), (new_v2_x, new_v2_y)


# --- Main Program ---
def main():
    pygame.init()
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Ball Collision: Raycasting & Normal Detection")
    clock = pygame.time.Clock()
    done = False

    ball_list = []
    ball_list.append(make_ball(ball_list))

    # Default: use Normal Collision Detection. Toggle with 'r'
    use_ray_casting = False

    while not done:
        # --- Event Processing ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    ball_list.append(make_ball(ball_list))
                elif event.key == pygame.K_r:
                    use_ray_casting = not use_ray_casting
                    print("Using Ray Casting:", use_ray_casting)

        # --- Update Ball Positions (and screen boundaries) ---
        for ball in ball_list:
            ball.x += ball.change_x
            ball.y += ball.change_y

            if ball.y > SCREEN_HEIGHT - ball.radius or ball.y < ball.radius:
                ball.change_y *= -1
            if ball.x > SCREEN_WIDTH - ball.radius or ball.x < ball.radius:
                ball.change_x *= -1

        # --- Collision Detection & Response ---
        dt = 1.0 / 60.0  # Time step
        # Loop through each unique pair of balls.
        for i in range(len(ball_list)):
            for j in range(i + 1, len(ball_list)):
                b1 = ball_list[i]
                b2 = ball_list[j]

                if use_ray_casting:
                    collided, t_hit, collision_angle, collision_x, collision_y = raycast_collision(b1, b2, dt)
                else:
                    collided, collision_angle, collision_x, collision_y = detect_collision_normal(b1, b2)

                if collided:
                    # Adjust positions: determine overlap and separate along the collision normal.
                    dx = b2.x - b1.x
                    dy = b2.y - b1.y
                    distance = math.hypot(dx, dy)
                    overlap = (b1.radius + b2.radius) - distance
                    b1.x -= (overlap / 2) * math.cos(collision_angle)
                    b1.y -= (overlap / 2) * math.sin(collision_angle)
                    b2.x += (overlap / 2) * math.cos(collision_angle)
                    b2.y += (overlap / 2) * math.sin(collision_angle)

                    # Compute new velocities using the collision angle, masses, and restitution.
                    v1 = (b1.change_x, b1.change_y)
                    v2 = (b2.change_x, b2.change_y)
                    new_v1, new_v2 = compute_post_collision_velocities(v1, v2, collision_angle, b1.mass, b2.mass,
                                                                       restitution=0.9)
                    b1.change_x, b1.change_y = new_v1
                    b2.change_x, b2.change_y = new_v2

        # --- Drawing ---
        screen.fill(BLACK)
        for ball in ball_list:
            pygame.draw.circle(screen, ball.color, (int(ball.x), int(ball.y)), ball.radius)
        pygame.display.flip()
        clock.tick(60)
    pygame.quit()


if __name__ == "__main__":
    main()
