import pygame

# Conversión de nombres → RGB
MAPA_COLORES = {
    "Negro":  (20, 20, 20),
    "Blanco": (240, 240, 240),
    "Rojo":   (180, 20, 20),
    "Verde":  (20, 80, 20),
    "Azul":   (20, 40, 120),
    "Morado": (80, 20, 80),
    "Dorado": (220, 180, 60)
}

def _color(nombre):
    """Convierte un nombre de color a RGB de forma segura."""
    if not isinstance(nombre, str):
        return (40, 40, 40)
    nombre = nombre.strip()
    return MAPA_COLORES.get(nombre, (40, 40, 40))


class HabitoNazareno:
    """
    Nazareno frontal estilo La Igualá A4.
    Compatible con tu menú_habito original.
    """

    def __init__(self, color_tunica, color_capirote, color_cingulo):

        # Convertimos nombres → RGB de forma segura
        self.tunica = _color(color_tunica)
        self.capirote = _color(color_capirote)
        self.cingulo = _color(color_cingulo)

        self.piel = (230, 200, 170)
        self.cirio = (240, 230, 200)
        self.sombra = (0, 0, 0)

    def dibujar(self, surf, x, y):

        # -------------------------
        # CAPIROTE
        # -------------------------
        pygame.draw.polygon(
            surf,
            self.capirote,
            [(x+50, y), (x+20, y+80), (x+80, y+80)]
        )
        pygame.draw.polygon(
            surf,
            self.sombra,
            [(x+50, y), (x+20, y+80), (x+80, y+80)],
            2
        )

        # -------------------------
        # TÚNICA
        # -------------------------
        pygame.draw.rect(surf, self.tunica, (x+20, y+80, 60, 140))
        pygame.draw.rect(surf, self.sombra, (x+20, y+80, 60, 140), 2)

        # Sombra lateral
        pygame.draw.rect(surf, (20,20,20), (x+20, y+80, 20, 140))

        # -------------------------
        # CÍNGULO
        # -------------------------
        pygame.draw.rect(surf, self.cingulo, (x+20, y+130, 60, 10))
        pygame.draw.rect(surf, self.sombra, (x+20, y+130, 60, 10), 2)

        # -------------------------
        # CIRIO
        # -------------------------
        pygame.draw.rect(surf, self.cirio, (x+70, y+80, 10, 140))
        pygame.draw.rect(surf, self.sombra, (x+70, y+80, 10, 140), 2)

        # Llama
        pygame.draw.circle(surf, (255,200,80), (x+75, y+75), 6)
        pygame.draw.circle(surf, self.sombra, (x+75, y+75), 6, 1)

        # -------------------------
        # SOMBRA GENERAL
        # -------------------------
        pygame.draw.rect(surf, (0,0,0,40), (x+20, y+80, 60, 140), 1)


    # -------------------------
    # VISTA CENITAL PARA PROCESIÓN
    # -------------------------
    def dibujar_topdown(self, surf, x, y, cam_x, cam_y):
        """Versión cenital simple para modo libre/procesión."""
        px = x - cam_x
        py = y - cam_y

        pygame.draw.circle(surf, self.tunica, (px, py), 12)
        pygame.draw.circle(surf, self.sombra, (px, py), 12, 2)
