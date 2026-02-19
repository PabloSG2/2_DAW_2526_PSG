import pygame
from config import ANCHO, ALTO
from core.datos import crear_estado_inicial

from modules.menus.inicio import menu_inicio
from modules.menus.titulares import menu_titulares
from modules.menus.secretaria import menu_secretaria
from modules.menus.economia import menu_economia
from modules.menus.bandas import menu_bandas
from modules.menus.habito import menu_habito
from modules.menus.talleres import menu_talleres
from modules.menus.enseres import menu_enseres
from modules.menus.procesion_menu import menu_procesion
from modules.menus.ayuda_ajustes import menu_ayuda_ajustes


def main():
    pygame.init()
    VENTANA = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("MyCofradía 3")
    estado = crear_estado_inicial()
    pantalla = "inicio"
    clock = pygame.time.Clock()

    while True:
        if pantalla == "inicio":
            pantalla = menu_inicio(VENTANA, estado)
        elif pantalla == "titulares":
            pantalla = menu_titulares(VENTANA, estado)
        elif pantalla == "secretaria":
            pantalla = menu_secretaria(VENTANA, estado)
        elif pantalla == "economia":
            pantalla = menu_economia(VENTANA, estado)
        elif pantalla == "bandas":
            pantalla = menu_bandas(VENTANA, estado)
        elif pantalla == "habito":
            pantalla = menu_habito(VENTANA, estado)
        elif pantalla == "talleres":
            pantalla = menu_talleres(VENTANA, estado)
        elif pantalla == "enseres":
            pantalla = menu_enseres(VENTANA, estado)
        elif pantalla == "procesion":
            pantalla = menu_procesion(VENTANA, estado)
        elif pantalla == "ayuda_ajustes":
            pantalla = menu_ayuda_ajustes(VENTANA, estado)
        else:
            pantalla = "inicio"

        clock.tick(60)

if __name__ == "__main__":
    main()
