import pygame

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_TEXTO = (255, 255, 255)
COLOR_BOTON = (70, 70, 130)
COLOR_BOTON_HOVER = (110, 110, 180)

class Boton:
    def __init__(self, rect, texto):
        self.rect = pygame.Rect(rect)
        self.texto = texto

    def dibujar(self, superficie, raton_pos):
        color = COLOR_BOTON_HOVER if self.rect.collidepoint(raton_pos) else COLOR_BOTON
        pygame.draw.rect(superficie, color, self.rect, border_radius=10)
        txt = FUENTE.render(self.texto, True, COLOR_TEXTO)
        superficie.blit(txt, (self.rect.centerx - txt.get_width()//2,
                              self.rect.centery - txt.get_height()//2))

    def clicado(self, raton_pos):
        return self.rect.collidepoint(raton_pos)
