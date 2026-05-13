import pygame
from config import COLORES

def dibujar_cristo(ancho, alto):
    s = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    pygame.draw.rect(s, (180, 160, 140), (50, 20, ancho - 100, alto - 40), border_radius=20)
    pygame.draw.circle(s, (200, 180, 160), (ancho // 2, 80), 40)
    return s

def dibujar_virgen(ancho, alto):
    s = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    pygame.draw.rect(s, (160, 140, 180), (50, 20, ancho - 100, alto - 40), border_radius=20)
    pygame.draw.circle(s, (210, 190, 210), (ancho // 2, 80), 40)
    return s

def dibujar_sanjuan(ancho, alto):
    s = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    pygame.draw.rect(s, (140, 180, 160), (50, 20, ancho - 100, alto - 40), border_radius=20)
    pygame.draw.circle(s, (180, 210, 190), (ancho // 2, 80), 40)
    return s
