import pygame
import os
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from config import COLORES

# -------------------------
# Cargar marchas desde carpeta
# -------------------------
def cargar_marchas():
    ruta = "assets/marchas"
    marchas = []

    if not os.path.exists(ruta):
        return ["(No hay marchas)"]

    for archivo in os.listdir(ruta):
        if archivo.lower().endswith((".mp3", ".wav", ".ogg")):
            marchas.append(archivo)

    return marchas if marchas else ["(No hay marchas)"]


def menu_procesion(VENTANA, estado):
    clock = pygame.time.Clock()

    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    # Botones de tipo de paso
    boton_cristo = BotonSimple((160, 220, 220, 55), "Cristo")
    boton_palio = BotonSimple((520, 220, 220, 55), "Palio")

    # Botones de modo
    boton_libre = BotonSimple((220, 460, 220, 55), "Modo libre")
    boton_mapa = BotonSimple((480, 460, 220, 55), "Modo procesión")

    tipo_seleccionado = estado.get("tipo_paso", "cristo")

    # Cargar marchas
    marchas = cargar_marchas()
    estado.setdefault("marchas", marchas)
    marcha_actual = estado.get("marcha_actual", marchas[0])

    # Desplegable de marchas
    dd_marchas = Desplegable((120, 360, 300, 45), marchas, marcha_actual)

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])

        dibujar_titulo(VENTANA, "LA IGUALÁ — PROCESIÓN", y=40)
        panel = pygame.Rect(80, 140, 740, 440)
        dibujar_panel(VENTANA, panel)

        # Títulos
        dibujar_texto(VENTANA, "Selecciona tipo de paso:", 120, 180, tamaño=22, negrita=True)
        dibujar_texto(VENTANA, "Marcha seleccionada:", 120, 320, tamaño=22, negrita=True)
        dibujar_texto(VENTANA, "Selecciona modo:", 120, 420, tamaño=22, negrita=True)

        # Fondo de selección
        if tipo_seleccionado == "cristo":
            pygame.draw.rect(VENTANA, (150, 110, 220), (150, 210, 240, 75), border_radius=15)
        else:
            pygame.draw.rect(VENTANA, (150, 110, 220), (510, 210, 240, 75), border_radius=15)

        # Botones
        for b in [boton_cristo, boton_palio, boton_libre, boton_mapa, boton_volver]:
            b.dibujar(VENTANA)

        # Desplegable de marchas (encima de todo)
        dd_marchas.dibujar(VENTANA)

        pos = pygame.mouse.get_pos()

        # Hover manual
        for b in [boton_cristo, boton_palio, boton_libre, boton_mapa, boton_volver]:
            if b.rect.collidepoint(pos):
                pygame.draw.rect(VENTANA, COLORES["dorado"], b.rect, 3, border_radius=8)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.clicado(pos):
                    return "diputado_mayor"

                if boton_cristo.clicado(pos):
                    tipo_seleccionado = "cristo"
                    estado["tipo_paso"] = "cristo"

                if boton_palio.clicado(pos):
                    tipo_seleccionado = "palio"
                    estado["tipo_paso"] = "palio"

                nueva_marcha = dd_marchas.click(pos)
                if nueva_marcha:
                    estado["marcha_actual"] = nueva_marcha

                if boton_libre.clicado(pos):
                    return "procesion_libre"

                if boton_mapa.clicado(pos):
                    return "procesion_mapa"

        pygame.display.update()
