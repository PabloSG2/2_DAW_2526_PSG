# Solicita al usuario que ingrese dos números
print("-----Ejercicio1-----")
numero1 = input("Ingresa el primer número: ")
numero2 = input("Ingresa el segundo número: ")

# Convierte las entradas a números enteros
numero1 = int(numero1)
numero2 = int(numero2)

# Compara los números y muestra el resultado
if numero1 < numero2:
    print("El número menor es: " + str(numero1))
elif numero2 < numero1:
    print("El número menor es: " + str(numero2))
else:
    print("Ambos números son iguales: " + str(numero1))

# Solicita al usuario un día de la semana
print("\n-----Ejercicio2-----")
dia = input("Ingresa un día de la semana: ")

# Convierte el texto a minúsculas para evitar problemas con mayúsculas
dia = dia.lower()

# Evalúa el día y muestra un mensaje correspondiente
if dia == "lunes":
    print("¡Ánimo, es el comienzo de la semana!")
elif dia == "viernes":
    print("¡Ya casi es fin de semana!")
elif dia == "sábado" or dia == "sabado" or dia == "domingo":
    print("¡Es fin de semana, disfruta!")
else:
    print("Es un día normal de la semana.")

# Solicita un número entero
print("\n-----Ejercicio3-----")
numero = int(input("Ingresa un número entero: "))

# Calcula el valor absoluto
if numero < 0:
    absoluto = numero * -1
else:
    absoluto = numero

# Muestra el resultado
print("El valor absoluto es:", absoluto)
