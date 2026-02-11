import pygame
from core.botones import Boton, get_fuente
from config import COLORES

def menu_inicio(VENTANA, estado):
    botones = [
        Boton((60, 200, 200, 50), "Hermanos"),
        Boton((60, 260, 200, 50), "Economía"),
        Boton((60, 320, 200, 50), "Cultos"),
        Boton((60, 380, 200, 50), "Ensayos"),
        Boton((60, 440, 200, 50), "Procesión"),
        Boton((60, 500, 200, 50), "Ajustes"),
        Boton((650, 500, 180, 50), "Salir"),
    ]

    while True:
        VENTANA.fill(COLORES["fondo_inicio"])

        fuente_titulo = get_fuente(40, True)
        titulo = fuente_titulo.render("MYCOFRADÍA 3", True, COLORES["dorado"])
        VENTANA.blit(titulo, (280, 80))

        fuente_sub = get_fuente(18, False)
        sub = fuente_sub.render("Gestión integral de la hermandad", True, COLORES["texto"])
        VENTANA.blit(sub, (300, 130))

        for b in botones:
            b.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if botones[0].clicado(pos):
                    return "hermanos"
                if botones[1].clicado(pos):
                    return "economia"
                if botones[2].clicado(pos):
                    return "cultos"
                if botones[3].clicado(pos):
                    return "ensayos"
                if botones[4].clicado(pos):
                    return "procesion"
                if botones[5].clicado(pos):
                    return "ajustes"
                if botones[6].clicado(pos):
                    pygame.quit()
                    exit()

        pygame.display.update()
