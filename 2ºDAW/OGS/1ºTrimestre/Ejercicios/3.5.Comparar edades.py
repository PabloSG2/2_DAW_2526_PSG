#Crea un programa donde pida por pantalla el nombre y
#edades de dos personas  y las compare, devolviendo
#la frase: "nombre1" es mayor que "nombre2"

# Nombre y edad de las dos personas
nombre1 = input("Ingrese el nombre de la primera persona: ")
edad1 = int(input("Ingrese la edad de la primera persona: "))

nombre2 = input("Ingrese el nombre de la segunda persona: ")
edad2 = int(input("Ingrese la edad de la segunda persona: "))

# Compara las edades y muestra el resultado
if edad1 > edad2:
    print(nombre1+ " es mayor que " +nombre2)
elif edad2 > edad1:
    print(nombre2+ " es mayor que " +nombre1)
else:
    print(nombre1+ "tiene la misma edad que " +nombre2)
