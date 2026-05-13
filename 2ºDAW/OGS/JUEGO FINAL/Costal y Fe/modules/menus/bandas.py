import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from core.render_preview import render_preview
from config import COLORES


def menu_bandas(VENTANA, estado):
    clock = pygame.time.Clock()
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    # Estado inicial
    estado.setdefault("bandas", [])
    bandas = estado["bandas"]

    # Desplegable principal
    opciones = ["Crear banda", "Comprar instrumentos", "Ver uniformes", "Ver bandas creadas"]
    dd_opciones = Desplegable((420, 200, 260, 45), opciones, opciones[0])
    subpantalla = opciones[0]

    # Crear banda
    tipos = ["AM", "CCyTT", "BM"]
    dd_tipo = Desplegable((420, 300, 260, 45), tipos, "AM")
    nombre = ""
    fuente = pygame.font.SysFont("Segoe UI", 20)

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])

        dibujar_titulo(VENTANA, "BANDAS", y=40)

        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        # Imagen arriba a la izquierda dentro del panel
        imagen = render_preview("banda")
        VENTANA.blit(imagen, (panel.x + 20, panel.y + 150))

        # Selector
        dibujar_texto(VENTANA, "Seleccionar sección:", 120, 210, tamaño=22)
        dd_opciones.dibujar(VENTANA)

        # Botón VOLVER
        boton_volver.actualizar_hover(pygame.mouse.get_pos())
        boton_volver.dibujar(VENTANA)

        # Título subpantalla
        dibujar_texto(VENTANA, f"{subpantalla}:", 420, 260, tamaño=24, negrita=True)

        # -------------------------
        # SUBPANTALLAS
        # -------------------------

        # CREAR BANDA
        if subpantalla == "Crear banda":
            dibujar_texto(VENTANA, "Tipo:", 420, 300, tamaño=22)
            dd_tipo.dibujar(VENTANA)

            dibujar_texto(VENTANA, "Nombre:", 420, 350, tamaño=22)
            caja = pygame.Rect(420, 385, 320, 40)
            pygame.draw.rect(VENTANA, (60, 40, 90), caja, border_radius=8)
            pygame.draw.rect(VENTANA, COLORES["dorado"], caja, 2, border_radius=8)
            txt = fuente.render(nombre, True, COLORES["texto"])
            VENTANA.blit(txt, (caja.x + 10, caja.y + 8))

            boton_crear = BotonSimple((420, 440, 220, 45), "Crear banda")
            boton_crear.actualizar_hover(pygame.mouse.get_pos())
            boton_crear.dibujar(VENTANA)

        # COMPRAR INSTRUMENTOS
        elif subpantalla == "Comprar instrumentos":
            instrumentos = ["Cornetas", "Tambores", "Bombos", "Trompetas"]
            y = 300
            for inst in instrumentos:
                dibujar_texto(VENTANA, f"• {inst}", 430, y)
                y += 30

        # VER UNIFORMES
        elif subpantalla == "Ver uniformes":
            uniformes = [
                "AM: uniforme rojo",
                "CCyTT: uniforme azul",
                "BM: uniforme negro"
            ]
            y = 300
            for u in uniformes:
                dibujar_texto(VENTANA, f"• {u}", 430, y)
                y += 30

        # VER BANDAS CREADAS
        elif subpantalla == "Ver bandas creadas":
            if len(bandas) == 0:
                dibujar_texto(VENTANA, "No hay ninguna banda creada", 420, 300, tamaño=22)
            else:
                y = 300
                for b in bandas:
                    dibujar_texto(VENTANA, f"{b['tipo']} — {b['nombre']}", 420, y, tamaño=22)
                    y += 30

        # -------------------------
        # 🔥 DIBUJAR DESPLEGABLES AL FINAL (ENCIMA DE TODO)
        # -------------------------
        dd_opciones.dibujar(VENTANA)

        if subpantalla == "Crear banda":
            dd_tipo.dibujar(VENTANA)

        # -------------------------
        # EVENTOS
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            # Escribir nombre
            if event.type == pygame.KEYDOWN and subpantalla == "Crear banda":
                if event.key == pygame.K_BACKSPACE:
                    nombre = nombre[:-1]
                elif len(nombre) < 20 and event.unicode.isprintable():
                    nombre += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Volver
                if boton_volver.clicado(pygame.mouse.get_pos()):
                    return "inicio"

                # Cambiar sección
                nuevo = dd_opciones.click(pygame.mouse.get_pos())
                if nuevo:
                    subpantalla = nuevo

                # Crear banda
                if subpantalla == "Crear banda":
                    nuevo_tipo = dd_tipo.click(pygame.mouse.get_pos())
                    if nuevo_tipo:
                        dd_tipo.valor = nuevo_tipo

                    if 'boton_crear' in locals() and boton_crear.clicado(pygame.mouse.get_pos()):
                        if nombre.strip():
                            bandas.append({"tipo": dd_tipo.valor, "nombre": nombre})
                            nombre = ""

        pygame.display.update()
