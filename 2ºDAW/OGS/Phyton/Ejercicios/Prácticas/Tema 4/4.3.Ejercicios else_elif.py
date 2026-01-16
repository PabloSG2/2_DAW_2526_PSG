#Prueba hacer tú solo, sin mirar la solución,
#cada ejercicio visto en clase a partir del
#apartado "Sentencias else y elif" (pág. 4) de
#los apuntes y sube captura de pantalla donde se
#vea que has probado el código en tu consola.

#Creamos la variable edad y la recojemos
strEdad = input('¿Que edad tiene? ')
edad= int(strEdad)
#Comprobamos si la edad es mayor o menor de 65 años
if edad > 65:
    print ('Usted puede jubilarse')
else:
    print('Usted NO puede jubilarse')