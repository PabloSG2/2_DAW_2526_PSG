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

#Ejercicio4-Número dentro de rango
#Pide al usuario un número y comprueba si se
#encuentra dentro del rango 1–100. Indica si está
#“dentro del rango”, “por debajo” o “por encima”.
def ejercicio4():
    numero = int(input("Introduzca un número: "))
    if numero in range(1, 101):
        print("Dentro del rango")
    elif numero < 1:
        print("Por debajo del rango")
    else:
        print("Por encima del rango")

#Ejercicio5-Múltiplos de 5 y 7
#Muestra todos los números del 1 al 1000
#que sean múltiplos de 5, de 7 o de ambos,
#indicando a qué conjunto pertenece cada uno.
def ejercicio5():
    numero = int(input("Introduzca multiplos del 1 al 1000"))
    for numero in range(1, 1001):
        if numero % 5 == 0 and numero % 7 == 0:
            print(f"{numero} es múltiplo de 5 y de 7")
        elif numero % 5 == 0:
            print(f"{numero} es múltiplo de 5")
        elif numero % 7 == 0:
            print(f"{numero} es múltiplo de 7")

#Ejercicio6-Sumatoria hasta N
#Pide un número entero positivo `N` y calcula
#la suma de todos los enteros desde 1 hasta
#`N` usando un bucle `for`. Luego muestra el
#resultado y la fórmula algebraica equivalente.
def ejercicio6():
    N= int(input("Introduzca un numero entero positivo"))
    if N > 0:
        suma = 0
        for i in range(1, N + 1):
            suma += i 
        # Fórmula algebraica: n * (n + 1) / 2
        formula = N * (N + 1) // 2
        print(f"La suma de los números del 1 al {N} es: {suma}")
        print(f"Fórmula algebraica equivalente: ({N} * ({N} + 1)) / 2 = {formula}")
    else:
        print("Por favor, introduce un número positivo.")

#Ejercicio7-Tabla de Multiplicar
#Crea un programa que muestre todas las tablas
#de multiplicar del 1 al 10 usando bucles anidados.
#Cada tabla debe tener un encabezado identificativo.
def ejercicio7():
    for i in range(1,11):
        print(f'\n---Tabla del {i}------')
        for j in range(1,11):
            print(f'{i} x {j} = {i*j}')

#Ejercico8-Adivina el numero
#Genera un número aleatorio entre 1 y 50.
#Pide al usuario que adivine el número.
#Usa un bucle `while` que indique si el número
#introducido es mayor o menor hasta acertar.
def ejercicio8():
    import random
    numero_secreto = random.randint(1, 50)
    numero = 0
    while numero != numero_secreto:
        numero = int(input("Adivina el número (1-50): "))
        if numero < numero_secreto:
            print("Más grande")
        elif numero > numero_secreto:
            print("Más pequeño")
        else:
            print("¡Acertaste!")
#Ejercicio9-Simulacion de consola
#Simula una consola de comandos donde el usuario
#pueda escribir “Encender”, “Apagar” o “Salir”.
#Cualquier otro comando debe devolver “Comando no reconocido”.
#Si elige “Apagar”, pide confirmación antes de salir.
def ejercicio9():
    comando = input("Introduzca un comando: ")
    if comando == "Encender" or comando == "Salir":
        print(f"{comando} consola")
    elif comando == "Apagar":
        confirmacion = input("¿Estás seguro de que quieres apagar? (s/n): ")
        if confirmacion.lower() == "s":
            print("Apagando consola...")
        else:
            print("Cancelando apagado...")
    else:
        print("Comando no reconocido.")

#Ejercicio 10-Contador con saltos
#Escribe un programa que imprima los números del
#1 al 100, pero: Si el número es múltiplo de 3, no se
#imprime (usa `continue`). Si el número llega a 77, el
#programa se detiene inmediatamente (usa `break`).
def ejercicio10():
    for i in range(1, 101):
        if i % 3 == 0:
            continue  # salta los múltiplos de 3
        if i == 77:
            break  # detiene el programa al llegar a 77
        print(i)

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
