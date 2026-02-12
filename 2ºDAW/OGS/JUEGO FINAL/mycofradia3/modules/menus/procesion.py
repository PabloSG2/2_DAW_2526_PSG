import pygame
from config import COLORES

# Timers globales para levantás
levanta_timer = 0
musica_timer = 0


# ---------------------------------------------------------
# 1. SELECCIONAR MODO
# ---------------------------------------------------------
def seleccionar_modo(VENTANA):
    fuente = pygame.font.SysFont("Segoe UI", 32, bold=True)
    clock = pygame.time.Clock()
    opciones = ["LIBRE", "PROCESIÓN"]

    while True:
        clock.tick(60)
        VENTANA.fill((20, 20, 30))

        t = fuente.render("Selecciona el modo", True, COLORES["dorado"])
        VENTANA.blit(t, (220, 120))

        for i, txt in enumerate(opciones):
            r = pygame.Rect(220, 200 + i * 90, 260, 70)
            pygame.draw.rect(VENTANA, (60, 60, 100), r, border_radius=10)
            pygame.draw.rect(VENTANA, COLORES["dorado"], r, 2, border_radius=10)
            VENTANA.blit(fuente.render(txt, True, COLORES["texto"]), (r.x + 20, r.y + 15))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, txt in enumerate(opciones):
                    r = pygame.Rect(220, 200 + i * 90, 260, 70)
                    if r.collidepoint(x, y):
                        return txt.lower()

        pygame.display.update()


# ---------------------------------------------------------
# 2. SELECCIONAR TIPO (CRISTO / VIRGEN)
# ---------------------------------------------------------
def seleccionar_tipo(VENTANA):
    fuente = pygame.font.SysFont("Segoe UI", 32, bold=True)
    clock = pygame.time.Clock()
    opciones = ["CRISTO", "VIRGEN"]

    while True:
        clock.tick(60)
        VENTANA.fill((20, 20, 30))

        t = fuente.render("Selecciona el tipo de paso", True, COLORES["dorado"])
        VENTANA.blit(t, (180, 120))

        for i, txt in enumerate(opciones):
            r = pygame.Rect(220, 220 + i * 90, 260, 70)
            pygame.draw.rect(VENTANA, (60, 60, 100), r, border_radius=10)
            pygame.draw.rect(VENTANA, COLORES["dorado"], r, 2, border_radius=10)
            VENTANA.blit(fuente.render(txt, True, COLORES["texto"]), (r.x + 20, r.y + 15))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i, txt in enumerate(opciones):
                    r = pygame.Rect(220, 220 + i * 90, 260, 70)
                    if r.collidepoint(x, y):
                        return txt.lower()

        pygame.display.update()


