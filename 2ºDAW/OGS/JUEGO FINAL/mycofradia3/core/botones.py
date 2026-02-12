import pygame
from config import COLORES

pygame.font.init()

_fuentes_cache = {}

def get_fuente(tamaño=20, negrita=False):
    clave = (tamaño, negrita)
    if clave not in _fuentes_cache:
        fuente = pygame.font.SysFont("Segoe UI", tamaño, bold=negrita)
        _fuentes_cache[clave] = fuente
    return _fuentes_cache[clave]


class BotonSimple:
    def __init__(self, rect, texto):
        self.rect = pygame.Rect(rect)
        self.texto = texto
        self.hover = False
        self._anim = 0  # animación hover

    def dibujar(self, ventana):
        objetivo = 1 if self.hover else 0
        self._anim += (objetivo - self._anim) * 0.2

        c1 = COLORES["boton"]
        c2 = COLORES["boton_hover"]
        color = (
            int(c1[0] + (c2[0] - c1[0]) * self._anim),
            int(c1[1] + (c2[1] - c1[1]) * self._anim),
            int(c1[2] + (c2[2] - c1[2]) * self._anim),
        )

        sombra = self.rect.move(3, 3)
        pygame.draw.rect(ventana, (10, 5, 25), sombra, border_radius=12)

        pygame.draw.rect(ventana, color, self.rect, border_radius=12)
        pygame.draw.rect(ventana, COLORES["borde_panel"], self.rect, 2, border_radius=12)

        fuente = get_fuente(18, True)
        t = fuente.render(self.texto, True, COLORES["boton_texto"])
        ventana.blit(t, (self.rect.centerx - t.get_width() // 2,
                         self.rect.centery - t.get_height() // 2))

    def actualizar_hover(self, pos):
        self.hover = self.rect.collidepoint(pos)

    def clicado(self, pos):
        return self.rect.collidepoint(pos)
