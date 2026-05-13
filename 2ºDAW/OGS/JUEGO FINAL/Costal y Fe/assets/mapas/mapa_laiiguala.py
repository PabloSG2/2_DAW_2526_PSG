import pygame

ANCHO_MAPA = 2600
ALTO_MAPA = 1600

def generar_mapa_laiiguala():
    """
    Mapa para MODO LIBRE:
    - Recta larga horizontal
    - Giro suave hacia abajo
    - Segunda recta
    - Aceras y público
    - META al final del recorrido
    """
    mapa = pygame.Surface((ANCHO_MAPA, ALTO_MAPA))
    mapa.fill((25, 25, 25))

    color_calle = (185, 185, 185)
    color_acera = (60, 60, 60)
    color_pub = (230, 210, 255)

    # Aceras generales
    pygame.draw.rect(mapa, color_acera, (0, 450, ANCHO_MAPA, 300))

    # RECTAS Y GIROS
    recta1 = pygame.Rect(150, 550, 1500, 200)
    pygame.draw.rect(mapa, color_calle, recta1)

    curva = pygame.Rect(1600, 550, 300, 400)
    pygame.draw.rect(mapa, color_calle, curva)

    recta2 = pygame.Rect(1600, 850, 200, 600)
    pygame.draw.rect(mapa, color_calle, recta2)

    recta3 = pygame.Rect(600, 1250, 1200, 200)
    pygame.draw.rect(mapa, color_calle, recta3)

    # -------------------------
    # META (cuadro azul grande)
    # -------------------------
    meta_rect = pygame.Rect(650, 1270, 200, 200)
    pygame.draw.rect(mapa, (0, 120, 255), meta_rect)

    fuente = pygame.font.SysFont("Segoe UI", 32, True)
    texto_meta = fuente.render("META", True, (255, 255, 255))
    mapa.blit(texto_meta, (meta_rect.x + 50, meta_rect.y + 70))

    # Público en recta 1
    for x in range(200, 1600, 80):
        pygame.draw.circle(mapa, color_pub, (x, 530), 5)
        pygame.draw.circle(mapa, color_pub, (x, 770), 5)

    # Público en curva
    for y in range(600, 900, 80):
        pygame.draw.circle(mapa, color_pub, (1580, y), 5)
        pygame.draw.circle(mapa, color_pub, (1900, y), 5)

    # Público en recta 2
    for y in range(900, 1400, 80):
        pygame.draw.circle(mapa, color_pub, (1580, y), 5)
        pygame.draw.circle(mapa, color_pub, (1800, y), 5)

    # Público en recta 3
    for x in range(650, 1700, 80):
        pygame.draw.circle(mapa, color_pub, (x, 1230), 5)
        pygame.draw.circle(mapa, color_pub, (x, 1470), 5)

    return mapa, meta_rect, obtener_calles_laiiguala()


def obtener_calles_laiiguala():
    """
    Calles para colisiones del modo libre.
    Deben coincidir con lo dibujado arriba.
    """
    calles = [
        pygame.Rect(150, 550, 1500, 200),   # recta 1
        pygame.Rect(1600, 550, 300, 400),   # curva
        pygame.Rect(1600, 850, 200, 600),   # recta 2
        pygame.Rect(600, 1250, 1200, 200),  # recta 3
    ]
    return calles
