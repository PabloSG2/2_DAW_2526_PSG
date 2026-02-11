import pygame
from config import ANCHO, ALTO
from core.datos import crear_estado_inicial
from modules.menus.inicio import menu_inicio
from modules.menus.hermanos import menu_hermanos
from modules.menus.economia import menu_economia
from modules.menus.cultos import menu_cultos
from modules.menus.ensayos import menu_ensayos
from modules.menus.procesion import menu_procesion
from modules.menus.ajustes import menu_ajustes

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
        elif pantalla == "hermanos":
            pantalla = menu_hermanos(VENTANA, estado)
        elif pantalla == "economia":
            pantalla = menu_economia(VENTANA, estado)
        elif pantalla == "cultos":
            pantalla = menu_cultos(VENTANA, estado)
        elif pantalla == "ensayos":
            pantalla = menu_ensayos(VENTANA, estado)
        elif pantalla == "procesion":
            pantalla = menu_procesion(VENTANA, estado)
        elif pantalla == "ajustes":
            pantalla = menu_ajustes(VENTANA, estado)
        else:
            pantalla = "inicio"

        clock.tick(60)

if __name__ == "__main__":
    main()
