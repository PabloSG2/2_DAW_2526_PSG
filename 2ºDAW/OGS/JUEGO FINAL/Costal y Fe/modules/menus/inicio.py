import pygame
import os
from core.botones import BotonSimple
from core.ui import dibujar_titulo
from config import COLORES, IMG

def cargar_icono(nombre):
    ruta = os.path.join(IMG, nombre)
    try:
        img = pygame.image.load(ruta).convert_alpha()
        return pygame.transform.smoothscale(img, (70, 70))
    except:
        s = pygame.Surface((70, 70), pygame.SRCALPHA)
        s.fill((120, 0, 0))
        return s

def menu_inicio(VENTANA, estado):
    clock = pygame.time.Clock()

    # Música de fondo
    try:
        pygame.mixer.music.load("assets/inicio.mp3")
        pygame.mixer.music.play(-1)
    except:
        pass

    # Fondo (NO SE TOCA)
    ruta_fondo = os.path.join(IMG, "fondo_menu.png")
    try:
        fondo = pygame.image.load(ruta_fondo).convert()
        fondo = pygame.transform.smoothscale(fondo, VENTANA.get_size())
    except:
        fondo = pygame.Surface(VENTANA.get_size())
        fondo.fill((20, 20, 40))

    # Iconos
    iconos = {
        "secretaria": cargar_icono("icono_secretaria.png"),
        "bandas": cargar_icono("icono_bandas.png"),
        "habito": cargar_icono("icono_habito.png"),
        "talleres": cargar_icono("icono_talleres.png"),
        "diputado_mayor": cargar_icono("icono_procesion.png"),
        "mayordomia": cargar_icono("icono_enseres.png"),
        "titulares": cargar_icono("icono_titulares.png"),
        "tesoreria": cargar_icono("icono_tesoreria.png"),
        "ayuda": cargar_icono("icono_ajustes.png"),
        "extra": cargar_icono("icono_extra.png"),
    }

    botones = []

    columna_izq = [
        ("Secretaría", "secretaria", iconos["secretaria"]),
        ("Hábito", "habito", iconos["habito"]),
        ("Diputado Mayor", "diputado_mayor", iconos["diputado_mayor"]),
        ("Titulares", "titulares", iconos["titulares"]),
        ("Ayuda / Ajustes", "ayuda_ajustes", iconos["ayuda"]),
    ]

    columna_der = [
        ("Bandas", "bandas", iconos["bandas"]),
        ("Talleres", "talleres", iconos["talleres"]),
        ("Mayordomía", "mayordomia", iconos["mayordomia"]),
        ("Tesorería", "tesoreria", iconos["tesoreria"]),
        ("Menu Extra", "extra", iconos["extra"]),
    ]

    y = 160
    for texto, destino, icono in columna_izq:
        botones.append((destino, icono, BotonSimple((140, y, 260, 60), texto)))
        y += 90

    y = 160
    for texto, destino, icono in columna_der:
        botones.append((destino, icono, BotonSimple((500, y, 260, 60), texto)))
        y += 90

    while True:
        clock.tick(60)
        VENTANA.blit(fondo, (0, 0))

        # -------------------------------
        # 🔵 TÍTULO AZUL
        # -------------------------------
        font = pygame.font.Font(None, 80)
        titulo = font.render("MENÚ PRINCIPAL", True, (0, 80, 200))

        VENTANA.blit(titulo, (VENTANA.get_width()//2 - titulo.get_width()//2, 40))

        pos = pygame.mouse.get_pos()

        for destino, icono, boton in botones:
            boton.actualizar_hover(pos)
            boton.dibujar(VENTANA)

            bx, by, bw, bh = boton.rect
            VENTANA.blit(icono, (bx - 80, by - 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                for destino, icono, boton in botones:
                    if boton.clicado(pos):
                        return destino

        pygame.display.update()
