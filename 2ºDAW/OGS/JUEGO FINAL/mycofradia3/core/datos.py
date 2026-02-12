def crear_estado_inicial():
    return {
        "hermandad": "Hermandad del Buen Paso",
        "ciudad": "Marchena (Sevilla)",
        "dia_salida": "Domingo de Ramos",
        "hermanos": [
            {"nombre": "Hermano 1", "moral": 70},
            {"nombre": "Hermano 2", "moral": 80},
            {"nombre": "Hermano 3", "moral": 60},
        ],
        "saldo": 12000,
        "gastos_anuales": 8000,

        # Procesión (todo lo que se guarda desde procesion_menu.py)
        "procesion": {
            "itinerario": [],
            "cortejo": {},
            "meteo": "Sin generar",
            "horarios": {
                "salida": "",
                "entrada": "",
                "duracion": ""
            },
            "papeleta": {
                "nombre": "",
                "numero": "",
                "donativo": ""
            }
        },

        # Ajustes
        "modo_oscuro": True,
        "sonido": True,
    }


def calcular_ingresos_cuotas(estado):
    return len(estado["hermanos"]) * 60
