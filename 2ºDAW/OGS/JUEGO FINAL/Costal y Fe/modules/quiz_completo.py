import tkinter as tk
import unicodedata

# ============================================================
# DATOS
# ============================================================

bloques = {
    "Viernes de Dolores": ["Bendición y Esperanza", "Pino Montano", "La Misión", "Bellavista", "La Corona", "Pasión y Muerte"],
    "Sábado de Pasión": ["Padre Pío", "La Milagrosa", "Torreblanca", "San José Obrero", "Divino Perdón"],
    "Domingo de Ramos": ["La Borriquita", "Jesús Despojado", "La Hiniesta", "La Paz", "La Cena", "San Roque", "La Amargura", "La Estrella", "El Amor"],
    "Lunes Santo": ["San Pablo", "La Redención", "Santa Genoveva", "Santa Marta", "San Gonzalo", "VeraCruz", "Las Penas", "Las Aguas", "El Museo"],
    "Martes Santo": ["El Cerro del Águila", "San Benito", "El Dulce Nombre", "La Candelaria", "San Esteban", "Los Javieres", "Los Estudiantes", "Santa Cruz"],
    "Miércoles Santo": ["El Carmen", "La Sed", "El Buen Fin", "San Bernardo", "La Lanzada", "El Baratillo", "Los Panaderos", "Las Siete Palabras", "El Cristo de Burgos"],
    "Jueves Santo": ["Los Negritos", "La Exaltación", "Las Cigarreras", "Montesión", "La Quinta Angustia", "El Valle", "Pasión"],
    "Madrugada": ["El Silencio", "El Gran Poder", "La Macarena", "El Calvario", "Esperanza de Triana", "Los Gitanos"],
    "Viernes Santo": ["La Carretería", "La Soledad de San Buenaventura", "El Cachorro", "La O", "San Isidoro", "Montserrat", "La Mortaja"],
    "Sábado Santo": ["El Sol", "Los Servitas", "La Trinidad", "Santo Entierro", "Soledad de San Lorenzo"],
    "Domingo de Resurrección": ["La Resurrección"]
}

COLUMNAS_MAPA = [
    ["Viernes de Dolores", "Sábado de Pasión", "Domingo de Ramos"],
    ["Lunes Santo", "Martes Santo", "Madrugada"],
    ["Miércoles Santo", "Jueves Santo"],
    ["Viernes Santo", "Sábado Santo", "Domingo de Resurrección"]
]

TOTAL_HERMANDADES = sum(len(h) for h in bloques.values())

def normalizar(txt):
    if not txt: return ""
    txt = txt.lower()
    txt = unicodedata.normalize("NFD", txt)
    txt = "".join(c for c in txt if unicodedata.category(c) != "Mn")
    return txt.strip()

# ============================================================
# QUIZ
# ============================================================

