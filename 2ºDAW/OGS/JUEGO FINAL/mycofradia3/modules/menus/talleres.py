import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES


def menu_talleres(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "TALLERES", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        dibujar_texto(VENTANA, "Encargos posibles:", 110, 160)
        dibujar_texto(VENTANA, "• Paso de Cristo", 130, 200)
        dibujar_texto(VENTANA, "• Paso de Palio", 130, 230)
        dibujar_texto(VENTANA, "• Titular de gloria", 130, 260)
        dibujar_texto(VENTANA, "• Restauración de imágenes", 130, 290)

        boton_volver.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.clicado(event.pos):
                    return "inicio"

        pygame.display.update()
