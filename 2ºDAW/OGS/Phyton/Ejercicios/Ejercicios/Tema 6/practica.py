#----------------EJERCICIO 1----------------------
#Solicitar al usuario que ingrese su dirección email.
#Imprimir un mensaje indicando si la dirección es válida o
#no, valiéndose de una función para decidirlo. Una dirección
#se considerará válida si contiene el símbolo "@".
def ejercicio1():
    email= input("Introduzca un email ")
    if "@" in email: #Se busca si se ha metido @ en el correo
        print("Email correcto")
    else:
        print ("Email no correcto\n")

#----------------EJERCICIO 2----------------------
#Solicitar números al usuario hasta que ingrese el
#cero.Por cada uno, mostrar la suma de sus dígitos
#(utilizando una función que realice dicha suma).
def ejercicio2():
    print("Hola")

#----------------EJERCICIO 3----------------------   
def ejercicio3():
    print("Hola")

#----------------EJERCICIO 4----------------------
def ejercicio4():
    print("Hola")

#----------------EJERCICIO 5----------------------
def ejercicio5():
    print("Hola")

#----------------EJERCICIO 6----------------------
def ejercicio6():
    print("Hola")       
        
#----------------EJERCICIO 7----------------------       
def ejercicio7():
    print("Hola")

#----------------EJERCICIO 8----------------------        
def ejercicio8():
    print("Hola")

#----------------EJERCICIO 9----------------------        
def ejercicio9():
    print("Hola")

#----------------EJERCICIO 10----------------------
def ejercicio10():
    print("Hola")

#----------------EJERCICIO 11----------------------
def ejercicio11():
    print("Hola")

#----------------EJERCICIO 12----------------------
def ejercicio12():
    print("Hola")

#----------------EJERCICIO 13----------------------
def ejercicio13():
    print("Hola")

#----------------EJERCICIO 14----------------------
def ejercicio14():
    print("Hola")

# -------------------------------
# MENÚ PRINCIPAL
# -------------------------------
while True:
    print("--- MENÚ PRINCIPAL ---")
    print("1-Ejercicio,  2-Ejercicio,  3-Ejercicio,")
    print("4-Ejercicio,  5-Ejercicio,  6-Ejercicio,")
    print("7-Ejercicio,  8-Ejercicio,  9-Ejercicio,")
    print("10-Ejercicio, 11-Ejercicio, 12-Ejercicio,")
    print("13-Ejercicio, 14-Ejercicio, 15-Salir")
    eleccion = input("Seleccione ejercicio (1-15): ")

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
        ejercicio11()
    elif eleccion == "12":
        ejercicio12()
    elif eleccion == "13":
        ejercicio13()
    elif eleccion == "14":
        ejercicio14()
    elif eleccion == "15":
        print("Programa finalizado")
        break
    else:
        print("Opción incorrecta")