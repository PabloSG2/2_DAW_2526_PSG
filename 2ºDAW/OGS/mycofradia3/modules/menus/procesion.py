import pygame
import random
from core.botones import Boton, get_fuente
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
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
# Clase Paso (Cristo / Virgen)
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

        self.x = max(120, min(780, self.x))
        self.y = max(140, min(460, self.y))

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

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, (220, 220, 220), (self.x - 10, self.y - 30, 20, 30))
        pygame.draw.circle(ventana, (230, 220, 200), (self.x, self.y - 40), 10)
        if self.brazo_arriba:
            pygame.draw.line(ventana, (230, 220, 200), (self.x, self.y - 20), (self.x + 20, self.y - 50), 4)
        else:
            pygame.draw.line(ventana, (230, 220, 200), (self.x, self.y - 20), (self.x + 20, self.y - 10), 4)

# -----------------------------
# Costaleros visuales
# -----------------------------
class CostaleroVisual:
    def __init__(self, offset_x, offset_y):
        self.offset_x = offset_x
        self.offset_y = offset_y

    def pos(self, paso: Paso):
        return (paso.x + self.offset_x, paso.y + self.offset_y - paso.altura // 2)

def crear_cuadrilla_visual(tipo):
    costaleros_visuales = []
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
            costaleros_visuales.append(CostaleroVisual(ox, oy))
    return costaleros_visuales

# -----------------------------
# Selección de Cristo / Virgen
# -----------------------------
def seleccionar_tipo_paso(VENTANA, estado):
    boton_cristo = Boton((220, 260, 200, 60), "Cristo", color_fondo=(80, 40, 140))
    boton_virgen = Boton((480, 260, 200, 60), "Virgen", color_fondo=(80, 40, 140))
    boton_volver = Boton((20, 20, 180, 55), "Volver", color_fondo=(180, 40, 40))

    while True:
        VENTANA.fill(COLORES["fondo_procesion"])
        dibujar_titulo(VENTANA, "SELECCIONAR PASO", y=120)

        dibujar_texto(VENTANA, "Elige el tipo de paso para el ensayo:", 220, 210)

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
                    return
                if boton_virgen.clicado(pos):
                    estado["tipo_paso"] = "virgen"
                    return
                if boton_volver.clicado(pos):
                    return

        pygame.display.update()

# -----------------------------
# Ensayo avanzado (Procesión)
# -----------------------------
def menu_procesion(VENTANA, estado):
    seleccionar_tipo_paso(VENTANA, estado)
    tipo = estado["tipo_paso"]

    boton_volver = Boton((20, 20, 180, 55), "Volver", color_fondo=(180, 40, 40))

    paso = Paso(450, 360, tipo)
    capataz = Capataz(450, 220)
    costaleros_visuales = crear_cuadrilla_visual(tipo)

    reloj = pygame.time.Clock()
    duracion_ensayo = 60 * 40
    tiempo_restante = duracion_ensayo

    sincronizacion = estado["sincronizacion"]
    fatiga = estado["fatiga"]
    riesgo = estado["riesgo_lesion"]
    moral_media = int(sum(c["moral"] for c in estado["hermanos"]) / len(estado["hermanos"]))

    mensaje = ""
    mensaje_timer = 0

    marcha_sonando = False
    tiempo_marcha = 0.0
    bpm = 60 if tipo == "cristo" else 72
    segundos_por_paso = 60 / bpm

    ultimo_estado = PARADO
    cambios_buenos = 0
    cambios_malos = 0

    while True:
        dt = reloj.tick(60)
        tiempo_restante -= 1
        if tiempo_restante <= 0:
            estado["sincronizacion"] = int(sincronizacion)
            estado["fatiga"] = int(fatiga)
            estado["riesgo_lesion"] = int(riesgo)
            return "inicio"

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver.clicado(pos):
                    estado["sincronizacion"] = int(sincronizacion)
                    estado["fatiga"] = int(fatiga)
                    estado["riesgo_lesion"] = int(riesgo)
                    return "inicio"

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

        VENTANA.fill(COLORES["fondo_procesion"])

        dibujar_titulo(VENTANA, f"ENSAYO AVANZADO — {tipo.upper()}", y=20)

        mapa_rect = pygame.Rect(80, 80, 740, 420)
        dibujar_panel(VENTANA, mapa_rect, color=(15, 15, 15), radio=20)

        pygame.draw.rect(VENTANA, (120, 80, 40), paso.rect(), border_radius=10)

        for cv in costaleros_visuales:
            cx, cy = cv.pos(paso)
            pygame.draw.circle(VENTANA, (200, 200, 200), (int(cx), int(cy)), 5)

        capataz.dibujar(VENTANA)

        fuente = get_fuente(18, False)
        info = [
            f"Sincronización: {int(sincronizacion)}",
            f"Fatiga: {int(fatiga)}",
            f"Riesgo lesión: {int(riesgo)}",
            f"Moral media: {int(moral_media)}",
            f"Tiempo restante: {max(0, tiempo_restante // 60)} s",
            f"Cambios buenos: {cambios_buenos}",
            f"Cambios malos: {cambios_malos}",
            f"Marcha: {'ON' if marcha_sonando else 'OFF'}",
        ]
        y = 520
        for linea in info:
            t = fuente.render(linea, True, COLORES["texto"])
            VENTANA.blit(t, (80, y))
            y += 20

        controles = [
            "Controles:",
            "1: De frente",
            "2: Para atrás",
            "3: Izquierda",
            "4: Derecha",
            "5: Costero izq",
            "6: Costero der",
            "7: Giro izq",
            "8: Giro der",
            "0: Parado",
            "ESPACIO: Levantá",
            "M: Marcha ON/OFF",
        ]
        y = 520
        for linea in controles:
            t = fuente.render(linea, True, COLORES["texto"])
            VENTANA.blit(t, (480, y))
            y += 18

        if mensaje:
            color = COLORES["verde"] if "fina" in mensaje or "moral" in mensaje else COLORES["rojo"]
            t = fuente.render(mensaje, True, color)
            VENTANA.blit(t, (100, 480))

        boton_volver.dibujar(VENTANA)

        pygame.display.update()
