#Termostato Versión 1
#Al igual que el ejercicio anterior:
#1. Pedimos la temperatura al usuario
#2. Comparamos la temperatura con dos valores:
#* Si es mayor que 25 -> Enciendo aire acondicionado
#* Si es menor  que 18 <- Enciendo la calefacción
#Utiliza para ello if/elif/else

# Pedimos la temperatura al usuario
temperatura = float(input("Introduce la temperatura actual: "))

# Comparamos la temperatura con dos valores
if temperatura > 25:
    print("Enciendo aire acondicionado")
elif temperatura < 18:
    print("Enciendo la calefacción")
else:
    print("La temperatura es agradable, no hago nada")
