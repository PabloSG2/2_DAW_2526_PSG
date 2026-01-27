import pygame
from modules.hermandad import DIAS_SALIDA
import random

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_PANEL = (35, 20, 70)
COLOR_TEXTO = (255, 255, 255)
COLOR_DORADO = (255, 215, 0)

def dibujar_cabildos(VENTANA, raton_pos, data, botones):
    herm = data["hermandad"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    lineas = [
        "TÍTULOS Y CABILDO",
        "",
        f"Títulos: {', '.join(herm['titulos']) if herm['titulos'] else 'Ninguno'}",
        "",
        "Teclas:",
        "- T: Añadir título (fijo: 'Real')",
        "- N: Cambiar nombre (fijo: 'Hermandad del Pueblo')",
        "- C: Cambiar día de salida (aleatorio)",
        "",
        "Historial de Cabildos:",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*28))

    for i, h in enumerate(herm["historial_cabildo"][-6:]):
        t = FUENTE.render(f"- {h}", True, COLOR_DORADO)
        VENTANA.blit(t, (x + 20, y + 220 + i*25))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)

def añadir_titulo(data, titulo="Real"):
    data["hermandad"]["titulos"].append(titulo)
    data["hermandad"]["historial_cabildo"].append(f"Se añadió el título: {titulo}")

def cambiar_nombre(data, nuevo="Hermandad del Pueblo"):
    data["hermandad"]["nombre"] = nuevo
    data["hermandad"]["historial_cabildo"].append(f"Nuevo nombre aprobado: {nuevo}")

def cambiar_dia(data):
    herm = data["hermandad"]
    nuevo = random.randint(0, len(DIAS_SALIDA)-1)
    herm["dia"] = nuevo
    herm["historial_cabildo"].append(f"Se aprobó cambiar el día a: {DIAS_SALIDA[nuevo]}")
