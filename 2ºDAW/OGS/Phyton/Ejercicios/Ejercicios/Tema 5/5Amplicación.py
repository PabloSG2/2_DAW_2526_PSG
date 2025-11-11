# Programa para convertir texto a código Morse
def ejercicio1():
    texto = input("Escribe un texto: ").upper()
    
# Convertir cada letra a Morse y mostrar en la misma línea
    for letra in texto:
        if letra == 'A':
            codigo = '.-'
        elif letra == 'B':
            codigo = '-...'
        elif letra == 'C':
            codigo = '-.-.'
        elif letra == 'D':
            codigo = '-..'
        elif letra == 'E':
            codigo = '.'
        elif letra == 'F':
            codigo = '..-.'
        elif letra == 'G':
            codigo = '--.'
        elif letra == 'H':
            codigo = '....'
        elif letra == 'I':
            codigo = '..'
        elif letra == 'J':
            codigo = '.---'
        elif letra == 'K':
            codigo = '-.-'
        elif letra == 'L':
            codigo = '.-..'
        elif letra == 'M':
            codigo = '--'
        elif letra == 'N':
            codigo = '-.'
        elif letra == 'O':
            codigo = '---'
        elif letra == 'P':
            codigo = '.--.'
        elif letra == 'Q':
            codigo = '--.-'
        elif letra == 'R':
            codigo = '.-.'
        elif letra == 'S':
            codigo = '...'
        elif letra == 'T':
            codigo = '-'
        elif letra == 'U':
            codigo = '..-'
        elif letra == 'V':
            codigo = '...-'
        elif letra == 'W':
            codigo = '.--'
        elif letra == 'X':
            codigo = '-..-'
        elif letra == 'Y':
            codigo = '-.--'
        elif letra == 'Z':
            codigo = '--..'
    
        print(letra, ":", codigo) # Mostrar letra y su código Morse

#Encriptar un mensaje usando el método de la "cifra del César"
#Este método consiste en correr cada letra del alfabeto una
#cierta cantidad de lugares. Si el corimiento es de 2 lugares
#la palabra "Hola" se transforma en "JQNC".
def ejercicio2():
    abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    texto = input("Escribe una palabra: ")
    corrimiento = 2
    texto_cifrado = ""
    for letra in texto.upper():
        if letra in abecedario:
            indice = abecedario.find(letra) + corrimiento
            if indice >= len(abecedario):
                indice = indice - len(abecedario)
            texto_cifrado += abecedario[indice]
        else:
            texto_cifrado += letra
    print(texto, "sería", texto_cifrado)

#Cadena S y un caracter C,Representa la distancia mas
#corta desde cada caracter en cadena hasta ocurrencia   
#ejemplo "algoritmo","o" salida: [3,2,1,0,1,2,2,1,0]
def ejercicio3():
    S = input("Escribe una palabra: ")
    C = input("Escribe una letra: ")
    for i in range(len(S)):
        distancia_minima = len(S)  # Comenzamos con una distancia grande
        for j in range(len(S)):
            if S[j] == C:
                distancia = abs(i - j)  # Calculamos la distancia
                if distancia < distancia_minima:
                    distancia_minima = distancia  # Guardamos la menor distancia
        # Mostramos el resultado para esa letra
        print("Distancia desde", S[i], "hasta", C, "es", distancia_minima)

while True:
    print("\n--- MENÚ PRINCIPAL ---")
    print("1- Ejercicio 1")
    print("2- Ejercicio 2")
    print("3- Ejercicio 3")
    print("4- Salir")
    eleccion = input("Seleccione ejercicio (1-3): ")

    if eleccion == "1":
        ejercicio1()
    elif eleccion == "2":
        ejercicio2()
    elif eleccion == "3":
        ejercicio3()
    elif eleccion == "4":
        print("Programa finalizado")
        break
    else:
        print("Opción incorrecta")