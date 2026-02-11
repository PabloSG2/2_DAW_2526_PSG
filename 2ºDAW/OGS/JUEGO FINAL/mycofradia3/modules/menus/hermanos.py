import pygame
from core.botones import BotonSimple, get_fuente
from core.ui import dibujar_titulo, dibujar_panel
from core.datos import calcular_ingresos_cuotas
from config import COLORES

def menu_hermanos(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")
    scroll = 0
    paso_scroll = 20
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
            if event.type == pygame.MOUSEWHEEL:
                scroll -= event.y * paso_scroll
                scroll = max(0, scroll)

        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "HERMANDAD", y=20)

        panel = pygame.Rect(60, 90, 780, 460)
        dibujar_panel(VENTANA, panel)

        fuente = get_fuente(18, False)
        hermanos = estado["hermanos"]
        ingresos = calcular_ingresos_cuotas(estado)

        y = 100
        info = [
            f"Total hermanos: {len(hermanos)}",
            f"Ingresos por cuotas: {ingresos} € / año",
        ]
        for linea in info:
            t = fuente.render(linea, True, COLORES["texto"])
            VENTANA.blit(t, (80, y))
            y += 24

        y = 160 - scroll
        for h in hermanos:
            linea = f"{h['nombre']} | {h['edad']} años | {h['antiguedad']} años | cuota {h['cuota']}€ | moral {h['moral']}"
            t = fuente.render(linea, True, COLORES["texto"])
            VENTANA.blit(t, (80, y))
            y += 22

        boton_volver.dibujar(VENTANA)
        pygame.display.update()
