# objects.py

import math
import pygame
from config import (
    WIDTH, HEIGHT, TABLE_MARGIN,
    BALL_RADIUS, FRICTION, MIN_SPEED,
    CUE_BALL_COLOR, ENEMY_BALL_COLOR,
    POCKET_RADIUS, POCKET_COLOR, GREEN, RAIL_COLOR
)

# -------------------------
# CLASE BOLA
# -------------------------
class Ball:
    def __init__(self, x, y, color, is_cue=False, is_enemy=False):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.color = color
        self.is_cue = is_cue
        self.is_enemy = is_enemy
        self.alive = True

    def update(self):
        if not self.alive:
            return

        self.x += self.vx
        self.y += self.vy

        self.vx *= FRICTION
        self.vy *= FRICTION

        if abs(self.vx) < MIN_SPEED:
            self.vx = 0
        if abs(self.vy) < MIN_SPEED:
            self.vy = 0

        self.handle_rails()

    def handle_rails(self):
        left = TABLE_MARGIN + BALL_RADIUS
        right = WIDTH - TABLE_MARGIN - BALL_RADIUS
        top = TABLE_MARGIN + BALL_RADIUS
        bottom = HEIGHT - TABLE_MARGIN - BALL_RADIUS

        if self.x < left:
            self.x = left
            self.vx *= -1
        elif self.x > right:
            self.x = right
            self.vx *= -1

        if self.y < top:
            self.y = top
            self.vy *= -1
        elif self.y > bottom:
            self.y = bottom
            self.vy *= -1

    def draw(self, screen):
        if self.alive:
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), BALL_RADIUS)

    def speed(self):
        return math.hypot(self.vx, self.vy)


# -------------------------
# AGUJEROS
# -------------------------
class Pocket:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self, screen):
        pygame.draw.circle(screen, POCKET_COLOR, (int(self.x), int(self.y)), POCKET_RADIUS)


# -------------------------
# MESA
# -------------------------
class Table:
    def __init__(self):
        self.left = TABLE_MARGIN
        self.right = WIDTH - TABLE_MARGIN
        self.top = TABLE_MARGIN
        self.bottom = HEIGHT - TABLE_MARGIN

        offset = 5

        self.pockets = [
            Pocket(self.left - offset, self.top - offset),
            Pocket(self.right + offset, self.top - offset),
            Pocket(self.left - offset, self.bottom + offset),
            Pocket(self.right + offset, self.bottom + offset),
            Pocket(WIDTH // 2, self.top - offset),
            Pocket(WIDTH // 2, self.bottom + offset)
        ]

    def draw(self, screen):
        screen.fill((0, 100, 0))

        pygame.draw.rect(screen, RAIL_COLOR,
                         (self.left - 20, self.top - 20,
                          self.right - self.left + 40,
                          self.bottom - self.top + 40))

        pygame.draw.rect(screen, GREEN,
                         (self.left, self.top,
                          self.right - self.left,
                          self.bottom - self.top))

        for p in self.pockets:
            p.draw(screen)


# -------------------------
# COLISIONES ENTRE BOLAS
# -------------------------
def balls_collide(b1, b2):
    if not b1.alive or not b2.alive:
        return

    dx = b2.x - b1.x
    dy = b2.y - b1.y
    dist = math.hypot(dx, dy)

    if dist < 2 * BALL_RADIUS and dist != 0:
        overlap = 2 * BALL_RADIUS - dist
        nx = dx / dist
        ny = dy / dist

        b1.x -= nx * overlap / 2
        b1.y -= ny * overlap / 2
        b2.x += nx * overlap / 2
        b2.y += ny * overlap / 2

        kx = b1.vx - b2.vx
        ky = b1.vy - b2.vy
        p = 2 * (nx * kx + ny * ky) / 2

        b1.vx -= p * nx
        b1.vy -= p * ny
        b2.vx += p * nx
        b2.vy += p * ny


# -------------------------
# DETECCIÓN DE AGUJEROS (CORREGIDA)
# -------------------------
def pocket_check(balls, pockets):
    for b in balls:
        if not b.alive:
            continue

        for p in pockets:
            dx = b.x - p.x
            dy = b.y - p.y
            dist = math.hypot(dx, dy)

            if dist < (POCKET_RADIUS - BALL_RADIUS):
                b.alive = False
                break


# -------------------------
# CREAR BOLAS
# -------------------------
def create_balls():
    balls = []

    cue = Ball(WIDTH * 0.25, HEIGHT / 2, CUE_BALL_COLOR, is_cue=True)
    balls.append(cue)

    start_x = WIDTH * 0.7
    start_y = HEIGHT / 2

    for row in range(5):
        for col in range(row + 1):
            x = start_x + row * (2 * BALL_RADIUS + 1)
            y = start_y - row * BALL_RADIUS + 2 * BALL_RADIUS * col
            balls.append(Ball(x, y, ENEMY_BALL_COLOR, is_enemy=True))

    return balls, cue


# -------------------------
# IA SIMPLE
# -------------------------
def ai_shot(cue, balls):
    target = None
    for b in balls:
        if b.is_enemy and b.alive:
            target = b
            break

    if not target:
        return

    dx = target.x - cue.x
    dy = target.y - cue.y
    dist = math.hypot(dx, dy)

    nx = dx / dist
    ny = dy / dist

    power = 10
    cue.vx = nx * power
    cue.vy = ny * power


def all_balls_stopped(balls):
    return all(b.speed() == 0 for b in balls if b.alive)
