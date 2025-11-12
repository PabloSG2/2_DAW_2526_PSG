#Calificación de notas

nota= int(input("Introduzca una nota: "))

#Comprobamos que la nota esta entre 0 y 4 y es igual a suspenso
if nota == 0 or nota <= 4:
    print ("Suspenso")
#Comprobamos que la nota es 5 y es igual a aprobado
elif nota == 5:
    print ("Aprobado")
#Comprobamos que la nota es 6 y es igual a Bien
elif nota == 6:
    print("Bien")
#Comprobamos que la nota es 7 y 8 y es igual a Notable
elif nota == 7 or nota == 8:
    print ("Notable")
#Comprobamos que la nota es 9 y 10 y es igual a Sobresaliente
elif nota == 9 or nota == 10:
    print ("Sobresaliente")
#Comprobamos que si la nota no está entre 0 y 10 y da el mensaje de error
else:
    print("Error al introducir una nota")