import pygame

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_PANEL = (35, 20, 70)
COLOR_TEXTO = (255, 255, 255)
COLOR_DORADO = (255, 215, 0)
COLOR_VERDE = (0, 200, 0)

LOGROS_DEFINICION = {
    "primer_culto": "Celebrar el primer culto",
    "permiso_obispo": "Conseguir permiso del obispo",
    "banda_propia": "Crear una banda propia",
    "prestigio_10": "Alcanzar 10 de prestigio",
    "prestigio_50": "Alcanzar 50 de prestigio",
    "balance_10000": "Conseguir 10.000€ de balance",
    "primer_hermano": "Registrar al primer hermano",
    "cien_hermanos": "Llegar a 100 hermanos",
}

def comprobar_logros(data, evento=None):
    herm = data["hermandad"]
    eco = data["economia"]
    hermanos = data["hermanos"]
    logros = data["logros"]

    # Primer culto
    if not logros.get("primer_culto") and len(herm["cultos"]) >= 1:
        logros["primer_culto"] = True
        data["dinero"] += 500

    # Permiso obispo
    if not logros.get("permiso_obispo") and herm["permiso_obispo"]:
        logros["permiso_obispo"] = True
        data["dinero"] += 1000

    # Banda propia
    if not logros.get("banda_propia") and herm["banda_propia"]:
        logros["banda_propia"] = True
        herm["prestigio"] += 5

    # Prestigio
    if not logros.get("prestigio_10") and herm["prestigio"] >= 10:
        logros["prestigio_10"] = True
        data["dinero"] += 500
    if not logros.get("prestigio_50") and herm["prestigio"] >= 50:
        logros["prestigio_50"] = True
        data["dinero"] += 2000

    # Balance
    if not logros.get("balance_10000") and eco["balance"] >= 10000:
        logros["balance_10000"] = True
        herm["prestigio"] += 10

    # Hermanos
    if not logros.get("primer_hermano") and len(hermanos) >= 1:
        logros["primer_hermano"] = True
        data["dinero"] += 300
    if not logros.get("cien_hermanos") and len(hermanos) >= 100:
        logros["cien_hermanos"] = True
        herm["prestigio"] += 20

def dibujar_logros(VENTANA, raton_pos, data, botones, theme):
    logros = data["logros"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, theme["panel"], panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    titulo = FUENTE.render("LOGROS", True, COLOR_DORADO)
    VENTANA.blit(titulo, (x, y))

    y += 40

    for clave, desc in LOGROS_DEFINICION.items():
        desbloqueado = logros.get(clave, False)
        color = COLOR_VERDE if desbloqueado else theme["texto"]
        estado = "✔" if desbloqueado else "✖"
        txt = FUENTE.render(f"{estado} {desc}", True, color)
        VENTANA.blit(txt, (x, y))
        y += 28

    for b in botones:
        b.dibujar(VENTANA, raton_pos)
