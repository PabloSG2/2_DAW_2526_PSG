import pygame
import tkinter as tk
import os

from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES, IMG

# Importaciones de los módulos
from modules.hermandades_musica import ModoBandas
from modules.quiz_completo import QuizCofrade


def lanzar_hermandades_musica():
    root = tk.Tk()
    ModoBandas(root, root.destroy)
    root.mainloop()


def lanzar_quiz_completo():
    root = tk.Tk()
    QuizCofrade(root)
    root.mainloop()


def menu_extra_pygame(VENTANA, estado):
    clock = pygame.time.Clock()

    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")
    boton_modo1 = BotonSimple((420, 260, 320, 55), "Música")
    boton_modo2 = BotonSimple((420, 340, 320, 55), "Quiz Completo")

    # -------------------------
    # CARGAR IMAGEN extra.png
    # -------------------------
    ruta_extra = os.path.join(IMG, "extra.png")
    try:
        imagen_extra = pygame.image.load(ruta_extra).convert_alpha()
        imagen_extra = pygame.transform.smoothscale(imagen_extra, (260, 260))
    except:
        imagen_extra = None

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES.get("fondo", (30, 30, 30)))

        dibujar_titulo(VENTANA, "MENÚ EXTRA", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        # -------------------------
        # MOSTRAR IMAGEN extra.png
        # -------------------------
        if imagen_extra:
            VENTANA.blit(imagen_extra, (panel.x + 40, panel.y + 120))

        dibujar_texto(VENTANA, "Modos extra:", 420, 210, tamaño=24, negrita=True)

        pos = pygame.mouse.get_pos()

        for b in [boton_volver, boton_modo1, boton_modo2]:
            b.actualizar_hover(pos)
            b.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if boton_volver.clicado(pos):
                    return "inicio"

                if boton_modo1.clicado(pos):
                    lanzar_hermandades_musica()
                    pygame.display.set_mode(VENTANA.get_size())

                if boton_modo2.clicado(pos):
                    lanzar_quiz_completo()
                    pygame.display.set_mode(VENTANA.get_size())

        pygame.display.update()
