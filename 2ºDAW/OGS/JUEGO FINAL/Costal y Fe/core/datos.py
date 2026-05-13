def crear_estado_inicial():
    return {
        "modo_oscuro": False,
        "sonido": True,

        # Secretaría
        "hermandad": {
            "nombre": "Hermandad del Buen Paso",
            "fundacion": "1950",
            "hermanos": 120,
            "puntos": 0,
            "cultos_mes": 3,
            "semana_santa": "Domingo de Ramos",
            "templo": "Parroquia de San Pedro",
            "dia_nacimiento": "01/01/1950",
            "escudo": {
                "corona": "Real",
                "izquierda": "Cruz",
                "derecha": "Ancla",
                "centro": "Corazón"
            },
            "titulo": "Real",
            "dia_salida": "Jueves Santo",
        },

        # Tesorería
        "economia": {
            "presupuesto": 5000,
            "ingreso_mensual": 800,
            "cuota_mensual": 10,
        },

        # Hábito
        "habito": {
            "tunica": "Morada",
            "cinturon": "Dorado",
            "antifaz": "Negro",
            "guantes": "Blancos",
            "sandalias": "Negras",
            "accesorios": "Escapulario bordado",
        },

        # Bandas
        "bandas": [],

        # Titulares
        "titular": {
            "nombre": "Ntro. Padre Jesús del Buen Paso",
            "autor": "Autor Desconocido",
            "anio": 1950,
            "restauraciones": "Restaurado en 1980 y 2005",
            "hermandad": "Hermandad del Buen Paso",
        },
    }
