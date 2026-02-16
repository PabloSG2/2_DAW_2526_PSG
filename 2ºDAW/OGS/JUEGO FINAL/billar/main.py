# main.py

import pygame
import math
from config import WIDTH, HEIGHT, FPS, WHITE, FONT_SIZE
from objects import (
    Table, create_balls, balls_collide,
    pocket_check, all_balls_stopped, ai_shot
)

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Billar vs Máquina")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, FONT_SIZE)

    table = Table()
    balls, cue = create_balls()

    running = True
    player_turn = True
    aiming = False
    aim_start = None
    winner = None

    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if winner:
                continue

            # -----------------------------
            #   CONTROL DEL JUGADOR
            # -----------------------------
            if player_turn:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if all_balls_stopped(balls):
                        aiming = True
                        aim_start = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if aiming and all_balls_stopped(balls):
                        aiming = False
                        mx, my = pygame.mouse.get_pos()
                        dx = aim_start[0] - mx
                        dy = aim_start[1] - my
                        power = math.hypot(dx, dy) / 10

                        if power > 0:
                            nx = dx / (math.hypot(dx, dy) + 1e-6)
                            ny = dy / (math.hypot(dx, dy) + 1e-6)
                            cue.vx = nx * power
                            cue.vy = ny * power

                            player_turn = False

        # -----------------------------
        #   FÍSICA DE LAS BOLAS
        # -----------------------------
        for b in balls:
            b.update()

        for i in range(len(balls)):
            for j in range(i + 1, len(balls)):
                balls_collide(balls[i], balls[j])

        before = sum(1 for b in balls if b.alive)
        pocket_check(balls, table.pockets)
        after = sum(1 for b in balls if b.alive)
        scored = before != after

        # -----------------------------
        #   TURNO DE LA IA
        # -----------------------------
        if not player_turn and all_balls_stopped(balls):
            ai_shot(cue, balls)

            if not scored:
                player_turn = True

        # -----------------------------
        #   VICTORIA
        # -----------------------------
        enemy_alive = any(b.is_enemy and b.alive for b in balls)
        cue_alive = any(b.is_cue and b.alive for b in balls)

        if not enemy_alive:
            winner = "Jugador"
        elif not cue_alive:
            winner = "Máquina"

        # -----------------------------
        #   DIBUJADO
        # -----------------------------
        table.draw(screen)
        for b in balls:
            b.draw(screen)

        if player_turn and aiming:
            mx, my = pygame.mouse.get_pos()
            pygame.draw.line(screen, WHITE, aim_start, (mx, my), 2)

        text = f"Ganador: {winner}" if winner else f"Turno: {'Jugador' if player_turn else 'Máquina'}"
        screen.blit(font.render(text, True, WHITE), (20, 10))

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
