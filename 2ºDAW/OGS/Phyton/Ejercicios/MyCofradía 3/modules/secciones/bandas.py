import pygame
from modules.hermandad import TIPOS_BANDA
from modules.assets import cargar_imagen

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_TEXTO = (255, 255, 255)
COLOR_PANEL = (35, 20, 70)
COLOR_DORADO = (255, 215, 0)

BANDAS_EXTERNAS = [
    ("BCT Rosario", 1500),
    ("AM Redención", 2000),
    ("BM Cigarreras", 2500),
]

BANDA_IMG = cargar_imagen("data/images/bandas/banda.png", (160, 120))

def dibujar_bandas(VENTANA, raton_pos, data, botones):
    herm = data["hermandad"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    banda_propia = herm["banda_propia"] if herm["banda_propia"] else "No creada"

    lineas = [
        "GESTIÓN DE BANDAS",
        "",
        f"Tu banda: {banda_propia}",
        f"Contratos activos: {len(herm['contratos'])}",
        "",
        "Teclas:",
        "- B: Crear banda propia (Cornetas y Tambores)",
        "- C: Contratar banda externa (primera de la lista)",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*28))

    if BANDA_IMG:
        VENTANA.blit(BANDA_IMG, (panel.right - 220, panel.y + 80))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)

def crear_banda(data, tipo="Cornetas y Tambores"):
    coste = TIPOS_BANDA[tipo]
    if data["dinero"] >= coste:
        data["dinero"] -= coste
        data["hermandad"]["banda_propia"] = tipo

def contratar_banda(data):
    nombre, precio = BANDAS_EXTERNAS[0]
    if data["dinero"] >= precio:
        data["dinero"] -= precio
        data["hermandad"]["contratos"].append(nombre)

def generar_ingresos_banda(data):
    herm = data["hermandad"]
    if herm["banda_propia"]:
        ingresos = 500 * len(herm["contratos"])
        data["dinero"] += ingresos
