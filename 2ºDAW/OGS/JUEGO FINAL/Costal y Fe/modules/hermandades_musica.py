import tkinter as tk
import unicodedata

# ============================================================
#  FUNCIÓN NORMALIZAR
# ============================================================
def normalizar(txt):
    txt = txt.lower()
    txt = unicodedata.normalize("NFD", txt)
    txt = "".join(c for c in txt if unicodedata.category(c) != "Mn")
    return txt.strip()

# ============================================================
#  DATOS DEL MODO 2 — ACOMPAÑAMIENTOS MUSICALES
# ============================================================
acompanamientos = {
    # VIERNES DE DOLORES
    "Cristo de la Corona": {
        "dia": "Viernes de Dolores",
        "cristo": "Capilla Musical Lignum Crucis y Escolanía Salesiana",
        "palio": "Capilla Musical Sonos Angeli"
    },
    "Bellavista": {
        "dia": "Viernes de Dolores",
        "cristo": "AM Redención de Sevilla",
        "palio": "Banda Santa Ana (Dos Hermanas)"
    },
    "La Misión": {
        "dia": "Viernes de Dolores",
        "cristo": "CCyTT Cigarreras",
        "palio": "Columna y Azotes (Cigarreras)"
    },
    "Pino Montano": {
        "dia": "Viernes de Dolores",
        "cristo": "AM Encarnación",
        "palio": "Banda Municipal Puebla del Río"
    },
    "Pasión y Muerte": {
        "dia": "Viernes de Dolores",
        "cristo": "Capilla Gólgota",
    },
    "Bendición y Esperanza": {
        "dia": "Viernes de Dolores",
        "cristo": "AM Fraternitas",
        "palio": "CCyTT Jesús Nazareno"
    },
    "Paz y Misericordia": {
        "dia": "Viernes de Dolores",
        "cristo": "CCyTT Ntra. Sra. de los Ángeles",
    },
    "Caridad": {
        "dia": "Viernes de Dolores",
        "cristo": "",
        "palio": "Banda Santa María de las Nieves (Olivares)"
    },
    "Lágrimas (Pío XII)": {
        "dia": "Viernes de Dolores",
        "cristo": "AM Santa María de la Cabeza",
    },

    # SÁBADO DE PASIÓN
    "Torreblanca": {
        "dia": "Sábado de Pasión",
        "cristo": "AM Sentencia",
        "palio": "Banda Nieves (Olivares)"
    },
    "Divino Perdón": {
        "dia": "Sábado de Pasión",
        "cristo": "AM Encarnación",
        "palio": "Banda Santa Ana"
    },
    "Padre Pío": {
        "dia": "Sábado de Pasión",
        "cristo": "AM Lágrimas",
        "palio": "Banda Angustias"
    },
    "San José Obrero": {
        "dia": "Sábado de Pasión",
        "cristo": "AM Salud",
        "palio": "Banda Coria del Río"
    },
    "La Milagrosa": {
        "dia": "Sábado de Pasión",
        "cristo": "AM Virgen de los Reyes",
        "palio": "Banda Cigarreras"
    },
    "San Jerónimo": {
        "dia": "Sábado de Pasión",
        "cristo": "AM Nazareno (La Algaba)",
        "palio": "Banda Bollullos"
    },
    "Las Maravillas": {
        "dia": "Sábado de Pasión",
        "cristo": "CCyTT Sol",
    },
    "La Humildad": {
        "dia": "Sábado de Pasión",
        "cristo": "AM Redención",
    },
    "Desamparados": {
        "dia": "Sábado de Pasión",
        "cristo": "Banda Puebla del Río",
        "palio": "Carmen de Salteras"
    },

    # DOMINGO DE RAMOS
    "La Borriquita": {
        "dia": "Domingo de Ramos",
        "cristo": "CCyTT Sol",
    },
    "Jesús Despojado": {
        "dia": "Domingo de Ramos",
        "cristo": "AM Virgen de los Reyes",
        "palio": "Banda Liceo Moguer"
    },
    "La Hiniesta": {
        "dia": "Domingo de Ramos",
        "cristo": "AM Santa María Magdalena",
        "palio": "Banda Mairena"
    },
    "La Paz": {
        "dia": "Domingo de Ramos",
        "cristo": "AM Encarnación",
        "palio": "Banda Puebla del Río"
    },
    "La Cena": {
        "dia": "Domingo de Ramos",
        "cristo": "Cigarreras",
        "palio": "Maestro Tejera"
    },
    "San Roque": {
        "dia": "Domingo de Ramos",
        "cristo": "Nazareno Huelva",
        "palio": "Banda Cruz Roja"
    },
    "La Amargura": {
        "dia": "Domingo de Ramos",
        "cristo": "Tres Caídas",
        "palio": "Carmen de Salteras"
    },
    "La Estrella": {
        "dia": "Domingo de Ramos",
        "cristo": "Rosario Cádiz",
        "palio": "Oliva de Salteras"
    },
    "El Amor": {
        "dia": "Domingo de Ramos",
        "cristo": "",
        "palio": "Banda Cigarreras"
    },

    # LUNES SANTO
    "San Pablo": {
        "dia": "Lunes Santo",
        "cristo": "AM Santa María Magdalena / AM Virgen de los Reyes",
        "palio": "Nieves / Puebla del Río"
    },
    "La Redención": {
        "dia": "Lunes Santo",
        "cristo": "AM Redención",
        "palio": "Banda Cruz Roja"
    },
    "Santa Genoveva": {
        "dia": "Lunes Santo",
        "cristo": "AM Pasión Linares",
        "palio": "Carmen de Salteras"
    },
    "Santa Marta": {
        "dia": "Lunes Santo",
        "cristo": "Silencio",
    },
    "San Gonzalo": {
        "dia": "Lunes Santo",
        "cristo": "Cigarreras",
        "palio": "Banda Santa Ana"
    },
    "VeraCruz": {
        "dia": "Lunes Santo",
        "cristo": "Capilla musical",
        "palio": "Capilla musical"
    },
    "Las Penas": {
        "dia": "Lunes Santo",
        "cristo": "Capilla",
        "palio": "Maestro Tejera"
    },
    "Las Aguas": {
        "dia": "Lunes Santo",
        "cristo": "Rosario Cádiz",
        "palio": "Banda Mairena"
    },
    "El Museo": {
        "dia": "Lunes Santo",
        "cristo": "Silencio",
        "palio": "Oliva de Salteras"
    },

    # MARTES SANTO
    "El Cerro": {
        "dia": "Martes Santo",
        "cristo": "Ángeles / Nazareno Huelva / Centuria",
        "palio": "Nieves"
    },
    "San Benito": {
        "dia": "Martes Santo",
        "cristo": "Encarnación / Sangre",
        "palio": "Puebla del Río"
    },
    "El Dulce Nombre": {
        "dia": "Martes Santo",
        "cristo": "Cigarreras",
        "palio": "Oliva"
    },
    "La Candelaria": {
        "dia": "Martes Santo",
        "cristo": "Tres Caídas",
        "palio": "Cruz Roja"
    },
    "San Esteban": {
        "dia": "Martes Santo",
        "cristo": "AM Virgen de los Reyes",
        "palio": "Banda Cigarreras"
    },
    "Los Javieres": {
        "dia": "Martes Santo",
        "cristo": "Silencio",
        "palio": "Julián Cerdán"
    },
    "Los Estudiantes": {
        "dia": "Martes Santo",
        "cristo": "Silencio",
        "palio": "Banda Águila"
    },
    "Santa Cruz": {
        "dia": "Martes Santo",
        "cristo": "Capilla",
        "palio": "Maestro Tejera"
    },

    # MIÉRCOLES SANTO
    "El Carmen": {
        "dia": "Miércoles Santo",
        "cristo": "AM Pasión Linares",
        "palio": "Banda Cantillana"
    },
    "La Sed": {
        "dia": "Miércoles Santo",
        "cristo": "Rosario Cádiz",
        "palio": "Oliva / Mairena"
    },
    "El Buen Fin": {
        "dia": "Miércoles Santo",
        "cristo": "Centuria",
        "palio": "Nieves"
    },
    "San Bernardo": {
        "dia": "Miércoles Santo",
        "cristo": "Presentación al Pueblo",
        "palio": "Cruz Roja"
    },
    "La Lanzada": {
        "dia": "Miércoles Santo",
        "cristo": "Tres Caídas",
        "palio": "Banda Málaga"
    },
    "El Baratillo": {
        "dia": "Miércoles Santo",
        "cristo": "Sol",
        "palio": "Carmen de Salteras"
    },
    "Los Panaderos": {
        "dia": "Miércoles Santo",
        "cristo": "Cigarreras",
        "palio": "Santa Ana"
    },
    "Las Siete Palabras": {
        "dia": "Miércoles Santo",
        "cristo": "Esencia",
        "palio": "Carmen Villalba"
    },
    "El Cristo de Burgos": {
        "dia": "Miércoles Santo",
        "cristo": "Capilla",
        "palio": "Maestro Tejera"
    },

    # JUEVES SANTO
    "Los Negritos": {
        "dia": "Jueves Santo",
        "cristo": "Capilla",
        "palio": "Nieves"
    },
    "La Exaltación": {
        "dia": "Jueves Santo",
        "cristo": "Rosario Cádiz",
        "palio": "Banda Arahal"
    },
    "Las Cigarreras": {
        "dia": "Jueves Santo",
        "cristo": "Cigarreras",
        "palio": "Banda Cigarreras"
    },
    "Montesión": {
        "dia": "Jueves Santo",
        "cristo": "AM Arahal",
        "palio": "Cruz Roja"
    },
    "La Quinta Angustia": {
        "dia": "Jueves Santo",
        "cristo": "Carmen Villalba"
    },
    "El Valle": {
        "dia": "Jueves Santo",
        "cristo": "Capilla",
        "palio": "Maestro Tejera"
    },
    "Pasión": {
        "dia": "Jueves Santo",
        "cristo": "Silencio",
        "palio": "Oliva"
    },

    # MADRUGÁ
    "El Silencio": {
        "dia": "Madrugada",
        "cristo": "Capilla",
        "palio": "Capilla"
    },
    "El Gran Poder": {
        "dia": "Madrugada",
        "cristo": "Silencio",
        "palio": "Silencio"
    },
    "La Macarena": {
        "dia": "Madrugada",
        "cristo": "Centuria",
        "palio": "Carmen de Salteras"
    },
    "El Calvario": {
        "dia": "Madrugada",
        "cristo": "Silencio",
        "palio": "Silencio"
    },
    "Esperanza de Triana": {
        "dia": "Madrugada",
        "cristo": "Tres Caídas",
        "palio": "Banda Cigarreras"
    },
    "Los Gitanos": {
        "dia": "Madrugada",
        "cristo": "AM Salud",
        "palio": "Nieves"
    },

    # VIERNES SANTO
    "La Carretería": {
        "dia": "Viernes Santo",
        "cristo": "Cigarreras",
        "palio": "Julián Cerdán"
    },
    "La Soledad de San Buenaventura": {
        "dia": "Viernes Santo",
        "palio": "Banda Mairena"
    },
    "El Cachorro": {
        "dia": "Viernes Santo",
        "cristo": "Puebla del Río",
        "palio": "Oliva"
    },
    "La O": {
        "dia": "Viernes Santo",
        "cristo": "Sol",
        "palio": "Carmen de Salteras"
    },
    "San Isidoro": {
        "dia": "Viernes Santo",
        "cristo": "Silencio",
        "palio": "Silencio"
    },
    "Montserrat": {
        "dia": "Viernes Santo",
        "cristo": "Tres Caídas",
        "palio": "Maestro Tejera"
    },
    "La Mortaja": {
        "dia": "Viernes Santo",
        "cristo": "Capilla"
    },

    # SÁBADO SANTO
    "El Sol": {
        "dia": "Sábado Santo",
        "cristo": "Sol",
        "palio": "Banda Los Palacios"
    },
    "Los Servitas": {
        "dia": "Sábado Santo",
        "cristo": "Banda Cantillana",
        "palio": "Banda Coria"
    },
    "La Trinidad": {
        "dia": "Sábado Santo",
        "cristo": "Cigarreras / Tres Caídas",
        "palio": "Oliva"
    },
    "Santo Entierro": {
        "dia": "Sábado Santo",
        "cristo": "Banda Sinfónica Sevilla",
        "palio": "Tablada"
    },
    "Soledad de San Lorenzo": {
        "dia": "Sábado Santo",
        "cristo": "Silencio"
    },

    # DOMINGO DE RESURRECCIÓN
    "La Resurrección": {
        "dia": "Domingo de Resurrección",
        "cristo": "AM Virgen de los Reyes",
        "palio": "Banda Cigarreras"
    }
}

