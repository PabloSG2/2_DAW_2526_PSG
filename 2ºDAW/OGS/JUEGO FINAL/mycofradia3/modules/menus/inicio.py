import pygame
from core.botones import get_fuente
from config import COLORES
import os


class BotonLateral:
    def __init__(self, x, y, icono, texto, destino):
        self.rect = pygame.Rect(x, y, 150, 120)
        self.icono = icono
        self.texto = texto
        self.destino = destino

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, (70, 40, 140), self.rect, border_radius=12)
        pygame.draw.rect(ventana, COLORES["dorado"], self.rect, 2, border_radius=12)

        ventana.blit(self.icono, (self.rect.x + 40, self.rect.y + 10))

        fuente = get_fuente(16, True)
        t = fuente.render(self.texto, True, COLORES["texto"])
        ventana.blit(t, (self.rect.centerx - t.get_width() // 2, self.rect.y + 85))

    def clicado(self, pos):
        return self.rect.collidepoint(pos)


def cargar_icono(ruta, color):
    try:
        img = pygame.image.load(ruta).convert_alpha()
        img = pygame.transform.smoothscale(img, (70, 70))
    except:
        img = pygame.Surface((70, 70), pygame.SRCALPHA)
        img.fill(color)
    return img


# ---------------------------------------------------------
# CARGA DE MÚSICA DE INICIO
# ---------------------------------------------------------
def cargar_sonido_inicio():
    ruta = os.path.join("assets", "sonidos", "inicio.mp3")
    if os.path.exists(ruta):
        try:
            pygame.mixer.music.load(ruta)
            pygame.mixer.music.set_volume(0.6)
            pygame.mixer.music.play(-1)
        except:
            print("Error al reproducir inicio.mp3")
    else:
        print("inicio.mp3 no encontrado en assets/sonidos/")


def menu_inicio(VENTANA, estado):

    # Reproducir música del menú
    cargar_sonido_inicio()

    # Fondo
    try:
        fondo = pygame.image.load("assets/img/fondo_menu.png").convert()
        fondo = pygame.transform.smoothscale(fondo, VENTANA.get_size())
    except:
        fondo = None

    iconos = {
        "titulares": cargar_icono("assets/img/icono_titulares.png", (0, 200, 150)),
        "secretaria": cargar_icono("assets/img/icono_secretaria.png", (150, 100, 200)),
        "tesoreria": cargar_icono("assets/img/icono_tesoreria.png", (200, 180, 0)),
        "bandas": cargar_icono("assets/img/icono_bandas.png", (0, 120, 220)),
        "habito": cargar_icono("assets/img/icono_habito.png", (150, 0, 200)),
        "talleres": cargar_icono("assets/img/icono_talleres.png", (200, 80, 80)),
        "enseres": cargar_icono("assets/img/icono_enseres.png", (200, 120, 200)),
        "procesion": cargar_icono("assets/img/icono_procesion.png", (200, 120, 0)),
        "ayuda": cargar_icono("assets/img/icono_ayuda.png", (120, 120, 120)),
        "ajustes": cargar_icono("assets/img/icono_ajustes.png", (120, 120, 120)),
    }

    botones = [
        BotonLateral(20, 120, iconos["titulares"], "Titulares", "titulares"),
        BotonLateral(20, 250, iconos["secretaria"], "Secretaría", "secretaria"),
        BotonLateral(20, 380, iconos["tesoreria"], "Tesorería", "economia"),

        BotonLateral(200, 120, iconos["bandas"], "Bandas", "bandas"),
        BotonLateral(200, 250, iconos["habito"], "Hábito", "habito"),
        BotonLateral(200, 380, iconos["talleres"], "Talleres", "talleres"),

        BotonLateral(380, 120, iconos["enseres"], "Enseres", "enseres"),
        BotonLateral(380, 250, iconos["procesion"], "Procesión", "procesion"),
        BotonLateral(380, 380, iconos["ayuda"], "Ayuda/Ajustes", "ayuda_ajustes"),
    ]

    while True:
        if fondo:
            VENTANA.blit(fondo, (0, 0))
        else:
            VENTANA.fill(COLORES["fondo"])

        fuente = get_fuente(30, True)
        t = fuente.render("MENÚ PRINCIPAL", True, COLORES["dorado"])
        VENTANA.blit(t, (VENTANA.get_width() // 2 - t.get_width() // 2, 40))

        for b in botones:
            b.dibujar(VENTANA)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for b in botones:
                    if b.clicado(pos):
                        pygame.mixer.music.stop()
                        return b.destino

        pygame.display.update()
