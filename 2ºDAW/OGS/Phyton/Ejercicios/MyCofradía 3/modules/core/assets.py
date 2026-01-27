import pygame
import os

def cargar_imagen(ruta, tamaño=None):
    """
    Carga una imagen si existe. Si no, devuelve None.
    """
    if not os.path.exists(ruta):
        return None
    img = pygame.image.load(ruta).convert_alpha()
    if tamaño:
        img = pygame.transform.scale(img, tamaño)
    return img

def cargar_sonido(ruta):
    """
    Carga un sonido si existe. Si no, devuelve None.
    """
    if not os.path.exists(ruta):
        return None
    return pygame.mixer.Sound(ruta)
