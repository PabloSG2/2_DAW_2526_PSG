import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from core.datos import calcular_ingresos_cuotas
from config import COLORES


def menu_economia(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "TESORERÍA", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        ingresos = calcular_ingresos_cuotas(estado)
        saldo = estado["saldo"]
        gastos = estado["gastos_anuales"]
        balance = ingresos - gastos

        y = 160
        dibujar_texto(VENTANA, f"Saldo actual: {saldo} €", 110, y)
        y += 40
        dibujar_texto(VENTANA, f"Ingresos por cuotas: {ingresos} € / año", 110, y)
        y += 40
        dibujar_texto(VENTANA, f"Gastos anuales estimados: {gastos} €", 110, y)
        y += 40

        color_balance = COLORES["dorado"] if balance >= 0 else (200, 50, 50)
        dibujar_texto(VENTANA, f"Balance anual: {balance} €", 110, y, color=color_balance)

        boton_volver.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.clicado(event.pos):
                    return "inicio"

        pygame.display.update()
