# Ejercicio1-Edad y Categoría
# Escribe un programa que pida la edad del usuario y
# muestre si es *niño, adolescente, joven, adulto o
# jubilado* según rangos de edad definidos por ti.
def ejercicio1():
    edad = int(input("¿Por favor dime tu edad?"))  # Convertimos a número
    if edad >= 65: #Si la edad es jubilado
        print("Estás jubilado.")
    elif edad <= 11: # Si la edad es de un niño
        print("Eres un niño.")
    elif edad > 11 and edad < 18:  # Si la edad es de un adolescente
        print("Eres un adolescente.")
    elif edad >= 18 and edad < 30: # Si la edad es de un joven
        print("Eres joven.")
    elif edad >= 30 and edad < 50: # Si la edad es de un adulto
        print("Eres un adulto.")

# Ejercicio2-Control de acceso simple
#Solicita un nombre de usuario y contraseña.
#Solo permite el acceso si el usuario es
#“admin” o “pepe” y la contraseña es “1234”.
#En caso contrario, muestra “Acceso denegado”. 
def ejercicio2():
    nombre = input("Introduzca su usuario: ")
    contrasena = input("Introduzca su contraseña: ")
    if (nombre == "pepe" or nombre == "admin") and contrasena == "1234":
        print("Acceso aceptado")
    else:
        print("Acceso denegado")

#Ejercicio3-Año bisiesto
#Crea un programa que determine si un año
#introducido por el usuario es bisiesto,
#aplicando las condiciones matemáticas
#correctas (divisible por 4, 100 y 400).    
def ejercicio3():
    año = int(input("Introduzca un año para comprobar si es bisiesto: "))
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        print("El año es bisiesto")
    else:
        print("El año no es bisiesto")

# -------------------------------
# MENÚ PRINCIPAL
# -------------------------------
while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1- Ejercicio 1")
    print("2- Ejercicio 2")
    print("3- Ejercicio 3")
    print("4- Ejercicio 4")
    print("5- Ejercicio 5")
    print("6- Ejercicio 6")
    print("7- Ejercicio 7")
    print("8- Ejercicio 8")
    print("9- Ejercicio 9")
    print("10- Ejercicio 10")
    print("11- Salir")
    eleccion = input("Seleccione ejercicio (1-10): ")

    if eleccion == "1":
        ejercicio1()
    elif eleccion == "2":
        ejercicio2()
    elif eleccion == "3":
        ejercicio3()
    elif eleccion == "4":
        ejercicio4()
    elif eleccion == "5":
        ejercicio5()
    elif eleccion == "6":
        ejercicio6()
    elif eleccion == "7":
        ejercicio7()
    elif eleccion == "8":
        ejercicio8()
    elif eleccion == "9":
        ejercicio9()
    elif eleccion == "10":
        ejercicio10()
    elif eleccion == "11":
        print("Programa finalizado")
        break
    else:
        print("Opción incorrecta")
