#Crea un programa donde pida por pantalla el nombre y
#edades de dos personas  y las compare, devolviendo
#la frase: "nombre1" es mayor que "nombre2"

#Creamos los nombre y edad
Nom1 = input('Nombre del usuario1: ')
Nom2 = input('Nombre del usuario2: ')
Edad1 = int(input('Edad de ' +Nom1+ ': '))
Edad2 = int(input('Edad de ' +Nom2+ ': '))

#Comprobamos las edades
if Edad1 > Edad2:
    print(Nom1 + ' es mayor que ' + Nom2)
elif Edad2 > Edad1:
    print(Nom2 + ' es mayor que ' + Nom1)
else:
    print(Nom1 + ' y ' + Nom2 + ' tienen la misma edad')
