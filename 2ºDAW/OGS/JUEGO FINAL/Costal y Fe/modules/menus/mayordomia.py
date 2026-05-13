import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from config import COLORES

def menu_mayordomia(VENTANA, estado):
    clock = pygame.time.Clock()
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    opciones = ["Gestión de pasos", "Retablos", "Insignias", "Imágenes secundarias"]
    dd_opciones = Desplegable((420, 200, 260, 45), opciones, opciones[0])

    subpantalla = opciones[0]

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "MAYORDOMÍA", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        dibujar_texto(VENTANA, "Seleccionar sección:", 120, 210, tamaño=22)

        # Botón VOLVER
        boton_volver.actualizar_hover(pygame.mouse.get_pos())
        boton_volver.dibujar(VENTANA)

        # SUBPANTALLAS
        dibujar_texto(VENTANA, f"{subpantalla}:", 420, 260, tamaño=24, negrita=True)

        if subpantalla == "Gestión de pasos":
            lista = ["Paso de palio", "Paso de misterio", "Estructura", "Iluminación"]

        elif subpantalla == "Retablos":
            lista = ["Retablo mayor", "Retablo lateral", "Restauraciones"]

        elif subpantalla == "Insignias":
            lista = ["Cruz de guía", "Estandarte", "Bocinas", "Faroles"]

        elif subpantalla == "Imágenes secundarias":
            lista = ["San Juan", "Magdalena", "Romanos"]

        y = 300
        for item in lista:
            dibujar_texto(VENTANA, f"• {item}", 430, y)
            y += 30

        # -------------------------
        # 🔥 DIBUJAR DESPLEGABLE AL FINAL (ENCIMA DE TODO)
        # -------------------------
        dd_opciones.dibujar(VENTANA)

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

                nuevo = dd_opciones.click(pygame.mouse.get_pos())
                if nuevo:
                    subpantalla = nuevo

        pygame.display.update()
