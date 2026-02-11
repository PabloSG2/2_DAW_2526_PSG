import pygame
from core.botones import Boton, get_fuente
from core.ui import dibujar_titulo
from config import COLORES

def menu_ajustes(VENTANA, estado):
    boton_volver = Boton((20, 20, 150, 40), "Volver")
    boton_modo = Boton((300, 250, 300, 50), "Cambiar modo (oscuro/claro)")
    boton_sonido = Boton((300, 320, 300, 50), "Activar/Desactivar sonido")

    while True:
        VENTANA.fill(COLORES["fondo_ajustes"])

        dibujar_titulo(VENTANA, "AJUSTES", y=120)

        fuente = get_fuente(18, False)
        txt_modo = "Oscuro" if estado["modo_oscuro"] else "Claro"
        txt_sonido = "Activado" if estado["sonido"] else "Desactivado"

        t1 = fuente.render(f"Modo actual: {txt_modo}", True, COLORES["texto"])
        t2 = fuente.render(f"Sonido: {txt_sonido}", True, COLORES["texto"])
        VENTANA.blit(t1, (320, 200))
        VENTANA.blit(t2, (320, 230))

        boton_volver.dibujar(VENTANA)
        boton_modo.dibujar(VENTANA)
        boton_sonido.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver.clicado(pos):
                    return "inicio"
                if boton_modo.clicado(pos):
                    estado["modo_oscuro"] = not estado["modo_oscuro"]
                if boton_sonido.clicado(pos):
                    estado["sonido"] = not estado["sonido"]

        pygame.display.update()
