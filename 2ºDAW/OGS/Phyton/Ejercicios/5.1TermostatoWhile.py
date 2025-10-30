#Programa igual al del termostato anterior,que utilice
#while para comprobar continuamente la temperatura.

# Definimos la temperatura mínima de referencia
temperatura_minima = 25

# Bucle infinito para pedir la temperatura hasta que se decida salir
while True:
    # Pedimos al usuario que introduzca la temperatura o 'salir'
    entrada = input("Introduce la temperatura actual (o escribe 'salir' para terminar): ")
    
    # Comprobamos si el usuario quiere salir del programa
    if entrada.lower() == "salir":
        print("Programa terminado.")  
        break  

    # Intentamos convertir la entrada a un número flotante
    try:
        temperatura = float(entrada)  
       
        if temperatura > temperatura_minima:
            print("Enciendo aire acondicionado")  
        else:
            print("Enciendo la calefacción")  
    # Capturamos el error si la conversión a float falla
    except ValueError:
        print("Por favor, introduce un número válido.")




