import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from config import COLORES

def menu_talleres(VENTANA, estado):
    clock = pygame.time.Clock()
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    talleres = ["Imaginería", "Orfebrería", "Carpintería", "Comprar elementos"]
    dd_taller = Desplegable((420, 200, 260, 45), talleres, talleres[0])

    subpantalla = talleres[0]

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "TALLERES", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        dibujar_texto(VENTANA, "Seleccionar taller:", 120, 210, tamaño=22)

        # Botón VOLVER
        boton_volver.actualizar_hover(pygame.mouse.get_pos())
        boton_volver.dibujar(VENTANA)

        # SUBPANTALLAS
        if subpantalla == "Imaginería":
            lista = ["Titulares", "Misterios", "Retablos", "Restauraciones"]

        elif subpantalla == "Orfebrería":
            lista = ["Candelería", "Respiraderos", "Varales", "Jarras", "Corona"]

        elif subpantalla == "Carpintería":
            lista = ["Parihuelas", "Palios", "Estructuras de paso", "Andas"]

        elif subpantalla == "Comprar elementos":
            lista = ["Canastillas", "Luces", "Respiraderos", "Caídas", "Bambalinas", "Faldones"]

        # Mostrar lista
        y = 280
        for item in lista:
            dibujar_texto(VENTANA, f"• {item}", 430, y)
            y += 30

        # -------------------------
        # 🔥 DIBUJAR DESPLEGABLE AL FINAL (ENCIMA DE TODO)
        # -------------------------
        dd_taller.dibujar(VENTANA)

        # -------------------------
        # EVENTOS
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if boton_volver.clicado(pygame.mouse.get_pos()):
                    return "inicio"

                nuevo = dd_taller.click(pygame.mouse.get_pos())
                if nuevo:
                    subpantalla = nuevo

        pygame.display.update()
