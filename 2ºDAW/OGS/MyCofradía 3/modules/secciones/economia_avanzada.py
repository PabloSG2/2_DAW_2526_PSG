import pygame
from datetime import datetime

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_PANEL = (35, 20, 70)
COLOR_TEXTO = (255, 255, 255)
COLOR_VERDE = (0, 200, 0)
COLOR_ROJO = (200, 0, 0)

INGRESOS = ["Donativos", "Contratos Banda", "Cultos", "Ensayos", "Traslados", "Subvención", "Cuotas", "Recuerdos"]
GASTOS = ["Flores", "Cera", "Banda", "Vestidor", "Restauración", "Electricidad", "Seguros", "Limpieza"]

def dibujar_economia(VENTANA, raton_pos, data, botones):
    eco = data["economia"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, COLOR_PANEL, panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    lineas = [
        "ECONOMÍA AVANZADA",
        "",
        "Teclas:",
        "- I: Añadir Ingreso (Donativos)",
        "- G: Añadir Gasto (Flores)",
        "",
        f"Balance total: {eco['balance']} €",
        "",
        "Últimos movimientos:",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, COLOR_TEXTO)
        VENTANA.blit(t, (x, y + i*28))

    movimientos = eco["ingresos"] + eco["gastos"]
    movimientos = movimientos[-10:]

    for i, mov in enumerate(movimientos):
        color = COLOR_VERDE if "INGRESO" in mov else COLOR_ROJO
        t = FUENTE.render(f"- {mov}", True, color)
        VENTANA.blit(t, (x + 20, y + 220 + i*25))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)

def añadir_ingreso(data, tipo="Donativos"):
    eco = data["economia"]
    cantidad = 500
    eco["balance"] += cantidad
    eco["ingresos"].append(f"INGRESO {tipo}: +{cantidad}€ ({datetime.now().strftime('%d/%m')})")
    data["dinero"] += cantidad

def añadir_gasto(data, tipo="Flores"):
    eco = data["economia"]
    cantidad = 300
    eco["balance"] -= cantidad
    eco["gastos"].append(f"GASTO {tipo}: -{cantidad}€ ({datetime.now().strftime('%d/%m')})")
    data["dinero"] -= cantidad
