import pygame
import math
import random
import os
from config import COLORES

# Timers globales
levanta_timer = 0
musica_timer = 0

# ---------------------------------------------------------
# CARGA DE SONIDOS (RUTA ABSOLUTA)
# ---------------------------------------------------------
def cargar_sonido(nombre, volumen=1.0):
    ruta_base = os.path.dirname(os.path.abspath(__file__))  # carpeta de procesion.py
    ruta_sonido = os.path.join(ruta_base, "..", "..", "assets", "sonidos", nombre)
    ruta_sonido = os.path.normpath(ruta_sonido)

    try:
        s = pygame.mixer.Sound(ruta_sonido)
        s.set_volume(volumen)
        return s
    except:
        print("No se pudo cargar:", ruta_sonido)
        return None

SON_RACHEO = cargar_sonido("racheo.mp3", 0.6)
SON_LEVANTA = cargar_sonido("levanta.mp3", 1.0)
SON_LEVANTA2 = cargar_sonido("levanta2.mp3", 1.0)
SON_LLAMADOR = cargar_sonido("llamador.mp3", 1.0)
SON_AMBIENTE = cargar_sonido("ambiente.mp3", 0.3)

VOCES = [
    cargar_sonido("a_esta_es.mp3", 1.0),
    cargar_sonido("valientes.mp3", 1.0),
    cargar_sonido("quieto_valientes.mp3", 1.0),
    cargar_sonido("al_cielo_con_ella.mp3", 1.0),
    cargar_sonido("vamonos_de_frente.mp3", 1.0),
]

def reproducir_voz():
    voz = random.choice(VOCES)
    if voz:
        voz.play()

# ---------------------------------------------------------
# MOVER SEGÚN DIRECCIÓN DEL GIRO
# ---------------------------------------------------------
def mover_en_direccion(angulo, velocidad):
    rad = math.radians(angulo)
    dx = -math.sin(rad) * velocidad
    dy = -math.cos(rad) * velocidad
    return dx, dy

