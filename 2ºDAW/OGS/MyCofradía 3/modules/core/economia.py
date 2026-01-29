import json
import time
import os

SAVE_PATH = "data/save.json"

def cargar_partida():
    if not os.path.exists("data"):
        os.makedirs("data")

    if not os.path.exists(SAVE_PATH):
        return {
            "dinero": 5000,
            "last_bonus": time.time(),
            "hermandad": {
                "nombre": "Hermandad sin nombre",
                "escudo": "ninguno.png",
                "dia": 0,
                "pueblo": 0,
                "cristo": 0,
                "paso": 0,
                "palio": 0,
                "banda": 0,
                "habito": "Sin definir",
                "mayordomia": "Sin definir",
                "prestigio": 0,
                "permiso_obispo": False,
                "banda_propia": None,
                "contratos": [],
                "virgen_manto": 0,
                "virgen_corona": 0,
                "cristo_tunica": 0,
                "cristo_potencias": 0,
                "tunica_color": 0,
                "capa_color": 0,
                "cingulo_color": 0,
                "capirote_color": 0,
                "titulos": [],
                "historial_cabildo": [],
                "cultos": [],
                "ensayos": [],
                "traslados": []
            },
            "economia": {
                "ingresos": [],
                "gastos": [],
                "balance": 0
            },
            "hermanos": [],
            "logros": {},
            "ajustes": {
                "modo_oscuro": True,
                "volumen_general": 0.8,
                "volumen_sonidos": 0.8,
                "volumen_banda": 0.8,
                "animaciones": True,
                "sonidos": True
            }
        }
    with open(SAVE_PATH, "r") as f:
        data = json.load(f)

    # Asegurar campos nuevos si se carga una partida antigua
    if "hermanos" not in data:
        data["hermanos"] = []
    if "logros" not in data:
        data["logros"] = {}
    if "ajustes" not in data:
        data["ajustes"] = {
            "modo_oscuro": True,
            "volumen_general": 0.8,
            "volumen_sonidos": 0.8,
            "volumen_banda": 0.8,
            "animaciones": True,
            "sonidos": True
        }
    return data

def guardar_partida(data):
    with open(SAVE_PATH, "w") as f:
        json.dump(data, f, indent=4)

def actualizar_bonus(data):
    ahora = time.time()
    if ahora - data["last_bonus"] >= 7200:  # 2 horas
        data["dinero"] += 800
        data["last_bonus"] = ahora
