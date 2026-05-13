import pygame
from config import COLORES

class BotonSimple:
    def __init__(self, rect, texto, tamaño=22):
        self.rect = pygame.Rect(rect)
        self.texto = texto
        self.hover = False
        self.fuente = pygame.font.SysFont("Segoe UI", tamaño)

    def actualizar_hover(self, pos):
        self.hover = self.rect.collidepoint(pos)

    def dibujar(self, ventana):
        color_fondo = (70, 50, 120) if self.hover else (50, 35, 90)
        pygame.draw.rect(ventana, color_fondo, self.rect, border_radius=10)
        pygame.draw.rect(ventana, COLORES["dorado"], self.rect, 2, border_radius=10)

        txt = self.fuente.render(self.texto, True, COLORES["texto"])
        ventana.blit(txt, (self.rect.x + 15, self.rect.y + 12))

    def clicado(self, pos):
        return self.rect.collidepoint(pos)
