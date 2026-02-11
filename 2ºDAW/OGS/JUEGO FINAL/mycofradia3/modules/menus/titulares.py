import pygame
from core.botones import BotonSimple, get_fuente
from core.ui import dibujar_titulo
from config import COLORES

def menu_titulares(VENTANA, estado):
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    try:
        img_cristo = pygame.image.load("assets/img/cristo.png").convert_alpha()
        img_virgen = pygame.image.load("assets/img/virgen.png").convert_alpha()
    except:
        img_cristo = pygame.Surface((200, 300))
        img_cristo.fill((120, 80, 80))
        img_virgen = pygame.Surface((200, 300))
        img_virgen.fill((80, 120, 80))

    img_cristo = pygame.transform.smoothscale(img_cristo, (250, 350))
    img_virgen = pygame.transform.smoothscale(img_virgen, (250, 350))

    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if boton_volver.clicado(pos):
                    return "inicio"

        VENTANA.fill(COLORES["fondo"])
        dibujar_titulo(VENTANA, "TITULARES", y=40)

        VENTANA.blit(img_cristo, (150, 150))
        VENTANA.blit(img_virgen, (500, 150))

        fuente = get_fuente(26, True)
        t1 = fuente.render("Cristo", True, COLORES["texto"])
        t2 = fuente.render("Virgen", True, COLORES["texto"])

        VENTANA.blit(t1, (150 + 125 - t1.get_width()//2, 510))
        VENTANA.blit(t2, (500 + 125 - t2.get_width()//2, 510))

        boton_volver.dibujar(VENTANA)
        pygame.display.update()
