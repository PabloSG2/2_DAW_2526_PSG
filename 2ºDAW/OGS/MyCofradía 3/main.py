import pygame
import sys
import math

# Importamos TODO desde modules/__init__.py
from modules import *

pygame.init()
pygame.mixer.init()

ANCHO, ALTO = 900, 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("MyCofradía 3")

FUENTE_GRANDE = pygame.font.SysFont("arial", 38, bold=True)
FUENTE = pygame.font.SysFont("arial", 22, bold=True)

THEME_DARK = {
    "fondo": (20, 10, 40),
    "panel": (35, 20, 70),
    "texto": (255, 255, 255),
    "barra": (25, 10, 50),
}
THEME_LIGHT = {
    "fondo": (230, 230, 240),
    "panel": (210, 210, 230),
    "texto": (10, 10, 30),
    "barra": (190, 190, 210),
}

COLOR_DORADO = (255, 215, 0)

ESTADO = "menu"

# Carga de imágenes y sonidos
PASO_IMG = cargar_imagen("data/images/pasos/paso.png", (260, 140))
ESCUDO_IMG = cargar_imagen("data/images/escudos/escudo.png", (80, 80))
FONDO_COF = cargar_imagen("data/images/fondos/cofradia.png", (ANCHO, ALTO))

SON_CLICK = cargar_sonido("data/sounds/click.wav")
SON_CULTO = cargar_sonido("data/sounds/culto.wav")
SON_DONATIVO = cargar_sonido("data/sounds/donativo.wav")
SON_PERMISO = cargar_sonido("data/sounds/permiso.wav")


def reproducir(sonido, data):
    if sonido and data["ajustes"]["sonidos"]:
        sonido.set_volume(data["ajustes"]["volumen_sonidos"] * data["ajustes"]["volumen_general"])
        sonido.play()


def dibujar_menu(raton_pos, boton_jugar, boton_salir, theme):
    VENTANA.fill(theme["fondo"])
    titulo = FUENTE_GRANDE.render("MYCOFRADÍA 3", True, COLOR_DORADO)
    VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 140))
    boton_jugar.dibujar(VENTANA, raton_pos)
    boton_salir.dibujar(VENTANA, raton_pos)


