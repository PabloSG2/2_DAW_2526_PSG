import pygame
from core.botones import BotonSimple
from core.ui import dibujar_titulo, dibujar_panel, dibujar_texto
from modules.desplegables import Desplegable
from assets.mapas.mapa_laiiguala import generar_mapa_laiiguala
from config import COLORES

def menu_diputado_mayor(VENTANA, estado):
    clock = pygame.time.Clock()
    boton_volver = BotonSimple((20, 20, 150, 45), "Volver")

    opciones = ["Itinerario", "Cortejo", "Meteorología", "Horarios", "Papeletas", "Procesión"]
    dd_opciones = Desplegable((420, 200, 260, 45), opciones, opciones[0])
    subpantalla = opciones[0]

    # Preview del mapa
    mapa_preview, _, _ = generar_mapa_laiiguala()
    mapa_preview = pygame.transform.scale(mapa_preview, (350, 250))

    estado.setdefault("horarios", {})
    estado["horarios"].setdefault("procesion", {"duracion": 300})

    while True:
        clock.tick(60)
        VENTANA.fill(COLORES["fondo"])

        dibujar_titulo(VENTANA, "DIPUTADO MAYOR", y=40)
        panel = pygame.Rect(80, 120, 740, 420)
        dibujar_panel(VENTANA, panel)

        dibujar_texto(VENTANA, "Seleccionar sección:", 120, 210, tamaño=22)
        boton_volver.actualizar_hover(pygame.mouse.get_pos())
        boton_volver.dibujar(VENTANA)

        dibujar_texto(VENTANA, f"{subpantalla}:", 420, 260, tamaño=24, negrita=True)

        # Subpantallas
        if subpantalla == "Itinerario":
            VENTANA.blit(mapa_preview, (420, 300))

        elif subpantalla == "Cortejo":
            lista = ["Nazarenos", "Insignias", "Tramos"]
            for i, item in enumerate(lista):
                dibujar_texto(VENTANA, f"• {item}", 430, 300 + i * 30)

        elif subpantalla == "Meteorología":
            dibujar_texto(VENTANA, "• Cielo: Despejado", 430, 300)
            dibujar_texto(VENTANA, "• Temperatura: 18ºC", 430, 330)

        elif subpantalla == "Horarios":
            tiempo = estado["horarios"]["procesion"]["duracion"]
            minutos, segundos = divmod(tiempo, 60)
            dibujar_texto(VENTANA, "Tiempo máximo de procesión:", 430, 300)
            dibujar_texto(VENTANA, f"{minutos} min {segundos} seg", 430, 330)

        elif subpantalla == "Papeletas":
            dibujar_texto(VENTANA, "• Emitidas: 120", 430, 300)
            dibujar_texto(VENTANA, "• Pendientes: 15", 430, 330)

        elif subpantalla == "Procesión":
            dibujar_texto(VENTANA, "Abrir simulación / igualá", 420, 300)
            dibujar_texto(VENTANA, "→ Esto enlaza con menu_procesion()", 420, 330)

        # Desplegable al final (encima de todo)
        dd_opciones.dibujar(VENTANA)

        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if boton_volver.clicado(pygame.mouse.get_pos()):
                    return "inicio"

                nuevo = dd_opciones.click(pygame.mouse.get_pos())
                if nuevo:
                    if nuevo == "Procesión":
                        return "procesion"
                    subpantalla = nuevo

        pygame.display.update()
