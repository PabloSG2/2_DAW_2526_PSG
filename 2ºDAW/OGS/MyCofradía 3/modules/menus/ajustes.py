import pygame

FUENTE = pygame.font.SysFont("arial", 22, bold=True)
COLOR_PANEL = (35, 20, 70)
COLOR_TEXTO = (255, 255, 255)

def dibujar_ajustes(VENTANA, raton_pos, data, botones, theme):
    aj = data["ajustes"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, theme["panel"], panel, border_radius=20)

    x = panel.x + 30
    y = panel.y + 30

    lineas = [
        "AJUSTES",
        "",
        f"Modo: {'Oscuro' if aj['modo_oscuro'] else 'Claro'}  (tecla M)",
        f"Animaciones: {'Activadas' if aj['animaciones'] else 'Desactivadas'}  (tecla A)",
        f"Sonidos: {'Activados' if aj['sonidos'] else 'Desactivados'}  (tecla S)",
        "",
        "Volúmenes (no se muestran sliders, pero se usan internamente):",
        "- Volumen general",
        "- Volumen sonidos",
        "- Volumen banda",
        "",
        "Tecla R: Reiniciar partida (dinero y prestigio básicos)",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, theme["texto"])
        VENTANA.blit(t, (x, y + i*28))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)

def reiniciar_partida(data):
    data["dinero"] = 5000
    data["hermandad"]["prestigio"] = 0
    data["hermandad"]["cultos"] = []
    data["hermandad"]["ensayos"] = []
    data["hermandad"]["traslados"] = []
    data["economia"]["ingresos"] = []
    data["economia"]["gastos"] = []
    data["economia"]["balance"] = 0
    data["hermanos"] = []
    data["logros"] = {}
