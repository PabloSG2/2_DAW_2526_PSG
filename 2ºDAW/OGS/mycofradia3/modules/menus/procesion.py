import pygame
import random
from core.botones import BotonSimple, get_fuente
from core.ui import dibujar_titulo
from config import COLORES

# -----------------------------
# Estados de movimiento
# -----------------------------
FRONTAL = "frontal"
ATRAS = "atras"
IZQUIERDA = "izquierda"
DERECHA = "derecha"
COSTERO_IZQ = "costero_izq"
COSTERO_DER = "costero_der"
PARADO = "parado"
GIRO_IZQ = "giro_izq"
GIRO_DER = "giro_der"

# -----------------------------
# Clase Paso
# -----------------------------
class Paso:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.angulo = 0
        self.altura = 0
        self.vel = 0
        self.estado = PARADO
        self.tipo = tipo

        if tipo == "cristo":
            self.max_vel = 0.45
            self.acel = 0.004
            self.giro = 0.18
            self.costero_factor = 0.25
            self.ancho = 200
            self.alto = 90
        else:
            self.max_vel = 0.65
            self.acel = 0.007
            self.giro = 0.32
            self.costero_factor = 0.45
            self.ancho = 180
            self.alto = 80

    def rect(self):
        return pygame.Rect(
            self.x - self.ancho // 2,
            self.y - self.alto // 2 - self.altura,
            self.ancho,
            self.alto
        )

    def levantá(self):
        self.altura = 18 if self.tipo == "cristo" else 14

    def animar_levanta(self):
        if self.altura > 0:
            self.altura -= 1

    def actualizar(self):
        if self.estado == FRONTAL:
            self.vel = min(self.max_vel, self.vel + self.acel)
            self.y -= self.vel
        elif self.estado == ATRAS:
            self.vel = min(self.max_vel, self.vel + self.acel)
            self.y += self.vel * 0.7
        elif self.estado == IZQUIERDA:
            self.vel = min(self.max_vel, self.vel + self.acel)
            self.x -= self.vel * 0.5
        elif self.estado == DERECHA:
            self.vel = min(self.max_vel, self.vel + self.acel)
            self.x += self.vel * 0.5
        elif self.estado == COSTERO_IZQ:
            self.vel = min(self.max_vel, self.vel + self.acel)
            self.x -= self.vel * self.costero_factor
            self.y -= self.vel * (1 - self.costero_factor)
        elif self.estado == COSTERO_DER:
            self.vel = min(self.max_vel, self.vel + self.acel)
            self.x += self.vel * self.costero_factor
            self.y -= self.vel * (1 - self.costero_factor)
        elif self.estado == GIRO_IZQ:
            self.angulo -= self.giro
        elif self.estado == GIRO_DER:
            self.angulo += self.giro
        else:
            if self.vel > 0:
                self.vel -= 0.02
            if self.vel < 0:
                self.vel = 0

# -----------------------------
# Capataz
# -----------------------------
class Capataz:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.brazo_arriba = False
        self.timer_brazo = 0

    def llamar(self):
        self.brazo_arriba = True
        self.timer_brazo = 30

    def actualizar(self):
        if self.brazo_arriba:
            self.timer_brazo -= 1
            if self.timer_brazo <= 0:
                self.brazo_arriba = False

    def dibujar(self, ventana, cam_x, cam_y):
        sx = self.x - cam_x
        sy = self.y - cam_y
        pygame.draw.rect(ventana, (220, 220, 220), (sx - 10, sy - 30, 20, 30))
        pygame.draw.circle(ventana, (230, 220, 200), (sx, sy - 40), 10)
        if self.brazo_arriba:
            pygame.draw.line(ventana, (230, 220, 200), (sx, sy - 20), (sx + 20, sy - 50), 4)
        else:
            pygame.draw.line(ventana, (230, 220, 200), (sx, sy - 20), (sx + 20, sy - 10), 4)

