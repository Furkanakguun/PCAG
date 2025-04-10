"""
Simple 2‑D ray‑caster with DDA.
Left‑click to move the player, right‑click to rotate the view.
Requires only pygame (pip install pygame).
"""
import math, sys, pygame as pg

# ── CONFIG ────────────────────────────────────────────────────────────────────
TILE      = 64                         # side length of a map square (px)
MAP       = [                          # 0 = empty, 1 = wall
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,1,1,0,0,0,1],
    [1,0,0,1,0,1,0,0,0,1],
    [1,0,0,1,0,1,0,0,0,1],
    [1,0,0,1,1,1,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
]
W, H      = len(MAP[0])*TILE, len(MAP)*TILE
FOV       = math.radians(60)          # field‑of‑view
NUM_RAYS  = 120                       # number of rays per frame
MAX_DIST  = 1000                      # fail‑safe limit

# ── INIT ──────────────────────────────────────────────────────────────────────
pg.init();  screen = pg.display.set_mode((W, H));  clock = pg.time.Clock()
player_x, player_y, player_a = 160.0, 160.0, 0.0   # pos (px) and angle (rad)

# ── CORE DDA FUNCTION ────────────────────────────────────────────────────────
def cast_single_ray(px, py, angle):
    """
    Return (hit_x, hit_y, distance, side) where side is 0 for vertical wall hit,
    1 for horizontal wall hit.  DDA steps grid‑by‑grid until a wall cell (1) is hit.
    """
    # Direction vector of the ray
    dx, dy = math.cos(angle), math.sin(angle)

    # Which grid square is the player in?
    map_x, map_y = int(px // TILE), int(py // TILE)

    # Length of ray from one x or y side to next x or y side
    delta_dist_x = abs(1 / dx) if dx else 1e30
    delta_dist_y = abs(1 / dy) if dy else 1e30

    # Step direction (+1 or −1) and first side‑distances
    if dx < 0:
        step_x = -1
        side_dist_x = (px - map_x * TILE) * delta_dist_x
    else:
        step_x = 1
        side_dist_x = ((map_x + 1) * TILE - px) * delta_dist_x
    if dy < 0:
        step_y = -1
        side_dist_y = (py - map_y * TILE) * delta_dist_y
    else:
        step_y = 1
        side_dist_y = ((map_y + 1) * TILE - py) * delta_dist_y

    # DDA loop
    side = None
    while True:
        if side_dist_x < side_dist_y:
            side_dist_x += delta_dist_x
            map_x += step_x
            side = 0                          # vertical grid‑line hit
        else:
            side_dist_y += delta_dist_y
            map_y += step_y
            side = 1                          # horizontal grid‑line hit
        if map_x < 0 or map_y < 0 or map_x >= len(MAP[0]) or map_y >= len(MAP):
            return px, py, MAX_DIST, side     # out of bounds
        if MAP[map_y][map_x] == 1:            # wall cell
            # Intersection point in world space
            if side == 0:
                dist = (map_x - px / TILE + (1 - step_x) / 2) / dx
            else:
                dist = (map_y - py / TILE + (1 - step_y) / 2) / dy
            hit_x, hit_y = px + dx * dist * TILE, py + dy * dist * TILE
            return hit_x, hit_y, dist * TILE, side

# ── MAIN LOOP ─────────────────────────────────────────────────────────────────
while True:
    for ev in pg.event.get():
        if ev.type == pg.QUIT:  pg.quit(); sys.exit()
        if ev.type == pg.MOUSEBUTTONDOWN:
            if ev.button == 1:  player_x, player_y = ev.pos   # teleport
            if ev.button == 3:  player_a = (player_a + math.radians(15)) % (2*math.pi)

    screen.fill((30,30,30))

    # draw map (top‑down for clarity)
    for y,row in enumerate(MAP):
        for x,val in enumerate(row):
            color = (200,200,200) if val else (50,50,50)
            pg.draw.rect(screen, color, (x*TILE, y*TILE, TILE-1, TILE-1))

    # cast rays
    start_angle = player_a - FOV/2
    for n in range(NUM_RAYS):
        ray_angle = start_angle + n * FOV / NUM_RAYS
        hx, hy, dist, _ = cast_single_ray(player_x, player_y, ray_angle)
        pg.draw.line(screen, (255,0,0), (player_x, player_y), (hx, hy), 1)

    # draw player
    pg.draw.circle(screen, (0,255,0), (int(player_x), int(player_y)), 5)
    pg.display.flip();  clock.tick(60)
