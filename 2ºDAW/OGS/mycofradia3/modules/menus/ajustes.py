import pygame
from core.botones import BotonSimple, get_fuente
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES

def menu_ajustes(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")
    boton_modo = BotonSimple((300, 260, 300, 60), "Modo oscuro/claro")
    boton_sonido = BotonSimple((300, 340, 300, 60), "Sonido ON/OFF")

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

                if boton_modo.clicado(pos):
                    estado["modo_oscuro"] = not estado["modo_oscuro"]

                if boton_sonido.clicado(pos):
                    estado["sonido"] = not estado["sonido"]

        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "AJUSTES", y=40)

        panel = pygame.Rect(200, 150, 500, 350)
        dibujar_panel(VENTANA, panel)

        modo = "Oscuro" if estado["modo_oscuro"] else "Claro"
        sonido = "Activado" if estado["sonido"] else "Desactivado"

        dibujar_texto(VENTANA, f"Modo actual: {modo}", 240, 180)
        dibujar_texto(VENTANA, f"Sonido: {sonido}", 240, 220)

        boton_modo.dibujar(VENTANA)
        boton_sonido.dibujar(VENTANA)
        boton_volver.dibujar(VENTANA)

        pygame.display.update()