# ---------------------------------------------------------
# BOTONES DE AUDIO
# ---------------------------------------------------------
class BotonAudio:
    def __init__(self, x, y, texto, sonido):
        self.rect = pygame.Rect(x, y, 160, 50)
        self.texto = texto
        self.sonido = sonido
        self.hover = False

    def dibujar(self, ventana):
        color = (90, 60, 150) if not self.hover else (120, 80, 200)
        pygame.draw.rect(ventana, color, self.rect, border_radius=10)
        pygame.draw.rect(ventana, COLORES["dorado"], self.rect, 2, border_radius=10)

        fuente = pygame.font.SysFont("Segoe UI", 20, True)
        t = fuente.render(self.texto, True, COLORES["texto"])
        ventana.blit(t, (self.rect.centerx - t.get_width() // 2,
                         self.rect.centery - t.get_height() // 2))

    def actualizar(self, pos):
        self.hover = self.rect.collidepoint(pos)

    def clicado(self, pos):
        if self.rect.collidepoint(pos):
            if self.sonido:
                self.sonido.play()
            return True
        return False

# ---------------------------------------------------------
# SELECCIONAR MODO
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
# SELECCIONAR TIPO
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
# MOTOR PRINCIPAL
# ---------------------------------------------------------
def menu_procesion_motor(VENTANA, estado):
    global levanta_timer, musica_timer

    # Ambiente
    if SON_AMBIENTE:
        SON_AMBIENTE.play(-1)

    modo = seleccionar_modo(VENTANA)
    if modo is None:
        return "procesion"

    tipo = seleccionar_tipo(VENTANA)
    if tipo is None:
        return "procesion"

    clock = pygame.time.Clock()

    # Marcha seleccionada
    marcha = estado["procesion"].get("marcha", None)
    if marcha:
        try:
            pygame.mixer.music.load(marcha)
            pygame.mixer.music.set_volume(0.8)
            pygame.mixer.music.play(-1)
        except:
            print("No se pudo cargar la marcha:", marcha)

    # Mapa
    try:
        mapa = pygame.image.load("assets/img/fondo_procesion.png").convert()
    except:
        mapa = pygame.Surface((2000, 2000))
        mapa.fill((60, 40, 80))

        # ---------------------------------------------------------
    # CARGA DEL PASO Y SU FONDO
    # ---------------------------------------------------------
    if tipo == "cristo":
        giro_vel = 1.2
        try:
            paso_img = pygame.image.load("assets/img/cristo.png").convert_alpha()
        except:
            paso_img = pygame.Surface((120, 180), pygame.SRCALPHA)
            pygame.draw.rect(paso_img, (200, 150, 50), (0, 0, 120, 180))

        # FONDO DEL CRISTO
        try:
            fondo_paso = pygame.image.load("assets/img/fondo_cristo.png").convert()
        except:
            fondo_paso = pygame.Surface((800, 600))
            fondo_paso.fill((50, 20, 20))

    else:  # VIRGEN
        giro_vel = 1.5
        try:
            paso_img = pygame.image.load("assets/img/virgen.png").convert_alpha()
            # ESCALA FIJA PARA QUE NO SEA GIGANTE
            paso_img = pygame.transform.smoothscale(paso_img, (110, 160))
        except:
            paso_img = pygame.Surface((110, 160), pygame.SRCALPHA)
            pygame.draw.rect(paso_img, (200, 200, 80), (0, 0, 110, 160))

        # FONDO DE LA VIRGEN
        try:
            fondo_paso = pygame.image.load("assets/img/fondo_virgen.png").convert()
        except:
            fondo_paso = pygame.Surface((800, 600))
            fondo_paso.fill((20, 20, 50))

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

    ancho = VENTANA.get_width()
    alto = VENTANA.get_height()

    boton_llamador = BotonAudio(ancho // 2 - 180, alto - 70, "LLAMADOR", SON_LLAMADOR)
    boton_voces = BotonAudio(ancho // 2 + 20, alto - 70, "VOCES", None)

    # ---------------------------------------------------------
    # BUCLE PRINCIPAL
    # ---------------------------------------------------------
    while True:
        clock.tick(60)

        pos = pygame.mouse.get_pos()
        boton_llamador.actualizar(pos)
        boton_voces.actualizar(pos)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                if SON_AMBIENTE:
                    SON_AMBIENTE.stop()
                return "procesion"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_llamador.clicado(pos):
                    pass
                if boton_voces.clicado(pos):
                    reproducir_voz()

            # SALIR CON ESC
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    if SON_AMBIENTE:
                        SON_AMBIENTE.stop()
                    return "procesion"

        keys = pygame.key.get_pressed()

        # ---------------------------------------------------------
        # ANDARES DEL CRISTO
        # ---------------------------------------------------------
        racheando = False

        if tipo == "cristo":

            if keys[pygame.K_1]:
                dx, dy = mover_en_direccion(paso_angulo, velocidad)
                paso_x += dx
                paso_y += dy

            if keys[pygame.K_2]:
                dx, dy = mover_en_direccion(paso_angulo, velocidad * 0.6)
                paso_x += dx
                paso_y += dy
                paso_altura = 1 if paso_altura == 0 else 0
                racheando = True

            if keys[pygame.K_3]:
                dx, dy = mover_en_direccion(paso_angulo - 90, velocidad * 0.8)
                paso_x += dx
                paso_y += dy

            if keys[pygame.K_4]:
                dx, dy = mover_en_direccion(paso_angulo + 90, velocidad * 0.8)
                paso_x += dx
                paso_y += dy

            if keys[pygame.K_5]:
                dx, dy = mover_en_direccion(paso_angulo, -velocidad * 0.8)
                paso_x += dx
                paso_y += dy

            if keys[pygame.K_6]:
                dx, dy = mover_en_direccion(paso_angulo, velocidad * 1.3)
                paso_x += dx
                paso_y += dy
                paso_altura = 6 if paso_altura == 0 else 0

            if keys[pygame.K_7]:
                paso_altura = 0
                reproducir_voz()

            if keys[pygame.K_8]:
                dx, dy = mover_en_direccion(paso_angulo, velocidad * 0.3)
                paso_x += dx
                paso_y += dy

            if keys[pygame.K_9]:
                ciclo = (pygame.time.get_ticks() // 300) % 4
                if ciclo < 3:
                    dx, dy = mover_en_direccion(paso_angulo, velocidad)
                    paso_x += dx
                    paso_y += dy

            if keys[pygame.K_0]:
                paso_altura = max(0, paso_altura - 1)

            # LEVANTÁ
            if keys[pygame.K_SPACE] and levanta_timer == 0:
                levanta_timer = 20
                paso_altura = 12
                if SON_LEVANTA:
                    SON_LEVANTA.play()

            if levanta_timer > 0:
                levanta_timer -= 1
                if levanta_timer < 10:
                    paso_altura -= 1

            # LEVANTÁ A LA MÚSICA
            if keys[pygame.K_BACKQUOTE] and musica_timer == 0:
                musica_timer = 60
                paso_altura = 12
                if SON_LEVANTA2:
                    SON_LEVANTA2.play()
                pygame.mixer.music.set_volume(1.0)

            if musica_timer > 0:
                musica_timer -= 1
                if musica_timer < 20:
                    pygame.mixer.music.set_volume(0.8)

            # RACHEO AUTOMÁTICO
            if racheando and SON_RACHEO:
                if not pygame.mixer.Channel(5).get_busy():
                    pygame.mixer.Channel(5).play(SON_RACHEO)

            controles = [
                "CRISTO:",
                "1 Siempre de frente",
                "2 Racheado",
                "3 Costero izq",
                "4 Costero der",
                "5 Para atrás",
                "6 Picaíto",
                "7 Muda",
                "8 Pasito",
                "9 Tres pasos",
                "0 Pararse",
                "ESPACIO → Levantá",
                "º → Levantá música",
                "A/D Girar"
            ]

        # ---------------------------------------------------------
        # ANDARES DE LA VIRGEN
        # ---------------------------------------------------------
        else:

            if keys[pygame.K_1]:
                dx, dy = mover_en_direccion(paso_angulo, velocidad * 0.9)
                paso_x += dx
                paso_y += dy

            if keys[pygame.K_2]:
                dx, dy = mover_en_direccion(paso_angulo, -velocidad * 0.9)
                paso_x += dx
                paso_y += dy

            if keys[pygame.K_3]:
                paso_altura = 3 if paso_altura == 0 else 0

            if keys[pygame.K_4]:
                dx, dy = mover_en_direccion(paso_angulo - 90, velocidad * 0.6)
                paso_x += dx
                paso_y += dy

            if keys[pygame.K_5]:
                dx, dy = mover_en_direccion(paso_angulo + 90, velocidad * 0.6)
                paso_x += dx
                paso_y += dy

            # LEVANTÁ VIRGEN
            if keys[pygame.K_SPACE] and levanta_timer == 0:
                levanta_timer = 20
                paso_altura = 10

            if levanta_timer > 0:
                levanta_timer -= 1
                if levanta_timer < 10:
                    paso_altura -= 1

            # LEVANTÁ A LA MÚSICA VIRGEN
            if keys[pygame.K_BACKQUOTE] and musica_timer == 0:
                musica_timer = 60
                paso_altura = 10
                pygame.mixer.music.set_volume(1.0)

            if musica_timer > 0:
                musica_timer -= 1
                if musica_timer < 20:
                    pygame.mixer.music.set_volume(0.8)

            controles = [
                "VIRGEN:",
                "1 De frente",
                "2 Para atrás",
                "3 Mecida",
                "4 Costero izq",
                "5 Costero der",
                "ESPACIO → Levantá",
                "º → Levantá música",
                "A/D Girar"
            ]

        # ---------------------------------------------------------
        # GIRO
        # ---------------------------------------------------------
        if keys[pygame.K_a]:
            paso_angulo += giro_vel
        if keys[pygame.K_d]:
            paso_angulo -= giro_vel

        # ---------------------------------------------------------
        # CÁMARA
        # ---------------------------------------------------------
        objetivo_cam_x = paso_x - 450
        objetivo_cam_y = paso_y - 300
        cam_x += (objetivo_cam_x - cam_x) * suavizado
        cam_y += (objetivo_cam_y - cam_y) * suavizado

        # ---------------------------------------------------------
        # DIBUJO
        # ---------------------------------------------------------
        VENTANA.fill(COLORES["fondo"])

        # FOTO GRANDE DEL PASO (Cristo o Virgen)
        VENTANA.blit(fondo_paso, (0, 0))

        # MAPA DETRÁS DEL PASO
        VENTANA.blit(mapa, (-cam_x, -cam_y))

        # PANEL DE CONTROLES
        fuente = pygame.font.SysFont("Segoe UI", 20, bold=True)
        panel = pygame.Rect(VENTANA.get_width() - 260, 80, 240, 330)
        pygame.draw.rect(VENTANA, (20, 15, 40), panel, border_radius=12)
        pygame.draw.rect(VENTANA, COLORES["dorado"], panel, 2, border_radius=12)

        y_texto = 95
        for linea in controles:
            t_linea = fuente.render(linea, True, COLORES["texto"])
            VENTANA.blit(t_linea, (VENTANA.get_width() - 245, y_texto))
            y_texto += 22

        # SPRITE DEL PASO (Cristo o Virgen)
        imagen_rotada = pygame.transform.rotate(paso_img, paso_angulo)
        rect_img = imagen_rotada.get_rect(center=(paso_x - cam_x, paso_y - cam_y - paso_altura))

        # SOMBRA
        sombra = pygame.Surface((rect_img.width, rect_img.height // 3), pygame.SRCALPHA)
        pygame.draw.ellipse(sombra, (0, 0, 0, 120), sombra.get_rect())
        VENTANA.blit(sombra, (rect_img.centerx - sombra.get_width() // 2,
                              rect_img.bottom - sombra.get_height() // 2))

        VENTANA.blit(imagen_rotada, rect_img)

        boton_llamador.dibujar(VENTANA)
        boton_voces.dibujar(VENTANA)

        pygame.display.update()