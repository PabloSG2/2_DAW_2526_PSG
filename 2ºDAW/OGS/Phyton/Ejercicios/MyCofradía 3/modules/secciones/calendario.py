import pygame
from modules.hermandad import DIAS_SALIDA
from modules.assets import cargar_imagen

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_PANEL = (35, 20, 70)
COLOR_TEXTO = (255, 255, 255)

CAL_IMG = cargar_imagen("data/images/calendario/calendario.png", (220, 160))

def dibujar_calendario(VENTANA, raton_pos, data, botones):
    herm = data["hermandad"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    lineas = [
        "CALENDARIO COFRADE",
        "",
        f"Salida oficial de tu Hermandad: {DIAS_SALIDA[herm['dia']]}",
        f"Salida Extraordinaria: {'Sí' if herm['permiso_obispo'] else 'No'}",
        "",
        "Días Cofrades:",
        "- Viernes de Dolores",
        "- Sábado de Pasión",
        "- Semana previa (cultos, ensayos, traslados)",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*28))

    if CAL_IMG:
        VENTANA.blit(CAL_IMG, (panel.right - 260, panel.y + 120))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)
