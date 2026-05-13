import pygame
from config import VENTANA, FPS
from core.datos import crear_estado_inicial

# Pantalla de bienvenida
from modules.menus.pantalla_bienvenida import pantalla_bienvenida

# Menús principales
from modules.menus.inicio import menu_inicio
from modules.menus.secretaria import menu_secretaria
from modules.menus.tesoreria import menu_tesoreria
from modules.menus.diputado_mayor import menu_diputado_mayor
from modules.menus.mayordomia import menu_mayordomia
from modules.menus.habito import menu_habito
from modules.menus.bandas import menu_bandas
from modules.menus.talleres import menu_talleres
from modules.menus.titulares import menu_titulares
from modules.menus.ayuda_ajustes import ayuda_ajustes

# Menú de procesión
from modules.menus.procesion.menu_procesion import menu_procesion

# Motores de procesión
from modules.menus.procesion.motor_libre import procesion_libre
from modules.menus.procesion.motor_procesion import procesion_modo, procesion_mapa

# Extra
try:
    from modules.menus.menu_extra import menu_extra_pygame
    EXTRA_OK = True
except:
    EXTRA_OK = False


def main():
    pygame.init()
    clock = pygame.time.Clock()
    estado = crear_estado_inicial()

    # MOSTRAR PANTALLA DE BIENVENIDA
    pantalla_bienvenida(VENTANA)

    pantalla_actual = "inicio"

    while True:
        clock.tick(FPS)

        if pantalla_actual == "inicio":
            pantalla_actual = menu_inicio(VENTANA, estado)

        elif pantalla_actual == "secretaria":
            pantalla_actual = menu_secretaria(VENTANA, estado)

        elif pantalla_actual == "tesoreria":
            pantalla_actual = menu_tesoreria(VENTANA, estado)

        elif pantalla_actual == "diputado_mayor":
            pantalla_actual = menu_diputado_mayor(VENTANA, estado)

        elif pantalla_actual == "mayordomia":
            pantalla_actual = menu_mayordomia(VENTANA, estado)

        elif pantalla_actual == "habito":
            pantalla_actual = menu_habito(VENTANA, estado)

        elif pantalla_actual == "bandas":
            pantalla_actual = menu_bandas(VENTANA, estado)

        elif pantalla_actual == "talleres":
            pantalla_actual = menu_talleres(VENTANA, estado)

        elif pantalla_actual == "titulares":
            pantalla_actual = menu_titulares(VENTANA, estado)

        elif pantalla_actual == "ayuda_ajustes":
            pantalla_actual = ayuda_ajustes(VENTANA, estado)

        elif pantalla_actual == "procesion":
            pantalla_actual = menu_procesion(VENTANA, estado)

        elif pantalla_actual == "procesion_libre":
            pantalla_actual = procesion_libre(VENTANA, estado)

        elif pantalla_actual == "procesion_mapa":
            pantalla_actual = procesion_mapa(VENTANA, estado)

        elif pantalla_actual == "extra" and EXTRA_OK:
            pantalla_actual = menu_extra_pygame(VENTANA, estado)

        else:
            pantalla_actual = "inicio"


if __name__ == "__main__":
    main()
