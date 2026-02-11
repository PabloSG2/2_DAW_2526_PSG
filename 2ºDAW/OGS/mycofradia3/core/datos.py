import random

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

def generar_hermano():
    nombre = random.choice(NOMBRES) + " " + random.choice(APELLIDOS)
    edad = random.randint(12, 80)
    antiguedad = random.randint(0, 50)
    cuota = random.choice([30, 40, 50, 60])
    devocion = random.randint(40, 100)
    moral = random.randint(40, 100)

    return {
        "nombre": nombre,
        "edad": edad,
        "antiguedad": antiguedad,
        "cuota": cuota,
        "devocion": devocion,
        "moral": moral,
        "activo": True,
    }

def crear_estado_inicial():
    hermanos = [generar_hermano() for _ in range(25)]
    estado = {
        "hermanos": hermanos,
        "saldo": 5000,
        "ingresos_anuales": 0,
        "gastos_anuales": 0,
        "ensayos_realizados": 0,
        "sincronizacion": 50,
        "riesgo_lesion": 30,
        "fatiga": 20,
        "modo_oscuro": True,
        "sonido": True,
        "tipo_paso": "cristo",
    }
    return estado

def calcular_ingresos_cuotas(estado):
    return sum(h["cuota"] for h in estado["hermanos"] if h["activo"])
