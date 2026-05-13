import pygame

ANCHO_MAPA = 2400
ALTO_MAPA = 1200

def generar_mapa_procesion():
    """
    Mapa tipo C:
    - Recta inicial a la derecha
    - Giro hacia abajo
    - Calle intermedia
    - Giro hacia la izquierda
    - Recta final hacia la izquierda
    - Meta azul en la esquina inferior-izquierda
    """
    mapa = pygame.Surface((ANCHO_MAPA, ALTO_MAPA))
    mapa.fill((20, 20, 20))

    # Fondo aceras
    pygame.draw.rect(mapa, (60, 60, 60), (0, 400, ANCHO_MAPA, 400))

    # Calles (blanco/gris claro)
    color_calle = (180, 180, 180)

    # Recta 1 (horizontal derecha)
    recta1 = pygame.Rect(100, 500, 1400, 200)
    pygame.draw.rect(mapa, color_calle, recta1)

    # Giro 1 (vertical hacia abajo)
    giro1 = pygame.Rect(1500, 500, 200, 400)
    pygame.draw.rect(mapa, color_calle, giro1)

    # Calle intermedia (horizontal izquierda, a media altura)
    recta2 = pygame.Rect(400, 700, 1100, 200)
    pygame.draw.rect(mapa, color_calle, recta2)

    # Giro 2 (vertical hacia abajo)
    giro2 = pygame.Rect(400, 700, 200, 300)
    pygame.draw.rect(mapa, color_calle, giro2)

    # Recta final (horizontal izquierda, abajo)
    recta3 = pygame.Rect(200, 900, 800, 200)
    pygame.draw.rect(mapa, color_calle, recta3)

    # META (cuadro azul en el suelo)
    meta_rect = pygame.Rect(220, 920, 200, 200)
    pygame.draw.rect(mapa, (0, 120, 255), meta_rect)

    # Texto META
    fuente = pygame.font.SysFont("Segoe UI", 32, True)
    texto_meta = fuente.render("META", True, (255, 255, 255))
    mapa.blit(texto_meta, (meta_rect.x + 50, meta_rect.y + 70))

    # Público (simple, a los lados)
    color_pub = (220, 200, 255)
    for x in range(120, 1500, 80):
        pygame.draw.circle(mapa, color_pub, (x, 480), 5)
        pygame.draw.circle(mapa, color_pub, (x, 720), 5)

    for y in range(520, 880, 80):
        pygame.draw.circle(mapa, color_pub, (1480, y), 5)
        pygame.draw.circle(mapa, color_pub, (1720, y), 5)

    for x in range(420, 1200, 80):
        pygame.draw.circle(mapa, color_pub, (x, 680), 5)
        pygame.draw.circle(mapa, color_pub, (x, 920), 5)

    return mapa, meta_rect, obtener_calles_procesion()

def obtener_calles_procesion():
    """
    Devuelve la lista de rects de las calles para colisiones.
    Debe coincidir con lo dibujado arriba.
    """
    calles = [
        pygame.Rect(100, 500, 1400, 200),   # recta 1
        pygame.Rect(1500, 500, 200, 400),   # giro 1
        pygame.Rect(400, 700, 1100, 200),   # recta 2
        pygame.Rect(400, 700, 200, 300),    # giro 2
        pygame.Rect(200, 900, 800, 200),    # recta 3
    ]
    return calles
