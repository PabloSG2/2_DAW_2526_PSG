import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES


def menu_bandas(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")
    boton_crear = BotonSimple((120, 420, 260, 55), "Crear banda")
    boton_contratar = BotonSimple((480, 420, 260, 55), "Contratar banda")

    clock = pygame.time.Clock()
    mensaje = ""
    timer = 0

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "BANDAS", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        dibujar_texto(VENTANA, "Gestión de bandas:", 110, 160)
        dibujar_texto(VENTANA, "• Crear tu propia banda", 130, 200)
        dibujar_texto(VENTANA, "• Contratar bandas para la estación de penitencia", 130, 230)

        if mensaje:
            dibujar_texto(VENTANA, mensaje, 110, 320, color=COLORES["dorado"])

        boton_crear.dibujar(VENTANA)
        boton_contratar.dibujar(VENTANA)
        boton_volver.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if boton_volver.clicado(pos):
                    return "inicio"

                if boton_crear.clicado(pos):
                    mensaje = "Has creado una banda (placeholder)."
                    timer = 180

                if boton_contratar.clicado(pos):
                    mensaje = "Has contratado una banda."
                    timer = 180

        if timer > 0:
            timer -= 1
            if timer == 0:
                mensaje = ""

        pygame.display.update()
