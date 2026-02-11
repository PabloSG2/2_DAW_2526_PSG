import pygame
from core.botones import Boton
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES

def menu_cultos(VENTANA, estado):
    boton_volver = Boton((20, 20, 150, 40), "Volver")

    while True:
        VENTANA.fill(COLORES["fondo_cultos"])

        dibujar_titulo(VENTANA, "CULTOS", y=20)

        panel = pygame.Rect(80, 100, 740, 420)
        dibujar_panel(VENTANA, panel)

        y = 130
        textos = [
            "Triduo al Señor: Marzo",
            "Función Principal: Domingo de Pasión",
            "Besapiés / Besamanos: según calendario",
            "Vía Crucis interno: Cuaresma",
        ]
        for t in textos:
            dibujar_texto(VENTANA, t, 100, y)
            y += 30

        boton_volver.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver.clicado(pos):
                    return "inicio"

        pygame.display.update()
