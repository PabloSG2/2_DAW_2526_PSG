 # Ejercicio 1
def ejercicio1():
    print("\n--Ejercicio 1--Ingresar y uno menos del doble--")
    numero = int(input("Ingrese un número entero positivo: "))
    if numero > 0:
        for i in range(numero, 2 * numero):
            print(i)
    else:
        print("El número no es positivo.")

# Ejercicio 2
def ejercicio2():
    print("\n--Ejercicio 2--Suma de números ingresados--")
    cantidad = int(input("¿Cuántos números desea ingresar? "))
    suma = 0
    for i in range(cantidad):
        num = int(input(f"Ingrese el número {i + 1}: "))
        suma += num
    print(f"La suma total es: {suma}")

# Ejercicio 3
def ejercicio3():
    print("\n--Ejercicio 3--Vocales únicas en la frase--")
    frase = input("Ingrese una frase: ").lower()
    vocales = {'a', 'e', 'i', 'o', 'u'}
    vocales_encontradas = set()
    for letra in frase:
        if letra in vocales:
            vocales_encontradas.add(letra)
    print("Vocales en la frase (sin repetir):", ", ".join(sorted(vocales_encontradas)))

# Ejercicio 4
def ejercicio4():
    print("\n--Ejercicio 4--Contar vocales en la frase--")
    frase = input("Ingrese una frase: ").lower()
    contador_vocales = 0
    for letra in frase:
        if letra in "aeiou":
            contador_vocales += 1
    print(f"Cantidad total de vocales en la frase: {contador_vocales}")

# Ejercicio 5
def ejercicio5():
    print("\n--Ejercicio 5--Sumatoria del 0 al 100--")
    suma_total = sum(range(101))
    print(f"La sumatoria del 0 al 100 es: {suma_total}")

# Ejercicio 6
def ejercicio6():
    print("\n--Ejercicio 6--Suma negativoYpromedio positivo--")
    suma_negativos = 0
    suma_positivos = 0
    contador_positivos = 0
    for i in range(6):
        num = int(input(f"Ingrese el número {i + 1}: "))
        if num < 0:
            suma_negativos += num
        elif num > 0:
            suma_positivos += num
            contador_positivos += 1
    print(f"Suma de números negativos: {suma_negativos}")
    if contador_positivos > 0:
        promedio_positivos = suma_positivos / contador_positivos
        print(f"Promedio de números positivos: {promedio_positivos}")
    else:
        print("No se ingresaron números positivos.")

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
    print("7- Salir")
    eleccion = input("Seleccione ejercicio (1-7): ")

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
        print("Programa finalizado")
        break
    else:
        print("Opción incorrecta")
