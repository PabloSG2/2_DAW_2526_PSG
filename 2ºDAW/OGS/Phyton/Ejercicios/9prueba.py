import os
import math
from fractions import Fraction
from zipfile import ZipFile
from random import randint, choice, sample, shuffle, seed
import time
from datetime import datetime, date
import calendar

# ====Muestra los archivos del directorio actual====
def ejemplo_os():
    print("=== MÓDULO OS ===")
    print("Archivos en esta carpeta:")
    print(os.listdir('.'))  # Lista los archivos del directorio actual

# ====Demuestra redondeos: round, floor y ceil====
def ejemplo_math():
    print("=== MÓDULO MATH ===")
    numeros = (0.5, 0.51, 1.6, 2.5, 2.51)
    print("\nround():")  # Redondeo normal
    for n in numeros:
        print(f"{n} -> {round(n)}")  # round redondea según la parte decimal
    print("\nmath.floor():")  # Redondeo hacia abajo
    for n in numeros:
        print(f"{n} -> {math.floor(n)}")  # floor siempre baja al entero inferior
    print("\nmath.ceil():")  # Redondeo hacia arriba
    for n in numeros:
        print(f"{n} -> {math.ceil(n)}")  # ceil siempre sube al entero superior

# =====Operaciones exactas con fracciones====
def ejemplo_fracciones():
    print("=== MÓDULO FRACTIONS ===")
    f1 = Fraction(1, 2)  # Crea 1/2
    f2 = Fraction(1, 3)  # Crea 1/3
    print("f1 =", f1)
    print("f2 =", f2)
    print("f1 + f2 =", f1 + f2)  # Suma exacta de fracciones
    print("3 * f2 =", 3 * f2)    # Multiplicación exacta

# ====Números aleatorios, elección, y semilla====
def ejemplo_random():
    print("=== MÓDULO RANDOM ===")
    print("Número aleatorio entre 1 y 10:", randint(1, 10))
    colores = ['rojo', 'verde', 'azul', 'amarillo']
    print("Color aleatorio:", choice(colores))  # Elige un color al azar
    print("\nSecuencia repetible con seed:")
    seed(123)  # Fija la semilla para que la secuencia sea siempre igual
    for _ in range(5):
        print(randint(0, 10))  # Genera siempre la misma secuencia

# ====Crea un archivo ZIP y añade este mismo archivo dentro=====
def ejemplo_zip():
    print("=== MÓDULO ZIPFILE ===")
    print("Creando archivo ZIP de ejemplo...")
    zipf = ZipFile('ejemplo.zip', 'w')  # Crea un ZIP en modo escritura
    zipf.write(__file__)  # Añade este archivo al ZIP
    zipf.close()  # Cierra el ZIP
    print("ZIP creado: ejemplo.zip")

# ====Mide el tiempo transcurrido y usa sleep====
def ejemplo_time():
    print("=== MÓDULO TIME ===")
    inicio = time.time()  # Tiempo actual en segundos
    print("Esperando 1 segundo...")
    time.sleep(1)  # Pausa de 1 segundo
    fin = time.time()  # Tiempo después de la pausa
    print("Tiempo transcurrido:", fin - inicio)  # Diferencia en segundos

# ======Muestra meses, días y el día actual=====
def ejemplo_calendar():
    print("=== MÓDULO CALENDAR ===")
    print("Meses del año:")
    print(list(calendar.month_name)[1:])  # Lista de meses (sin el índice 0)
    print("\nDías de la semana:")
    print(list(calendar.day_name))  # Lista de días
    hoy = date.today()  # Fecha actual
    ahora = datetime.now()  # Fecha y hora actual
    print("\nFecha actual:", ahora.strftime('%Y-%m-%d %H:%M:%S'))  # Formateo
    print("Hoy es:", calendar.day_name[hoy.weekday()])  # Nombre del día