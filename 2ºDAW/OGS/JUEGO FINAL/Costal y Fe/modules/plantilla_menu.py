import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from config import COLORES

def plantilla_menu(VENTANA, estado, titulo, campos):
    """
    campos = [
        ("Texto a mostrar", "clave_estado", ["op1", "op2", "op3"]),
        ...
    ]
    """

    clock = pygame.time.Clock()

    # Inicializar valores por defecto
    for texto, clave, opciones in campos:
        estado.setdefault(clave, opciones[0])

    # Crear desplegables
    desplegables = []
    y = 260
    for texto, clave, opciones in campos:
        desplegables.append((
            texto,
            clave,
            Desplegable((420, y, 260, 45), opciones, estado[clave])
        ))
        y += 70

    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])

        dibujar_titulo(VENTANA, titulo, y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        # Dibujar textos + desplegables
        y = 270
        for texto, clave, dd in desplegables:
            dibujar_texto(VENTANA, texto, 120, y)
            dd.dibujar(VENTANA)
            y += 70

        boton_volver.dibujar(VENTANA)

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if boton_volver.clicado(pos):
                    return "inicio"

                # Procesar desplegables
                for texto, clave, dd in desplegables:
                    nuevo = dd.click(pos)
                    if nuevo:
                        estado[clave] = nuevo

        pygame.display.update()
