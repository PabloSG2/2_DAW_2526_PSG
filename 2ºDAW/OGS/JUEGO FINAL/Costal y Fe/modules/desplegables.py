import pygame
from core.botones import BotonSimple
from config import COLORES

class Desplegable:
    def __init__(self, rect, opciones, valor_actual):
        self.rect = pygame.Rect(rect)
        self.opciones = opciones
        self.valor = valor_actual
        self.abierto = False
        self.boton = BotonSimple(rect, valor_actual)

    def dibujar(self, ventana):
        self.boton.texto = self.valor
        self.boton.dibujar(ventana)

        if self.abierto:
            y = self.rect.y + self.rect.height
            for op in self.opciones:
                r = pygame.Rect(self.rect.x, y, self.rect.width, self.rect.height)
                pygame.draw.rect(ventana, (40, 40, 40), r)
                pygame.draw.rect(ventana, (200, 200, 200), r, 2)

                fuente = pygame.font.SysFont("Segoe UI", 20)
                ventana.blit(fuente.render(op, True, COLORES["texto"]), (r.x + 10, r.y + 10))

                y += self.rect.height

    def click(self, pos):
        if self.boton.clicado(pos):
            self.abierto = not self.abierto
            return None

        if self.abierto:
            y = self.rect.y + self.rect.height
            for op in self.opciones:
                r = pygame.Rect(self.rect.x, y, self.rect.width, self.rect.height)
                if r.collidepoint(pos):
                    self.valor = op
                    self.abierto = False
                    return op
                y += self.rect.height

        return None
