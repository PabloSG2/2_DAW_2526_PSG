import pygame
from config import COLORES

def get_fuente(size=22, bold=True):
    if not pygame.font.get_init():
        pygame.font.init()
    return pygame.font.SysFont("arial", size, bold=bold)

class Boton:
    def __init__(self, rect, texto, color_fondo=None, color_texto=None):
        self.rect = pygame.Rect(rect)
        self.texto = texto

        # Colores visibles por defecto
        self.color_fondo = color_fondo if color_fondo else (70, 40, 140)
        self.color_texto = color_texto if color_texto else (255, 255, 255)

        # Hover
        self.color_hover = (
            min(self.color_fondo[0] + 40, 255),
            min(self.color_fondo[1] + 40, 255),
            min(self.color_fondo[2] + 40, 255),
        )

    def dibujar(self, ventana):
        mouse_pos = pygame.mouse.get_pos()

        # Hover dinámico
        if self.rect.collidepoint(mouse_pos):
            color = self.color_hover
        else:
            color = self.color_fondo

        pygame.draw.rect(ventana, color, self.rect, border_radius=12)

        fuente = get_fuente(24, True)
        txt = fuente.render(self.texto, True, self.color_texto)
        ventana.blit(
            txt,
            (
                self.rect.centerx - txt.get_width() // 2,
                self.rect.centery - txt.get_height() // 2
            )
        )

    def clicado(self, pos):
        return self.rect.collidepoint(pos)
