#----------------EJERCICIO 1----------------------
#Solicitar al usuario que ingrese su dirección email.
#Imprimir un mensaje indicando si la dirección es válida o
#no, valiéndose de una función para decidirlo. Una dirección
#se considerará válida si contiene el símbolo "@".
def ejercicio1():
    email = input("Introduzca un email: ")
    if "@" in email:
        print("Email correcto")
    else:
        print("Email no correcto")

#----------------EJERCICIO 2----------------------
#Solicitar números al usuario hasta que ingrese el
#cero.Por cada uno, mostrar la suma de sus dígitos
#(utilizando una función que realice dicha suma).
def suma_digitos(n):
    total = 0
    for d in str(n):
        total += int(d)
    return total

def ejercicio2():
    num = int(input("Ingrese un número (0 para salir): "))
    while num != 0:
        print("Suma de dígitos:", suma_digitos(num))
        num = int(input("Ingrese un número (0 para salir): "))

#----------------EJERCICIO 3----------------------
#Solicitar números al usuario hasta que ingrese el cero.
#Por cada uno, mostrar la suma de sus dígitos.
#Al finalizar, mostrar la sumatoria de todos los números
#ingresados y la suma de sus dígitos.Reutilizar la misma
#función realizada en el ejercicio 2.
def ejercicio3():
    total = 0
    num = int(input("Ingrese un número (0 para salir): "))
    while num != 0:
        print("Suma de dígitos:", suma_digitos(num))
        total += num
        num = int(input("Ingrese un número (0 para salir): "))
    print("Sumatoria de todos los números:", total)
    print("Suma de dígitos de la sumatoria:", suma_digitos(total))

#----------------EJERCICIO 4----------------------
#Requerir al usuario que ingrese un número entero
#e informar si es primo o no, utilizando una
#función booleana que lo decida.
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def ejercicio4():
    n = int(input("Ingrese un número: "))
    if es_primo(n):
        print("Es primo")
    else:
        print("No es primo")

#----------------EJERCICIO 5----------------------
#Solicitar usuario un número entero y luego un dígito.
#Informar cantidad ocurrencias del dígito en número,
#utilizando para ello una función que calcule frecuencia.
def ejercicio5():
    numero = input("Número: ")
    digito = input("Dígito: ")
    print("Aparece", numero.count(digito), "veces")

