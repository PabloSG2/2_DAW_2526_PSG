import pygame
from config import COLORES
from core.botones import get_fuente

def dibujar_titulo(ventana, texto, y=20, size=36):
    fuente = get_fuente(size=size, bold=True)
    surf = fuente.render(texto, True, COLORES["dorado"])
    x = ventana.get_width() // 2 - surf.get_width() // 2
    ventana.blit(surf, (x, y))

def dibujar_panel(ventana, rect, color=None, radio=15):
    if color is None:
        color = COLORES["panel"]
    pygame.draw.rect(ventana, color, rect, border_radius=radio)

def dibujar_texto(ventana, texto, x, y, size=20, color=None, bold=False):
    if color is None:
        color = COLORES["texto"]
    fuente = get_fuente(size=size, bold=bold)
    surf = fuente.render(texto, True, color)
    ventana.blit(surf, (x, y))
    return surf.get_width(), surf.get_height()
