import pygame
from datetime import datetime

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_PANEL = (35, 20, 70)
COLOR_TEXTO = (255, 255, 255)
COLOR_DORADO = (255, 215, 0)

CULTOS = ["Triduo", "Quinario", "Septenario", "Función Principal", "Besamanos"]
ENSAYOS = ["Ensayo General", "Ensayo de Costaleros", "Igualá", "Mudá"]
TRASLADOS = ["Al Altar", "Al Paso", "A la Iglesia"]

def dibujar_cultos(VENTANA, raton_pos, data, botones):
    herm = data["hermandad"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    lineas = [
        "CULTOS, ENSAYOS Y TRASLADOS",
        "",
        "Teclas:",
        "- C: Añadir Culto",
        "- E: Añadir Ensayo",
        "- T: Añadir Traslado",
        "",
        "Historial reciente:",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*28))

    eventos = herm["cultos"] + herm["ensayos"] + herm["traslados"]
    eventos = eventos[-8:]

    for i, ev in enumerate(eventos):
        t = FUENTE.render(f"- {ev}", True, COLOR_DORADO)
        VENTANA.blit(t, (x + 20, y + 220 + i*25))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)

def añadir_culto(data):
    evento = f"CULTO: {datetime.now().strftime('%d/%m')} - {CULTOS[0]}"
    data["hermandad"]["cultos"].append(evento)
    data["hermandad"]["prestigio"] += 2

def añadir_ensayo(data):
    evento = f"ENSAYO: {datetime.now().strftime('%d/%m')} - {ENSAYOS[0]}"
    data["hermandad"]["ensayos"].append(evento)
    data["hermandad"]["prestigio"] += 1

def añadir_traslado(data):
    evento = f"TRASLADO: {datetime.now().strftime('%d/%m')} - {TRASLADOS[0]}"
    data["hermandad"]["traslados"].append(evento)
    data["hermandad"]["prestigio"] += 3
