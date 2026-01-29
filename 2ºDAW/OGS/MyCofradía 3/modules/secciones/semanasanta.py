import pygame
from modules.hermandad import DIAS_SALIDA
from modules.assets import cargar_imagen

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_PANEL = (35, 20, 70)
COLOR_TEXTO = (255, 255, 255)
COLOR_DORADO = (255, 215, 0)
COLOR_VERDE = (0, 200, 0)
COLOR_AZUL = (0, 120, 255)

DIAS_SS = [
    "Domingo de Ramos",
    "Lunes Santo",
    "Martes Santo",
    "Miércoles Santo",
    "Jueves Santo",
    "Viernes Santo",
    "Sábado Santo",
    "Domingo de Resurrección"
]

FONDO_SS = cargar_imagen("data/images/semanasanta/fondo.png", (780, 440))

def dibujar_semanasanta(VENTANA, raton_pos, data, botones):
    herm = data["hermandad"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    if FONDO_SS:
        VENTANA.blit(FONDO_SS, (panel.x, panel.y))

    x = panel.x + 30
    y = panel.y + 30

    lineas = [
        "SEMANA SANTA COMPLETA",
        "",
        "Días y salidas:",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*28))

    for i, dia in enumerate(DIAS_SS):
        color = COLOR_TEXTO

        if DIAS_SALIDA[herm["dia"]] in dia:
            color = COLOR_DORADO

        if herm["banda_propia"] and i % 2 == 0:
            color = COLOR_AZUL

        if herm["permiso_obispo"] and i == 3:
            color = COLOR_VERDE

        t = FUENTE.render(f"- {dia}", True, color)
        VENTANA.blit(t, (x + 20, y + 120 + i*28))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)
