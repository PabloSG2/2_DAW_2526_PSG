import pygame
import sys
import os
from config import IMG

def pantalla_bienvenida(VENTANA):
    pygame.init()
    clock = pygame.time.Clock()

    # Música de inicio
    try:
        pygame.mixer.music.load("assets/inicio.mp3")
        pygame.mixer.music.play(-1)
    except:
        pass

    # Cargar logo
    ruta_logo = os.path.join(IMG, "logo.png")
    logo = pygame.image.load(ruta_logo).convert_alpha()
    logo = pygame.transform.smoothscale(logo, (420, 420))

    font = pygame.font.Font(None, 70)
    small_font = pygame.font.Font(None, 40)

    boton_rect = pygame.Rect(0, 0, 300, 80)
    boton_rect.center = (VENTANA.get_width() // 2, VENTANA.get_height() // 2 + 260)

    while True:
        clock.tick(60)
        VENTANA.fill((10, 20, 40))

        VENTANA.blit(
            logo,
            (
                VENTANA.get_width() // 2 - logo.get_width() // 2,
                VENTANA.get_height() // 2 - 320
            )
        )

        pygame.draw.rect(VENTANA, (0, 90, 200), boton_rect, border_radius=12)
        pygame.draw.rect(VENTANA, (255, 255, 255), boton_rect, 3, border_radius=12)

        texto = font.render("ENTRAR", True, (255, 255, 255))
        VENTANA.blit(
            texto,
            (
                boton_rect.centerx - texto.get_width() // 2,
                boton_rect.centery - texto.get_height() // 2
            )
        )

        credit = small_font.render("Costal y Fe", True, (180, 180, 180))
        VENTANA.blit(credit, (10, VENTANA.get_height() - 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_rect.collidepoint(event.pos):
                    return

        pygame.display.flip()
