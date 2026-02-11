import pygame
from core.botones import BotonSimple, get_fuente
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from core.datos import calcular_ingresos_cuotas
from config import COLORES

def menu_economia(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    clock = pygame.time.Clock()

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

        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "ECONOMÍA", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        ingresos = calcular_ingresos_cuotas(estado)
        saldo = estado["saldo"]
        gastos = estado["gastos_anuales"]

        y = 150
        datos = [
            f"Saldo actual: {saldo} €",
            f"Ingresos por cuotas: {ingresos} € / año",
            f"Gastos anuales estimados: {gastos} €",
            f"Balance anual: {ingresos - gastos} €",
        ]

        for d in datos:
            dibujar_texto(VENTANA, d, 110, y)
            y += 40

        boton_volver.dibujar(VENTANA)
        pygame.display.update()
