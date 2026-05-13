import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from core.render_preview import render_preview
from config import COLORES


def menu_titulares(VENTANA, estado):
    clock = pygame.time.Clock()
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    # Crear diccionarios si no existen
    estado.setdefault("titular_cristo", {
        "nombre": "Cristo de la Sentencia",
        "autor": "Anónimo",
        "anio": "1650",
        "restauraciones": "Restaurado en 1998 y 2010",
        "hermandad": "Hermandad de la Macarena",
        "tipo": "Flagelado"
    })

    estado.setdefault("titular_virgen", {
        "nombre": "Esperanza Macarena",
        "autor": "Juan Manuel Rodríguez",
        "anio": "1940",
        "restauraciones": "Restaurada en 2005",
        "hermandad": "Hermandad de la Macarena",
        "tipo": "Dolorosa"
    })

    # Selector principal
    dd_selector = Desplegable(
        (350, 160, 260, 45),
        ["Cristo", "Virgen"],
        "Cristo"
    )

    fuente = pygame.font.SysFont("Segoe UI", 20)

    # CONSTANTES DE MAQUETACIÓN
    COL_IZQ = 200
    COL_DER_X = 80 + COL_IZQ + 40
    FILA_INICIAL = 230
    SALTO = 45

    editando = None
    buffer = ""

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "TITULARES", y=40)

        # PANEL PRINCIPAL
        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        # CABECERA
        header = pygame.Rect(panel.x, panel.y, panel.w, 55)
        pygame.draw.rect(VENTANA, (60, 40, 100), header, border_radius=8)
        dibujar_texto(VENTANA, "Ficha del Titular",
                      header.x + 20, header.y + 12, tamaño=24, negrita=True)

        # SELECTOR CRISTO / VIRGEN (NO dibujar aquí)
        dibujar_texto(VENTANA, "Tipo de Titular:", 200, 170, tamaño=22)

        tipo = dd_selector.valor  # "Cristo" o "Virgen"

        # Seleccionar ficha según tipo
        ficha = estado["titular_cristo"] if tipo == "Cristo" else estado["titular_virgen"]

        # IMAGEN (usando tus sprites nuevos)
        imagen = render_preview("titular_cristo" if tipo == "Cristo" else "titular_virgen")
        VENTANA.blit(imagen, (panel.x + 20, panel.y + 150))

        # COLUMNA DERECHA
        y = FILA_INICIAL

        campos = [
            ("nombre", "Nombre"),
            ("autor", "Autor"),
            ("anio", "Año"),
            ("restauraciones", "Restauraciones"),
            ("hermandad", "Hermandad"),
        ]

        botones = {}

        for clave, texto in campos:
            dibujar_texto(VENTANA, f"{texto}: {ficha[clave]}", COL_DER_X, y, tamaño=22)
            boton = BotonSimple((COL_DER_X + 300, y - 5, 150, 35), "Editar")
            boton.dibujar(VENTANA)
            botones[clave] = boton
            y += SALTO

        # DESPLEGABLE DE TIPO (NO dibujar aquí)
        dibujar_texto(VENTANA, "Tipo:", COL_DER_X, y + 10, tamaño=22)

        dd_tipo = Desplegable(
            (COL_DER_X + 80, y, 260, 45),
            ["Nazareno", "Crucificado", "Flagelado"] if tipo == "Cristo"
            else ["Dolorosa", "Esperanza", "Angustias"],
            ficha["tipo"]
        )

        # CAMPO DE EDICIÓN
        if editando:
            caja = pygame.Rect(COL_DER_X, panel.y + panel.h - 60, 350, 40)
            pygame.draw.rect(VENTANA, (40, 30, 80), caja, border_radius=8)
            pygame.draw.rect(VENTANA, COLORES["dorado"], caja, 2, border_radius=8)
            txt = fuente.render(buffer, True, COLORES["texto"])
            VENTANA.blit(txt, (caja.x + 8, caja.y + 8))
            dibujar_texto(VENTANA, f"Editar {editando}", caja.x, caja.y - 25, tamaño=18)

        # BOTÓN VOLVER
        boton_volver.actualizar_hover(pygame.mouse.get_pos())
        boton_volver.dibujar(VENTANA)

        pos = pygame.mouse.get_pos()

        # -------------------------
        # 🔥 DIBUJAR DESPLEGABLES AL FINAL (ENCIMA DE TODO)
        # -------------------------
        dd_selector.dibujar(VENTANA)
        dd_tipo.dibujar(VENTANA)

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

                # Selector Cristo/Virgen
                nuevo = dd_selector.click(pos)
                if nuevo:
                    continue

                # Editar texto
                for clave, boton in botones.items():
                    if boton.clicado(pos):
                        editando = clave
                        buffer = str(ficha[clave])

                # Cambiar tipo
                nuevo_tipo = dd_tipo.click(pos)
                if nuevo_tipo:
                    ficha["tipo"] = nuevo_tipo

            # Teclado
            if event.type == pygame.KEYDOWN and editando:
                if event.key == pygame.K_RETURN:
                    ficha[editando] = buffer
                    editando = None

                elif event.key == pygame.K_BACKSPACE:
                    buffer = buffer[:-1]

                elif len(buffer) < 40 and event.unicode.isprintable():
                    buffer += event.unicode

        pygame.display.update()
