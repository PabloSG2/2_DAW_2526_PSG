import pygame
import random

FUENTE = pygame.font.SysFont("arial", 20, bold=True)
COLOR_PANEL = (35, 20, 70)
COLOR_TEXTO = (255, 255, 255)
COLOR_DORADO = (255, 215, 0)

NOMBRES = [
    "Antonio", "Manuel", "José", "Francisco", "Juan", "David", "Javier",
    "Miguel", "Rafael", "Carlos", "Alejandro", "Pablo", "Luis",
    "María", "Carmen", "Ana", "Laura", "Lucía", "Rocío", "Sara"
]

APELLIDOS = [
    "García", "Fernández", "López", "Martínez", "Sánchez", "Pérez",
    "Gómez", "Ruiz", "Díaz", "Moreno", "Muñoz", "Álvarez", "Romero",
    "Navarro", "Torres", "Domínguez", "Vargas", "Castro"
]

CARGOS = ["Nazareno", "Costalero", "Músico", "Acólito", "Hermano de luz"]

def generar_hermano():
    nombre = random.choice(NOMBRES)
    apellido = random.choice(APELLIDOS)
    edad = random.randint(12, 75)
    antiguedad = random.randint(0, 40)
    cuota = random.choice([30, 40, 50])
    cargo = random.choice(CARGOS)
    devocion = random.randint(40, 100)
    return {
        "nombre": f"{nombre} {apellido}",
        "edad": edad,
        "antiguedad": antiguedad,
        "cuota": cuota,
        "cargo": cargo,
        "devocion": devocion,
        "activo": True
    }

def añadir_hermano(data):
    h = generar_hermano()
    data["hermanos"].append(h)

def calcular_ingresos_cuotas(data):
    return sum(h["cuota"] for h in data["hermanos"] if h["activo"])

def dibujar_hermanos(VENTANA, raton_pos, data, botones, theme):
    hermanos = data["hermanos"]

    panel = pygame.Rect(60, 80, 780, 440)
    pygame.draw.rect(VENTANA, theme["panel"], panel, border_radius=20)

    x = panel.x + 20
    y = panel.y + 20

    titulo = FUENTE.render("HERMANOS", True, COLOR_DORADO)
    VENTANA.blit(titulo, (x, y))

    y += 30

    resumen = [
        f"Total hermanos: {len(hermanos)}",
        f"Ingresos por cuotas: {calcular_ingresos_cuotas(data)} € / año",
        "",
        "Teclas:",
        "- H: Añadir hermano aleatorio",
        "- B: Dar de baja al último hermano",
    ]

    for txt in resumen:
        t = FUENTE.render(txt, True, theme["texto"])
        VENTANA.blit(t, (x, y))
        y += 24

    y += 10
    t = FUENTE.render("Listado (máx. 10 últimos):", True, COLOR_DORADO)
    VENTANA.blit(t, (x, y))
    y += 26

    for h in hermanos[-10:]:
        estado = "Activo" if h["activo"] else "Baja"
        txt = FUENTE.render(
            f"{h['nombre']} | {h['edad']} años | {h['cargo']} | {h['cuota']}€ | {estado}",
            True, theme["texto"]
        )
        VENTANA.blit(txt, (x, y))
        y += 22

    for b in botones:
        b.dibujar(VENTANA, raton_pos)

def baja_ultimo_hermano(data):
    if data["hermanos"]:
        data["hermanos"][-1]["activo"] = False
