#Programa que pide el nombre y edad de un usuario.
#Dependiendo de la edad hará un saludo distinto:
#1. Si es >= 65 --> salude con su nombre y "está jubilado, disfruta"
#2. Si es <18 --> salude con su nombre y diciendo: "estás en edad de formarte"
#3. Si está entre 18 y 30 --> salude con su nombre  y " estás en edad de empezar a trabajar"
#4. Si está entre 30 y 50 -->salude con su nombre  y " estás en edad de trabajar"
#5. Si está entre  50 y 65 --> salude y "Te quedan X años  para jubilarte"

# Solicita al usuario su nombre y su edad
nombreUsuario = input("¿Cómo te llamas? ")
strEdad = input("¿Qué edad tienes? ")

# Convierte la edad de texto a número entero
edad = int(strEdad)

# Saludo inicial
print("Hola "+nombreUsuario+" tienes "+str(edad)+" años.")

# Condición 1: Si la edad es mayor o igual a 65
if edad >= 65:
    print("Estás jubilado, disfruta.")

# Condición 2: Si la edad es menor de 18
elif edad < 18:
    print("Estás en edad de formarte.")

# Condición 3: Si la edad está entre 18 y 30 
elif edad >= 18 and edad < 30:
    print("Estás en edad de empezar a trabajar.")

# Condición 4: Si la edad está entre 30 y 50 
elif edad >= 30 and edad < 50:
    print("Estás en edad de trabajar.")

# Condición 5: Si la edad está entre 50 y 65
elif edad >= 50 and edad < 65:
    años_restantes = 65 - edad
    print("Te quedan "+str(años_restantes)+" años para jubilarte.")
