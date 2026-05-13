import pygame

class PasoMacarena:
    """
    Vista cenital del Paso de la Esperanza Macarena
    Estilo geométrico limpio como la imagen de referencia (izquierda).
    Tamaño aproximado: 120×180 px
    """

    def __init__(self):
        self.manto = (20, 80, 20)
        self.saya = (245, 240, 220)
        self.oro = (220, 180, 60)
        self.madera = (110, 70, 40)
        self.borde = (240, 200, 40)
        self.alfombra = (180, 20, 20)
        self.sombra = (0, 0, 0)

    def dibujar_topdown(self, surf, x, y, cam_x=0, cam_y=0):

        px = int(x - cam_x)
        py = int(y - cam_y)

        # BASE RECTANGULAR
        pygame.draw.rect(surf, self.madera, (px-60, py-90, 120, 180))
        pygame.draw.rect(surf, self.sombra, (px-60, py-90, 120, 180), 3)

        # RESPIRADEROS
        for dx in range(-50, 60, 25):
            pygame.draw.rect(surf, self.oro, (px+dx, py+70, 20, 20))
            pygame.draw.rect(surf, self.sombra, (px+dx, py+70, 20, 20), 2)

        # ALFOMBRA ROJA
        pygame.draw.rect(surf, self.alfombra, (px-40, py-80, 80, 160))
        pygame.draw.rect(surf, self.borde, (px-40, py-80, 80, 160), 4)

        # MANTO VERDE (triangular)
        pygame.draw.polygon(
            surf,
            self.manto,
            [(px, py-60), (px-45, py+20), (px+45, py+20)]
        )
        pygame.draw.polygon(
            surf,
            self.sombra,
            [(px, py-60), (px-45, py+20), (px+45, py+20)],
            3
        )

        # BAMBALINAS
        pygame.draw.rect(surf, self.oro, (px-45, py+10, 90, 15))
        pygame.draw.rect(surf, self.sombra, (px-45, py+10, 90, 15), 2)

        for dx in range(-40, 45, 10):
            pygame.draw.line(surf, self.oro, (px+dx, py+25), (px+dx, py+35), 3)

        # SAYA CENTRAL
        pygame.draw.rect(surf, self.saya, (px-18, py-5, 36, 60))
        pygame.draw.rect(surf, self.sombra, (px-18, py-5, 36, 60), 2)

        # CANDELERÍA FRONTAL
        for dx in range(-40, 45, 15):
            pygame.draw.rect(surf, self.oro, (px+dx, py+40, 10, 30))
            pygame.draw.rect(surf, self.sombra, (px+dx, py+40, 10, 30), 2)

            pygame.draw.circle(surf, (255,200,80), (px+dx+5, py+35), 5)
            pygame.draw.circle(surf, self.sombra, (px+dx+5, py+35), 5, 1)
