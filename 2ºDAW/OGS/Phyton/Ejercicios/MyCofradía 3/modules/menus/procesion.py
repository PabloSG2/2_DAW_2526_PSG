import pygame
import math
from modules.assets import cargar_imagen, cargar_sonido

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_TEXTO = (255, 255, 255)

FONDO_PROC = cargar_imagen("data/images/procesion/fondo_calle.png", (900, 600))
PASO_IMG = cargar_imagen("data/images/procesion/paso_procesion.png", (260, 180))
BANDA_IMG = cargar_imagen("data/images/procesion/banda_procesion.png", (220, 120))
NAZARENOS_IMG = cargar_imagen("data/images/procesion/nazarenos.png", (220, 140))
PUBLICO_IMG = cargar_imagen("data/images/procesion/publico.png", (900, 120))

SON_BANDA = cargar_sonido("data/sounds/banda.wav")
SON_APLAUSOS = cargar_sonido("data/sounds/aplausos.wav")

def dibujar_procesion(VENTANA, raton_pos, data, botones, theme, estado_proc):
    if FONDO_PROC:
        VENTANA.blit(FONDO_PROC, (0, 0))
    else:
        VENTANA.fill(theme["fondo"])

    if PUBLICO_IMG:
        VENTANA.blit(PUBLICO_IMG, (0, 0))

    t = pygame.time.get_ticks() / 300.0
    offset = int(5 * math.sin(t)) if estado_proc["mecida"] else 0

    x_paso = estado_proc["x_paso"]
    y_paso = 260 + offset

    if PASO_IMG:
        VENTANA.blit(PASO_IMG, (x_paso, y_paso))
    else:
        pygame.draw.rect(VENTANA, (180, 140, 40), (x_paso, y_paso, 260, 180), border_radius=15)

    if BANDA_IMG:
        VENTANA.blit(BANDA_IMG, (x_paso - 260, y_paso + 60))

    if NAZARENOS_IMG:
        VENTANA.blit(NAZARENOS_IMG, (x_paso + 260, y_paso + 40))

    panel = pygame.Rect(20, 20, 380, 120)
    pygame.draw.rect(VENTANA, (0, 0, 0, 120), panel, border_radius=10)

    lineas = [
        "MODO PROCESIÓN",
        "",
        "Teclas:",
        "- A: Avanzar",
        "- S: Parar",
        "- M: Mecida",
        "- P: Aplausos",
    ]

    yy = panel.y + 10
    for txt in lineas:
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (panel.x + 10, yy))
        yy += 22

    for b in botones:
        b.dibujar(VENTANA, raton_pos)

def actualizar_procesion(estado_proc):
    if estado_proc["avanzando"]:
        estado_proc["x_paso"] -= 2
        if estado_proc["x_paso"] < -300:
            estado_proc["x_paso"] = 900

def reproducir_banda(data):
    if data["ajustes"]["sonidos"] and SON_BANDA:
        SON_BANDA.play(-1)

def parar_banda():
    pygame.mixer.stop()

def reproducir_aplausos(data):
    if data["ajustes"]["sonidos"] and SON_APLAUSOS:
        SON_APLAUSOS.play()