class QuizCofrade:
    def __init__(self, root):
        self.root = root
        self.root.title("Semana Santa de Sevilla - Quiz")
        self.root.geometry("1300x900")
        self.root.configure(bg="#f2f2f2")

        self.acertadas = set()
        self.tiempo_inicial = 600
        self.tiempo = self.tiempo_inicial
        self.pausado = False
        self.juego_terminado = False
        self.modo_sin_tiempo = False
        self.celdas = {}
        
        # AJUSTE DE VELOCIDAD: 1200ms hace que el "segundo" dure un 20% más
        self.velocidad_reloj = 1200 

        self.crear_interfaz_superior()
        self.crear_tablero_estilo_imagen()
        self.actualizar_timer()

    def crear_interfaz_superior(self):
        header = tk.Frame(self.root, bg="#f2f2f2")
        header.pack(pady=10, fill="x")

        self.timer_label = tk.Label(header, text="10:00", font=("Arial", 26, "bold"), bg="#f2f2f2")
        self.timer_label.pack(side="left", padx=30)

        self.entry = tk.Entry(header, font=("Arial", 20), justify="center", width=20)
        self.entry.pack(side="left", padx=10)
        self.entry.bind("<Return>", self.comprobar)
        self.entry.focus_set()

        btn_frame = tk.Frame(header, bg="#f2f2f2")
        btn_frame.pack(side="left", padx=10)

        self.pause_btn = tk.Button(btn_frame, text="Pausar", command=self.toggle_pause, width=10)
        self.pause_btn.pack(side="left", padx=2)

        self.reset_btn = tk.Button(btn_frame, text="Reiniciar", command=self.reiniciar, width=10)
        self.reset_btn.pack(side="left", padx=2)

        self.time_mode_btn = tk.Button(btn_frame, text="Sin Tiempo", command=self.toggle_modo_tiempo, width=10)
        self.time_mode_btn.pack(side="left", padx=2)

        self.progress = tk.Label(header, text=f"0 / {TOTAL_HERMANDADES}", font=("Arial", 16, "bold"), bg="#f2f2f2", fg="#4B0082")
        self.progress.pack(side="right", padx=30)

    def crear_tablero_estilo_imagen(self):
        main_frame = tk.Frame(self.root, bg="#f2f2f2")
        main_frame.pack(expand=True, fill="both", padx=10)

        for col_idx, dias_en_columna in enumerate(COLUMNAS_MAPA):
            col_frame = tk.Frame(main_frame, bg="#f2f2f2")
            col_frame.grid(row=0, column=col_idx, sticky="n", padx=5)

            for dia in dias_en_columna:
                dia_container = tk.Frame(col_frame, bg="#f2f2f2", pady=10)
                dia_container.pack(fill="x")

                lbl_dia = tk.Label(
                    dia_container, text=dia.upper(),
                    font=("Arial", 10, "bold"), bg="#4B0082", fg="white",
                    width=26, height=2, relief="flat"
                )
                lbl_dia.pack()

                for i, h in enumerate(bloques[dia]):
                    lbl_h = tk.Label(
                        dia_container, text=" ", 
                        bg="white", fg="black", font=("Arial", 8),
                        borderwidth=1, relief="solid", width=33, height=1
                    )
                    lbl_h.pack(pady=1)
                    self.celdas[(dia, i)] = lbl_h

    def comprobar(self, event=None):
        if self.pausado or self.juego_terminado: return
        entrada = self.entry.get()
        txt = normalizar(entrada)
        self.entry.delete(0, tk.END)

        if not txt or txt in self.acertadas: return

        for dia, hermandades in bloques.items():
            for i, h in enumerate(hermandades):
                if normalizar(h) == txt:
                    self.celdas[(dia, i)].config(text=h, bg="#90EE90")
                    if txt not in self.acertadas:
                        self.acertadas.add(txt)
                        self.progress.config(text=f"{len(self.acertadas)} / {TOTAL_HERMANDADES}")
                    
                    if len(self.acertadas) == TOTAL_HERMANDADES:
                        self.finalizar_juego(True)
                    return

    def actualizar_timer(self):
        if not self.pausado and not self.juego_terminado and not self.modo_sin_tiempo:
            self.tiempo -= 1
            m, s = divmod(self.tiempo, 60)
            self.timer_label.config(text=f"{m:02d}:{s:02d}")
            
            if self.tiempo <= 0:
                self.finalizar_juego(False)
            else:
                # Aquí se aplica la lentitud (1200ms en lugar de 1000ms)
                self.root.after(self.velocidad_reloj, self.actualizar_timer)

    def toggle_pause(self):
        if self.juego_terminado: return
        self.pausado = not self.pausado
        if self.pausado:
            self.pause_btn.config(text="Reanudar")
            self.entry.config(state="disabled")
        else:
            self.pause_btn.config(text="Pausar")
            self.entry.config(state="normal")
            self.entry.focus_set()
            if not self.modo_sin_tiempo:
                self.actualizar_timer()

    def reiniciar(self):
        self.acertadas.clear()
        self.tiempo = self.tiempo_inicial
        self.pausado = False
        self.juego_terminado = False
        self.timer_label.config(text="10:00" if not self.modo_sin_tiempo else "∞", fg="black")
        self.progress.config(text=f"0 / {TOTAL_HERMANDADES}")
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.pause_btn.config(text="Pausar")
        for lbl in self.celdas.values():
            lbl.config(text=" ", bg="white", fg="black")
        if not self.modo_sin_tiempo:
            self.actualizar_timer()

    def toggle_modo_tiempo(self):
        self.modo_sin_tiempo = not self.modo_sin_tiempo
        if self.modo_sin_tiempo:
            self.time_mode_btn.config(text="Con Tiempo")
            self.timer_label.config(text="∞")
        else:
            self.time_mode_btn.config(text="Sin Tiempo")
            self.tiempo = self.tiempo_inicial
            self.timer_label.config(text="10:00")
            self.actualizar_timer()

    def finalizar_juego(self, victoria):
        self.juego_terminado = True
        self.entry.config(state="disabled")
        if victoria:
            self.timer_label.config(text="¡COMPLETO!", fg="green")
        else:
            self.timer_label.config(text="¡TIEMPO!", fg="red")
            for (dia, i), lbl in self.celdas.items():
                if lbl.cget("text") == " ":
                    lbl.config(text=bloques[dia][i], fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizCofrade(root)
    root.mainloop()