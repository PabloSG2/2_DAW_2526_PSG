import pygame
from config import COLORES

def get_fuente(size=22, bold=True):
    if not pygame.font.get_init():
        pygame.font.init()
    return pygame.font.SysFont("arial", size, bold=bold)

class BotonSimple:
    def __init__(self, rect, texto):
        self.rect = pygame.Rect(rect)
        self.texto = texto

        # Colores estilo MyCofradía2
        self.color_fondo = (70, 40, 140)      # morado visible
        self.color_hover = (110, 70, 200)     # más claro al pasar el ratón
        self.color_borde = (255, 215, 0)      # dorado
        self.color_texto = (255, 255, 255)    # blanco

    def dibujar(self, ventana):
        mouse = pygame.mouse.get_pos()

        # Hover
        color = self.color_hover if self.rect.collidepoint(mouse) else self.color_fondo

        # Fondo del botón
        pygame.draw.rect(ventana, color, self.rect, border_radius=12)

        # Borde dorado
        pygame.draw.rect(ventana, self.color_borde, self.rect, 3, border_radius=12)

        # Texto
        fuente = get_fuente(26, True)
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

class BotonImagen:
    def __init__(self, rect, texto, ruta_imagen):
        self.rect = pygame.Rect(rect)
        self.texto = texto
        try:
            img = pygame.image.load(ruta_imagen).convert_alpha()
            self.imagen = pygame.transform.smoothscale(img, (rect[2], rect[3]))
        except:
            self.imagen = pygame.Surface((rect[2], rect[3]))
            self.imagen.fill((60, 60, 60))
        self.color_borde = COLORES["dorado"]

    def dibujar(self, ventana):
        ventana.blit(self.imagen, self.rect.topleft)
        pygame.draw.rect(ventana, self.color_borde, self.rect, 2, border_radius=10)

        fuente = get_fuente(18, True)
        txt = fuente.render(self.texto, True, COLORES["texto"])
        ventana.blit(
            txt,
            (
                self.rect.centerx - txt.get_width() // 2,
                self.rect.bottom + 4
            )
        )

    def clicado(self, pos):
        return self.rect.collidepoint(pos)
