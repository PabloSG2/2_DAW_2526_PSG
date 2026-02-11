import pygame
from core.botones import Boton, get_fuente
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from core.datos import calcular_ingresos_cuotas
from config import COLORES

def menu_economia(VENTANA, estado):
    boton_volver = Boton((20, 20, 150, 40), "Volver")

    while True:
        VENTANA.fill(COLORES["fondo_economia"])

        dibujar_titulo(VENTANA, "ECONOMÍA", y=20)

        panel = pygame.Rect(80, 100, 740, 420)
        dibujar_panel(VENTANA, panel)

        ingresos_cuotas = calcular_ingresos_cuotas(estado)
        saldo = estado["saldo"]
        gastos = estado["gastos_anuales"]

        y = 130
        dibujar_texto(VENTANA, f"Saldo actual: {saldo} €", 100, y); y += 30
        dibujar_texto(VENTANA, f"Ingresos por cuotas: {ingresos_cuotas} € / año", 100, y); y += 30
        dibujar_texto(VENTANA, f"Gastos anuales estimados: {gastos} €", 100, y); y += 30

        boton_volver.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver.clicado(pos):
                    return "inicio"

        pygame.display.update()
