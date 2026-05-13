import pygame
import math

class TitularSentencia:
    """
    Cristo de la Sentencia (frontal)
    Estilo La Igualá A4: pixel‑art limpio, contorno negro, sombras suaves,
    volumen, romanos simplificados y postura realista.
    """

    def __init__(self):
        # Colores base
        self.piel = (230, 200, 170)
        self.pelo = (40, 25, 15)
        self.tunica = (245, 245, 245)
        self.capa = (170, 20, 20)
        self.columna = (200, 180, 160)
        self.oro = (220, 180, 60)
        self.romano_armor = (200, 160, 80)
        self.sombra = (0, 0, 0)

    def dibujar(self, surf, x, y):

        # ----------------------------------------------------
        # CABEZA (ligeramente inclinada hacia abajo)
        # ----------------------------------------------------
        pygame.draw.circle(surf, self.piel, (x+150, y+70), 32)
        pygame.draw.circle(surf, self.sombra, (x+150, y+70), 32, 2)

        # Pelo
        pygame.draw.ellipse(surf, self.pelo, (x+118, y+50, 64, 28))
        pygame.draw.ellipse(surf, self.sombra, (x+118, y+50, 64, 28), 2)

        # Ojos caídos
        pygame.draw.rect(surf, (0,0,0), (x+138, y+68, 5, 4))
        pygame.draw.rect(surf, (0,0,0), (x+158, y+68, 5, 4))

        # Boca triste
        pygame.draw.rect(surf, (120,40,40), (x+145, y+85, 12, 3))

        # ----------------------------------------------------
        # COLUMNA (real, detrás del Cristo)
        # ----------------------------------------------------
        pygame.draw.rect(surf, self.columna, (x+140, y+120, 40, 150))
        pygame.draw.rect(surf, self.sombra, (x+140, y+120, 40, 150), 2)

        # ----------------------------------------------------
        # TÚNICA BLANCA (volumen realista)
        # ----------------------------------------------------
        pygame.draw.rect(surf, self.tunica, (x+115, y+120, 70, 170))
        pygame.draw.rect(surf, self.sombra, (x+115, y+120, 70, 170), 2)

        # Sombra lateral
        pygame.draw.rect(surf, (210,210,210), (x+115, y+120, 22, 170))

        # ----------------------------------------------------
        # CAPA ROJA (recogida, volumen real)
        # ----------------------------------------------------
        pygame.draw.polygon(
            surf,
            self.capa,
            [(x+95, y+115), (x+205, y+115), (x+235, y+210), (x+65, y+210)]
        )
        pygame.draw.polygon(
            surf,
            self.sombra,
            [(x+95, y+115), (x+205, y+115), (x+235, y+210), (x+65, y+210)],
            2
        )

        # Sombra capa
        pygame.draw.polygon(
            surf,
            (120,10,10),
            [(x+95, y+115), (x+150, y+115), (x+180, y+210), (x+65, y+210)]
        )

        # ----------------------------------------------------
        # BRAZOS ATADOS (postura real)
        # ----------------------------------------------------
        # Brazo izquierdo
        pygame.draw.rect(surf, self.piel, (x+132, y+145, 22, 65))
        pygame.draw.rect(surf, self.sombra, (x+132, y+145, 22, 65), 2)

        # Brazo derecho
        pygame.draw.rect(surf, self.piel, (x+156, y+145, 22, 65))
        pygame.draw.rect(surf, self.sombra, (x+156, y+145, 22, 65), 2)

        # Cuerda realista
        pygame.draw.line(surf, (160,120,80), (x+138, y+185), (x+172, y+185), 4)

        # ----------------------------------------------------
        # ROMANOS LATERALES (simplificados)
        # ----------------------------------------------------
        # Izquierdo
        pygame.draw.circle(surf, self.romano_armor, (x+70, y+150), 28)
        pygame.draw.circle(surf, self.sombra, (x+70, y+150), 28, 2)
        pygame.draw.rect(surf, (180,20,20), (x+60, y+120, 20, 10))

        # Derecho
        pygame.draw.circle(surf, self.romano_armor, (x+230, y+150), 28)
        pygame.draw.circle(surf, self.sombra, (x+230, y+150), 28, 2)
        pygame.draw.rect(surf, (180,20,20), (x+220, y+120, 20, 10))

        # ----------------------------------------------------
        # DETALLES FINALES
        # ----------------------------------------------------
        pygame.draw.rect(surf, (0,0,0,40), (x+100, y+100, 120, 220), 1)
