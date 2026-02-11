import pygame
from core.botones import BotonSimple, get_fuente
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES

def menu_cultos(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver.clicado(pos):
                    return "inicio"

        VENTANA.fill(COLORES["fondo"])

        dibujar_titulo(VENTANA, "CULTOS", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        y = 150
        cultos = [
            "• Triduo al Señor – Marzo",
            "• Función Principal – Domingo de Pasión",
            "• Vía Crucis interno – Cuaresma",
            "• Besapiés / Besamanos – Según calendario",
            "• Rosario de la Aurora – Octubre",
        ]

        for c in cultos:
            dibujar_texto(VENTANA, c, 110, y)
            y += 40

        boton_volver.dibujar(VENTANA)
        pygame.display.update()
