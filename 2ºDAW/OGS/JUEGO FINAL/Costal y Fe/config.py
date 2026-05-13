import pygame

pygame.init()

ANCHO = 900
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Costal y Fe")

FPS = 60

COLORES = {
    "fondo": (20, 15, 40),
    "panel": (40, 25, 70),
    "dorado": (200, 170, 60),
    "texto": (230, 230, 240),
}

# Ruta de imágenes
IMG = "assets/img"