# ---------------------------------------------------------
# 3. MOTOR PRINCIPAL DE LA PROCESIÓN
# ---------------------------------------------------------
def menu_procesion_motor(VENTANA, estado):

    global levanta_timer, musica_timer

    # PRIMERO: elegir modo
    modo = seleccionar_modo(VENTANA)
    if modo is None:
        return "procesion"

    # SEGUNDO: elegir tipo
    tipo = seleccionar_tipo(VENTANA)
    if tipo is None:
        return "procesion"

    clock = pygame.time.Clock()

    # ---------------------------------------------------------
    # CARGA DEL MAPA
    # ---------------------------------------------------------
    try:
        mapa = pygame.image.load("assets/img/fondo_procesion.png").convert()
    except:
        mapa = pygame.Surface((2000, 2000))
        mapa.fill((60, 40, 80))

    # ---------------------------------------------------------
    # CARGA DEL PASO (CRISTO / VIRGEN)
    # ---------------------------------------------------------
    if tipo == "cristo":
        giro_vel = 1.2
        try:
            paso_img = pygame.image.load("assets/img/paso_cristo.png").convert_alpha()
        except:
            paso_img = pygame.Surface((120, 180), pygame.SRCALPHA)
            pygame.draw.rect(paso_img, (200, 150, 50), (0, 0, 120, 180))
    else:
        giro_vel = 2.0
        try:
            paso_img = pygame.image.load("assets/img/paso_virgen.png").convert_alpha()
        except:
            paso_img = pygame.Surface((140, 200), pygame.SRCALPHA)
            pygame.draw.rect(paso_img, (200, 200, 80), (0, 0, 140, 200))

    # ---------------------------------------------------------
    # VARIABLES DEL PASO
    # ---------------------------------------------------------
    paso_x = 1000
    paso_y = 1000
    paso_angulo = 0
    paso_altura = 0

    cam_x = paso_x - 450
    cam_y = paso_y - 300

    velocidad = 4
    suavizado = 0.1

    # ---------------------------------------------------------
    # RECORRIDO AUTOMÁTICO (solo modo procesión)
    # ---------------------------------------------------------
    recorrido = [(1000, 800), (1200, 800), (1200, 600), (1000, 600)]
    punto_actual = 0

    # ---------------------------------------------------------
    # BUCLE PRINCIPAL
    # ---------------------------------------------------------
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "procesion"
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "procesion"

        keys = pygame.key.get_pressed()

        # ---------------------------------------------------------
        # ANDARES DEL CRISTO Y VIRGEN
        # ---------------------------------------------------------
        # Timers de levantás (usan las globales)
        global levanta_timer, musica_timer

        # =========================
        # CRISTO
        # =========================
        if tipo == "cristo":

            # 1 → Siempre de frente
            if keys[pygame.K_1]:
                paso_y -= velocidad * 1.0

            # 2 → Paso racheado
            if keys[pygame.K_2]:
                paso_y -= velocidad * 0.6
                paso_altura = 1 if paso_altura == 0 else 0
                paso_x += 0.3 * (1 if pygame.time.get_ticks() % 400 < 200 else -1)

            # 3 → Costero izquierdo
            if keys[pygame.K_3]:
                paso_x -= velocidad * 0.8
                paso_y -= velocidad * 0.4
                paso_altura = 2 if paso_altura == 0 else 0

            # 4 → Costero derecho
            if keys[pygame.K_4]:
                paso_x += velocidad * 0.8
                paso_y -= velocidad * 0.4
                paso_altura = 2 if paso_altura == 0 else 0

            # 5 → Para atrás
            if keys[pygame.K_5]:
                paso_y += velocidad * 0.8

            # 6 → Picaíto
            if keys[pygame.K_6]:
                paso_y -= velocidad * 1.3
                paso_altura = 6 if paso_altura == 0 else 0

            # 7 → Paso muda
            if keys[pygame.K_7]:
                paso_y -= velocidad * 0.9
                paso_altura = 0

            # 8 → Pasito (ajuste fino)
            if keys[pygame.K_8]:
                paso_y -= velocidad * 0.3

            # 9 → Tres pasos
            if keys[pygame.K_9]:
                ciclo = (pygame.time.get_ticks() // 300) % 4
                if ciclo < 3:
                    paso_y -= velocidad * 1.0

            # 0 → Pararse ahí y se baja
            if keys[pygame.K_0]:
                paso_altura = max(0, paso_altura - 1)

            # LEVANTÁ (ESPACIO)
            if keys[pygame.K_SPACE] and levanta_timer == 0 and musica_timer == 0:
                levanta_timer = 20
                paso_altura = 12

            if levanta_timer > 0:
                levanta_timer -= 1
                if levanta_timer < 10:
                    paso_altura -= 1
                # durante la levantá no se mueve nada más
                # saltamos al final del bucle
                # (no pongas 'continue' si te da problemas con el resto)
            
            # LEVANTÁ A LA MÚSICA (º → BACKQUOTE)
            if keys[pygame.K_BACKQUOTE] and musica_timer == 0 and levanta_timer == 0:
                musica_timer = 60
                paso_altura = 12

            if musica_timer > 0:
                musica_timer -= 1
                if musica_timer > 40:
                    paso_altura = 12
                elif musica_timer > 30:
                    paso_altura = 6
                elif musica_timer > 20:
                    paso_y -= velocidad * 1.2
                elif musica_timer > 0:
                    paso_y -= velocidad * 0.8

            # Controles para el panel
            controles = [
                "CRISTO:",
                "1 Siempre de frente",
                "2 Paso racheado",
                "3 Costero izq",
                "4 Costero der",
                "5 Para atrás",
                "6 Picaíto",
                "7 Paso muda",
                "8 Pasito",
                "9 Tres pasos",
                "0 Pararse y bajar",
                "ESPACIO Levantá",
                "º Levantá a la música",
                "A/D Girar",
                "ESC Volver"
            ]

        # =========================
        # VIRGEN
        # =========================
        else:
            # 1 → De frente
            if keys[pygame.K_1]:
                paso_y -= velocidad * 0.9

            # 2 → Para atrás
            if keys[pygame.K_2]:
                paso_y += velocidad * 0.9

            # 3 → En el sitio (mecida)
            if keys[pygame.K_3]:
                paso_altura = 3 if paso_altura == 0 else 0

            # 4 → Costero suave izq
            if keys[pygame.K_4]:
                paso_x -= velocidad * 0.6
                paso_y -= velocidad * 0.3

            # 5 → Costero suave der
            if keys[pygame.K_5]:
                paso_x += velocidad * 0.6
                paso_y -= velocidad * 0.3

            # LEVANTÁ (ESPACIO)
            if keys[pygame.K_SPACE] and levanta_timer == 0 and musica_timer == 0:
                levanta_timer = 20
                paso_altura = 10

            if levanta_timer > 0:
                levanta_timer -= 1
                if levanta_timer < 10:
                    paso_altura -= 1

            # LEVANTÁ A LA MÚSICA (º)
            if keys[pygame.K_BACKQUOTE] and musica_timer == 0 and levanta_timer == 0:
                musica_timer = 60
                paso_altura = 10

            if musica_timer > 0:
                musica_timer -= 1
                if musica_timer > 40:
                    paso_altura = 10
                elif musica_timer > 30:
                    paso_altura = 5
                elif musica_timer > 20:
                    paso_y -= velocidad * 0.9
                elif musica_timer > 0:
                    paso_y -= velocidad * 0.6

            controles = [
                "VIRGEN:",
                "1 De frente",
                "2 Para atrás",
                "3 En el sitio",
                "4 Costero izq",
                "5 Costero der",
                "ESPACIO Levantá",
                "º Levantá a la música",
                "A/D Girar",
                "ESC Volver"
            ]

        # ---------------------------------------------------------
        # PANEL LATERAL (USANDO 'controles')
        # ---------------------------------------------------------
        y_texto = 95
        for linea in controles:
            t_linea = fuente.render(linea, True, COLORES["texto"])
            VENTANA.blit(t_linea, (VENTANA.get_width() - 245, y_texto))
            y_texto += 22


        # ---------------------------------------------------------
        # GIROS SUAVES
        # ---------------------------------------------------------
        if tipo == "cristo":
            giro_suave = giro_vel * 0.6
        else:
            giro_suave = giro_vel

        if keys[pygame.K_a]:
            paso_angulo += giro_suave
        if keys[pygame.K_d]:
            paso_angulo -= giro_suave

        # ---------------------------------------------------------
        # RECORRIDO AUTOMÁTICO
        # ---------------------------------------------------------
        if modo == "procesión":
            tx, ty = recorrido[punto_actual]
            dx = tx - paso_x
            dy = ty - paso_y

            if abs(dx) < 5 and abs(dy) < 5:
                punto_actual = (punto_actual + 1) % len(recorrido)
            else:
                paso_x += dx * 0.02
                paso_y += dy * 0.02

        # ---------------------------------------------------------
        # CÁMARA SUAVE
        # ---------------------------------------------------------
        objetivo_cam_x = paso_x - 450
        objetivo_cam_y = paso_y - 300
        cam_x += (objetivo_cam_x - cam_x) * suavizado
        cam_y += (objetivo_cam_y - cam_y) * suavizado

        # ---------------------------------------------------------
        # DIBUJO DEL MAPA
        # ---------------------------------------------------------
        VENTANA.fill(COLORES["fondo"])
        VENTANA.blit(mapa, (-cam_x, -cam_y))

        # Barra superior
        pygame.draw.rect(VENTANA, (10, 5, 25), (0, 0, VENTANA.get_width(), 60))
        pygame.draw.line(VENTANA, COLORES["dorado"], (0, 60), (VENTANA.get_width(), 60), 2)

        fuente = pygame.font.SysFont("Segoe UI", 20, bold=True)
        t = fuente.render(f"PROCESIÓN - {tipo.upper()} ({modo.upper()})", True, COLORES["dorado"])
        VENTANA.blit(t, (20, 20))

        # ---------------------------------------------------------
        # PANEL LATERAL
        # ---------------------------------------------------------
        panel = pygame.Rect(VENTANA.get_width() - 260, 80, 240, 330)
        pygame.draw.rect(VENTANA, (20, 15, 40), panel, border_radius=12)
        pygame.draw.rect(VENTANA, COLORES["dorado"], panel, 2, border_radius=12)

        # El contenido del panel se rellenará en PARTE 3 y PARTE 4

        # ---------------------------------------------------------
        # DIBUJAR PASO
        # ---------------------------------------------------------
        imagen_rotada = pygame.transform.rotate(paso_img, paso_angulo)
        rect_img = imagen_rotada.get_rect(center=(paso_x - cam_x, paso_y - cam_y - paso_altura))

        sombra = pygame.Surface((rect_img.width, rect_img.height // 3), pygame.SRCALPHA)
        pygame.draw.ellipse(sombra, (0, 0, 0, 120), sombra.get_rect())
        VENTANA.blit(sombra, (rect_img.centerx - sombra.get_width() // 2,
                              rect_img.bottom - sombra.get_height() // 2))

        VENTANA.blit(imagen_rotada, rect_img)

        pygame.display.update()
