import pygame

class Banda:
    """
    Banda cenital estilo La Igualá A4.
    Pixel‑art limpio, contorno negro, sombras suaves.
    """

    def __init__(self):
        self.uniforme = (20, 40, 80)
        self.piel = (230, 200, 170)
        self.instrumento = (180, 160, 60)
        self.sombra = (0,0,0)

    def dibujar(self, surf, x, y):

        # -------------------------
        # FILAS DE MÚSICOS (cenital)
        # -------------------------
        fila_y = y
        for fila in range(3):  # 3 filas
            col_x = x
            for col in range(5):  # 5 músicos por fila

                # Cabeza
                pygame.draw.circle(surf, self.piel, (col_x+15, fila_y+15), 10)
                pygame.draw.circle(surf, self.sombra, (col_x+15, fila_y+15), 10, 2)

                # Cuerpo (uniforme)
                pygame.draw.rect(surf, self.uniforme, (col_x+5, fila_y+25, 20, 25))
                pygame.draw.rect(surf, self.sombra, (col_x+5, fila_y+25, 20, 25), 2)

                # Instrumento (corneta/tambor simplificado)
                pygame.draw.rect(surf, self.instrumento, (col_x+10, fila_y+50, 10, 10))
                pygame.draw.rect(surf, self.sombra, (col_x+10, fila_y+50, 10, 10), 2)

                col_x += 40

            fila_y += 60

        # -------------------------
        # SOMBRA GENERAL
        # -------------------------
        pygame.draw.rect(surf, (0,0,0,40), (x, y, 200, 180), 1)