#----------------EJERCICIO 6----------------------
#Escribir un programa que pida números al usuario,
#mostrar el factorial de cada uno y, al finalizar,
#la cantidad total de números leídos en total.
#Utilizar una o más funciones, según sea necesario.
def factorial(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f

def ejercicio6():
    cantidad = 0
    num = int(input("Número (0 para salir): "))
    while num != 0:
        print("Factorial:", factorial(num))
        cantidad += 1
        num = int(input("Número (0 para salir): "))
    print("Cantidad de números leídos:", cantidad)

#----------------EJERCICIO 7----------------------
#Escribir un programa que pida números positivos al
#usuario.Mostrar el número cuya sumatoria de dígitos
#fue mayor y la cantidad de números cuya sumatoria de
#dígitos fue menor que 10. Utilizar una o más funciones,
#según sea necesario.
def ejercicio7():
    mayor_num = 0          # Número con mayor suma de dígitos
    mayor_suma = 0         # Suma de dígitos mayor
    menores_10 = 0         # Contador de sumas < 10
    while True:
        num = int(input("Número positivo (0 para salir): "))
        if num == 0:
            break
        suma = suma_digitos(num)
        if suma > mayor_suma:
            mayor_suma = suma
            mayor_num = num
        if suma < 10:
            menores_10 += 1
    print("Número con mayor suma de dígitos:", mayor_num)
    print("Cantidad de números con suma < 10:", menores_10)

#----------------EJERCICIO 8----------------------
#Solicitar al usuario el ingreso de números primos.
#La lectura finalizará cuando ingrese un número que
#no sea primo. Por cada número, mostrar la suma de
#sus dígitos. También solicitar al usuario un dígito e
#informar la cantidad de veces que aparece en el
#número (frecuencia). Al finalizar el programa,
#mostrar el factorial del mayor número ingresado.
def ejercicio8():
    mayor = 0
    num = int(input("Ingrese un número primo (otro para terminar): "))
    while es_primo(num):
        print("Suma de dígitos:", suma_digitos(num))
        dig = input("Dígito a contar: ")
        cont = 0
        for d in str(num):
            if d == dig:
                cont += 1
        print("Aparece", cont, "veces")
        if num > mayor:
            mayor = num
        num = int(input("Ingrese un número primo (otro para terminar): "))
    print("Factorial del número mayor ingresado:", factorial(mayor))

#----------------EJERCICIO 9----------------------
#Sin ejecutar el siguiente programa, determinar cuál
#es la salida en pantalla si se ingresan los valores
#x=6, y=7: def coordenadaZ(x,y): x=x+10 y=y+15 return x+y
#x=int(input("Coordenada eje x: "))
#y=int(input("Coordenada eje y: "))
#for i in range(3): z=coordenadaZ(x,y)
#x=x+1 y=y+1 print(x," . ",y)
def ejercicio9():
    print("7  .  8")
    print("8  .  9")
    print("9  .  10")

#----------------EJERCICIO 10----------------------
#El siguiente programa debería imprimir el número 2 si se le ingresan como valores x=5, y=1 pero
#en su lugar imprime 5. ¿Qué hay que corregir?
#def maximo(a,b): if x>y: return x else: return y
#def minimo(a,b): if x<y: return x else: return y
#x=int(input("Un número: "))y=int(input("Otro número: "))
#print(maximo(x-3, minimo(x+2, y-5)))
def maximo(a, b):
    if a > b:
        return a
    else:
        return b
def minimo(a, b):
    if a < b:
        return a
    else:
        return b

def ejercicio10():
    x = int(input("Un número: "))
    y = int(input("Otro número: "))
    resultado = maximo(x-3, minimo(x+2, y-5))
    print("Resultado:", resultado)

#----------------EJERCICIO 11----------------------
#Escribir una función que, dado un número de DNI,retorne
#True si el número es válido y False si no lo es.Para
#un número DNI sea válido debe tener entre 7 y 8 dígitos.
def dni_valido(dni):
    return len(dni) == 7 or len(dni) == 8

def ejercicio11():
    dni = input("DNI: ")
    print(dni_valido(dni))

#----------------EJERCICIO 12----------------------
#Escribir una función que, dado un string, retorne
#la longitud de la última palabra. Se considera que las
#palabras están separadas por uno o más espacios. También
#podría haber espacios al principio o al final del string
#pasado por parámetro.
def ejercicio12():
    texto = input("Texto: ").strip()
    palabras = texto.split()
    if len(palabras) > 0:
        ultima = palabras[-1]
        longitud = len(ultima)
    else:
        longitud = 0
    print(longitud)

#----------------EJERCICIO 13----------------------
#Escribir un programa que permita al usuario obtener un
#identificador para cada uno de los socios de un club.
#Para eso ingresará nombre completo y número de DNI de
#cada socio, indicando que finalizará el procesamiento
#mediante el ingreso de un nombre vacío.
#Precondición: el formato del nombre de los socios será:
#nombre apellido. Podría ingresarse más de un nombre, en
#cuyo caso será: nombre1 nombre2 apellido. Si un socio
#tuviera más de un apellido, el usuario sólo ingresará uno.
#Se debe validar que el número de DNI tenga 7 u 8 dígitos.
#En caso contrario, el programa debe dejar al usuario en
#un bucle hasta que ingrese un DNI correcto.Por cada socio
#se debe imprimir su identificador único, el cual estará
#formado por: el primer nombre, la cantidad de letras del
#apellido y los primeros 3 dígitos de su DNI.
def ejercicio13():
    nombre = input("Nombre completo (enter para salir): ")
    while nombre != "":
        dni = input("DNI: ")
        while not dni_valido(dni):
            dni = input("DNI inválido, ingrese de nuevo: ")
        partes = nombre.split()
        primer_nombre = partes[0]
        apellido = partes[-1]
        identificador = primer_nombre + str(len(apellido)) + dni[:3]
        print("ID:", identificador)
        nombre = input("Nombre completo (enter para salir): ")

#----------------EJERCICIO 14----------------------
#Escribir la función titulo(), la cual recibe un string y
#lo retorna convirtiendo la primera letra de cada palabra
#mayúscula y demás letras a minúscula, dejando inalterados
#demás caracteres.Precondición:el separador de palabras
#es el espacio:"". Agregar doctests con suficientes casos
#de prueba para validar que la función retorna el valor
#esperado ante distintos argumentos.
def titulo(texto):
    palabras = texto.split()
    resultado = ""
    for p in palabras:
        primera = p[0].upper()
        resto = p[1:].lower()
        resultado += primera + resto + " "
    return resultado.strip()

def ejercicio14():
    texto = input("Ingrese un texto: ")
    print("Texto con título:", titulo(texto))

#-------------------------------
# MENÚ PRINCIPAL
#-------------------------------
while True:
    print("--- MENÚ PRINCIPAL ---")
    print("1-Ejercicio,  2-Ejercicio,  3-Ejercicio,")
    print("4-Ejercicio,  5-Ejercicio,  6-Ejercicio,")
    print("7-Ejercicio,  8-Ejercicio,  9-Ejercicio,")
    print("10-Ejercicio, 11-Ejercicio, 12-Ejercicio,")
    print("13-Ejercicio, 14-Ejercicio, 15-Salir")
    eleccion = input("Seleccione ejercicio (1-15): ")

    if eleccion == "1": ejercicio1()
    elif eleccion == "2": ejercicio2()
    elif eleccion == "3": ejercicio3()
    elif eleccion == "4": ejercicio4()
    elif eleccion == "5": ejercicio5()
    elif eleccion == "6": ejercicio6()
    elif eleccion == "7": ejercicio7()
    elif eleccion == "8": ejercicio8()
    elif eleccion == "9": ejercicio9()
    elif eleccion == "10": ejercicio10()
    elif eleccion == "11": ejercicio11()
    elif eleccion == "12": ejercicio12()
    elif eleccion == "13": ejercicio13()
    elif eleccion == "14": ejercicio14()
    elif eleccion == "15":
        print("Programa finalizado")
        break
    else:
        print("Opción incorrecta")
