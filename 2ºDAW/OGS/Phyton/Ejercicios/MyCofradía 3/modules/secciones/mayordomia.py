import pygame
from modules.assets import cargar_imagen

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_TEXTO = (255, 255, 255)
COLOR_PANEL = (35, 20, 70)

MANTOS = ["Azul", "Rojo", "Verde", "Dorado"]
CORONAS = ["Plata", "Oro", "Oro Detallado"]
TUNICAS = ["Blanca", "Morada", "Roja"]
POTENCIAS = ["Plata", "Oro"]

VIRGEN_IMG = cargar_imagen("data/images/mayordomia/virgen.png", (140, 200))
CRISTO_IMG = cargar_imagen("data/images/mayordomia/cristo.png", (140, 200))

def dibujar_mayordomia(VENTANA, raton_pos, data, botones):
    herm = data["hermandad"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    lineas = [
        "MAYORDOMÍA",
        "",
        f"Manto Virgen: {MANTOS[herm['virgen_manto']]}  (1 / 2)",
        f"Corona Virgen: {CORONAS[herm['virgen_corona']]}  (3 / 4)",
        "",
        f"Túnica Cristo: {TUNICAS[herm['cristo_tunica']]}  (5 / 6)",
        f"Potencias Cristo: {POTENCIAS[herm['cristo_potencias']]}  (7 / 8)",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*28))

    if VIRGEN_IMG:
        VENTANA.blit(VIRGEN_IMG, (panel.right - 340, panel.y + 120))
    if CRISTO_IMG:
        VENTANA.blit(CRISTO_IMG, (panel.right - 180, panel.y + 120))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)
