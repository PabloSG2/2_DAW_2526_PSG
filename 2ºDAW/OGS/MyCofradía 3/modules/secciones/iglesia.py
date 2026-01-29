import pygame
import random
from modules.assets import cargar_imagen

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_TEXTO = (255, 255, 255)
COLOR_PANEL = (35, 20, 70)
COLOR_DORADO = (255, 215, 0)

IGLESIA_IMG = cargar_imagen("data/images/iglesia/iglesia.png", (140, 140))

def dibujar_iglesia(VENTANA, raton_pos, data, botones):
    herm = data["hermandad"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    lineas = [
        "IGLESIA Y OBISPADO",
        "",
        f"Prestigio: {herm['prestigio']}",
        f"Permiso del Obispo: {'Concedido' if herm['permiso_obispo'] else 'No concedido'}",
        "",
        "Teclas:",
        "- D: Donar 500€",
        "- P: Pedir permiso al Obispo",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*28))

    if IGLESIA_IMG:
        VENTANA.blit(IGLESIA_IMG, (panel.right - 180, panel.y + 40))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)

def donar(data, cantidad=500):
    if data["dinero"] >= cantidad:
        data["dinero"] -= cantidad
        data["hermandad"]["prestigio"] += cantidad // 100

def pedir_permiso(data):
    resultado = random.choice([True, False])
    data["hermandad"]["permiso_obispo"] = resultado
    return resultado
