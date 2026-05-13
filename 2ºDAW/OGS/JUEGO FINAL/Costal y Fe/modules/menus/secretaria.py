import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES, IMG
import os

def cargar_logo():
    ruta = os.path.join(IMG, "escudo.png")
    try:
        img = pygame.image.load(ruta).convert_alpha()
        return pygame.transform.smoothscale(img, (120, 120))
    except:
        s = pygame.Surface((120, 120))
        s.fill((120, 0, 0))
        return s

def menu_secretaria(VENTANA, estado):
    clock = pygame.time.Clock()
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    herm = estado["hermandad"]
    fuente = pygame.font.SysFont("Segoe UI", 20)

    # Estados de edición
    editando = None
    buffer = ""

    # Desplegables
    desplegable_titulo = False
    opciones_titulo = ["Real", "Venerable", "Sacramental", "Antigua"]

    desplegable_templo = False
    templos = ["San Pedro", "San Roque", "Santa María", "San Juan"]

    desplegable_salida = False
    dias_salida = ["Domingo de Ramos", "Lunes Santo", "Martes Santo", "Miércoles Santo",
                   "Jueves Santo", "Viernes Santo", "Sábado Santo"]

    logo = cargar_logo()

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "SECRETARÍA", y=40)

        panel = pygame.Rect(60, 120, 780, 420)
        dibujar_panel(VENTANA, panel)

        header = pygame.Rect(panel.x, panel.y, panel.w, 50)
        pygame.draw.rect(VENTANA, (60, 40, 100), header, border_radius=8)
        dibujar_texto(VENTANA, "Ficha de la hermandad", header.x + 20, header.y + 12, tamaño=24, negrita=True)

        # --- FICHA IZQUIERDA ---
        x = panel.x + 20
        y = panel.y + 70

        dibujar_texto(VENTANA, f"Nombre: {herm['nombre']}", x, y); y += 30
        dibujar_texto(VENTANA, f"Fundación: {herm['fundacion']}", x, y); y += 30
        dibujar_texto(VENTANA, f"Hermanos totales: {herm['hermanos']}", x, y); y += 30
        dibujar_texto(VENTANA, f"Puntos (cultos): {herm['puntos']}", x, y); y += 30
        dibujar_texto(VENTANA, f"Cultos del mes: {herm['cultos_mes']}", x, y); y += 30
        dibujar_texto(VENTANA, f"Semana Santa: {herm['semana_santa']}", x, y); y += 30

        # --- ESCUDO ---
        VENTANA.blit(logo, (panel.x + 400, panel.y + 70))
        dibujar_texto(VENTANA, "Escudo actual", panel.x + 400, panel.y + 200)

        # --- OPCIONES A LA DERECHA ---
        x2 = panel.x + 400
        y2 = panel.y + 240

        boton_nombre = BotonSimple((x2, y2, 260, 35), "Cambiar nombre hermandad")
        boton_nombre.dibujar(VENTANA)
        y2 += 45

        boton_templo = BotonSimple((x2, y2, 260, 35), "Cambiar templo")
        boton_templo.dibujar(VENTANA)
        y2 += 45

        boton_titulo = BotonSimple((x2, y2, 260, 35), "Solicitar título")
        boton_titulo.dibujar(VENTANA)
        y2 += 45

        boton_salida = BotonSimple((x2, y2, 260, 35), "Cambiar día de salida")
        boton_salida.dibujar(VENTANA)
        y2 += 45

        # --- CAMPO DE TEXTO ---
        pos = pygame.mouse.get_pos()

        if editando:
            caja = pygame.Rect(panel.x + 20, panel.y + panel.h - 60, 350, 35)
            pygame.draw.rect(VENTANA, (40, 30, 80), caja, border_radius=8)
            pygame.draw.rect(VENTANA, COLORES["dorado"], caja, 2, border_radius=8)
            txt = fuente.render(buffer, True, COLORES["texto"])
            VENTANA.blit(txt, (caja.x + 8, caja.y + 6))

        # --- BOTÓN VOLVER ---
        boton_volver.dibujar(VENTANA)

        # -------------------------
        # 🔥 DESPLEGABLES AL FINAL (ENCIMA DE TODO)
        # -------------------------

        # DESPLEGABLE TÍTULO
        if desplegable_titulo:
            for i, op in enumerate(opciones_titulo):
                r = pygame.Rect(x2, panel.y + 240 + 45 + i * 35, 260, 35)
                pygame.draw.rect(VENTANA, (50, 30, 80), r)
                pygame.draw.rect(VENTANA, COLORES["dorado"], r, 2)
                dibujar_texto(VENTANA, op, r.x + 10, r.y + 8)

        # DESPLEGABLE TEMPLO
        if desplegable_templo:
            for i, t in enumerate(templos):
                r = pygame.Rect(x2, panel.y + 240 + 45*2 + i * 35, 260, 35)
                pygame.draw.rect(VENTANA, (50, 30, 80), r)
                pygame.draw.rect(VENTANA, COLORES["dorado"], r, 2)
                dibujar_texto(VENTANA, t, r.x + 10, r.y + 8)

        # DESPLEGABLE DÍA DE SALIDA
        if desplegable_salida:
            for i, d in enumerate(dias_salida):
                r = pygame.Rect(x2, panel.y + 240 + 45*3 + i * 35, 260, 35)
                pygame.draw.rect(VENTANA, (50, 30, 80), r)
                pygame.draw.rect(VENTANA, COLORES["dorado"], r, 2)
                dibujar_texto(VENTANA, d, r.x + 10, r.y + 8)

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

                # Cambiar nombre
                if boton_nombre.clicado(pos):
                    editando = "nombre"
                    buffer = herm["nombre"]

                # Cambiar templo
                if boton_templo.clicado(pos):
                    desplegable_templo = not desplegable_templo

                # Solicitar título
                if boton_titulo.clicado(pos):
                    desplegable_titulo = not desplegable_titulo

                # Cambiar día salida
                if boton_salida.clicado(pos):
                    desplegable_salida = not desplegable_salida

                # Selección de título
                if desplegable_titulo:
                    for i, op in enumerate(opciones_titulo):
                        r = pygame.Rect(x2, panel.y + 240 + 45 + i * 35, 260, 35)
                        if r.collidepoint(pos):
                            herm["titulo"] = op
                            desplegable_titulo = False

                # Selección de templo
                if desplegable_templo:
                    for i, t in enumerate(templos):
                        r = pygame.Rect(x2, panel.y + 240 + 45*2 + i * 35, 260, 35)
                        if r.collidepoint(pos):
                            herm["templo"] = t
                            desplegable_templo = False

                # Selección día salida
                if desplegable_salida:
                    for i, d in enumerate(dias_salida):
                        r = pygame.Rect(x2, panel.y + 240 + 45*3 + i * 35, 260, 35)
                        if r.collidepoint(pos):
                            herm["dia_salida"] = d
                            desplegable_salida = False

            # TECLADO
            if event.type == pygame.KEYDOWN and editando:
                if event.key == pygame.K_RETURN:
                    herm["nombre"] = buffer
                    editando = None
                elif event.key == pygame.K_BACKSPACE:
                    buffer = buffer[:-1]
                elif len(buffer) < 30 and event.unicode.isprintable():
                    buffer += event.unicode

        pygame.display.update()
