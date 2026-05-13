import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from config import COLORES

def ayuda_ajustes(VENTANA, estado):
    clock = pygame.time.Clock()
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    opciones = ["Ayuda", "Controles Cristo", "Controles Virgen"]
    dd = Desplegable((420, 150, 260, 45), opciones, opciones[0])
    seleccionado = opciones[0]

    while True:
        clock.tick(60)

        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "AYUDA / AJUSTES", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        dibujar_texto(VENTANA, "Sección:", 110, 160, tamaño=24, negrita=True)

        # Columnas
        col1_x = 110
        col2_x = 430
        y_start = 220

        # -------------------------
        # SECCIÓN 1 — AYUDA
        # -------------------------
        if seleccionado == "Ayuda":
            y = y_start
            dibujar_texto(VENTANA, "¿Qué es este juego?", col1_x, y, tamaño=24, negrita=True)
            y += 40
            dibujar_texto(VENTANA, "• Simulador de una hermandad de Semana Santa.", col1_x, y); y += 25
            dibujar_texto(VENTANA, "• Gestiona titulares, cortejo, horarios y más.", col1_x, y); y += 25
            dibujar_texto(VENTANA, "• En Diputado Mayor → Procesión accedes a la igualá.", col1_x, y); y += 25
            dibujar_texto(VENTANA, "• Controla un paso en modo libre o procesión.", col1_x, y); y += 40

            dibujar_texto(VENTANA, "Ajustes generales:", col1_x, y, tamaño=24, negrita=True)
            y += 40

            modo = "Oscuro" if estado.get("modo_oscuro", True) else "Claro"
            sonido = "Activado" if estado.get("sonido", True) else "Desactivado"

            dibujar_texto(VENTANA, f"• Modo de color: {modo}", col1_x, y); y += 25
            dibujar_texto(VENTANA, f"• Sonido: {sonido}", col1_x, y)

        # -------------------------
        # SECCIÓN 2 — CONTROLES CRISTO
        # -------------------------
        elif seleccionado == "Controles Cristo":
            y = y_start

            dibujar_texto(VENTANA, "Movimiento (flechas):", col1_x, y, tamaño=22, negrita=True)
            y += 35
            dibujar_texto(VENTANA, "↑   Arriba", col1_x, y); y += 20
            dibujar_texto(VENTANA, "↓   Abajo", col1_x, y); y += 20
            dibujar_texto(VENTANA, "←   Izquierda", col1_x, y); y += 20
            dibujar_texto(VENTANA, "→   Derecha", col1_x, y); y += 30

            dibujar_texto(VENTANA, "Diagonales:", col1_x, y, tamaño=22, negrita=True)
            y += 35
            dibujar_texto(VENTANA, "↖  Arriba–Izquierda  (↑ + ←)", col1_x, y); y += 20
            dibujar_texto(VENTANA, "↗  Arriba–Derecha    (↑ + →)", col1_x, y); y += 20
            dibujar_texto(VENTANA, "↙  Abajo–Izquierda   (↓ + ←)", col1_x, y); y += 20
            dibujar_texto(VENTANA, "↘  Abajo–Derecha     (↓ + →)", col1_x, y)

            y2 = y_start
            dibujar_texto(VENTANA, "Controles especiales:", col2_x, y2, tamaño=22, negrita=True)
            y2 += 35
            dibujar_texto(VENTANA, "• Izquierdo", col2_x, y2); y2 += 20
            dibujar_texto(VENTANA, "• Picaíto", col2_x, y2); y2 += 20
            dibujar_texto(VENTANA, "• Más mecía", col2_x, y2); y2 += 20
            dibujar_texto(VENTANA, "• Menos mecía", col2_x, y2); y2 += 20
            dibujar_texto(VENTANA, "• Costero", col2_x, y2); y2 += 35

            dibujar_texto(VENTANA, "Pausa:", col2_x, y2, tamaño=22, negrita=True)
            y2 += 35
            dibujar_texto(VENTANA, "• Botón del HUD", col2_x, y2); y2 += 20
            dibujar_texto(VENTANA, "• SPACE → Pausar/Reanudar", col2_x, y2)

        # -------------------------
        # SECCIÓN 3 — CONTROLES VIRGEN
        # -------------------------
        elif seleccionado == "Controles Virgen":
            y = y_start

            dibujar_texto(VENTANA, "Movimiento (flechas):", col1_x, y, tamaño=22, negrita=True)
            y += 35
            dibujar_texto(VENTANA, "↑   Arriba", col1_x, y); y += 20
            dibujar_texto(VENTANA, "↓   Abajo", col1_x, y); y += 20
            dibujar_texto(VENTANA, "←   Izquierda", col1_x, y); y += 20
            dibujar_texto(VENTANA, "→   Derecha", col1_x, y); y += 30

            dibujar_texto(VENTANA, "Diagonales:", col1_x, y, tamaño=22, negrita=True)
            y += 35
            dibujar_texto(VENTANA, "↖  Arriba–Izquierda  (↑ + ←)", col1_x, y); y += 20
            dibujar_texto(VENTANA, "↗  Arriba–Derecha    (↑ + →)", col1_x, y); y += 20
            dibujar_texto(VENTANA, "↙  Abajo–Izquierda   (↓ + ←)", col1_x, y); y += 20
            dibujar_texto(VENTANA, "↘  Abajo–Derecha     (↓ + →)", col1_x, y)

            y2 = y_start
            dibujar_texto(VENTANA, "Controles especiales:", col2_x, y2, tamaño=22, negrita=True)
            y2 += 35
            dibujar_texto(VENTANA, "• Más mecía", col2_x, y2); y2 += 20
            dibujar_texto(VENTANA, "• Menos mecía", col2_x, y2); y2 += 20
            dibujar_texto(VENTANA, "• Cintura", col2_x, y2); y2 += 35

            dibujar_texto(VENTANA, "Pausa:", col2_x, y2, tamaño=22, negrita=True)
            y2 += 35
            dibujar_texto(VENTANA, "• Botón del HUD", col2_x, y2); y2 += 20
            dibujar_texto(VENTANA, "• SPACE → Pausar/Reanudar", col2_x, y2)

        # Botón volver
        boton_volver.dibujar(VENTANA)

        # Desplegable encima de todo
        dd.dibujar(VENTANA)

        # EVENTOS
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                nuevo = dd.click(event.pos)
                if nuevo:
                    seleccionado = nuevo

                if boton_volver.clicado(event.pos):
                    return "inicio"

        pygame.display.update()
