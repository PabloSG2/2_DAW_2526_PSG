import pygame

class PasoSentencia:
    """
    Paso cenital estilo La Igualá
    Orientado hacia ARRIBA (de frente)
    Tamaño: 160×260 px
    """

    def __init__(self):
        self.madera = (110, 70, 40)
        self.oro = (220, 180, 60)
        self.alfombra = (180, 20, 20)
        self.borde = (240, 200, 40)
        self.sombra = (0, 0, 0)

    def dibujar(self, surf, x, y, cam_x=0, cam_y=0):
        self.dibujar_topdown(surf, x, y, cam_x, cam_y)

    def dibujar_topdown(self, surf, x, y, cam_x=0, cam_y=0):

        px = int(x - cam_x)
        py = int(y - cam_y)

        # BASE DEL PASO (vertical)
        pygame.draw.rect(surf, self.madera, (px-80, py-130, 160, 260))
        pygame.draw.rect(surf, self.sombra, (px-80, py-130, 160, 260), 4)

        # RESPIRADEROS SUPERIORES (frente del paso)
        for dx in range(-70, 80, 30):
            pygame.draw.rect(surf, self.oro, (px+dx, py-130, 24, 24))
            pygame.draw.rect(surf, self.sombra, (px+dx, py-130, 24, 24), 2)

        # RESPIRADEROS INFERIORES (parte trasera)
        for dx in range(-70, 80, 30):
            pygame.draw.rect(surf, self.oro, (px+dx, py+110, 24, 24))
            pygame.draw.rect(surf, self.sombra, (px+dx, py+110, 24, 24), 2)

        # RESPIRADEROS LATERALES
        for dy in range(-120, 120, 40):
            pygame.draw.rect(surf, self.oro, (px-80, py+dy, 24, 24))
            pygame.draw.rect(surf, self.sombra, (px-80, py+dy, 24, 24), 2)

            pygame.draw.rect(surf, self.oro, (px+56, py+dy, 24, 24))
            pygame.draw.rect(surf, self.sombra, (px+56, py+dy, 24, 24), 2)

        # ALFOMBRA (vertical)
        pygame.draw.rect(surf, self.alfombra, (px-50, py-120, 100, 240))
        pygame.draw.rect(surf, self.borde, (px-50, py-120, 100, 240), 5)

        # CANDELERÍA (arriba del paso)
        for dx in range(-45, 50, 15):
            pygame.draw.rect(surf, self.oro, (px+dx, py-100, 12, 40))
            pygame.draw.rect(surf, self.sombra, (px+dx, py-100, 12, 40), 2)

            pygame.draw.circle(surf, (255,200,80), (px+dx+6, py-105), 6)
            pygame.draw.circle(surf, self.sombra, (px+dx+6, py-105), 6, 1)

        # SOMBRA GENERAL
        sombra = pygame.Surface((160, 260), pygame.SRCALPHA)
        sombra.fill((0, 0, 0, 60))
        surf.blit(sombra, (px-80, py-130))
