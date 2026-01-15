# =====================================================
# EJERCICIO 1
# Trabaja con LISTAS
# - Carga números hasta que el usuario ingrese 0
# - Elimina un número
# - Suma los elementos
# - Crea una lista con los menores a un valor
# - Crea una lista de tuplas (numero, cantidad de veces)
# =====================================================
def ejercicio1():
    print("\n--- EJERCICIO 1 ---")

    # Lista vacía para guardar números
    lista = []

    # Cargar números
    num = int(input("Número (0 termina): "))
    while num != 0:
        lista.append(num)
        num = int(input("Número (0 termina): "))
    print("Lista:", lista)

    # Eliminar un número
    n = int(input("Número a eliminar: "))
    if n in lista:
        lista.remove(n)
        print("Número eliminado")
    else:
        print("No se puede eliminar")

    # Sumar elementos
    suma = 0
    for x in lista:
        suma = suma + x
    print("Suma:", suma)

    # Crear lista de menores
    limite = int(input("Número límite: "))
    menores = []
    for x in lista:
        if x < limite:
            menores.append(x)
    print("Menores:", menores)

    # Crear lista de tuplas (numero, veces)
    resultado = []
    for x in lista:
        if (x, lista.count(x)) not in resultado:
            resultado.append((x, lista.count(x)))
    print("Tuplas:", resultado)

# =====================================================
# EJERCICIO 2
# Trabaja con LISTAS DE TUPLAS
# - Guarda pasajeros (nombre, dni, ciudad)
# - Guarda ciudades (ciudad, país)
# - Permite consultar datos con un menú
# =====================================================
def ejercicio2():
    print("\n--- EJERCICIO 2 ---")

    viajeros = []
    ciudades = []

    while True:
        print("\n1- Agregar pasajero")
        print("2- Agregar ciudad")
        print("3- Ver ciudad por DNI")
        print("4- Salir ejercicio 2")

        op = input("Opción: ")

        if op == "1":
            nombre = input("Nombre: ")
            dni = int(input("DNI: "))
            ciudad = input("Ciudad: ")
            viajeros.append((nombre, dni, ciudad))

        elif op == "2":
            ciudad = input("Ciudad: ")
            pais = input("País: ")
            ciudades.append((ciudad, pais))

        elif op == "3":
            dni = int(input("DNI: "))
            for v in viajeros:
                if v[1] == dni:
                    print("Viaja a", v[2])
        elif op == "4":
            break

# =====================================================
# EJERCICIO 3
# Trabaja con CONJUNTOS (set)
# - Guarda nombres sin repetir
# - Muestra unión, intersección y diferencia-
# =====================================================
def ejercicio3():
    print("\n--- EJERCICIO 3 ---")

    primaria = set()
    secundaria = set()

    nombre = input("Primaria (x termina): ")
    while nombre != "x":
        primaria.add(nombre)
        nombre = input("Primaria (x termina): ")

    nombre = input("Secundaria (x termina): ")
    while nombre != "x":
        secundaria.add(nombre)
        nombre = input("Secundaria (x termina): ")

    print("Todos:", primaria | secundaria)
    print("Repetidos:", primaria & secundaria)
    print("Solo primaria:", primaria - secundaria)

# =====================================================
# EJERCICIO 4
# Trabaja con LISTAS DE TUPLAS
# - Obtiene domicilios sin repetir
# Evitar duplicados y Recorrer listas
# =====================================================
def ejercicio4():
    print("\n--- EJERCICIO 4 ---")

    ventas = [
        ("Nuria Costa", 5, 12780, "Calle Las Flores 355"),
        ("Jorge Russo", 7, 699, "Mirasol 218"),
        ("Nuria Costa", 7, 532, "Calle Las Flores 355")
    ]

    domicilios = []

    for v in ventas:
        if v[3] not in domicilios:
            domicilios.append(v[3])
    print("Domicilios a facturar:", domicilios)

# =====================================================
# EJERCICIO 5
# Trabaja con DICCIONARIOS
# - Cuenta cuántas veces aparece cada carácter
# - Diccionario clave : valor y Acumuladores
# =====================================================
def ejercicio5():
    print("\n--- EJERCICIO 5 ---")
    conteo = {}

    for i in range(3):   # se usa 3 en vez de 50 para practicar
        texto = input("Texto: ")
        for c in texto:
            if c in conteo:
                conteo[c] = conteo[c] + 1
            else:
                conteo[c] = 1
    print("Conteo:", conteo)

# =====================================================
# EJERCICIO 6
# Trabaja con DICCIONARIOS
# Gestiona socios de un club, Alta, baja y modificación
# Borrar elementos con del
# =====================================================
def ejercicio6():
    print("\n--- EJERCICIO 6 ---")
    socios = {
        1: ["Amanda Núñez", "17032009", "s"],
        2: ["Bárbara Molina", "17032009", "s"],
        3: ["Lautaro Campos", "17032009", "s"]
    }

    print("Cantidad de socios:", len(socios))

    num = int(input("Número de socio que paga: "))
    if num in socios:
        socios[num][2] = "s"

    nombre = input("Nombre a borrar: ")
    for k in list(socios.keys()):
        if socios[k][0] == nombre:
            del socios[k]
            
    print("Listado final:")
    for k in socios:
        print(k, socios[k])

# =====================================================
# MENÚ PRINCIPAL
# =====================================================
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