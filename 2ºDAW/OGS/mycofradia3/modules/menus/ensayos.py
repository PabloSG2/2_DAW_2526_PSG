import pygame
import random
from core.botones import BotonSimple, get_fuente
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES

def menu_ensayos(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")
    boton_ensayar = BotonSimple((VENTANA.get_width()//2 - 120, 420, 240, 60), "Realizar ensayo")

    clock = pygame.time.Clock()
    mensaje = ""
    timer = 0

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()

                if boton_volver.clicado(pos):
                    return "inicio"

                if boton_ensayar.clicado(pos):
                    mejora = random.randint(3, 8)
                    estado["ensayos_realizados"] += 1
                    estado["sincronizacion"] = min(100, estado["sincronizacion"] + mejora)
                    estado["fatiga"] = min(100, estado["fatiga"] + random.randint(5, 10))
                    mensaje = f"Ensayo completado: +{mejora} sincronización"
                    timer = 120

        if timer > 0:
            timer -= 1
            if timer == 0:
                mensaje = ""

        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "ENSAYOS", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        y = 150
        datos = [
            f"Ensayos realizados: {estado['ensayos_realizados']}",
            f"Sincronización: {estado['sincronizacion']}",
            f"Riesgo de lesión: {estado['riesgo_lesion']}",
            f"Fatiga acumulada: {estado['fatiga']}",
        ]

        for d in datos:
            dibujar_texto(VENTANA, d, 110, y)
            y += 40

        if mensaje:
            dibujar_texto(VENTANA, mensaje, 110, 330, color=COLORES["verde"])

        boton_ensayar.dibujar(VENTANA)
        boton_volver.dibujar(VENTANA)

        pygame.display.update()
