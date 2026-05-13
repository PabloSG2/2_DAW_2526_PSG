import pygame
from config import COLORES
from modules.menus.procesion.hud_controles import HUDControles
from modules.menus.procesion.animaciones import AnimacionesPaso
from assets.mapas.mapa_laiiguala import generar_mapa_laiiguala

# SPRITES CENITALES
from modules.sprites.paso_sentencia import PasoSentencia as PasoCristo
from modules.sprites.paso_macarena import PasoMacarena as PasoVirgen
from modules.sprites.mod_habito import HabitoNazareno


def procesion_libre(VENTANA, estado):
    clock = pygame.time.Clock()

    # Tipo de paso
    tipo = estado.get("tipo_paso", "cristo")

    # HUD + Animaciones
    hud = HUDControles(tipo)
    anim = AnimacionesPaso(tipo)

    pausa = False

    # -------------------------
    # REPRODUCIR MARCHA
    # -------------------------
    marcha = estado.get("marcha_actual", None)

    try:
        if marcha:
            pygame.mixer.music.load(f"assets/marchas/{marcha}")
            pygame.mixer.music.set_volume(1.0)
            pygame.mixer.music.play(-1)
    except Exception as e:
        print("ERROR cargando marcha:", marcha, e)

    # -------------------------
    # MAPA
    # -------------------------
    mapa, meta_rect, calles = generar_mapa_laiiguala()
    mapa_w, mapa_h = mapa.get_size()

    # -------------------------
    # SPRITE DEL PASO (CENITAL)
    # -------------------------
    paso_sprite = PasoCristo() if tipo == "cristo" else PasoVirgen()

    # -------------------------
    # NAZARENO (cenital)
    # -------------------------
    nazareno = HabitoNazareno(
        estado.get("color_tunica", "Rojo"),
        estado.get("color_capirote", "Rojo"),
        estado.get("color_cingulo", "Dorado")
    )

    # -------------------------
    # POSICIÓN INICIAL
    # -------------------------
    x, y = 300, 600
    velocidad = 4

    fuente = pygame.font.SysFont("Segoe UI", 28, True)
    vw, vh = VENTANA.get_size()

    while True:
        clock.tick(60)
        anim.actualizar()

        # -------------------------
        # CÁMARA
        # -------------------------
        cam_x = x - vw // 2
        cam_y = y - vh // 2

        cam_x = max(0, min(cam_x, mapa_w - vw))
        cam_y = max(0, min(cam_y, mapa_h - vh))

        # Fondo
        VENTANA.blit(mapa, (0, 0), pygame.Rect(cam_x, cam_y, vw, vh))

        # HUD
        hud.dibujar(VENTANA)

        # Título
        VENTANA.blit(
            fuente.render(f"MODO LIBRE — {tipo.upper()}", True, COLORES["texto"]),
            (20, 20)
        )

        # -------------------------
        # POSICIÓN DEL PASO + ANIMACIONES
        # -------------------------
        paso_x = x + anim.costero_val
        paso_y = y + anim.mecia_val + anim.vibracion_val

        # 🔥 DIBUJAR PASO CENITAL
        paso_sprite.dibujar_topdown(VENTANA, paso_x, paso_y, cam_x, cam_y)

        # DIBUJAR NAZARENO (cenital)
        nazareno.dibujar_topdown(VENTANA, paso_x - 80, paso_y + 40, cam_x, cam_y)

        pos = pygame.mouse.get_pos()

        # -------------------------
        # EVENTOS
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                accion = hud.click(pos)

                if accion == "pausa":
                    pausa = not pausa

                if pausa:
                    continue

                # Controles especiales
                if tipo == "cristo":
                    if accion == "picaito": anim.set_picaito(True)
                    if accion == "mas": anim.set_mecia(True)
                    if accion == "menos": anim.set_mecia(False)
                    if accion == "costero": anim.set_costero(True)
                else:
                    if accion == "mas": anim.set_mecia(True)
                    if accion == "menos": anim.set_mecia(False)
                    if accion == "cintura": anim.set_cintura(True)

            if event.type == pygame.MOUSEBUTTONUP:
                anim.set_picaito(False)
                anim.set_costero(False)
                anim.set_cintura(False)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.mixer.music.stop()
                    return "procesion"
                if event.key == pygame.K_SPACE:
                    pausa = not pausa

        if pausa:
            pygame.display.update()
            continue

        # -------------------------
        # MOVIMIENTO EN 8 DIRECCIONES
        # -------------------------
        viejo_x, viejo_y = x, y

        keys = pygame.key.get_pressed()

        dx = 0
        dy = 0

        if keys[pygame.K_LEFT]:  dx -= velocidad
        if keys[pygame.K_RIGHT]: dx += velocidad
        if keys[pygame.K_UP]:    dy -= velocidad
        if keys[pygame.K_DOWN]:  dy += velocidad

        # Normalizar diagonales
        if dx != 0 and dy != 0:
            dx *= 0.75
            dy *= 0.75

        x += dx
        y += dy

        # -------------------------
        # COLISIONES SUAVES
        # -------------------------
        nuevo_rect = pygame.Rect(x - 40, y - 20, 80, 40)

        if not any(nuevo_rect.colliderect(c) for c in calles):
            x = viejo_x
            y = viejo_y

        # -------------------------
        # META
        # -------------------------
        if nuevo_rect.colliderect(meta_rect):
            pygame.mixer.music.stop()
            return "procesion"

        pygame.display.update()
