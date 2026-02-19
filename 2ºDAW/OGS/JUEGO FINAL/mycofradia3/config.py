import pygame
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(BASE_DIR, "assets")
SONIDOS = os.path.join(ASSETS, "sonidos")
MARCHAS = os.path.join(ASSETS, "marchas")
IMG = os.path.join(ASSETS, "img")

ANCHO = 900
ALTO = 600

COLORES = {
    "fondo": (20, 15, 40),
    "fondo_panel": (35, 25, 70),
    "borde_panel": (255, 215, 0),
    "texto": (240, 240, 240),
    "dorado": (255, 215, 0),
    "boton": (90, 60, 150),
    "boton_hover": (120, 80, 190),
    "boton_texto": (255, 255, 255),
}