# ============================================================
#  CLASE DÍA + BANDAS
# ============================================================
class ModoBandas:
    def __init__(self, root, callback_menu):
        self.root = root
        self.callback_menu = callback_menu
        self.root.title("Acompañamientos Musicales")
        self.root.geometry("650x480")

        # Datos
        self.hermandades = list(acompanamientos.keys())
        self.indice = 0
        self.aciertos = 0
        self.errores = 0

        # Frame principal
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(expand=True, fill="both")

        # Botón volver
        self.btn_volver = tk.Button(
            self.main_frame, text="← Cerrar y Volver",
            command=self.volver, bg="#444", fg="white"
        )
        self.btn_volver.pack(pady=10)

        # Contenedor del formulario
        cont = tk.Frame(self.main_frame)
        cont.pack(pady=10)

        # Nombre hermandad
        self.lbl_nombre = tk.Label(cont, text="", font=("Arial", 20, "bold"))
        self.lbl_nombre.grid(row=0, column=0, columnspan=2, pady=10)

        # Día
        tk.Label(cont, text="Día de salida:", font=("Arial", 12)).grid(row=1, column=0, sticky="e")
        self.entry_dia = tk.Entry(cont, font=("Arial", 12), width=30)
        self.entry_dia.grid(row=1, column=1, pady=5)

        # Banda Cristo
        tk.Label(cont, text="Banda del Cristo:", font=("Arial", 12)).grid(row=2, column=0, sticky="e")
        self.entry_cristo = tk.Entry(cont, font=("Arial", 12), width=30)
        self.entry_cristo.grid(row=2, column=1, pady=5)

        # Banda Palio
        tk.Label(cont, text="Banda del Palio:", font=("Arial", 12)).grid(row=3, column=0, sticky="e")
        self.entry_palio = tk.Entry(cont, font=("Arial", 12), width=30)
        self.entry_palio.grid(row=3, column=1, pady=5)

        # Resultado
        self.lbl_resultado = tk.Label(self.main_frame, text="", font=("Arial", 14))
        self.lbl_resultado.pack(pady=10)

        # Botones inferiores
        botones_frame = tk.Frame(self.main_frame)
        botones_frame.pack(pady=10)

        self.btn_comprobar = tk.Button(
            botones_frame, text="Comprobar", font=("Arial", 12, "bold"),
            bg="#2c3e50", fg="white", width=12, command=self.comprobar
        )
        self.btn_comprobar.grid(row=0, column=0, padx=5)

        self.btn_pasar = tk.Button(
            botones_frame, text="Pasar →", font=("Arial", 12),
            bg="#555", fg="white", width=12, command=self.pasar
        )
        self.btn_pasar.grid(row=0, column=1, padx=5)

        self.btn_reiniciar = tk.Button(
            botones_frame, text="Reiniciar", font=("Arial", 12),
            bg="#8a0000", fg="white", width=12, command=self.reiniciar
        )
        self.btn_reiniciar.grid(row=0, column=2, padx=5)

        # Marcadores
        self.lbl_aciertos = tk.Label(self.main_frame, text="Aciertos: 0", font=("Arial", 12, "bold"))
        self.lbl_aciertos.pack()

        self.lbl_errores = tk.Label(self.main_frame, text="Errores: 0", font=("Arial", 12, "bold"))
        self.lbl_errores.pack()

        self.mostrar()

    # --------------------------------------------------------
    # MOSTRAR SIGUIENTE HERMANDAD
    # --------------------------------------------------------
    def mostrar(self):
        nombre = self.hermandades[self.indice]
        self.lbl_nombre.config(text=nombre)

        self.entry_dia.delete(0, tk.END)
        self.entry_cristo.delete(0, tk.END)
        self.entry_palio.delete(0, tk.END)

        self.lbl_resultado.config(text="", bg=self.root.cget("bg"))

    # --------------------------------------------------------
    # COMPROBAR RESPUESTAS
    # --------------------------------------------------------
    def comprobar(self):
        nombre = self.hermandades[self.indice]
        datos = acompanamientos[nombre]

        ok_dia = normalizar(self.entry_dia.get()) == normalizar(datos["dia"])
        ok_cristo = normalizar(self.entry_cristo.get()) == normalizar(datos["cristo"])
        ok_palio = normalizar(self.entry_palio.get()) == normalizar(datos["palio"])

        if ok_dia and ok_cristo and ok_palio:
            self.aciertos += 1
            self.lbl_resultado.config(text="¡Correcto!", bg="#8df58d")
            self.indice = (self.indice + 1) % len(self.hermandades)
            self.actualizar_marcadores()
            self.root.after(1200, self.mostrar)
        else:
            self.errores += 1
            self.lbl_resultado.config(text="Incorrecto", bg="#f58d8d")
            self.actualizar_marcadores()

    # --------------------------------------------------------
    # PASAR SIN RESPONDER
    # --------------------------------------------------------
    def pasar(self):
        self.indice = (self.indice + 1) % len(self.hermandades)
        self.mostrar()

    # --------------------------------------------------------
    # REINICIAR TODO
    # --------------------------------------------------------
    def reiniciar(self):
        self.indice = 0
        self.aciertos = 0
        self.errores = 0
        self.actualizar_marcadores()
        self.mostrar()

    # --------------------------------------------------------
    # ACTUALIZAR MARCADORES
    # --------------------------------------------------------
    def actualizar_marcadores(self):
        total = len(self.hermandades)
        self.lbl_aciertos.config(text=f"Aciertos: {self.aciertos} / {total}")
        self.lbl_errores.config(text=f"Errores: {self.errores}")

    # --------------------------------------------------------
    # VOLVER A PYGAME
    # --------------------------------------------------------
    def volver(self):
        self.root.destroy()