def dibujar_cofradia(raton_pos, data, botones, theme):
    if FONDO_COF:
        VENTANA.blit(FONDO_COF, (0, 0))
    else:
        VENTANA.fill(theme["fondo"])

    pygame.draw.rect(VENTANA, theme["barra"], (0, 0, ANCHO, 70))
    titulo = FUENTE_GRANDE.render("TU COFRADÍA", True, COLOR_DORADO)
    VENTANA.blit(titulo, (30, 15))

    actualizar_bonus(data)
    generar_ingresos_banda(data)
    comprobar_logros(data)

    txt_monedas = FUENTE.render(f"Dinero: {data['dinero']} €", True, COLOR_DORADO)
    VENTANA.blit(txt_monedas, (ANCHO - txt_monedas.get_width() - 30, 20))

    herm = data["hermandad"]

    panel = pygame.Rect(80, 90, ANCHO - 160, 260)
    pygame.draw.rect(VENTANA, theme["panel"], panel, border_radius=20)

    if data["ajustes"]["animaciones"]:
        t = pygame.time.get_ticks() / 300.0
        offset = int(5 * math.sin(t))
    else:
        offset = 0

    paso_rect = pygame.Rect(panel.x + 40, panel.y + 60 + offset, 260, 140)
    if PASO_IMG:
        VENTANA.blit(PASO_IMG, (paso_rect.x, paso_rect.y))
    else:
        pygame.draw.rect(VENTANA, (180, 140, 40), paso_rect, border_radius=15)

    txt_paso = FUENTE.render("Paso de tu Cofradía", True, theme["texto"])
    VENTANA.blit(txt_paso, (paso_rect.centerx - txt_paso.get_width() // 2, paso_rect.y - 30))

    if ESCUDO_IMG:
        VENTANA.blit(ESCUDO_IMG, (panel.right - 120, panel.y + 20))

    x_stats = paso_rect.right + 40
    y_stats = panel.y + 30

    lineas = [
        f"Hermandad: {herm['nombre']}",
        f"Día de salida: {DIAS_SALIDA[herm['dia']]}",
        f"Pueblo: {PUEBLOS[herm['pueblo']]}",
        f"Cristo: {list(TIPOS_CRISTO.keys())[herm['cristo']]}",
        f"Paso: {list(TIPOS_PASO.keys())[herm['paso']]}",
        f"Palio: {list(TIPOS_PALIO.keys())[herm['palio']]}",
        f"Banda: {list(TIPOS_BANDA.keys())[herm['banda']]}",
        f"Prestigio: {herm['prestigio']}",
        f"Hermanos: {len(data['hermanos'])}",
    ]

    for i, txt in enumerate(lineas):
        t = FUENTE.render(txt, True, theme["texto"])
        VENTANA.blit(t, (x_stats, y_stats + i * 30))

    for b in botones:
        b.dibujar(VENTANA, raton_pos)


def main():
    global ESTADO
    reloj = pygame.time.Clock()
    data = cargar_partida()

    # Botones principales
    boton_jugar = Boton((ANCHO // 2 - 150, 280, 300, 60), "Entrar en la Cofradía")
    boton_salir = Boton((ANCHO // 2 - 150, 360, 300, 60), "Salir")

    # Botones de secciones
    boton_gestion = Boton((80, 380, 220, 40), "Gestión Hermandad")
    boton_iglesia = Boton((320, 380, 220, 40), "Iglesia / Obispo")
    boton_bandas = Boton((560, 380, 220, 40), "Bandas")
    boton_mayordomia = Boton((80, 430, 220, 40), "Mayordomía")
    boton_calendario = Boton((320, 430, 220, 40), "Calendario Cofrade")
    boton_habitos = Boton((560, 430, 220, 40), "Hábitos")
    boton_cabildos = Boton((80, 480, 220, 40), "Títulos y Cabildos")
    boton_cultos = Boton((320, 480, 220, 40), "Cultos / Ensayos")
    boton_economia = Boton((560, 480, 220, 40), "Economía")
    boton_semanasanta = Boton((80, 530, 220, 40), "Semana Santa")
    boton_ajustes = Boton((320, 530, 220, 40), "Ajustes")
    boton_logros = Boton((560, 530, 220, 40), "Logros")
    boton_hermanos = Boton((80, 340, 220, 40), "Hermanos")
    boton_procesion = Boton((560, 340, 220, 40), "Modo Procesión")
    boton_volver_menu = Boton((ANCHO - 180, 10, 160, 40), "Volver al menú")

    botones_cof = [
        boton_gestion, boton_iglesia, boton_bandas, boton_mayordomia,
        boton_calendario, boton_habitos, boton_cabildos, boton_cultos,
        boton_economia, boton_semanasanta, boton_ajustes, boton_logros,
        boton_hermanos, boton_procesion, boton_volver_menu
    ]

    boton_volver_simple = Boton((ANCHO - 180, 90, 160, 40), "Volver")

    estado_procesion = {
        "x_paso": 500,
        "avanzando": False,
        "mecida": False
    }

    while True:
        reloj.tick(60)
        raton_pos = pygame.mouse.get_pos()
        theme = THEME_DARK if data["ajustes"]["modo_oscuro"] else THEME_LIGHT

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                guardar_partida(data)
                pygame.quit()
                sys.exit()

            # CLIC
            if e.type == pygame.MOUSEBUTTONDOWN:
                reproducir(SON_CLICK, data)

                if ESTADO == "menu":
                    if boton_jugar.clicado(raton_pos):
                        ESTADO = "cofradia"
                    elif boton_salir.clicado(raton_pos):
                        guardar_partida(data)
                        pygame.quit()
                        sys.exit()

                elif ESTADO == "cofradia":
                    if boton_gestion.clicado(raton_pos):
                        ESTADO = "gestion"
                    elif boton_iglesia.clicado(raton_pos):
                        ESTADO = "iglesia"
                    elif boton_bandas.clicado(raton_pos):
                        ESTADO = "bandas"
                    elif boton_mayordomia.clicado(raton_pos):
                        ESTADO = "mayordomia"
                    elif boton_calendario.clicado(raton_pos):
                        ESTADO = "calendario"
                    elif boton_habitos.clicado(raton_pos):
                        ESTADO = "habitos"
                    elif boton_cabildos.clicado(raton_pos):
                        ESTADO = "cabildos"
                    elif boton_cultos.clicado(raton_pos):
                        ESTADO = "cultos"
                    elif boton_economia.clicado(raton_pos):
                        ESTADO = "economia"
                    elif boton_semanasanta.clicado(raton_pos):
                        ESTADO = "semanasanta"
                    elif boton_ajustes.clicado(raton_pos):
                        ESTADO = "ajustes"
                    elif boton_logros.clicado(raton_pos):
                        ESTADO = "logros"
                    elif boton_hermanos.clicado(raton_pos):
                        ESTADO = "hermanos"
                    elif boton_procesion.clicado(raton_pos):
                        ESTADO = "procesion"
                        reproducir_banda(data)
                    elif boton_volver_menu.clicado(raton_pos):
                        ESTADO = "menu"

                else:
                    if boton_volver_simple.clicado(raton_pos):
                        if ESTADO == "procesion":
                            parar_banda()
                        ESTADO = "cofradia"

            # TECLAS
            if e.type == pygame.KEYDOWN:
                h = data["hermandad"]

                if ESTADO == "ajustes":
                    if e.key == pygame.K_m:
                        data["ajustes"]["modo_oscuro"] = not data["ajustes"]["modo_oscuro"]
                    if e.key == pygame.K_a:
                        data["ajustes"]["animaciones"] = not data["ajustes"]["animaciones"]
                    if e.key == pygame.K_s:
                        data["ajustes"]["sonidos"] = not data["ajustes"]["sonidos"]
                    if e.key == pygame.K_r:
                        reiniciar_partida(data)

                if ESTADO == "gestion":
                    if e.key == pygame.K_LEFT:
                        h["dia"] = (h["dia"] - 1) % len(DIAS_SALIDA)
                    if e.key == pygame.K_RIGHT:
                        h["dia"] = (h["dia"] + 1) % len(DIAS_SALIDA)
                    if e.key == pygame.K_a:
                        h["pueblo"] = (h["pueblo"] - 1) % len(PUEBLOS)
                    if e.key == pygame.K_d:
                        h["pueblo"] = (h["pueblo"] + 1) % len(PUEBLOS)
                    if e.key == pygame.K_1:
                        h["cristo"] = (h["cristo"] - 1) % len(TIPOS_CRISTO)
                    if e.key == pygame.K_2:
                        h["cristo"] = (h["cristo"] + 1) % len(TIPOS_CRISTO)
                    if e.key == pygame.K_3:
                        h["paso"] = (h["paso"] - 1) % len(TIPOS_PASO)
                    if e.key == pygame.K_4:
                        h["paso"] = (h["paso"] + 1) % len(TIPOS_PASO)
                    if e.key == pygame.K_5:
                        h["palio"] = (h["palio"] - 1) % len(TIPOS_PALIO)
                    if e.key == pygame.K_6:
                        h["palio"] = (h["palio"] + 1) % len(TIPOS_PALIO)
                    if e.key == pygame.K_7:
                        h["banda"] = (h["banda"] - 1) % len(TIPOS_BANDA)
                    if e.key == pygame.K_8:
                        h["banda"] = (h["banda"] + 1) % len(TIPOS_BANDA)

                elif ESTADO == "iglesia":
                    if e.key == pygame.K_d:
                        donar(data)
                        reproducir(SON_DONATIVO, data)
                    if e.key == pygame.K_p:
                        res = pedir_permiso(data)
                        reproducir(SON_PERMISO if res else SON_CLICK, data)

                elif ESTADO == "bandas":
                    if e.key == pygame.K_b:
                        crear_banda(data)
                    if e.key == pygame.K_c:
                        contratar_banda(data)

                elif ESTADO == "habitos":
                    from modules.secciones.habitos import COLORES
                    if e.key == pygame.K_1:
                        h["tunica_color"] = (h["tunica_color"] - 1) % len(COLORES)
                    if e.key == pygame.K_2:
                        h["tunica_color"] = (h["tunica_color"] + 1) % len(COLORES)
                    if e.key == pygame.K_3:
                        h["capa_color"] = (h["capa_color"] - 1) % len(COLORES)
                    if e.key == pygame.K_4:
                        h["capa_color"] = (h["capa_color"] + 1) % len(COLORES)
                    if e.key == pygame.K_5:
                        h["cingulo_color"] = (h["cingulo_color"] - 1) % len(COLORES)
                    if e.key == pygame.K_6:
                        h["cingulo_color"] = (h["cingulo_color"] + 1) % len(COLORES)
                    if e.key == pygame.K_7:
                        h["capirote_color"] = (h["capirote_color"] - 1) % len(COLORES)
                    if e.key == pygame.K_8:
                        h["capirote_color"] = (h["capirote_color"] + 1) % len(COLORES)

                elif ESTADO == "cabildos":
                    if e.key == pygame.K_t:
                        añadir_titulo(data)
                    if e.key == pygame.K_n:
                        cambiar_nombre(data)
                    if e.key == pygame.K_c:
                        cambiar_dia(data)

                elif ESTADO == "cultos":
                    if e.key == pygame.K_c:
                        añadir_culto(data)
                        reproducir(SON_CULTO, data)
                    if e.key == pygame.K_e:
                        añadir_ensayo(data)
                    if e.key == pygame.K_t:
                        añadir_traslado(data)

                elif ESTADO == "economia":
                    if e.key == pygame.K_i:
                        añadir_ingreso(data)
                    if e.key == pygame.K_g:
                        añadir_gasto(data)

                elif ESTADO == "hermanos":
                    if e.key == pygame.K_h:
                        añadir_hermano(data)
                    if e.key == pygame.K_b:
                        baja_ultimo_hermano(data)

                elif ESTADO == "procesion":
                    if e.key == pygame.K_a:
                        estado_procesion["avanzando"] = True
                    if e.key == pygame.K_s:
                        estado_procesion["avanzando"] = False
                    if e.key == pygame.K_m:
                        estado_procesion["mecida"] = not estado_procesion["mecida"]
                    if e.key == pygame.K_p:
                        reproducir_aplausos(data)

        # DIBUJO DE PANTALLAS
        if ESTADO == "menu":
            dibujar_menu(raton_pos, boton_jugar, boton_salir, theme)
        elif ESTADO == "cofradia":
            dibujar_cofradia(raton_pos, data, botones_cof, theme)
        elif ESTADO == "gestion":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("GESTIÓN HERMANDAD", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_gestion(VENTANA, raton_pos, data, boton_volver_simple)
        elif ESTADO == "iglesia":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("IGLESIA / OBISPO", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_iglesia(VENTANA, raton_pos, data, [boton_volver_simple])
        elif ESTADO == "bandas":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("BANDAS", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_bandas(VENTANA, raton_pos, data, [boton_volver_simple])
        elif ESTADO == "mayordomia":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("MAYORDOMÍA", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_mayordomia(VENTANA, raton_pos, data, [boton_volver_simple])
        elif ESTADO == "calendario":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("CALENDARIO COFRADE", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_calendario(VENTANA, raton_pos, data, [boton_volver_simple])
        elif ESTADO == "habitos":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("HÁBITOS", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_habito(VENTANA, raton_pos, data, [boton_volver_simple])
        elif ESTADO == "cabildos":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("TÍTULOS Y CABILDO", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_cabildos(VENTANA, raton_pos, data, [boton_volver_simple])
        elif ESTADO == "cultos":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("CULTOS / ENSAYOS", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_cultos(VENTANA, raton_pos, data, [boton_volver_simple])
        elif ESTADO == "economia":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("ECONOMÍA", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_economia(VENTANA, raton_pos, data, [boton_volver_simple])
        elif ESTADO == "semanasanta":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("SEMANA SANTA", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_semanasanta(VENTANA, raton_pos, data, [boton_volver_simple])
        elif ESTADO == "ajustes":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("AJUSTES", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_ajustes(VENTANA, raton_pos, data, [boton_volver_simple], theme)
        elif ESTADO == "logros":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("LOGROS", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_logros(VENTANA, raton_pos, data, [boton_volver_simple], theme)
        elif ESTADO == "hermanos":
            VENTANA.fill(theme["fondo"])
            titulo = FUENTE_GRANDE.render("HERMANOS", True, COLOR_DORADO)
            VENTANA.blit(titulo, (ANCHO // 2 - titulo.get_width() // 2, 20))
            dibujar_hermanos(VENTANA, raton_pos, data, [boton_volver_simple], theme)
        elif ESTADO == "procesion":
            actualizar_procesion(estado_procesion)
            dibujar_procesion(VENTANA, raton_pos, data, [boton_volver_simple], theme, estado_procesion)

        pygame.display.flip()


if __name__ == "__main__":
    main()
