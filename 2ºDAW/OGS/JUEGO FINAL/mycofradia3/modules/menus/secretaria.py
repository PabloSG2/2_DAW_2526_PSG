import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES


def menu_secretaria(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    try:
        logo = pygame.image.load("assets/img/logo.png").convert_alpha()
        logo = pygame.transform.smoothscale(logo, (150, 150))
    except:
        logo = pygame.Surface((150, 150))
        logo.fill((120, 80, 160))

    while True:
        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "SECRETARÍA", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        VENTANA.blit(logo, (100, 160))

        x = 280
        y = 160

        dibujar_texto(VENTANA, f"Hermandad: {estado['hermandad']}", x, y)
        y += 30
        dibujar_texto(VENTANA, f"Ciudad: {estado['ciudad']}", x, y)
        y += 30
        dibujar_texto(VENTANA, f"Día de salida: {estado['dia_salida']}", x, y)
        y += 30
        dibujar_texto(VENTANA, f"Hermanos: {len(estado['hermanos'])}", x, y)
        y += 40

        dibujar_texto(VENTANA, "Cultos programados:", x, y, negrita=True)
        y += 30

        cultos = [
            "Triduo al Señor – Marzo",
            "Función Principal – Domingo de Pasión",
            "Vía Crucis interno – Cuaresma",
        ]

        for c in cultos:
            dibujar_texto(VENTANA, f"• {c}", x + 20, y)
            y += 25

        boton_volver.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.clicado(event.pos):
                    return "inicio"

        pygame.display.update()
