# EJERCICIO 1: Sumar todos los números ingresados hasta que se ingrese 0
def ejercicio1():
    print("\n--- EJERCICIO 1 ---")
    suma = 0
    while True:
        n = int(input("Ingrese un número (0 para terminar): "))
        if n == 0:
            break
        suma += n
    print("Suma total:", suma)

# EJERCICIO 2: Sumar solo números positivos hasta que se ingrese 0
def ejercicio2():
    print("\n--- EJERCICIO 2 ---")
    suma = 0
    while True:
        n = int(input("Ingrese un número (0 para terminar): "))
        if n == 0:
            break
        if n > 0:
            suma += n
    print("Suma de positivos:", suma)

# EJERCICIO 3: Encontrar el mayor número ingresado
def ejercicio3():
    print("\n--- EJERCICIO 3 ---")
    mayor = None
    while True:
        n = int(input("Ingrese un número positivo (0 para terminar): "))
        if n == 0:
            break
        if mayor is None or n > mayor:
            mayor = n
    if mayor is not None:
        print("Mayor número ingresado:", mayor)
    else:
        print("No se ingresaron números.")

# EJERCICIO 4: Sumar los dígitos de un número positivo
def ejercicio4():
    print("\n--- EJERCICIO 4 ---")
    n = int(input("Ingrese un número positivo: "))
    suma = sum(int(d) for d in str(n))
    print("Suma de los dígitos:", suma)

# EJERCICIO 5: Sumar dígitos de varios números y contar pares
def ejercicio5():
    print("\n--- EJERCICIO 5 ---")
    pares = 0
    while True:
        n = int(input("Ingrese un número positivo (-1 para terminar): "))
        if n == -1:
            break
        suma = sum(int(d) for d in str(n))
        print(f"Suma de dígitos de {n}: {suma}")
        if n % 2 == 0:
            pares += 1
    print("Cantidad de números pares ingresados:", pares)

# EJERCICIO 6: Menú interno con opciones 1, 2 y 3
def ejercicio6():
    print("\n--- EJERCICIO 6 ---")
    while True:
        print("\n1- Comenzar programa")
        print("2- Imprimir listado")
        print("3- Finalizar")
        op = input("Seleccione opción: ")
        if op == "1":
            print("Programa iniciado...")
        elif op == "2":
            print("Listado de elementos...")
        elif op == "3":
            print("Saliendo del ejercicio 6...")
            break
        else:
            print("Opción incorrecta")

# EJERCICIO 7: Total de compras con descuento sobre $1000
def ejercicio7():
    print("\n--- EJERCICIO 7 ---")
    total = 0
    while True:
        monto = float(input("Ingrese monto (0 para terminar): "))
        if monto == 0:
            break
        if monto < 0:
            print("Monto inválido")
            continue
        total += monto
    if total > 1000:
        total *= 0.9
    print("Total a pagar:", total)

# EJERCICIO 8: Buscar letra en una frase y mostrar posición
def ejercicio8():
    print("\n--- EJERCICIO 8 ---")
    frase = input("Ingrese una frase: ")
    letra = input("Ingrese una letra a buscar: ")
    encontrado = False
    for i, c in enumerate(frase):
        if c == letra:
            print(f"Letra '{letra}' encontrada en posición {i}")
            encontrado = True
            break
        else:
            print(f"No hay coincidencia en posición {i}")
    if not encontrado:
        print(f"Letra '{letra}' no encontrada")

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
    print("9- Salir")
    eleccion = input("Seleccione ejercicio (1-9): ")

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
        print("Programa finalizado")
        break
    else:
        print("Opción incorrecta")