import pygame
from core.botones import BotonSimple, get_fuente
from config import COLORES

def menu_inicio(VENTANA, estado):
    try:
        fondo = pygame.image.load("assets/img/fondo_menu.png").convert()
        fondo = pygame.transform.smoothscale(fondo, VENTANA.get_size())
    except:
        fondo = None

    try:
        logo = pygame.image.load("assets/img/logo.png").convert_alpha()
    except:
        logo = None

    botones = [
        ("Hermanos", "hermanos"),
        ("Titulares", "titulares"),
        ("Cultos", "cultos"),
        ("Economía", "economia"),
        ("Ensayos", "ensayos"),
        ("Procesión", "procesion"),
        ("Ajustes", "ajustes"),
        ("Salir", "salir"),
    ]

    botones_ui = []
    x = 100
    y = 260
    ancho = 200
    alto = 55
    sep = 220

    for texto, destino in botones:
        botones_ui.append((BotonSimple((x, y, ancho, alto), texto), destino))
        x += sep
        if x + ancho > VENTANA.get_width() - 100:
            x = 100
            y += 90

    while True:
        if fondo:
            VENTANA.blit(fondo, (0, 0))
        else:
            VENTANA.fill(COLORES["fondo"])

        if logo:
            rect = logo.get_rect(center=(VENTANA.get_width()//2, 150))
            VENTANA.blit(logo, rect)
        else:
            fuente = get_fuente(40, True)
            t = fuente.render("MYCOFRADÍA 2+", True, COLORES["dorado"])
            VENTANA.blit(t, (VENTANA.get_width()//2 - t.get_width()//2, 140))

        for boton, destino in botones_ui:
            boton.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for boton, destino in botones_ui:
                    if boton.clicado(pos):
                        if destino == "salir":
                            pygame.quit()
                            exit()
                        return destino

        pygame.display.update()
