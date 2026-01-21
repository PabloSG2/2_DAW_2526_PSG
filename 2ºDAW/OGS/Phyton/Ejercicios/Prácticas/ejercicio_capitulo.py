# Importamos date del módulo datetime y random
from datetime import date        # Módulo para manejar fechas
import random                    # Módulo de aleatoriedad


#Ejercicio 1: Calcular tu Edad con datetime
def calcular_edad():             # Definición de la función
    # Pedimos el año,mes y día de nacimiento al usuario
    anio = int(input("Año de nacimiento: "))   # Año como entero
    mes = int(input("Mes de nacimiento: "))    # Mes como entero
    dia = int(input("Día de nacimiento: "))    # Día como entero

    # Creamos un objeto fecha con la fecha de nacimiento
    nacimiento = date(anio, mes, dia)          # Fecha de nacimiento

    # Obtenemos la fecha actual y retamos edad 
    hoy = date.today()                         
    edad = hoy.year - nacimiento.year           # Edad aproximada

    # Comprobamos si aún no ha cumplido años este año
    if (hoy.month, hoy.day) < (nacimiento.month, nacimiento.day):  # Comparación de fechas
        edad -= 1                               # Restamos un año si no ha cumplido
    print("Tu edad es:", edad)                  

#Ejercicio 2: Advinar número entre 1 y 10 con random
def adivinar_numero():           
    # Nºaleatorio entre 1 y 10,pedimos al usuario un úmero
    numero_secreto = random.randint(1, 10)     
    numero = int(input("Adivina un número entre 1 y 10: "))  

    # Comparamos el número introducido con el secreto
    if numero == numero_secreto:                # Si coincide
        print("¡Has acertado!")                 # Mensaje de acierto
    else:
        print("No has acertado. El número era:", numero_secreto)  # Mensaje de error

#Ejercicio 3: Advinar número entre 1 y 10 con random + intentos
def adivinar_con_intentos():  
    # Generamos el número secreto
    numero_secreto = random.randint(1, 10) # Número aleatorio

    # Contador de intentos y variable del usaurio
    intentos = 0   # Contador a cero
    numero = 0     # Valor inicial

    # Bucle que se repite hasta que el usuario acierta
    while numero != numero_secreto: # Condición del bucle
        numero = int(input("Adivina un número entre 1 y 10: "))  # Pedimos número
        intentos += 1     # Aumentamos intentos                   
    print("Correcto lo acertaste en: ", intentos)      