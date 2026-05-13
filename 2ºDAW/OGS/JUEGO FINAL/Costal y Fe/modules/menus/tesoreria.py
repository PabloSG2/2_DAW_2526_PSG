import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from config import COLORES

def menu_tesoreria(VENTANA, estado):
    clock = pygame.time.Clock()
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    econ = estado["economia"]
    fuente = pygame.font.SysFont("Segoe UI", 20)

    # Estados de edición
    editando = None
    buffer = ""

    # Desplegable para cuotas predefinidas
    cuotas = ["10", "15", "20", "25", "30", "40", "50"]
    dd_cuota = Desplegable((420, 260, 260, 45), cuotas, str(econ["cuota_mensual"]))

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "TESORERÍA", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        header = pygame.Rect(panel.x, panel.y, panel.w, 50)
        pygame.draw.rect(VENTANA, (60, 40, 100), header, border_radius=8)
        dibujar_texto(VENTANA, "Gestión económica", header.x + 20, header.y + 12, tamaño=24, negrita=True)

        x = panel.x + 20
        y = panel.y + 80

        dibujar_texto(VENTANA, f"Presupuesto actual: {econ['presupuesto']} €", x, y); y += 35
        dibujar_texto(VENTANA, f"Ingreso mensual estimado: {econ['ingreso_mensual']} €", x, y); y += 35

        # Cuota mensual (texto)
        dibujar_texto(VENTANA, "Cuota mensual:", x, y, tamaño=22)
        y += 80

        # Botones de acciones
        boton_donacion = BotonSimple((x, y, 260, 40), "Realizar donación")
        boton_donacion.dibujar(VENTANA)
        y += 50

        boton_prestamo = BotonSimple((x, y, 260, 40), "Solicitar préstamo")
        boton_prestamo.dibujar(VENTANA)

        # Campo editable
        if editando:
            caja = pygame.Rect(panel.x + 350, panel.y + 330, 300, 40)
            pygame.draw.rect(VENTANA, (40, 30, 80), caja, border_radius=8)
            pygame.draw.rect(VENTANA, COLORES["dorado"], caja, 2, border_radius=8)
            txt = fuente.render(buffer, True, COLORES["texto"])
            VENTANA.blit(txt, (caja.x + 8, caja.y + 8))
            dibujar_texto(VENTANA, f"Introduce cantidad ({editando})", caja.x, caja.y - 25, tamaño=18)

        boton_volver.dibujar(VENTANA)
        pos = pygame.mouse.get_pos()

        # -------------------------
        # 🔥 DIBUJAR DESPLEGABLE AL FINAL (ENCIMA DE TODO)
        # -------------------------
        dd_cuota.dibujar(VENTANA)

        # -------------------------
        # EVENTOS
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:

                if boton_volver.clicado(pos):
                    return "inicio"

                # Cambiar cuota mensual
                nuevo = dd_cuota.click(pos)
                if nuevo:
                    econ["cuota_mensual"] = int(nuevo)

                # Donación
                if boton_donacion.clicado(pos):
                    editando = "donacion"
                    buffer = ""

                # Préstamo
                if boton_prestamo.clicado(pos):
                    editando = "prestamo"
                    buffer = ""

            # Edición de cantidades
            if event.type == pygame.KEYDOWN and editando:
                if event.key == pygame.K_RETURN:
                    if buffer.isdigit():
                        cantidad = int(buffer)

                        if editando == "donacion":
                            econ["presupuesto"] += cantidad

                        elif editando == "prestamo":
                            econ["presupuesto"] += cantidad

                    editando = None

                elif event.key == pygame.K_BACKSPACE:
                    buffer = buffer[:-1]

                elif event.unicode.isdigit() and len(buffer) < 6:
                    buffer += event.unicode

        pygame.display.update()