# -----------------------------
# Costaleros visuales
# -----------------------------
class CostaleroVisual:
    def __init__(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y

    def pos(self, paso, cam_x, cam_y):
        return (
            paso.x + self.offset_x - cam_x,
            paso.y + self.offset_y - cam_y - paso.altura // 2
        )

def crear_cuadrilla_visual(tipo):
    costaleros = []
    filas = 3 if tipo == "cristo" else 2
    por_fila = 6 if tipo == "cristo" else 5
    sep_x = 30
    sep_y = 18
    inicio_x = - (por_fila - 1) * sep_x // 2
    inicio_y = -10

    for f in range(filas):
        for i in range(por_fila):
            ox = inicio_x + i * sep_x
            oy = inicio_y + f * sep_y
            costaleros.append(CostaleroVisual(ox, oy))

    return costaleros

# -----------------------------
# Selección de modo (ESTILO MYCOFRADÍA2)
# -----------------------------
def seleccionar_modo(VENTANA):
    ancho = 260
    alto = 70
    x = VENTANA.get_width() // 2 - ancho // 2

    boton_recorrido = BotonSimple((x, 240, ancho, alto), "RECORRIDO")
    boton_ensayo = BotonSimple((x, 330, ancho, alto), "ENSAYO LIBRE")
    boton_volver = BotonSimple((x, 420, ancho, alto), "VOLVER")

    while True:
        VENTANA.fill(COLORES["fondo_procesion"])
        dibujar_titulo(VENTANA, "MODO DE PROCESIÓN", y=120)

        boton_recorrido.dibujar(VENTANA)
        boton_ensayo.dibujar(VENTANA)
        boton_volver.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_recorrido.clicado(pos):
                    return "recorrido"
                if boton_ensayo.clicado(pos):
                    return "ensayo"
                if boton_volver.clicado(pos):
                    return None

        pygame.display.update()

# -----------------------------
# Selección de tipo de paso
# -----------------------------
def seleccionar_tipo_paso(VENTANA, estado):
    ancho = 260
    alto = 70
    x = VENTANA.get_width() // 2 - ancho // 2

    boton_cristo = BotonSimple((x, 260, ancho, alto), "CRISTO")
    boton_virgen = BotonSimple((x, 350, ancho, alto), "VIRGEN")
    boton_volver = BotonSimple((x, 440, ancho, alto), "VOLVER")

    while True:
        VENTANA.fill(COLORES["fondo_procesion"])
        dibujar_titulo(VENTANA, "SELECCIONAR PASO", y=120)

        boton_cristo.dibujar(VENTANA)
        boton_virgen.dibujar(VENTANA)
        boton_volver.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_cristo.clicado(pos):
                    estado["tipo_paso"] = "cristo"
                    return True
                if boton_virgen.clicado(pos):
                    estado["tipo_paso"] = "virgen"
                    return True
                if boton_volver.clicado(pos):
                    return False

        pygame.display.update()

# -----------------------------
# Cargar mapa
# -----------------------------
def cargar_mapa():
    try:
        mapa = pygame.image.load("assets/mapas/recorrido_urbano.png").convert()
    except:
        mapa = pygame.Surface((1600, 1200))
        mapa.fill((40, 40, 40))
    return mapa

# -----------------------------
# Cámara
# -----------------------------
def calcular_camara(paso, mapa, w, h):
    cam_x = paso.x - w // 2
    cam_y = paso.y - h // 2

    cam_x = max(0, min(cam_x, mapa.get_width() - w))
    cam_y = max(0, min(cam_y, mapa.get_height() - h))

    return cam_x, cam_y

# -----------------------------
# Motor principal
# -----------------------------
def ejecutar_modo(VENTANA, estado, modo):
    tipo = estado["tipo_paso"]
    paso = Paso(400, 800, tipo)
    capataz = Capataz(420, 760)
    costaleros = crear_cuadrilla_visual(tipo)

    mapa = cargar_mapa()
    reloj = pygame.time.Clock()

    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")
    boton_marcha = BotonSimple((VENTANA.get_width() - 170, 20, 150, 45), "Marcha")

    sincronizacion = estado["sincronizacion"]
    fatiga = estado["fatiga"]
    riesgo = estado["riesgo_lesion"]
    moral_media = int(sum(h["moral"] for h in estado["hermanos"]) / len(estado["hermanos"]))

    mensaje = ""
    mensaje_timer = 0

    marcha_sonando = False
    tiempo_marcha = 0.0
    bpm = 60 if tipo == "cristo" else 72
    segundos_por_paso = 60 / bpm

    ultimo_estado = PARADO
    cambios_buenos = 0
    cambios_malos = 0

    objetivo_rect = pygame.Rect(700, 200, 120, 120) if modo == "recorrido" else None
    completado = False

    while True:
        dt = reloj.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver.clicado(pos):
                    return "inicio"
                if boton_marcha.clicado(pos):
                    marcha_sonando = not marcha_sonando

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paso.levantá()
                    capataz.llamar()
                    sincronizacion += 2
                    fatiga += 3

                if event.key == pygame.K_m:
                    marcha_sonando = not marcha_sonando

                if event.key == pygame.K_1:
                    paso.estado = FRONTAL
                if event.key == pygame.K_2:
                    paso.estado = ATRAS
                if event.key == pygame.K_3:
                    paso.estado = IZQUIERDA
                if event.key == pygame.K_4:
                    paso.estado = DERECHA
                if event.key == pygame.K_5:
                    paso.estado = COSTERO_IZQ
                if event.key == pygame.K_6:
                    paso.estado = COSTERO_DER
                if event.key == pygame.K_7:
                    paso.estado = GIRO_IZQ
                if event.key == pygame.K_8:
                    paso.estado = GIRO_DER
                if event.key == pygame.K_0:
                    paso.estado = PARADO

        if paso.estado != ultimo_estado:
            if ultimo_estado == PARADO and paso.estado in (FRONTAL, COSTERO_IZQ, COSTERO_DER):
                cambios_buenos += 1
                sincronizacion += 0.5
            elif paso.estado == PARADO:
                cambios_buenos += 1
                sincronizacion += 0.3
            else:
                cambios_malos += 1
                sincronizacion -= 0.5
                riesgo += 0.3
            ultimo_estado = paso.estado

        paso.actualizar()
        paso.animar_levanta()
        capataz.actualizar()

        if marcha_sonando and paso.estado != PARADO:
            tiempo_marcha += dt / 1000.0
            if tiempo_marcha >= segundos_por_paso:
                tiempo_marcha = 0.0
                paso.y -= 0.8 if tipo == "cristo" else 1.0
                sincronizacion += 0.1
                fatiga += 0.05

        if paso.estado != PARADO:
            fatiga += 0.02 * (1 + abs(paso.vel))
        if fatiga > 70:
            riesgo += 0.03 * (fatiga - 70)

        if random.random() < 0.002:
            if fatiga > 60 and riesgo > 40:
                mensaje = "Un costalero se descompone, baja sincronización."
                mensaje_timer = 180
                sincronizacion -= 4
                moral_media -= 3
            elif sincronizacion > 75:
                mensaje = "La cuadrilla va fina, sube moral."
                mensaje_timer = 180
                moral_media += 2

        sincronizacion = max(0, min(100, sincronizacion))
        fatiga = max(0, min(120, fatiga))
        riesgo = max(0, min(120, riesgo))
        moral_media = max(0, min(100, moral_media))

        if mensaje_timer > 0:
            mensaje_timer -= 1
            if mensaje_timer == 0:
                mensaje = ""

        cam_x, cam_y = calcular_camara(paso, mapa, VENTANA.get_width(), VENTANA.get_height())

        VENTANA.fill(COLORES["fondo_procesion"])
        VENTANA.blit(mapa, (-cam_x, -cam_y))

        if modo == "recorrido" and objetivo_rect:
            obj_screen = pygame.Rect(
                objetivo_rect.x - cam_x,
                objetivo_rect.y - cam_y,
                objetivo_rect.width,
                objetivo_rect.height
            )
            pygame.draw.rect(VENTANA, (80, 160, 80), obj_screen, 3)

            if paso.rect().colliderect(objetivo_rect) and not completado:
                completado = True
                mensaje = "Recorrido completado. ¡La cuadrilla va de lujo!"
                mensaje_timer = 300
                sincronizacion += 5
                moral_media += 5

        paso_rect_screen = paso.rect().move(-cam_x, -cam_y)
        pygame.draw.rect(VENTANA, (120, 80, 40), paso_rect_screen, border_radius=10)

        for cv in costaleros:
            cx, cy = cv.pos(paso, cam_x, cam_y)
            pygame.draw.circle(VENTANA, (200, 200, 200), (int(cx), int(cy)), 5)

        capataz.dibujar(VENTANA, cam_x, cam_y)

        fuente = get_fuente(18, False)
        info = [
            f"Modo: {'Recorrido' if modo == 'recorrido' else 'Ensayo libre'}",
            f"Tipo: {tipo.capitalize()}",
            f"Sincronización: {int(sincronizacion)}",
            f"Fatiga: {int(fatiga)}",
            f"Riesgo lesión: {int(riesgo)}",
            f"Moral media: {int(moral_media)}",
            f"Marcha: {'ON' if marcha_sonando else 'OFF'}",
        ]
        y = 80
        for linea in info:
            t = fuente.render(linea, True, (255, 255, 255))
            VENTANA.blit(t, (20, y))
            y += 20

        # -----------------------------
        # PANEL DE CONTROLES (SIEMPRE VISIBLE)
        # -----------------------------
        controles = [
            "CONTROLES:",
            "1 → De frente",
            "2 → Atrás",
            "3 → Izquierda",
            "4 → Derecha",
            "5 → Costero Izq",
            "6 → Costero Der",
            "7 → Giro Izq",
            "8 → Giro Der",
            "0 → Parado",
            "ESPACIO → Levantá",
            "M → Marcha ON/OFF",
        ]

        panel_controles = pygame.Rect(VENTANA.get_width() - 260, 120, 240, 260)
        pygame.draw.rect(VENTANA, (20, 15, 40), panel_controles, border_radius=12)
        pygame.draw.rect(VENTANA, (255, 215, 0), panel_controles, 2, border_radius=12)

        y_texto = 130
        for linea in controles:
            t = fuente.render(linea, True, (255, 255, 255))
            VENTANA.blit(t, (VENTANA.get_width() - 245, y_texto))
            y_texto += 22

        # Mensaje de eventos
        if mensaje:
            t = fuente.render(mensaje, True, (255, 255, 0))
            VENTANA.blit(t, (20, VENTANA.get_height() - 40))

        boton_volver.dibujar(VENTANA)
        boton_marcha.dibujar(VENTANA)

        pygame.display.update()

# -----------------------------
# Entrada principal del menú de procesión
# -----------------------------
def menu_procesion(VENTANA, estado):
    modo = seleccionar_modo(VENTANA)
    if modo is None:
        return "inicio"

    ok = seleccionar_tipo_paso(VENTANA, estado)
    if not ok:
        return "inicio"

    return ejecutar_modo(VENTANA, estado, modo)
