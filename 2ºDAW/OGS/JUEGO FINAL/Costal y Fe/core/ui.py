import pygame
from config import COLORES

fuente_titulo = pygame.font.SysFont("Segoe UI", 36, True)
fuente_texto = pygame.font.SysFont("Segoe UI", 22)

def dibujar_titulo(ventana, texto, y=20):
    txt = fuente_titulo.render(texto, True, COLORES["texto"])
    ventana.blit(txt, (450 - txt.get_width() // 2, y))

def dibujar_panel(ventana, rect):
    pygame.draw.rect(ventana, COLORES["panel"], rect, border_radius=12)
    pygame.draw.rect(ventana, COLORES["dorado"], rect, 3, border_radius=12)

def dibujar_texto(ventana, texto, x, y, tamaño=22, negrita=False, color=None):
    fuente = pygame.font.SysFont("Segoe UI", tamaño, negrita)
    txt = fuente.render(texto, True, color if color else COLORES["texto"])
    ventana.blit(txt, (x, y))
