#Crea un código que:
#1.Pedimos la temperatura al usuario
#2.Comparamos con la temperatura minima que será 25.
#* Si es mayor -> Enciendo aire acondicionado
#* Si es menor  <- Enciendo la calefaccion

# Pedimos temperatura al usuario 
temperatura = float(input("Introduce la temperatura actual: "))

# Comparamos la temperatura con la temperatura mínima
temperatura_minima = 25
if temperatura > temperatura_minima:
    print("Enciendo aire acondicionado")
else:
    print("Enciendo la calefacción")
    
