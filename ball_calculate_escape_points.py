import pygame, random, math

"""
@author fakgun
"""

# ────────────────────────── Constants ──────────────────────────
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 500
BLACK = (0, 0, 0)
CM_COLOR = (255, 0, 0)  # CM artı işareti
TEXT_COLOR = (255, 150, 0)  # ortadaki momentum sayısı

pygame.init()
FONT = pygame.font.SysFont(None, 28)


# ────────────────────────── Ball Class ─────────────────────────
class Ball:
    def __init__(self):
        self.radius = random.randint(10, 60)  # Radius between 10 and 60 px
        self.x = self.y = 0
        self.change_x = random.uniform(-4, 4)
        self.change_y = random.uniform(-4, 4)
        # kütleyi alanla orantılı yapalım ki sayı büyüsün
        self.mass = 0.02 * (self.radius ** 2)
        # Ball color based on radius
        if self.radius > 40:
            self.color = (255, 0, 0)  # Red if radius > 40px
        else:
            self.color = (0, 255, 0)  # Blue if radius <= 40px


# ––––– yeni top çakışmasız
def make_ball(lst):
    for _ in range(100):
        b = Ball()
        b.x = random.randrange(b.radius, SCREEN_WIDTH - b.radius)
        b.y = random.randrange(b.radius, SCREEN_HEIGHT - b.radius)
        if all(math.hypot(b.x - o.x, b.y - o.y) >= b.radius + o.radius for o in lst):
            return b
    return b


# ––––– genel kütle merkezi (CG) hesaplama
def calculate_cg(balls):
    M = sum(b.mass for b in balls)
    cx = sum(b.mass * b.x for b in balls) / M
    cy = sum(b.mass * b.y for b in balls) / M
    return cx, cy


# ––––– momentum hesaplamaları (SKALER! - toplam momentum büyüklüğü)
def calculation_of_momentum(balls):
    return sum(b.mass * math.hypot(b.change_x, b.change_y) for b in balls)


# ––––– Normal çarpışma tespiti (basit)
def detect_collision_normal(b1, b2):
    dx, dy = b2.x - b1.x, b2.y - b1.y
    dist = math.hypot(dx, dy)
    if dist <= b1.radius + b2.radius:
        angle = math.atan2(dy, dx)
        return True, angle, dist
    return False, None, None


def post_velocities(v1, v2, angle, m1, m2, e=0.9):
    v1n = v1[0] * math.cos(angle) + v1[1] * math.sin(angle)
    v1t = -v1[0] * math.sin(angle) + v1[1] * math.cos(angle)
    v2n = v2[0] * math.cos(angle) + v2[1] * math.sin(angle)
    v2t = -v2[0] * math.sin(angle) + v2[1] * math.cos(angle)

    v1n2 = ((m1 - e * m2) * v1n + (1 + e) * m2 * v2n) / (m1 + m2)
    v2n2 = ((m2 - e * m1) * v2n + (1 + e) * m1 * v1n) / (m1 + m2)

    v1x = v1n2 * math.cos(angle) - v1t * math.sin(angle)
    v1y = v1n2 * math.sin(angle) + v1t * math.cos(angle)
    v2x = v2n2 * math.cos(angle) - v2t * math.sin(angle)
    v2y = v2n2 * math.sin(angle) + v2t * math.cos(angle)
    return (v1x, v1y), (v2x, v2y)


# ––––– Kinetik Enerji Hesaplama
def calculation_of_kinetic_energy(balls):
    """
    Calculates the total kinetic energy of all particles in the system.

    Parameters:
        balls (list of Ball objects): List of balls with mass and velocity.

    Returns:
        float: Total kinetic energy of the system.
    """
    total_ke = 0
    for ball in balls:
        # Kinetik enerji = 0.5 * m * v^2
        v_magnitude = math.hypot(ball.change_x, ball.change_y)  # Hızın büyüklüğü
        total_ke += 0.5 * ball.mass * v_magnitude ** 2  # Toplam enerji
    return total_ke


# ───────────────────── Main Loop ─────────────────────
def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Total |p| and KE display")
    clock = pygame.time.Clock()

    balls = [make_ball([])]

    while True:
        # — Events —
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit();
                return
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                balls.append(make_ball(balls))

        # — Physics: move & wall bounce —
        for b in balls:
            b.x += b.change_x
            b.y += b.change_y
            if b.x < b.radius or b.x > SCREEN_WIDTH - b.radius: b.change_x *= -1
            if b.y < b.radius or b.y > SCREEN_HEIGHT - b.radius: b.change_y *= -1

        # — Pairwise collisions —
        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                b1, b2 = balls[i], balls[j]
                hit, angle, dist = detect_collision_normal(b1, b2)
                if hit:
                    overlap = b1.radius + b2.radius - dist
                    nx, ny = math.cos(angle), math.sin(angle)
                    b1.x -= nx * overlap / 2;
                    b1.y -= ny * overlap / 2
                    b2.x += nx * overlap / 2;
                    b2.y += ny * overlap / 2
                    (b1.change_x, b1.change_y), (b2.change_x, b2.change_y) = \
                        post_velocities((b1.change_x, b1.change_y),
                                        (b2.change_x, b2.change_y),
                                        angle, b1.mass, b2.mass)

        # — Draw —
        screen.fill(BLACK)
        for b in balls:
            pygame.draw.circle(screen, b.color, (int(b.x), int(b.y)), b.radius)

            # Radius'ı çiz
            radius_text = FONT.render(f"r: {b.radius}", True, (255, 255, 255))
            screen.blit(radius_text, (b.x - b.radius // 2, b.y - b.radius // 2))

        # CM
        cx, cy = calculate_cg(balls)
        pygame.draw.line(screen, CM_COLOR, (cx - 4, cy), (cx + 4, cy), 2)
        pygame.draw.line(screen, CM_COLOR, (cx, cy - 4), (cx, cy + 4), 2)

        # Total scalar momentum
        P_sum = int(calculation_of_momentum(balls))
        text = FONT.render(f"Total |p|: {P_sum}", True, TEXT_COLOR)
        rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        screen.blit(text, rect)

        # Total kinetic energy
        KE_sum = calculation_of_kinetic_energy(balls)
        text_KE = FONT.render(f"Total KE: {KE_sum:.2f}", True, TEXT_COLOR)
        rect_KE = text_KE.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30))
        screen.blit(text_KE, rect_KE)

        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
