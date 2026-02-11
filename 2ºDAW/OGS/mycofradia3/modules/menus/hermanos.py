import pygame
from core.botones import Boton, get_fuente
from core.ui import dibujar_panel, dibujar_titulo, dibujar_texto
from core.datos import generar_hermano, calcular_ingresos_cuotas
from config import COLORES

def menu_hermanos(VENTANA, estado):
    boton_volver = Boton((20, 20, 150, 40), "Volver")
    boton_añadir = Boton((700, 20, 180, 40), "Añadir hermano")
    boton_baja = Boton((700, 70, 180, 40), "Baja último")

    scroll = 0
    paso_scroll = 20

    while True:
        VENTANA.fill(COLORES["fondo_hermanos"])

        dibujar_titulo(VENTANA, "HERMANOS", y=20)

        panel = pygame.Rect(60, 100, 780, 440)
        dibujar_panel(VENTANA, panel)

        hermanos = estado["hermanos"]
        ingresos = calcular_ingresos_cuotas(estado)

        fuente = get_fuente(18, False)
        y = 110
        info = [
            f"Total hermanos: {len(hermanos)}",
            f"Ingresos por cuotas: {ingresos} € / año",
        ]
        for linea in info:
            t = fuente.render(linea, True, COLORES["texto"])
            VENTANA.blit(t, (80, y))
            y += 24

        y = 170 - scroll
        x = 80
        for h in hermanos:
            estado_txt = "Activo" if h["activo"] else "Baja"
            linea = f"{h['nombre']} | {h['edad']} años | {h['antiguedad']} años de antigüedad | {h['cuota']}€ | {estado_txt}"
            t = fuente.render(linea, True, COLORES["texto"])
            VENTANA.blit(t, (x, y))
            y += 24

        boton_volver.dibujar(VENTANA)
        boton_añadir.dibujar(VENTANA)
        boton_baja.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver.clicado(pos):
                    return "inicio"
                if boton_añadir.clicado(pos):
                    estado["hermanos"].append(generar_hermano())
                if boton_baja.clicado(pos) and estado["hermanos"]:
                    estado["hermanos"][-1]["activo"] = False

            if event.type == pygame.MOUSEWHEEL:
                scroll -= event.y * paso_scroll
                scroll = max(0, scroll)

        pygame.display.update()
