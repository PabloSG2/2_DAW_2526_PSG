import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES


def menu_ayuda_ajustes(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "AYUDA / AJUSTES", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        y = 150
        dibujar_texto(VENTANA, "Cómo jugar:", 110, y, tamaño=24, negrita=True)
        y += 40
        dibujar_texto(VENTANA, "• Usa el menú principal para gestionar la hermandad.", 130, y)
        y += 25
        dibujar_texto(VENTANA, "• En Procesión, configura todo antes de salir.", 130, y)
        y += 25
        dibujar_texto(VENTANA, "• Los botones guardan automáticamente la información.", 130, y)

        y += 50
        dibujar_texto(VENTANA, "Ajustes:", 110, y, tamaño=24, negrita=True)
        y += 40

        modo = "Oscuro" if estado["modo_oscuro"] else "Claro"
        sonido = "Activado" if estado["sonido"] else "Desactivado"

        dibujar_texto(VENTANA, f"• Modo de color: {modo}", 130, y)
        y += 25
        dibujar_texto(VENTANA, f"• Sonido: {sonido}", 130, y)

        boton_volver.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.clicado(event.pos):
                    return "inicio"

        pygame.display.update()
