import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from core.render_preview import render_preview
from config import COLORES


def menu_habito(VENTANA, estado):
    clock = pygame.time.Clock()

    # Valores por defecto
    estado.setdefault("color_tunica", "Rojo")
    estado.setdefault("color_capirote", "Rojo")
    estado.setdefault("color_cingulo", "Dorado")

    colores = ["Negro", "Blanco", "Rojo", "Verde", "Azul", "Morado", "Dorado"]

    # Desplegables
    dd_tunica = Desplegable((540, 260, 260, 45), colores, estado["color_tunica"])
    dd_capirote = Desplegable((540, 330, 260, 45), colores, estado["color_capirote"])
    dd_cingulo = Desplegable((540, 400, 260, 45), colores, estado["color_cingulo"])

    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])

        dibujar_titulo(VENTANA, "HÁBITO NAZARENO", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        # SPRITE PIXEL-ART DEL NAZARENO
        imagen = render_preview("habito", estado)
        VENTANA.blit(imagen, (panel.x + 20, panel.y + 150))

        # Etiquetas
        dibujar_texto(VENTANA, "Color túnica:",   380, 270)
        dibujar_texto(VENTANA, "Color capirote:", 380, 340)
        dibujar_texto(VENTANA, "Color cíngulo:",  380, 410)

        dd_tunica.dibujar(VENTANA)
        dd_capirote.dibujar(VENTANA)
        dd_cingulo.dibujar(VENTANA)

        boton_volver.dibujar(VENTANA)

        pos = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if boton_volver.clicado(pos):
                    return "inicio"

                nuevo = dd_tunica.click(pos)
                if nuevo:
                    estado["color_tunica"] = nuevo

                nuevo = dd_capirote.click(pos)
                if nuevo:
                    estado["color_capirote"] = nuevo

                nuevo = dd_cingulo.click(pos)
                if nuevo:
                    estado["color_cingulo"] = nuevo

        pygame.display.update()
