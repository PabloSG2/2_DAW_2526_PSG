import pygame
import random
from core.botones import Boton, get_fuente
from core.ui import dibujar_titulo
from config import COLORES

def menu_ensayos(VENTANA, estado):
    boton_volver = Boton((20, 20, 150, 40), "Volver")
    boton_ensayar = Boton((350, 500, 200, 50), "Realizar ensayo")

    mensaje = ""
    contador_mensaje = 0

    while True:
        VENTANA.fill(COLORES["fondo_ensayos"])

        dibujar_titulo(VENTANA, "ENSAYOS DE CUADRILLA", y=20)

        fuente = get_fuente(18, False)

        info = [
            f"Ensayos realizados: {estado['ensayos_realizados']}",
            f"Sincronización: {estado['sincronizacion']}",
            f"Riesgo de lesión: {estado['riesgo_lesion']}",
            f"Fatiga acumulada: {estado['fatiga']}",
        ]
        y = 80
        for linea in info:
            t = fuente.render(linea, True, COLORES["texto"])
            VENTANA.blit(t, (80, y))
            y += 28

        if mensaje and contador_mensaje > 0:
            t = fuente.render(mensaje, True, COLORES["verde"] if "mejora" in mensaje else COLORES["rojo"])
            VENTANA.blit(t, (80, 220))

        boton_volver.dibujar(VENTANA)
        boton_ensayar.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver.clicado(pos):
                    return "inicio"
                if boton_ensayar.clicado(pos):
                    mensaje = realizar_ensayo_simple(estado)
                    contador_mensaje = 120

        if contador_mensaje > 0:
            contador_mensaje -= 1

        pygame.display.update()

def realizar_ensayo_simple(estado):
    estado["ensayos_realizados"] += 1
    mejora_sync = random.randint(3, 8)
    estado["sincronizacion"] = min(100, estado["sincronizacion"] + mejora_sync)
    estado["fatiga"] = min(100, estado["fatiga"] + random.randint(5, 10))
    return f"Ensayo completado: mejora de sincronización de {mejora_sync} puntos."
