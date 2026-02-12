import pygame
from config import COLORES
from core.botones import get_fuente


def dibujar_titulo(ventana, texto, y=40):
    fuente = get_fuente(32, True)
    t = fuente.render(texto, True, COLORES["dorado"])
    x = ventana.get_width() // 2 - t.get_width() // 2
    ventana.blit(t, (x, y))

    pygame.draw.line(
        ventana,
        COLORES["dorado"],
        (x, y + t.get_height() + 5),
        (x + t.get_width(), y + t.get_height() + 5),
        2,
    )


def dibujar_texto(ventana, texto, x, y, color=None, tamaño=20, negrita=False):
    if color is None:
        color = COLORES["texto"]
    fuente = get_fuente(tamaño, negrita)
    t = fuente.render(texto, True, color)
    ventana.blit(t, (x, y))


def dibujar_panel(ventana, rect):
    superficie = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    c1 = COLORES["fondo_panel"]
    c2 = (c1[0] + 20, c1[1] + 20, c1[2] + 20)

    for i in range(rect.height):
        alpha = i / rect.height
        color = (
            int(c1[0] + (c2[0] - c1[0]) * alpha),
            int(c1[1] + (c2[1] - c1[1]) * alpha),
            int(c1[2] + (c2[2] - c1[2]) * alpha),
            230,
        )
        pygame.draw.line(superficie, color, (0, i), (rect.width, i))

    ventana.blit(superficie, rect.topleft)
    pygame.draw.rect(ventana, COLORES["borde_panel"], rect, 2, border_radius=12)
