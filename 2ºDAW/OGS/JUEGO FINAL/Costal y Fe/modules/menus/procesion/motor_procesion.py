import pygame
from config import COLORES
from assets.mapas.procesion_mapa import generar_mapa_procesion
from modules.menus.procesion.animaciones import AnimacionesPaso
from modules.menus.procesion.hud_controles import HUDControles

# SPRITES CENITALES
from modules.sprites.paso_sentencia import PasoSentencia as PasoCristo
from modules.sprites.paso_macarena import PasoMacarena as PasoVirgen
from modules.sprites.mod_habito import HabitoNazareno


def procesion_modo(VENTANA, estado):
    clock = pygame.time.Clock()

    tipo = estado.get("tipo_paso", "cristo")
    hud = HUDControles(tipo)
    anim = AnimacionesPaso(tipo)

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
        print("ERROR cargando marcha en procesión:", marcha, e)

    # -------------------------
    # MAPA
    # -------------------------
    mapa, meta_rect, calles = generar_mapa_procesion()
    mapa_w, mapa_h = mapa.get_size()

    # -------------------------
    # SPRITE DEL PASO (CENITAL)
    # -------------------------
    paso_sprite = PasoCristo() if tipo == "cristo" else PasoVirgen()

    # -------------------------
    # NAZARENO
    # -------------------------
    nazareno = HabitoNazareno(
        estado.get("color_tunica", "Rojo"),
        estado.get("color_capirote", "Rojo"),
        estado.get("color_cingulo", "Dorado")
    )

    # Posición inicial
    x, y = 150, 600
    velocidad = 3.2

    fuente = pygame.font.SysFont("Segoe UI", 28, True)
    fuente_grande = pygame.font.SysFont("Segoe UI", 48, True)

    vw, vh = VENTANA.get_size()

    # Cronómetro
    tiempo_inicio = pygame.time.get_ticks()
    terminado = False
    mostrar_resultado = False
    resultado_textos = []

    pausa = False

    while True:
        clock.tick(60)
        anim.actualizar()

        # -------------------------
        # EVENTOS
        # -------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:

                # Salir durante la procesión (antes de terminar)
                if event.key == pygame.K_ESCAPE and not mostrar_resultado:
                    pygame.mixer.music.stop()
                    return "procesion"

                # Salir DESPUÉS de terminar (pantalla final)
                if event.key == pygame.K_ESCAPE and mostrar_resultado:
                    pygame.mixer.music.stop()
                    return "menu_procesion"

                if event.key == pygame.K_SPACE and not mostrar_resultado:
                    pausa = not pausa

            if event.type == pygame.MOUSEBUTTONDOWN and not mostrar_resultado:
                accion = hud.click(event.pos)
                if accion == "pausa":
                    pausa = not pausa

                # Controles especiales
                if not pausa:
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

        if pausa and not mostrar_resultado:
            _dibujar_escena(
                VENTANA, mapa, mapa_w, mapa_h, x, y, vw, vh,
                hud, anim, tipo, fuente, tiempo_inicio, terminado,
                paso_sprite, nazareno
            )
            pygame.display.update()
            continue

        # -------------------------
        # MOVIMIENTO MANUAL
        # -------------------------
        if not terminado and not mostrar_resultado:
            viejo_x, viejo_y = x, y

            keys = pygame.key.get_pressed()
            dx = dy = 0

            if keys[pygame.K_LEFT]:  dx -= velocidad
            if keys[pygame.K_RIGHT]: dx += velocidad
            if keys[pygame.K_UP]:    dy -= velocidad
            if keys[pygame.K_DOWN]:  dy += velocidad

            if dx != 0 and dy != 0:
                dx *= 0.75
                dy *= 0.75

            x += dx
            y += dy

            # -------------------------
            # COLISIONES
            # -------------------------
            paso_rect = pygame.Rect(x - 40, y - 20, 80, 40)

            if not any(paso_rect.colliderect(c) for c in calles):
                x = viejo_x
                y = viejo_y

            # -------------------------
            # META
            # -------------------------
            if paso_rect.colliderect(meta_rect):
                terminado = True
                tiempo_total_ms = pygame.time.get_ticks() - tiempo_inicio
                tiempo_total = tiempo_total_ms / 1000

                tiempo_obj = estado.get("horarios", {}).get("procesion", {}).get("duracion", 300)

                dinero = estado.get("dinero", 0)
                if tiempo_total <= tiempo_obj:
                    recompensa = 500
                    dinero += recompensa
                    resultado = "HAS CUMPLIDO EL HORARIO"
                    detalle = f"Recompensa: +{recompensa}€"
                else:
                    penalizacion = 300
                    dinero -= penalizacion
                    resultado = "HAS LLEGADO CON RETRASO"
                    detalle = f"Penalización: -{penalizacion}€"

                estado["dinero"] = dinero

                mins_tot = int(tiempo_total // 60)
                segs_tot = int(tiempo_total % 60)
                mins_obj = int(tiempo_obj // 60)
                segs_obj = int(tiempo_obj % 60)

                resultado_textos = [
                    "GRAN PROCESIÓN — HAS FINALIZADO",
                    f"Tiempo total: {mins_tot:02d}:{segs_tot:02d}",
                    f"Tiempo objetivo: {mins_obj:02d}:{segs_obj:02d}",
                    resultado,
                    detalle,
                    "Pulsa ESC para volver"
                ]
                mostrar_resultado = True

        # -------------------------
        # DIBUJAR ESCENA
        # -------------------------
        _dibujar_escena(
            VENTANA, mapa, mapa_w, mapa_h, x, y, vw, vh,
            hud, anim, tipo, fuente, tiempo_inicio, terminado,
            paso_sprite, nazareno
        )

        if mostrar_resultado:
            _dibujar_resultado(VENTANA, resultado_textos, fuente_grande, fuente)

        pygame.display.update()


def _dibujar_escena(VENTANA, mapa, mapa_w, mapa_h, x, y, vw, vh,
                    hud, anim, tipo, fuente, tiempo_inicio, terminado,
                    paso_sprite, nazareno):

    cam_x = x - vw // 2
    cam_y = y - vh // 2
    cam_x = max(0, min(cam_x, mapa_w - vw))
    cam_y = max(0, min(cam_y, mapa_h - vh))

    VENTANA.blit(mapa, (0, 0), pygame.Rect(cam_x, cam_y, vw, vh))

    # Animaciones
    paso_x = x + anim.costero_val
    paso_y = y + anim.mecia_val + anim.vibracion_val

    # 🔥 DIBUJAR PASO CENITAL
    paso_sprite.dibujar_topdown(VENTANA, paso_x, paso_y, cam_x, cam_y)

    # NAZARENO
    nazareno.dibujar_topdown(VENTANA, paso_x - 80, paso_y + 40, cam_x, cam_y)

    hud.dibujar(VENTANA)

    VENTANA.blit(
        fuente.render(f"MODO PROCESIÓN — {tipo.upper()}", True, COLORES["texto"]),
        (20, 20)
    )

    if not terminado:
        ahora = pygame.time.get_ticks()
        t = (ahora - tiempo_inicio) / 1000
        mins = int(t // 60)
        segs = int(t % 60)
        txt_tiempo = fuente.render(f"Tiempo: {mins:02d}:{segs:02d}", True, COLORES["texto"])
        VENTANA.blit(txt_tiempo, (20, 60))


def _dibujar_resultado(VENTANA, lineas, fuente_grande, fuente):
    ancho, alto = VENTANA.get_size()
    overlay = pygame.Surface((ancho, alto), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 180))
    VENTANA.blit(overlay, (0, 0))

    y = alto // 2 - 140
    for i, linea in enumerate(lineas):
        if i == 0:
            surf = fuente_grande.render(linea, True, (255, 255, 255))
        else:
            surf = fuente.render(linea, True, (230, 230, 230))
        rect = surf.get_rect(center=(ancho // 2, y))
        VENTANA.blit(surf, rect)
        y += 50


def procesion_mapa(VENTANA, estado):
    return procesion_modo(VENTANA, estado)
