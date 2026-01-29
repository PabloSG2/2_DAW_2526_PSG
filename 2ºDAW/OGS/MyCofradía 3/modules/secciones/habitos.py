import pygame
from modules.assets import cargar_imagen

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_PANEL = (35, 20, 70)
COLOR_TEXTO = (255, 255, 255)

COLORES = [
    ("Blanco", (240, 240, 240)),
    ("Negro", (20, 20, 20)),
    ("Morado", (80, 0, 80)),
    ("Rojo", (150, 0, 0)),
    ("Verde", (0, 120, 0)),
    ("Azul", (0, 0, 150)),
]

HABITO_BASE = cargar_imagen("data/images/habitos/habito_base.png", (120, 260))

def dibujar_habito(VENTANA, raton_pos, data, botones):
    herm = data["hermandad"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    lineas = [
        "HÁBITO DE LA HERMANDAD",
        "",
        f"Túnica: {COLORES[herm['tunica_color']][0]}  (1 / 2)",
        f"Capa: {COLORES[herm['capa_color']][0]}  (3 / 4)",
        f"Cíngulo: {COLORES[herm['cingulo_color']][0]}  (5 / 6)",
        f"Capirote: {COLORES[herm['capirote_color']][0]}  (7 / 8)",
        "",
        "Dibujo del hábito:",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*28))

    base_x = x + 350
    base_y = y + 80

    if HABITO_BASE:
        VENTANA.blit(HABITO_BASE, (base_x - 20, base_y - 40))
    else:
        pygame.draw.rect(VENTANA, COLORES[herm["tunica_color"]][1], (base_x, base_y, 80, 150))
        pygame.draw.rect(VENTANA, COLORES[herm["capa_color"]][1], (base_x - 20, base_y, 120, 150), 4)
        pygame.draw.rect(VENTANA, COLORES[herm["cingulo_color"]][1], (base_x, base_y + 70, 80, 10))
        pygame.draw.polygon(
            VENTANA,
            COLORES[herm["capirote_color"]][1],
            [(base_x + 40, base_y - 80), (base_x, base_y), (base_x + 80, base_y)]
        )

    for b in botones:
        b.dibujar(VENTANA, raton_pos)
