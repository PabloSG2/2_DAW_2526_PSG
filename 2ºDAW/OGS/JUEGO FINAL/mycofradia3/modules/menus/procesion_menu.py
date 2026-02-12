import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from config import COLORES
from modules.menus.procesion import menu_procesion_motor


def cargar_icono(ruta, tamaño=(40, 40), color=(120, 120, 120)):
    try:
        img = pygame.image.load(ruta).convert_alpha()
        img = pygame.transform.smoothscale(img, tamaño)
    except:
        img = pygame.Surface(tamaño, pygame.SRCALPHA)
        img.fill(color)
    return img


def dibujar_fondo(VENTANA):
    try:
        fondo = pygame.image.load("assets/img/fondo_procesion.png").convert()
        fondo = pygame.transform.smoothscale(fondo, VENTANA.get_size())
        VENTANA.blit(fondo, (0, 0))
    except:
        VENTANA.fill(COLORES["fondo"])


def guardar_itinerario(estado):
    estado["procesion"]["itinerario"] = [
        "Salida: Parroquia",
        "Calle A",
        "Plaza Mayor",
        "Calle B",
        "Entrada: Parroquia"
    ]


def guardar_cortejo(estado):
    estado["procesion"]["cortejo"] = {
        "Cruz de guía": 1,
        "Faroles": 2,
        "Tramo de cirios": 3,
        "Estandarte": 1,
        "Acólitos": 8,
        "Capataz": 1,
    }


def generar_meteo(estado):
    import random
    partes = [
        "Soleado, 22ºC, viento suave",
        "Nublado, 18ºC, sin lluvia",
        "Lluvia débil, 16ºC, riesgo moderado",
        "Lluvia intensa, 14ºC, riesgo alto",
        "Viento fuerte, 17ºC, precaución con cirios",
    ]
    estado["procesion"]["meteo"] = random.choice(partes)


def guardar_horarios(estado):
    estado["procesion"]["horarios"] = {
        "salida": "17:00",
        "entrada": "22:30",
        "duracion": "5h 30m"
    }


def guardar_papeleta(estado):
    estado["procesion"]["papeleta"] = {
        "nombre": "Hermano Ejemplo",
        "numero": "152",
        "donativo": "20€"
    }


def menu_procesion(VENTANA, estado):

    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    botones = [
        BotonSimple((110, 170, 240, 55), "Itinerario"),
        BotonSimple((110, 240, 240, 55), "Cortejo"),
        BotonSimple((110, 310, 240, 55), "Meteorología"),
        BotonSimple((110, 380, 240, 55), "Horarios"),
        BotonSimple((110, 450, 240, 55), "Papeletas"),
        BotonSimple((520, 450, 260, 55), "Iniciar procesión"),
    ]

    iconos = {
        "itinerario": cargar_icono("assets/img/icono_procesion.png"),
        "cortejo": cargar_icono("assets/img/icono_enseres.png"),
        "meteo": cargar_icono("assets/img/icono_ayuda.png"),
        "horarios": cargar_icono("assets/img/icono_secretaria.png"),
        "papeletas": cargar_icono("assets/img/icono_tesoreria.png"),
    }

    subpantalla = "itinerario"
    clock = pygame.time.Clock()

    while True:
        clock.tick(60)

        dibujar_fondo(VENTANA)
        dibujar_titulo(VENTANA, "PROCESIÓN", y=40)

        panel_izq = pygame.Rect(80, 120, 300, 420)
        panel_der = pygame.Rect(400, 120, 420, 420)
        dibujar_panel(VENTANA, panel_izq)
        dibujar_panel(VENTANA, panel_der)

        pos = pygame.mouse.get_pos()
        for b in botones:
            b.actualizar_hover(pos)
        boton_volver.actualizar_hover(pos)

        # Panel izquierdo: botones + iconos
        secciones = ["itinerario", "cortejo", "meteo", "horarios", "papeletas"]
        for i, b in enumerate(botones[:5]):
            b.dibujar(VENTANA)
            nombre = secciones[i]
            icono = iconos.get(nombre)
            if icono:
                VENTANA.blit(icono, (b.rect.x - 50, b.rect.y + 7))

        # Botón iniciar
        botones[5].dibujar(VENTANA)
        boton_volver.dibujar(VENTANA)

        # Panel derecho: contenido
        dibujar_texto(VENTANA, "Resumen de la sección:", 420, 135, tamaño=22, negrita=True)

        if subpantalla == "itinerario":
            dibujar_texto(VENTANA, "Itinerario guardado:", 420, 175, tamaño=20, negrita=True)
            for i, calle in enumerate(estado["procesion"]["itinerario"]):
                dibujar_texto(VENTANA, f"• {calle}", 430, 210 + i * 25)

        elif subpantalla == "cortejo":
            dibujar_texto(VENTANA, "Cortejo:", 420, 175, tamaño=20, negrita=True)
            for i, (k, v) in enumerate(estado["procesion"]["cortejo"].items()):
                dibujar_texto(VENTANA, f"{k}: {v}", 430, 210 + i * 25)

        elif subpantalla == "meteo":
            dibujar_texto(VENTANA, "Parte meteorológico:", 420, 175, tamaño=20, negrita=True)
            dibujar_texto(VENTANA, estado["procesion"]["meteo"], 430, 210, tamaño=18)

        elif subpantalla == "horarios":
            h = estado["procesion"]["horarios"]
            dibujar_texto(VENTANA, "Horarios:", 420, 175, tamaño=20, negrita=True)
            dibujar_texto(VENTANA, f"Salida:  {h['salida']}", 430, 210, tamaño=18)
            dibujar_texto(VENTANA, f"Entrada: {h['entrada']}", 430, 240, tamaño=18)
            dibujar_texto(VENTANA, f"Duración: {h['duracion']}", 430, 270, tamaño=18)

        elif subpantalla == "papeletas":
            p = estado["procesion"]["papeleta"]
            dibujar_texto(VENTANA, "Última papeleta generada:", 420, 175, tamaño=20, negrita=True)
            dibujar_texto(VENTANA, f"Nombre:   {p['nombre']}", 430, 210, tamaño=18)
            dibujar_texto(VENTANA, f"Número:   {p['numero']}", 430, 240, tamaño=18)
            dibujar_texto(VENTANA, f"Donativo: {p['donativo']}", 430, 270, tamaño=18)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "inicio"

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos

                if boton_volver.clicado(pos):
                    return "inicio"

                if botones[0].clicado(pos):
                    subpantalla = "itinerario"
                    guardar_itinerario(estado)

                if botones[1].clicado(pos):
                    subpantalla = "cortejo"
                    guardar_cortejo(estado)

                if botones[2].clicado(pos):
                    subpantalla = "meteo"
                    generar_meteo(estado)

                if botones[3].clicado(pos):
                    subpantalla = "horarios"
                    guardar_horarios(estado)

                if botones[4].clicado(pos):
                    subpantalla = "papeletas"
                    guardar_papeleta(estado)

                if botones[5].clicado(pos):
                    menu_procesion_motor(VENTANA, estado)

        pygame.display.update()
