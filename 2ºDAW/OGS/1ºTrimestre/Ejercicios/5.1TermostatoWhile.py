#Programa igual al del termostato anterior,que utilice
#while para comprobar continuamente la temperatura.

temperatura_minima = 25

while True:
    entrada = input("Introduce la temperatura actual): ")
    try:
        temperatura = float(entrada)
        if temperatura > temperatura_minima:
            print("Enciendo aire acondicionado")
            break
        else:
            print("Enciendo la calefacción")
            break
    except ValueError:
        print("Por favor, introduce un número válido o 'salir'.")

