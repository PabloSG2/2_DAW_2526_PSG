import pygame
from modules.hermandad import *
from modules.ui import *
from modules.assets import cargar_imagen

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_TEXTO = (255, 255, 255)
COLOR_PANEL = (35, 20, 70)

ESCUDO_IMG = cargar_imagen("data/images/escudos/escudo.png", (80, 80))

def dibujar_gestion(VENTANA, raton_pos, data, boton_volver):
    herm = data["hermandad"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    if ESCUDO_IMG:
        VENTANA.blit(ESCUDO_IMG, (panel.right - 100, panel.y + 20))

    lineas = [
        "GESTIÓN DE HERMANDAD",
        "",
        f"Nombre: {herm['nombre']}",
        f"Día de salida: {DIAS_SALIDA[herm['dia']]}  (← →)",
        f"Pueblo: {PUEBLOS[herm['pueblo']]}  (A / D)",
        f"Cristo: {list(TIPOS_CRISTO.keys())[herm['cristo']]}  (1 / 2)",
        f"Paso: {list(TIPOS_PASO.keys())[herm['paso']]}  (3 / 4)",
        f"Palio: {list(TIPOS_PALIO.keys())[herm['palio']]}  (5 / 6)",
        f"Banda: {list(TIPOS_BANDA.keys())[herm['banda']]}  (7 / 8)",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*30))

    boton_volver.dibujar(VENTANA, raton_pos)
