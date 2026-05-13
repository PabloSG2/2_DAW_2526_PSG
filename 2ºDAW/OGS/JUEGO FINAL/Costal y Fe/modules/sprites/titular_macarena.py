import pygame
import math

class TitularMacarena:
    """
    Virgen de la Esperanza Macarena (frontal)
    Estilo La Igualá A4: pixel‑art limpio, contorno negro, bordados,
    candelería detallada, sombras suaves y expresión realista.
    """

    def __init__(self):
        self.manto = (20, 80, 20)
        self.saya = (245, 240, 220)
        self.oro = (220, 180, 60)
        self.piel = (240, 210, 180)
        self.sombra = (0, 0, 0)
        self.labios = (150, 60, 60)
        self.cejas = (40, 20, 10)

    def dibujar(self, surf, x, y):

        # ----------------------------------------------------
        # MANTO VERDE REALISTA (forma de triángulo ancho)
        # ----------------------------------------------------
        pygame.draw.polygon(
            surf,
            self.manto,
            [(x+150, y+40), (x+30, y+310), (x+270, y+310)]
        )
        pygame.draw.polygon(
            surf,
            self.sombra,
            [(x+150, y+40), (x+30, y+310), (x+270, y+310)],
            3
        )

        # Bordados dorados inferiores
        for i in range(40, 260, 18):
            pygame.draw.circle(surf, self.oro, (x+i, y+310), 5)
            pygame.draw.circle(surf, self.sombra, (x+i, y+310), 5, 1)

        # ----------------------------------------------------
        # SAYA BLANCA Y ORO (vertical realista)
        # ----------------------------------------------------
        pygame.draw.rect(surf, self.saya, (x+110, y+150, 80, 170))
        pygame.draw.rect(surf, self.sombra, (x+110, y+150, 80, 170), 2)

        # Bordados verticales
        for dy in range(160, 300, 22):
            pygame.draw.circle(surf, self.oro, (x+150, y+dy), 6)
            pygame.draw.circle(surf, self.sombra, (x+150, y+dy), 6, 1)

        # ----------------------------------------------------
        # CORONA REALISTA (círculo + rayos + estrellas)
        # ----------------------------------------------------
        pygame.draw.circle(surf, self.oro, (x+150, y+40), 38)
        pygame.draw.circle(surf, self.sombra, (x+150, y+40), 38, 2)

        # Rayos dorados
        for ang in range(0, 360, 20):
            rad = math.radians(ang)
            dx = int(150 + 55 * math.cos(rad))
            dy = int(40 + 55 * math.sin(rad))
            pygame.draw.line(surf, self.oro, (x+150, y+40), (x+dx, y+dy), 3)

        # Estrellas pequeñas
        for ang in range(0, 360, 30):
            rad = math.radians(ang)
            sx = int(150 + 70 * math.cos(rad))
            sy = int(40 + 70 * math.sin(rad))
            pygame.draw.circle(surf, self.oro, (x+sx, y+sy), 5)
            pygame.draw.circle(surf, self.sombra, (x+sx, y+sy), 5, 1)

        # ----------------------------------------------------
        # ROSTRO REALISTA
        # ----------------------------------------------------
        pygame.draw.circle(surf, self.piel, (x+150, y+100), 34)
        pygame.draw.circle(surf, self.sombra, (x+150, y+100), 34, 2)

        # Ojos
        pygame.draw.rect(surf, (0,0,0), (x+138, y+95, 5, 4))
        pygame.draw.rect(surf, (0,0,0), (x+158, y+95, 5, 4))

        # Cejas
        pygame.draw.line(surf, self.cejas, (x+135, y+90), (x+145, y+88), 3)
        pygame.draw.line(surf, self.cejas, (x+155, y+88), (x+165, y+90), 3)

        # Boca suave
        pygame.draw.rect(surf, self.labios, (x+145, y+115, 12, 4))

        # Lágrimas (icono clásico)
        pygame.draw.circle(surf, (200,200,255), (x+142, y+105), 3)
        pygame.draw.circle(surf, (200,200,255), (x+158, y+105), 3)

        # ----------------------------------------------------
        # CANDELERÍA FRONTAL REALISTA
        # ----------------------------------------------------
        for cx in range(x+70, x+230, 25):
            pygame.draw.rect(surf, self.oro, (cx, y+260, 14, 50))
            pygame.draw.rect(surf, self.sombra, (cx, y+260, 14, 50), 2)

            # Llama
            pygame.draw.circle(surf, (255,200,80), (cx+7, y+255), 7)
            pygame.draw.circle(surf, self.sombra, (cx+7, y+255), 7, 1)

        # ----------------------------------------------------
        # SOMBRA GENERAL
        # ----------------------------------------------------
        pygame.draw.rect(surf, (0,0,0,40), (x+100, y+100, 120, 240), 1)
